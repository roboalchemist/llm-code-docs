# Source: https://docs-containers.back4app.com/docs/platform/parse-server-live-query-example.md

---
title: Real-time database
slug: docs/platform/parse-server-live-query-example
description: In this guide you learn how to add real time capability to your App
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-02-01T14:27:02.523Z
updatedAt: 2025-01-27T19:45:28.809Z
---

# How to use Parse Server Live Query

## Introduction

Live queries are meant to be used in **real-time reactive applications**, where just using the traditional query paradigm could cause several problems, like increased response time and high network and server usage. Live queries should be used in cases where you need to continuously update a page with fresh data coming from the database, which often happens in (but is not limited to) online games, messaging clients and shared to-do lists.

This section explains how to use Back4App’s Live Query in a JavaScript environment through Back4App.

For this tutorial, as an example, you will build a **Todo Online List** using Live Queries, as shown below:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/kt59SWYYaqeQXSBhaNuwt_image.png" signedSrc size="80" width="680" height="740" position="center" caption}

:::hint{type="info"}
See the complete **Todo Online List** project at [**Live Query Todo List Project**](https://github.com/igor-ribeiiro/OnlineTodoList).
:::

:::hint{type="info"}
See more about Parse SDK at [**JavaScript SDK API Reference**](https://parseplatform.org/Parse-SDK-JS/api/4.3.1/) and[**&#x20;Parse open source documentation for JavaScript SDK**](https://docs.parseplatform.org/js/guide/#live-queries).
:::

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- A basic JavaScript App connected with Back4App or the [**Live Query Todo List Project**](https://github.com/igor-ribeiiro/OnlineTodoList).
  - **Note:&#x20;**&#x59;ou can use the app created in our [**JavaScript Install Parse SDK**](https://www.back4app.com/docs/javascript/parse-javascript-sdk) tutorial or the [**Live Query Todo List Project**](https://github.com/igor-ribeiiro/OnlineTodoList).
- Sufficient knowledge of [**JavaScript Parse Queries**](https://docs.parseplatform.org/js/guide/#queries) (but not mandatory).
:::

## 1 - Enable Live Query

Before you start coding, it’s necessary to have a class in your database to enable Live Query. To do that, simply find your app at the [**Back4App Website**](https://www.back4app.com/), and click on Dashboard > Create a class, as shown below:&#x20;

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/EZk9j8BkQLq6JNVtTh7Yj_image.png)

:::hint{type="info"}
**Note:&#x20;**&#x48;ere, this class will be called Message.
:::

Now, to enable the Live Query feature, log in to your account at [**Back4App Website**](https://www.back4app.com/), find your app, and click on App Settings > Server Settings. Look for the “Server URL and Live Query” block and click on SETTINGS.
The “Server URL and Live Query” block looks like this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/ujWY8spojft4dh-Vay9Yh_image.png" signedSrc size="50" width="308" height="358" position="center" caption}

Then, you will arrive at a page like the one below. On this page you will need to check the Activate your Back4App subdomain option, the Activate Live Query option, and all the classes on which you want Live Query to be activated, as shown below:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/oBKSK5CCjDiQV-Wstg9zy_image.png" signedSrc size="60" width="461" height="514" position="center" caption}

:::hint{type="info"}
It’s necessary to activate your subdomain to use Live Queries because it will work as the live server.
:::

## 2 - Subscribe to your Query

To start using LiveQueries, you first need to create a LiveQueryClient that will manage the
WebSocket connections for you. To do this, you will have to provide the application ID, its JavaScript Key for verifying purposes, and also a server URL that should be the domain with which you did the setup in the previous step.

Here’s the code for LiveQueryClient:

:::CodeblockTabs
liveQueryClient.js

```javascript
1   var client = new Parse.LiveQueryClient({
2       applicationId: 'Your app Id here',
3       serverURL: 'wss://' + 'Your domain here', // Example: 'wss://livequerytutorial.back4app.io'
4       javascriptKey: 'Your JavaScript key here'
5   });
6   client.open();
```
:::

After following the above-mentioned steps, you should create a query for the type of object you want to subscribe. A subscription is an
event emitter, which will fire events when changes happen to an object that satisfies your query.
In this example, you will make a basic query and will subscribe all changes done to
the Todo object.

:::hint{type="info"}
See more about queries at [**Parse Official Queries Documentation**](https://docs.parseplatform.org/js/guide/#queries).
:::

Below is the code for querySubscribe:

:::CodeblockTabs
querySubscribe.js

```javascript
1   var query = new Parse.Query('Todo');
2   query.ascending('createdAt').limit(5);
3   var subscription = client.subscribe(query);
```
:::

## 3 - Listen to events

With the setup ready, it’s necessary to code what your app will do when an event fires.
In this part, we are going to show how to listen to these events in a practical example.

The **Todo Online List** example will serve as a guideline for your project because there is little to no boilerplate code used.

The two main events that you are going to use here are the create event and the delete event. The complete list of events can be found [**here**](http://docs.parseplatform.org/js/guide/#event-handling).

### **3.1 - The Create Event**

The createEvent is fired every time a ParseObject is created and fulfills the query constraints you’ve inserted. This event returns the created object.
In the **Todo Online List** example, the array of activities is stored in the this.todos variable and we will add the new objects of our database in this array, when a create event happens.

The code for createEvent is shown below:

:::CodeblockTabs
createEvent.js

```javascript
1   subscription.on('create', todo => {
2       this.todos.add(todo);
3       console.log('On create event');
4   });
```
:::

### **3.2 - The Delete Event**

Whenever an existing ParseObject that fulfills your query constraints is deleted from the database, you’ll get this event, which returns the deleted object.
In the **Todo Online List** example, you have to delete an object from the list every time it is deleted from the database. Look for matching IDs between the server and the code, to identify the deleted objects.

The code for deleteEvent is the following:

:::CodeblockTabs
deleteEvent.js

```javascript
1   subscription.on('delete', todo => {
2       this.todos.forEach(t => {
3           if (t.id === todo.id) {
4               console.log('On delete event');
5               this.todos.delete(t);
6           }
7       });
8   });
```
:::

## It’s done!

At this point, you know how to use Live Queries to make real-time reactive applications.
You also know how to do the correct Live Query setup using Back4App and can start by implementing it in your app.
