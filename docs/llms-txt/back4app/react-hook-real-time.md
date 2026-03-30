# Source: https://docs-containers.back4app.com/docs/react/real-time/react-hook-real-time.md

# Source: https://docs-containers.back4app.com/docs/react-native/parse-sdk/real-time/react-hook-real-time.md

---
title: useParseQuery
slug: docs/react-native/parse-sdk/real-time/react-hook-real-time
description: In this section you will learn how to get started with **Parse React Native**, a library made up of some core utilities for using an Back4App services in **React Native** Apps.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-19T13:52:08.857Z
updatedAt: 2024-03-20T17:14:44.624Z
---

# Getting started with the React hook for real time updates using Parse

## Introduction

Welcome to Parse React Native Lib! In this guide, you’ll learn what the Parse React Lib is, how to install and start to use it on your React Native project.

## Motivation

The easiest way to integrate Parse/Back4App into your Javascript-based project is through the [**Parse Javascript SDK**](https://www.npmjs.com/package/parse). This library works on multiple Javascript environments such as NodeJS, ReactJS, VueJS, AngularJS, React-Native, and gives you access to the Back4App features.

Parse React Native’s goal is to make this experience even better for React Native developers by delivering a light-weight and easy-to-use layer that provides minimal configuration, code re-usability, and native optimizations for Android and iOS.

Using this package will ensure that items like setting up credentials, HTTP requests, real-time synchronization, offline-first interaction are automatically available to your React Native App. The lib is written entirely in Typescript, on top of [**Parse Javascript SDK**](https://www.npmjs.com/package/parse), and is currently on the Alpha version.

In this initial guide, you will install and set up the @parse/react-native library on your React Native project.

:::hint{type="danger"}
Parse React Native is currently on the Alpha version. The lib is under testing, so we recommend to proceed with caution. Your feedback is very appreciated, so feel free to use the lib and send us your questions and first impressions by dropping an email to community\@back4app.com.
:::

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- An [**app created**](https://www.back4app.com/docs/get-started/new-parse-app) on Back4App:
- Follow the [**Enable Live Query**](https://www.back4app.com/docs/platform/parse-live-query) tutorial.
- [**Npm&#x20;**](https://www.npmjs.com/get-npm?utm_source=house\&utm_medium=homepage\&utm_campaign=free%20orgs\&utm_term=Install%20npm)or yarn installed:
- [**Npx&#x20;**](https://www.npmjs.com/package/npx)package runner installed.
:::

## 1 - Installation

If you don’t have a React Native application, then go ahead and create a new project with npx package runner using the following command line:

:::BlockQuote
npx react-native init startWithParseRN
:::

Install @parse/react-native and its peer dependency parse in your React Native application:

:::BlockQuote
\# Using yarn
yarn add @parse/react-native parse

\# Using npm
npm install --save @parse/react-native parse
:::

## 2 - Application Setup

To allow the App to connect to Back4App servers securely, you must provide Parse JavaScript SDK with App’s credentials.

```javascript
1	//In your App.js
2	import { initializeParse } from  '@parse/react-native';
3	
4	initializeParse(
5	  'https://YOUR-SUBDOMAIN.b4a.io/',
6	  'APPLICATION_ID',
7	  'JAVASCRIPT_KEY'
8	);
```

You can find yourApp Id and Javascript Key credentials by opening your app Dashboard at [**Back4App Website**](https://www.back4app.com/) and clicking on App Settings > Core Settings, under Server Settings.

Your subdomain must be enabled at App Settings > Core Settings > Server URL and Live Query. For more information, please check this guide [**here**](https://www.back4app.com/docs/platform/parse-live-query).

## 3 - Creating your first Query

Next, you will build your first Query and display it in your App. The @parse/react-native library exports a useParseQuery hook, so you don’t waste time looking into how to implement features like offline support, real-time changes, and so on.

It takes a Parse.Query and returns an object with some props that you can use to access data returned by queries:

```javascript
1	// In your App.js
2	
3	import React from 'react';
4	import { ActivityIndicator, FlatList, View,Text } from 'react-native';
5	import { initializeParse, useParseQuery } from  '@parse/react-native';
6	
7	// remember to call initializeParse with your credentials before using useParseQuery
8	initializeParse(
9	  'https://YOUR-SUBDOMAIN.b4a.io/',
10	  'APPLICATION_ID',
11	  'JAVASCRIPT_KEY'
12	);
13	
14	export default function App() {
15	 const parseQuery = new Parse.Query('Todo');
16	 const {
17	  isLive,
18	  isLoading,
19	  isSyncing,
20	  results,
21	  count,
22	  error,
23	  reload
24	 } = useParseQuery(parseQuery);
25	
26	if (isLoading) {
27	  return <ActivityIndicator/>;
28	}
29	
30	return (
31	<FlatList
32	   data={results}
33	   renderItem={({item}) => (
34	   <View
35	     style={ {
36	      height:  70,
37	      flex:  1,
38	      alignItems:  'center',
39	      justifyContent:  'center',
40	    } }>
41	      <Text>Task: {item.get('title')}</Text>
42	   </View>
43	)}
44	/>);
45	}
```

When passing a query to the hook, it will first look for cached results that it might have stored. Then, it creates a WebSocket connection to communicate with the Back4app LiveQuery server, which synchronizes automatically. In other words, the offline-first approach and real-time changes are enabled by default.

To check the query state use the props returned by the hook:

- IsLive: Iftrue, indicates the query have subscribed to realtime updates.
- isLoading\:Iftrue, the query is fetching the results.
- isSyncing\:Iftrue, the query is getting updated results from Back4app servers.
- results: This is the data returned from the query.
- count: Indicates the number of objects that matched the query
- error: When something goes wrong with the query it returns an error.
- reload: Reload your query results.

The useParseQuery accepts any Parse.Query and you can see the [**full documentation**](https://github.com/neon-bindings/examples/blob/master/thread-count/native/src/lib.rs) with examples about Parse queries.

## 4 - Test the App Hook

Now you should be able to run your React Native App and see the results.

:::BlockQuote
\# on Android
npx react-native run-android

\# on iOS
npx react-native run-ios
:::

Keep in mind that you should add some data to your Back4app project to see some items in your App.

## It’s done!

At this point, you have installed @parse/react-native on your project, configured the connections with Back4App, and written your first Query. In the next guide, you will see one of the main features of this lib how to use it. Let’s continue to [**“Realtime Changes”**](https://reactnavigation.org/docs/1.x/hello-react-navigation) to start writing some more queries.
