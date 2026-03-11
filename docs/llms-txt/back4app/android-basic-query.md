# Source: https://docs-containers.back4app.com/docs/docs/android/data-objects/android-basic-query.md

---
title: Basic Queries
slug: docs/docs/android/data-objects/android-basic-query
description: In this guide, you'll learn how to perform basic data querying in Parse on a Android application
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-13T14:02:54.879Z
updatedAt: 2025-01-16T20:44:34.317Z
---

# Basic Queries on Android

## Introduction

In this guide, you will perform basic queries in Parse and implement an Android app using these queries. You will learn how to set up and query realistic data using Back4App and Android.

This tutorial uses an app created in Android Studio 4.1.1 with buildToolsVersion=30.0.2 , Compile SDK Version = 30.0.2 and targetSdkVersion=30

:::hint{type="success"}
At any time, you can access the complete Android Project built with this tutorial at our Github repositories

- [**Kotlin Example Repository**](https://github.com/templates-back4app/Android-Parse-Sdk-Kotlin)
- [**Java Example Repository**](https://github.com/templates-back4app/Android-Parse-Sdk-Java)
:::

## Goal

Our goal is query data stored on Back4App from an Android app.

Here is a preview of what we are gonna achieve:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/2P-b0YNHro11-ifKLt8YQ_image.png" signedSrc size="50" width="346" height="750" position="center" caption}

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, we need:**

- [**Android Studio**](https://developer.android.com/studio/index.html)
- An app created on Back4App.
  - **Note:&#x20;**&#x46;ollow the [**New Parse App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse App on Back4App.
- An android app connected to Back4App.
  - **Note:&#x20;**&#x46;ollow the [**Install Parse SDK tutoria**](https://www.back4app.com/docs/android/parse-android-sdk)l to create an Android Studio Project connected to Back4App.
- A device (or[**&#x20;virtual device**](https://developer.android.com/studio/run/managing-avds.html)) running Android 4.1 (Jelly Bean) or newer.
:::

## Let’s get started!

:::hint{type="info"}
Before next steps, we need to connect Back4App to our application. You should save the appId and clientKey from the Back4App to string.xml file and then init Parse in our App.java or App.kt file.
Follow the [**New Parse App tutorial**](https://www.back4app.com/docs/android/parse-android-sdk) if you don’t know how to init Parse to your app.

Or you can download the projects we shared the github links above and edit only the appId and clientKey parts according to you.
:::

## 1 - Understanding the Parse.Query class

Any Parse query operation uses the ParseQuery object type, which will help you retrieve specific data from your database throughout your app. It is crucial to know that a ParseQuery will only resolve after calling a retrieve method (like query.findInBackground), so a query can be set up and several modifiers can be chained before actually being called.

To create a new ParseQuery, you need to pass as a parameter the desired ParseObject subclass, which is the one that will contain your query results. An example query can be seen below, in which a fictional Profile subclass is being queried.

:::CodeblockTabs
```java
1   // This will create your query
2   ParseQuery<ParseObject> query = new ParseQuery<>("Profile");
3   // The query will resolve only after calling this method
4   query.findInBackground();
```

```kotlin
1   // This will create your query
2    val query = ParseQuery<ParseObject>("Profile")
3   // The query will resolve only after calling this method
4   query.findInBackground()
```
:::

You can read more about the Parse.Query class [**here at the official documentation**](https://www.back4app.com/docs/javascript/parse-javascript-sdk).&#x20;

## 2 - Save some data on Back4App

:::hint{type="info"}
In this step, we will create a Class with the JS Console and Javascript codes provided by Parse and we will create queries for this Class.
:::

Let’s create a Profile class, which will be the target of our queries in this guide. On Parse Dashboard Javascript Console is possible to run JavaScript code directly, querying and updating your application database contents using the JS SDK commands. Run the code below from your JS Console and insert the data on Back4App.

Here is how the JS Console looks like in your dashboard:



![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Wlu7TX7N6ZuOhocNdNmrc_image.png)

Go ahead and create the userProfileclass with the following example content:

```java
1   // Add Profile objects and create table
2   // Adam Sandler
3   let Profile = new Parse.Object('Profile');
4   Profile.set('name', 'Adam Sandler');
5   Profile.set('birthDay', new Date('09/09/1966'));
6   Profile.set('friendCount', 2);
7   Profile.set('favoriteFoods', ['Lobster', 'Bread']);
8   await Profile.save();
9
10  // Adam Levine
11  Profile = new Parse.Object('Profile');
12  Profile.set('name', 'Adam Levine');
13  Profile.set('birthDay', new Date('03/18/1979'));
14  Profile.set('friendCount', 52);
15  Profile.set('favoriteFoods', ['Cake', 'Bread']);
16  await Profile.save();
17
18  // Carson Kressley
19  Profile = new Parse.Object('Profile');
20  Profile.set('name', 'Carson Kressley');
21  Profile.set('birthDay', new Date('11/11/1969'));
22  Profile.set('friendCount', 12);
23  Profile.set('favoriteFoods', ['Fish', 'Cookies']);
24  await Profile.save();
25
26  // Dan Aykroyd
27  Profile = new Parse.Object('Profile');
28  Profile.set('name', 'Dan Aykroyd');
29  Profile.set('birthDay', new Date('07/01/1952'));
30  Profile.set('friendCount', 66);
31  Profile.set('favoriteFoods', ['Jam', 'Peanut Butter']);
32  await Profile.save();
33
34  // Eddie Murphy
35  Profile = new Parse.Object('Profile');
36  Profile.set('name', 'Eddie Murphy');
37  Profile.set('birthDay', new Date('04/03/1961'));
38  Profile.set('friendCount', 49);
39  Profile.set('favoriteFoods', ['Lettuce', 'Pepper']);
40  await Profile.save();
41
42  // Fergie
43  Profile = new Parse.Object('Profile');
44  Profile.set('name', 'Fergie');
45  Profile.set('birthDay', new Date('03/27/1975'));
46  Profile.set('friendCount', 55);
47  Profile.set('favoriteFoods', ['Lobster', 'Shrimp']);
48  await Profile.save();
49  
50  console.log('Success!');
```

### &#x20;3 - Query the data

Now that you have a populated class, we can now perform some basic queries in it. Let’s begin by filtering Profile results by name, which is a string type field, searching for values that contain the name Adam using the Parse.Query.contains method:

```java
1   // Create your query
2   let parseQuery = new Parse.Query('Profile');
3
4   // `contains` is a basic query method that checks if string field
5   // contains a specific substring
6   parseQuery.contains('name', 'Adam');
7
8   // The query will resolve only after calling this method, retrieving
9   // an array of `Parse.Objects`
10  let queryResults = await parseQuery.find();
11
12  // Let's show the results
13  for (let result of queryResults) {
14    // You access `Parse.Objects` attributes by using `.get`
15    console.log(result.get('name'));
16  };
```

Let’s now query by the number type field friendCount by using another common query method, Parse.Query.greaterThan. In this case, we want user Profiles in which the friend count is greater than 20.

```java
1   // Create your query
2   let parseQuery = new Parse.Query('Profile');
3
4   // `greaterThan` is a basic query method that does what it
5   // says on the tin
6   parseQuery.greaterThan('friendCount', 20);
7
8   // The query will resolve only after calling this method, retrieving
9   // an array of `Parse.Objects`
10  let queryResults = await parseQuery.find();
11
12  // Let's show the results
13  for (let result of queryResults) {
14    // You access `Parse.Objects` attributes by using `.get`
15    console.log(`name: ${result.get('name')}, friend count: ${result.get('friendCount')}`);
16  };
```

Other recurring query methods are Parse.Query.ascending and Parse.Query.descending, responsible for ordering your queries. This ordering can be done in most data types, so let’s order a query by the date field birthDay by the youngest.

```java
1   // Create your query
2   let parseQuery = new Parse.Query('Profile');
3
4   // `descending` and `ascending` can and should be chained
5   // with other query methods to improve your queries
6   parseQuery.descending('birthDay');
7
8   // The query will resolve only after calling this method, retrieving
9   // an array of `Parse.Objects`
10  let queryResults = await parseQuery.find();
11 
12  // Let's show the results
13  for (let result of queryResults) {
14    // You access `Parse.Objects` attributes by using `.get`
15    console.log(`name: ${result.get('name')}, birthday: ${result.get('birthDay')}`);
16  };
```

As stated here before, you can and should chain query methods to achieve more refined results. Let’s then combine the previous examples in a single query request:

```java
1   // Create your query
2   let parseQuery = new Parse.Query('Profile');
3
4   parseQuery.contains('name', 'Adam');
5   parseQuery.greaterThan('friendCount', 20);
6   parseQuery.descending('birthDay');
7
8   // The query will resolve only after calling this method, retrieving
9   // an array of `Parse.Objects`
10  let queryResults = await parseQuery.find();
11
12  // Let's show the results
13  for (let result of queryResults) {
14    // You access `Parse.Objects` attributes by using `.get`
15    console.log(`name: ${result.get('name')}, friend count: ${result.get('friendCount')}, birthday: ${result.get('birthDay')}`);
16  };
```

## 4 - Query from our Android App

We will now do the operations we did above from the JS Console with Java and Kotlin in our Android application. We will list the profiles by making 4 different queries.

:::CodeblockTabs
```java
1   private void doQueryByName() {
2           ParseQuery<ParseObject> query = new ParseQuery<>("Profile");
3           query.whereContains("name", "Adam");
4           progressDialog.show();
5           query.findInBackground((objects, e) -> {
6               progressDialog.hide();
7               if (e == null) {
8                   adapter = new ResultAdapter(this, objects);
9                   resultList.setLayoutManager(new LinearLayoutManager(this));
10                  resultList.setAdapter(adapter);
11              } else {
12                  Toast.makeText(this, e.getLocalizedMessage(), Toast.LENGTH_SHORT).show();
13              }
14          });
15      }
16
17      private void doQueryByFriendCount() {
18          ParseQuery<ParseObject> query = new ParseQuery<>("Profile");
19          query.whereGreaterThan("friendCount", 20);
20          progressDialog.show();
21          query.findInBackground((objects, e) -> {
22              progressDialog.hide();
23              if (e == null) {
24                  adapter = new ResultAdapter(this, objects);
25                  resultList.setLayoutManager(new LinearLayoutManager(this));
26                  resultList.setAdapter(adapter);
27              } else {
28                  Toast.makeText(this, e.getLocalizedMessage(), Toast.LENGTH_SHORT).show();
29              }
30          });
31      }
32 
33      private void doQueryByOrdering() {
34          ParseQuery<ParseObject> query = new ParseQuery<>("Profile");
35          query.orderByDescending("birthDay");
36          progressDialog.show();
37          query.findInBackground((objects, e) -> {
38              progressDialog.hide();
39              if (e == null) {
40                  adapter = new ResultAdapter(this, objects);
41                  resultList.setLayoutManager(new LinearLayoutManager(this));
42                  resultList.setAdapter(adapter);
43              } else {
44                  Toast.makeText(this, e.getLocalizedMessage(), Toast.LENGTH_SHORT).show();
45              }
46          });
47      }
48  
49      private void doQueryByAll() {
50          ParseQuery<ParseObject> query = new ParseQuery<>("Profile");
51          query.whereContains("name", "Adam");
52          query.whereGreaterThan("friendCount", 20);
53          query.orderByDescending("birthDay");
54          progressDialog.show();
55
56          query.findInBackground((objects, e) -> {
57              progressDialog.hide();
58
59              if (e == null) {
60                  adapter = new ResultAdapter(this, objects);
61                  resultList.setLayoutManager(new LinearLayoutManager(this));
62                  resultList.setAdapter(adapter);
63                  resultList.setNestedScrollingEnabled(false);
64              } else {
65                  Toast.makeText(this, e.getLocalizedMessage(), Toast.LENGTH_SHORT).show();
66              }
67          });
68      }
```

```kotlin
1   private fun doQueryByName() {
2           val query = ParseQuery<ParseObject>("Profile")
3           query.whereContains("name", "Adam")
4           progressDialog!!.show()
5           query.findInBackground { objects: List<ParseObject>?, e: ParseException? ->
6               progressDialog!!.hide()
7               if (e == null) {
8                   adapter = ResultAdapter(this, objects)
9                   resultList!!.layoutManager = LinearLayoutManager(this)
10                  resultList!!.adapter = adapter
11              } else {
12                  Toast.makeText(this, e.localizedMessage, Toast.LENGTH_SHORT).show()
13              }
14          }
15      }
16
17      private fun doQueryByFriendCount() {
18          val query = ParseQuery<ParseObject>("Profile")
19          query.whereGreaterThan("friendCount", 20)
20          progressDialog!!.show()
21          query.findInBackground { objects: List<ParseObject>?, e: ParseException? ->
22              progressDialog!!.hide()
23              if (e == null) {
24                  adapter = ResultAdapter(this, objects)
25                  resultList!!.layoutManager = LinearLayoutManager(this)
26                  resultList!!.adapter = adapter
27              } else {
28                  Toast.makeText(this, e.localizedMessage, Toast.LENGTH_SHORT).show()
29              }
30          }
31      }
32
33      private fun doQueryByOrdering() {
34          val query = ParseQuery<ParseObject>("Profile")
35          query.orderByDescending("birthDay")
36          progressDialog!!.show()
37          query.findInBackground { objects: List<ParseObject>?, e: ParseException? ->
38              progressDialog!!.hide()
39              if (e == null) {
40                  adapter = ResultAdapter(this, objects)
41                  resultList!!.layoutManager = LinearLayoutManager(this)
42                  resultList!!.adapter = adapter
43              } else {
44                  Toast.makeText(this, e.localizedMessage, Toast.LENGTH_SHORT).show()
45              }
46          }
47      }
48  
49      private fun doQueryByAll() {
50          val query = ParseQuery<ParseObject>("Profile")
51          query.whereContains("name", "Adam")
52          query.whereGreaterThan("friendCount", 20)
53          query.orderByDescending("birthDay")
54          progressDialog!!.show()
55          query.findInBackground { objects: List<ParseObject>?, e: ParseException? ->
56              progressDialog!!.hide()
57              if (e == null) {
58                  adapter = ResultAdapter(this, objects)
59                  resultList!!.layoutManager = LinearLayoutManager(this)
60                  resultList!!.adapter = adapter
61                  resultList!!.isNestedScrollingEnabled = false
62              } else {
63                  Toast.makeText(this, e.localizedMessage, Toast.LENGTH_SHORT).show()
64              }
65          }
66      }
```
:::

## It’s done!

At the end of this guide, you learned how basic data queries work on Parse and how to perform them on Back4App from an Android App.
