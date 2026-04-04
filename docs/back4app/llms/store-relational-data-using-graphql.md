# Source: https://docs-containers.back4app.com/docs/flutter/graphql/store-relational-data-using-graphql.md

---
title: Relational Mutations
slug: docs/flutter/graphql/store-relational-data-using-graphql
description: In this tutorial we're going to show how to store relational data on Back4App from a Flutter project using GraphQL.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-18T19:44:31.722Z
updatedAt: 2025-01-16T20:51:29.931Z
---

# Store relational data using GraphQL



## Introduction

In the last two tutorials we have performed GraphQL queries and mutations on a Back4App database from our Flutter App Project. We’re using [**GraphQL Flutter**](https://pub.dev/packages/graphql_flutter/install) as our GraphQL client once this is a very robust and far used project. For those tutorials we’ve used a very simple data model with the most common types for our Classes.

Back4App is a flexible platform which allows you to create, store and query relational data. In this tutorial we’re going to give a dive deep into this capability by showing you how to use relations and pointers when saving and querying relational data on Back4App backend. Also, we are going to explore other data types that Back4App offers like: GeoPointer and Datetime.

## Goals

At the end of this article you’ll be able to:

- **Create/update and delete Relational data (using Pointers and Relations)**
- **Create/update GeoPointers**
- **Create/update Date-Time.**

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- Make sure you have read the previous two guides - [**Start from template**](https://www.back4app.com/docs/flutter/graphql/flutter-graphql-project-with-source-code-download) and [**GraphQL Mutation**](https://www.back4app.com/docs/flutter/graphql/flutter-crud-app-example).
- Download the project file from [**GitHub Repo**](https://github.com/templates-back4app/Flutter-GraphQL/tree/complex-mutations) which includes the previous code as well as the new GUI you would need.
- Open the downloaded project on a Flutter IDE like VS Code or Android Studio.
- Back4App account that can be created [**here**](https://www.back4app.com/).&#x20;
- Connect your tutorial to Back4App as per the previous tutorials. [**Start from template**](https://www.back4app.com/docs/flutter/graphql/flutter-graphql-project-with-source-code-download).
:::

## 1 - Setting up Back-end

On our [**previous project**](https://www.back4app.com/docs/flutter/flutter-crud-app-example) our data model was very simple with just a single class: Language. Now we’re going to make it more complex by adding 2 new classes and relating them to Language.

**Founder with format**

| **Column Name** | **Description**                     |
| --------------- | ----------------------------------- |
| name            | Name of the founder of the language |

| **Column Name** | **Description**                      |
| --------------- | ------------------------------------ |
| name            | Name of owner company                |
| date\_owned     | Date ownership gained by company     |
| headquarters    | Headquarters location of the company |

We will create a one-to-one relation between class **Language** and class **Founder** using Parse Pointers, which will tell the founder of the specific language. Then, we create will one-to-many relation between class **Language** and class **Ownership** using Parse Relations that will tell which organisation/company owned the language, their Headquarters and the date they acquired the ownership of the language. The data model will look like that:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/MSTrpoeUG0ptgqYO82xGh_image.png)

Before we move to our app let’s create the classes and data in our back-end that we would require. Go to your Back4App App and then go to the GraphQL Playground. Using the mutation below, create a class **Founder** where we will store the Language’s founders names.

```dart
1   mutation CreateClass {
2   	createClass(input:{
3       name: "Founder"
4       schemaFields: {
5         addStrings: [{name: "name"}]
6       }
7     }){
8       class{
9         schemaFields{
10          name
11          __typename
12        }
13      }
14    }
15  }
```

Now let’s populate our class with some founder’s names. In the following steps we will use this data to create new languages pointing to Founder’s class. Use the mutation below on Back4App GraphQL Playground to create your founders.

```dart
1   mutation CreateObject{
2     createFounder(input: {fields: {name: "James Gosling"}}){
3       founder{
4         id
5         name
6       }
7     }
8   }
```

Here we have entered the JAVA programming language founder’s name. You can similarly for others too but right now this is enough for our guide.

Let’s create the **Ownership** class where we will store the language ownership, foundation date (Date-Time) and the Owner’s headquarter’s location (GeoPointer). Later we will create the relation between the Language class and Ownership. Proceed by running the code below for creating the class:

```dart
1   mutation CreateClass {
2   	createClass(input:{
3       name: "Ownership"
4       schemaFields: {
5         addStrings: [{name: "name"}]
6         addDates: [{name: "date_owned"}]
7       }
8     }){
9       class{
10        schemaFields{
11          name
12          __typename
13        }
14      }
15    }
16  }  
```

Now populate the **Ownership&#x20;**&#x63;lass using the following mutations:

```dart
1   mutation CreateObject{
2     createOwnership(input: {fields: {name: "Sun Microsystems"}}){
3       ownership{
4         id
5         name
6       }
7     }
8   }
```

```dart
1   mutation CreateObject{
2     createOwnership(input: {fields: {name: "Oracle"}}){
3       ownership{
4         id
5         name
6       }
7     }
8   }
```

Now refresh the page, go to Ownership class on Database browser. Select the **Add new Column** from the top right. Select GeoPoint from the first drop down and name it **headquarters** in the second text field. And leave everything as it is and press the **Add Column** button.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Agqec5Oovt3OYFjV0n0Fe_image.png" signedSrc size="50" width="538" height="477" position="center" caption}

Then go to your Language class on Database browser. Let’s add the relations to Ownership and Founder classes. Click over **add new column** and then choose the data type Pointer and the target class: Founder. Give the column the same name - founder - then press Add Column.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/O1dj3LFxgci_OtxB898BI_image.png" signedSrc size="60" width="536" height="555" position="center" caption}

Now repeat that process by adding a new column called ownership using the data type Relation and selecting the class Ownership.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/ALxoJ61kaL4mYrOdQMI6s_image.png" signedSrc size="70" width="536" height="393" position="center" caption}

Now you have your data model ready to use on your Flutter App and to start saving and updating the data.

## 2 - Creating/Adding and Deleting Pointers

Now you need to download the project boilerplate code from our [**GitHub repo**](https://github.com/templates-back4app/Flutter-GraphQL/tree/complex-mutations) open on your IDE. To connect your project to Back4App go to the GraphQL Playground and open then copy the Keys and the API URL as shown on the image below. Now paste them into the constants.dart and run your project.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/OO8tAOtsr-U2s62pAqSyy_image.png)

Run the application in your Emulator. Got to the **M** floating Button on the bottom. That will take us to the page where we performed simple mutations. Here you will find an extra floating action button **CM**. That is hte button we’re going to use to perform our complex GraphQL mutations. Click on the **CM** button, and you will see another four buttons one for each operation we’re going to make on this guide.

Now open the databaseutils.dart file and scroll down to the addPointers() method. Here we will add the logic for adding pointers. We are going to point James Gosling as a Founder of Java Language. So first you will need to proceed to your Back4App backend and copy both Founder’s (James Gosling) and Language (Java) objectId.

**Updating/Creating Pointer to Data**

Proceed to our app inside the databaseutils.dart and inside the addPointers() method initialize a String addPointerQuery where we will assign the GraphQL query for adding Pointers as follows:

```dart
1   String addPointerQuery=
2      '''
3       mutation addPointer(\$languageId: ID!, \$founderId: UpdateLanguageFieldsInput! ){
4         updateLanguage(input : {id : \$languageId, fields : \$founderId})
5         {
6           language{
7             objectId
8           }
9         }
10      }
11     ''';
```

and initialize final variable to assign variables, notice we are taking the rowObjectId and pointersId as parameters where

- rowObjectId- The object Id of row from where we will point
- pointersId- The object Id to the row to be pointed.

So declare variable as:

```dart
1   final variable={
2     "userId" : rowObjectId,
3        "founderId": {
4          "founder": {
5            "link": pointersId
6          }
7        }
8      };
```

Now like the last guide we will initialize the GraphQLClient and send query with the help of QueryOptions() and return its instance with QueryResults():

```dart
1   GraphQlConfiguration configuration = GraphQlConfiguration();
2      GraphQLClient client = configuration.clientToQuery();
3
4      QueryResult queryResult = await client.query(
5        QueryOptions(documentNode: gql(addPointerQuery), variables: variable),
6      );
7       return queryResult;
```

This is how your addPointers() method should look like:

```dart
1   Future<QueryResult> addPointers(String rowObjectId, String pointersId) async{
2      print('addPointers');
3      //code for add/update Pointers
4      String addPointerQuery=
5      '''
6       mutation addPointer(\$languageId: ID!, \$founderId: UpdateLanguageFieldsInput! ){
7         updateLanguage(input : {id : \$languageId, fields : \$founderId})
8         {
9           language{
10            objectId
11          }
12       }
13     }
14     ''';
15     final variable={
16       "userId" : rowObjectId,
17       "founderId": {
18         "founder": {
19           "link": pointersId
20         }
21       }
22     };
23     GraphQlConfiguration configuration = GraphQlConfiguration();
24     GraphQLClient client = configuration.clientToQuery();
25
26     QueryResult queryResult = await client.query(
27       QueryOptions(documentNode: gql(addPointerQuery), variables: variable),
28     );
29      return queryResult;
30   }
```

Hot Restart your app now, go to the **CM** button on the mutation page and then press the set **Add Pointers** button. Here enter the row objectId where the pointer needs to be added in the first Text Field and objectId of row where it would point in the second Text Field and then press **Done**. Now check your Dashboard and you must be able to see a relation under the **founder** column. You could click on it where it would take you to the row pointing to the **Founder** class.

**Deleting Pointer to Data**

Now proceed to the method deletePointers() where we will write logic to delete relations. To delete relations you just have to make minor changes to the query above, that is, in the variables just change the "link" with "remove". So after initializing final variable it would be:

```dart
1   final variable={
2        "languageId" : rowObjectId,
3        "founderId": {
4          "founder": {
5            "remove": pointersId
6          }
7        }
8      };
```

Everything else will look exactly the same as the addPointers(). So your deletePointers() method looks like:

```dart
1   Future<QueryResult> deletePointers(String rowObjectId, String pointersId) async{
2      print('deletePointers');
3      //code for delete pointers
4      String removePointersQuery=
5      '''
6       mutation addPointer(\$languageId: ID!, \$founderId: UpdateLanguageFieldsInput! ){
7         updateLanguage(input : {id : \$languageId, fields : \$founderId})
8         {
9           language{
10            objectId
11          }
12        }
13      }
14     ''';
15     final variable={
16       "languageId" : rowObjectId,
17       "founderId": {
18         "founder": {
19           "remove": pointersId
20         }
21       }
22     };
23     GraphQlConfiguration configuration = GraphQlConfiguration();
24     GraphQLClient client = configuration.clientToQuery();
25  
26     QueryResult queryResult = await client.query(
27       QueryOptions(documentNode: gql(removePointersQuery), variables: variable),
28     );
29     return queryResult;
30
31   }
```

You could now proceed to your Back4App dashboard and see that the \*founder column of the specific row was deleted.

## 3 - Creating/Adding and Deleting Date-time data

If you remember we have created a class **Ownership** ealier in *Step 1* and stored some data into it. These are names of companies that owned Java Programing Language. So first let’s enter the dates the acuired the ownership.

Let’s proceed to databaseutils.dart and create or scroll down to addDateTime() function. Here we will write logic to add Data-Time datatype to our class. Initialize String addDateTimeQuery and assign it the query for creating date-time data:

```dart
1   String addDateTimeQuery=
2      '''
3      mutation addTime(\$rowId: ID!,\$dateOwned: Date!){
4         updateOwnership(input : {id : \$rowId, fields : {date_owned : \$dateOwned}})
5         {
6           ownership{
7             objectId
8           }
9         }
10      } 
11     ''';
```

And the final variable as:

```dart
1   final variable={
2        "rowId": rowObjectId,
3        "dateOwned": dateTime
4      };
```

Now initialize the GraphQLClient and pass the query throught the QueryOption(). This is how your function would look like:

```dart
1   Future<QueryResult> addDateTime(String rowObjectId, String dateTime) async{
2      print('addDateTime');
3      //code for add/update date-time
4      String addDateTimeQuery=
5       '''
6       mutation addTime(\$rowId: ID!,\$dateOwned: Date!){
7         updateOwnership(input : {id : \$rowId, fields : {date_owned : \$dateOwned}})
8         {
9           ownership{
10            objectId
11          }
12        }
13      } 
14     ''';
15     final variable={
16       "rowId": rowObjectId,
17       "dateOwned": dateTime
18     };
19     GraphQlConfiguration configuration = GraphQlConfiguration();
20     GraphQLClient client = configuration.clientToQuery();
21     QueryResult queryResult = await client.query(
22       QueryOptions(documentNode: gql(addDateTimeQuery), variables: variable),
23     );
24     return queryResult;
25   }
```

Now **Hot Restart** application and note down the **objectId** of row containing *Sun Microsystems* in **name** column. Press the **Add Date-time** button. Now enter the *objectId* noted in the first text field and **“02-24-1982”** as **MM-DD-YYYY** format at the day when Java was pubished and press the **Done** button.

Proceed to your Back4App backend and you would date in form of **24 Feb 1982 at 00:00:00 UTC** which means it has identified the datatype as Date-Time datatype. Similarly, you could add **“01-27-2010”** for the **date\_owned** for *Oracle*.

## 4 - Adding/updating GeoPointer Data

Let’s add GeoPointer data to locate Head Quateres of of the comapnies from the **Ownership** table.
Proceed to database\_utils.dart file and scroll down to addGeoPointers() function. Now initialize String addGeoPointers and assign the respective query:

```dart
1   String addGeoPointers=
2       '''
3       mutation addGeoPointer(\$objectId: ID!,\$latitude: Float!,\$longitude: Float!){
4         updateOwnership(input : {id : \$objectId, fields : { headquarters:  {latitude : \$latitude, longitude : \$longitude}}})
5         {
6           ownership{
7             objectId
8           }
9         }
10      } 
11      ''';
```

and final variable as:

```dart
1   final variable={
2        "objectId": rowObjectId,
3        "latitude": double.parse(latitude),
4        "longitude":  double.parse(longitude),
5      };
```

Since latitude and longitude are double values we need to parse them from String to double before sending it.Initialise the GrapQLClient and pass query with by QueryOption(). This is how your addGeoPointers() function would look like:

```dart
1   Future<QueryResult> addGeoPointers(String rowObjectId, String latitude, String longitude) async{
2      print('add GeoPointers');
3      //code for add/update Geopointers
4      String addGeoPointers=
5       '''
6       mutation addGeoPointer(\$objectId: ID!,\$latitude: Float!,\$longitude: Float!){
7         updateOwnership(input : {id : \$objectId, fields : { headquarters:  {latitude : \$latitude, longitude : \$longitude}}})
8         {
9           ownership{
10            objectId
11          }
12        }
13      } 
14      ''';
15     final variable={
16       "objectId": rowObjectId,
17       "latitude": double.parse(latitude),
18       "longitude":  double.parse(longitude),
19     };
20     GraphQlConfiguration configuration = GraphQlConfiguration();
21     GraphQLClient client = configuration.clientToQuery();
22     QueryResult queryResult = await client.query(
23       QueryOptions(documentNode: gql(addGeoPointers), variables: variable),
24     );
25     return queryResult;
26   }
```

Hot Restart your app and select the **Add GeoPointers** button. Enter 37.35 in the first text box and 121.95 in the second text box. Enter the **objectId** of the row with Sun Microsystems as **name** and press done. Now proceed to your Back4App Backend and you would see **(37.35, 121.95)** which are co-ordinates of the HeadQuaters and states that it identifies it as GeoPointers.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/TN9iBvaF5x-BMN2ydq0DI_image.png)

## 5 - Adding/Updating and Deleting Relation

In pointers we can nly point to one row, but with the help of relations we can make connection to multiple rows. So lets make relation of our **Language** table to these two rows for **Ownership** of the **Java** language.

**Adding/Updating Relation**

Proceed to database\_utils.dart file and proceed to addRelation() function for writing the logic. Initialize String addRelationQuery and assign the query for relation as follows:

```dart
1   String addRelationQuery=
2        '''
3        mutation addRelation(\$objectId: ID!, \$relationId: OwnershipRelationInput){
4         updateLanguage(input : {id : \$objectId, fields : {ownership : \$relationId}})
5           {
6             language{
7               objectId
8             }
9           }
10         }
11       ''';
```

and the final variable would be:

```dart
1   final variable= {
2        "objectId": objectId,
3        "relationId": relationId
4      };
```

So after initializing the GraphQLClient and passing the query like before this is how your database\_utils.dart would look like:

```dart
1   Future<QueryResult> addRelation(String rowObjectId, String relationId) async{
2      //code for add/update Relation.
3      print('addRelation');
4      String addRelationQuery=
5        '''
6        mutation addRelation(\$objectId: ID!, \$relationId: OwnershipRelationInput){
7         updateLanguage(input : {id : \$objectId, fields : {ownership : \$relationId}})
8           {
9             language{
10              objectId
11            }
12          }
13        }
14       ''';
15     final variable= {
16       "objectId": rowObjectId,
17       "relationId": {
18         "add": relationId
19       }
20     };
21     GraphQlConfiguration configuration = GraphQlConfiguration();
22     GraphQLClient client = configuration.clientToQuery();
23     QueryResult queryResult = await client.query(
24       QueryOptions(documentNode: gql(addRelationQuery), variables: variable),
25     );
26     print(queryResult);
27     return queryResult;
28   }
```

***SUCCESS*** your app has finally stored relational, datetime and GeoPointers data on Back4App!

## Conclusion

In this guide we learned how to store relational data on Back4App using GraphQL form a Flutter App project. Also we worked with other GraphQL mutations like GeoPointers and Datetime, creating, updating and deleting data. On the next tutorial we are going to deep dive into queries to our flutter App.

This guide was written by Asim Junain, from [**HybrowLabs**](https://www.back4app.com/partners/software-development-company).
