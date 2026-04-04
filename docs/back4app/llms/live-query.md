# Source: https://docs-containers.back4app.com/docs/android/real-time/live-query.md

---
title: Live Queries
slug: docs/android/real-time/live-query
description: Bring real time capabilities to your Android App
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-13T16:38:56.278Z
updatedAt: 2025-01-16T20:44:57.296Z
---

# Real time application using Live Queries

## Introduction

Live queries are meant to be used in **real-time reactive applications**, where just using the traditional query paradigm would come with some problems, like increased response time and high network and server usage. Live queries should be used in cases where you need to continuous update a page with fresh data coming from the database, which often happens in, but is not limited to, online games, messaging clients and shared to do lists.

This section explains how to use Back4App’s Live Query in an Android environment through [**Back4App**](https://www.back4app.com/).

This tutorial uses a basic app created in Android Studio Arctic Fox 2020.3.1 Patch 1 with compileSdk 30 , minSdk 21 and targetSdk 30

:::hint{type="success"}
**At any time, you can access the complete Project via our GitHub repositories.**

- [**Kotlin Example Repository**](https://github.com/templates-back4app/android_crud_operations_kotlin)
- [**Java Example Repository**](https://github.com/templates-back4app/android_crud_operations_java)
:::

## Goal

Here is a preview of what we are gonna achive :

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/lEZABE-g4Zzsl_m0EIWm9_image.png" signedSrc size="50" width="346" height="750" position="center" caption}

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

## 1 - Enable Live Query

Before you start coding, it’s necessary to have a class in your database to enable Live Query. To do that, simply find your app at [**Back4App website**](https://www.back4app.com/), and click on Dashboard > Create a class, as shown here:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/qrg5XoslBM4XVGIav5Muh_image.png)

Now, to enable Live Query feature, log in to your account at [**Back4App website**](https://www.back4app.com/), find your app and click on Server Settings, then find the “Server URL and Live Query” block and click on SETTINGS.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/-Dbz5b-ITMitwi2VOjI4Y_image.png)

Then, you will arrive at a page like the one below. At this page you will need to check the Activate your Back4App subdomain option, the Activate Live Query option and all the classes you want Live Query to be activated, as shown below:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/qtWsNKo65bANo55f_82EK_image.png)

:::hint{type="info"}
It’s necessary to activate **WebHosting** to use Live Queries, because your domain will work as the live server.

- **Note:&#x20;**&#x54;o know more about WebHosting look at [**Back4App WebHosting Tutorial**](https://www.back4app.com/docs/platform/activating-web-hosting).      &#x20;
:::

## 2 - Set up the LiveQuery client

[**Parse Server’s Official GitHub**](https://github.com/parse-community) have an implementation of the Live Query Client for [**Android**](https://github.com/parse-community/ParseLiveQuery-Android). It is necessary to implement the official Live Query client, which works nicely. To do so, add the following lines to your app app/build.gradle file, in the dependencies section and sync your project:

:::CodeblockTabs
app/build.gradle

```java
1    dependencies {
2        ...
3       // Don't forget to change the line below with the latest version of Parse SDK for Android
4       implementation "com.github.parse-community.Parse-SDK-Android:parse:1.26.0"
5       implementation 'com.github.parse-community:ParseLiveQuery-Android:1.2.2'
6       ...
7    }
```
:::

In this project, we will also create a class named Message, which will contains our messages.

## 3 - Subscribe to your query

To start using Live Queries, first create a LiveQueryClient that will manage the WebSocket connections for you. To do this, you will have to provide the Application ID, it’s JavaScript Key and also a server URL of Live Query which you did the setup in the first step.

:::CodeblockTabs
```java
1      Parse.initialize(new Parse.Configuration.Builder(this)
2                   .applicationId(getString(R.string.back4app_app_id))
3                   .clientKey(getString(R.string.back4app_client_key))
4                   .server(getString(R.string.back4app_server_url))
5                   .build());
```

```kotlin
1      Parse.initialize(Parse.Configuration.Builder(this)
2                   .applicationId(getString(R.string.back4app_app_id))
3                   .clientKey(getString(R.string.back4app_client_key))
4                   .server(getString(R.string.back4app_server_url))
5                   .build())
```
:::

The code for initializingLiveQueryClientis the following:

:::CodeblockTabs
```java
1     ParseLiveQueryClient parseLiveQueryClient = ParseLiveQueryClient.Factory.getClient();
```

```kotlin
1      val parseLiveQueryClient = ParseLiveQueryClient.Factory.getClient()
```
:::

&#x20;We have a RecyclerView adapter named MessageAdapter. messageAdapter.\* functions are trigerring when object added,deleted or updated. Here the our messageAdapter functions.

:::CodeblockTabs
```java
1      public void addItem(ParseObject t) {
2          this.list.add(t);
3          notifyItemInserted(list.size() - 1);
4      }
5
6      public void removeItem(ParseObject object) {
7          for (int i = 0; i < list.size(); i++) {
8              if (list.get(i).getObjectId().equals(object.getObjectId())){
9                  list.remove(i);
10                 notifyItemRemoved(i);
11                 notifyItemRangeChanged(i, list.size());
12                 return;
13             }
14         }
15     }
16     public void updateItem(ParseObject object) {
17         for (int i = 0; i < list.size(); i++) {
18             if (list.get(i).getObjectId().equals(object.getObjectId())){
19                 list.set(i,object);
20                 notifyDataSetChanged();
21                 return;
22             }
23         }
24     }
```

```kotlin
1      fun addItem(t: ParseObject?) {
2      list!!.add(t!!)
3      notifyDataSetChanged()
4      }
5  
6      fun removeItem(`object`: ParseObject) {
7          for (i in list!!.indices) {
8              if (list!![i].objectId == `object`.objectId) {
9                  list!!.removeAt(i)
10                 notifyItemRemoved(i)
11                 notifyItemRangeChanged(i, list!!.size)
12                 return
13             }
14         }
15     }
16
17     fun updateItem(`object`: ParseObject) {
18         for (i in list!!.indices) {
19             if (list!![i].objectId == `object`.objectId) {
20                 list!![i] = `object`
21                 notifyDataSetChanged()
22                 return
23             }
24         }
25     }
```
:::

Then, you should create a ParseQuery for what type of object you want to subscribe. A subscription is an event emitter, which will fire events when changes happen to an object that satisfies your query.
In this example, you will make a basic query and will subscribe all changes done to the Message objects.

:::hint{type="success"}
**See more about queries and subscriptions at&#x20;**[**Parse Official Queries Documentation**](http://docs.parseplatform.org/android/guide/#queries)**.**
:::

:::CodeblockTabs
```java
1        ParseQuery<ParseObject> parseQuery = new ParseQuery<>("Message");
2        subscriptionHandling = parseLiveQueryClient.subscribe(parseQuery);
3        subscriptionHandling.handleSubscribe(q -> {
4            subscriptionHandling.handleEvent(SubscriptionHandling.Event.CREATE, (query, object) -> {
5                MainActivity.this.runOnUiThread(() -> {
6                    messagesAdapter.addItem(object);
7                });
8            });
9            subscriptionHandling.handleEvent(SubscriptionHandling.Event.DELETE, (query, object) -> {
10                MainActivity.this.runOnUiThread(() -> {
11                    messagesAdapter.removeItem(object);
12                });
13            });
14            subscriptionHandling.handleEvent(SubscriptionHandling.Event.UPDATE, (query, object) -> {
15                MainActivity.this.runOnUiThread(() -> {
16                    messagesAdapter.updateItem(object);
17                });
18            });
19        });
```

```kotlin
1   val parseQuery = ParseQuery<ParseObject>("Message")
2           subscriptionHandling = parseLiveQueryClient!!.subscribe(parseQuery)
3           subscriptionHandling!!.handleSubscribe { subscriptionHandling!!.handleEvent(SubscriptionHandling.Event.CREATE
4               ) { _: ParseQuery<ParseObject?>?, `object`: ParseObject? ->
5                   runOnUiThread { messagesAdapter!!.addItem(`object`) }
6               }
7               subscriptionHandling!!.handleEvent(SubscriptionHandling.Event.DELETE
8               ) { _: ParseQuery<ParseObject?>?, `object`: ParseObject? ->
9                   runOnUiThread { messagesAdapter!!.removeItem(`object`!!) }
10              }
11              subscriptionHandling!!.handleEvent(SubscriptionHandling.Event.UPDATE
12              ) { _: ParseQuery<ParseObject?>?, `object`: ParseObject? ->
13                  runOnUiThread { messagesAdapter!!.updateItem(`object`!!) }
14              } 
15          }
```
:::

:::hint{type="info"}
**Note:&#x20;**&#x57;e are triggered all this events in the app. Also you can trigger this create,update and delete events from the Back4App (From table or javascript console)
:::

## It’s done!

At this point, you have the knowledge in how to use Live Queries to make real-time reactive applications in an Android environment and also how to setup Live Query using Back4App. Now you can start by implementing it in your own app.

You are now ready to explore [**Parse Server core features**](https://www.back4app.com/product/parse-server) and [**Back4App add-ons**](https://www.back4app.com/product/addons).
