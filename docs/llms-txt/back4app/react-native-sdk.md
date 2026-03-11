# Source: https://docs-containers.back4app.com/docs/react-native/parse-sdk/react-native-sdk.md

---
title: Quickstart
slug: docs/react-native/parse-sdk/react-native-sdk
description: In this guide you learn how to install and connect the Parse Server SDK to your React Native project and get ready to use Back4App with React Native CLI
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-19T11:17:49.274Z
updatedAt: 2025-01-28T13:50:04.349Z
---

## Introduction

This guide will help you set up and use Back4App with a new or existing project using the **React Native CLI**. You’ll install the `Parse SDK`, initialize it with your app keys, and create your first API call to save and retrieve data from Back4App.

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- An [**app created**](https://www.back4app.com/docs/get-started/new-parse-app) on Back4App.
- [**Npm&#x20;**](https://www.npmjs.com/get-npm?utm_source=house\&utm_medium=homepage\&utm_campaign=free%20orgs\&utm_term=Install%20npm)or yarn installed.
- [**Npx&#x20;**](https://www.npmjs.com/package/npx)package runner installed.
:::

## 1 - Create your React Native project

There are two main ways to create a React Native project: **React Native CLI&#x20;**&#x61;nd **Expo**. Choose based on your development environment and target platform (iOS or Android)

:::ExpandableHeading
**React Native CLI**

The instructions depend on your development operating system, and whether you want to start developing for iOS or Android. For more information, check the official documentation [**here**](https://reactnative.dev/docs/environment-setup).


:::

::::ExpandableHeading
**Expo**

**Install Expo CLI globally**

:::BlockQuote
npm install -g expo-cli
:::

**Create a new React Native project**

:::BlockQuote
expo init B4aProject

cd B4aProject
expo start
:::

:::BlockQuote

:::
::::

## 2 - Install dependencies

In your React Native project, install `Parse Javascript SDK` and `AsyncStorage` by running:

:::BlockQuote
npm install parse @react-native-async-storage/async-storage --save
:::

- **Parse Javascript SDK&#x20;**- To integrate your App with Back4app servers.
- **React Native Async Storage&#x20;**- To use Parse SDK, an AsyncStorage handler is required.

For iOS, also add native AsyncStorage support:

:::BlockQuote
cd ios & pod install
:::

## 3 - Get your App Keys

After creating your app on Back4App, find your App Keys under **App Settings > Security & Keys**. You’ll need both the **Application ID** and **JavaScript KEY** to connect.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/IZ0wzNH_Parph4S2-2Nwe_rn-quickstart-1.png)

## 4 - Initialize Parse and connect to Back4App

Open `index.tsx` and initialize Parse with your `Application ID` and `JavaScript KEY`:

:::CodeblockTabs
index.tsx

```typescript
import Parse from 'parse/react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';

// Initialize Parse only once
Parse.setAsyncStorage(AsyncStorage);
Parse.initialize('YOUR_APPLICATION_ID', 'YOUR_JAVASCRIPT_KEY');
Parse.serverURL = 'https://parseapi.back4app.com/';

```
:::

## 5 - Save and Retrieve Data

With Parse initialized, create two functions in `index.tsx` to save and fetch data from Back4App.

```typescript
  // Function to create a new Person 
  async function createPerson() {
    setLoading(true);
    setError(null);
    
    try {
      const PersonObject = Parse.Object.extend("Person");
      const personObject = new PersonObject();
      
      personObject.set("name", "Back4App User");
      
      const result = await personObject.save();
      setResult(`Object created with ID: ${result.id}`);
      
    } catch (error) {
      setError(error instanceof Error ? error.message : 'Unknown error');
    } finally {
      setLoading(false);
    }
  }

  async function fetchPeople() {
    setLoading(true);
    setError(null);
    
    try {
      const PersonObject = Parse.Object.extend("Person");
      const query = new Parse.Query(PersonObject);
  
      const results = await query.find();
      const names = results.map(result => ({
        objectId: result.id,
        name: result.get("name"),
      }));
      
      setResult(`Fetched names: ${JSON.stringify(names, null, 2)}`);
      
    } catch (error) {
      setError(error instanceof Error ? error.message : 'Unknown error');
    } finally {
      setLoading(false);
    }
  }
```

## 6 - Test your App

1. Open your project’s terminal.
2. Run the project.

:::ExpandableHeading
**React Native CLI**

Run npx react-native run-android or npx react-native run-ios to open the application on your target platform.
:::

:::ExpandableHeading
**Expo**

Run expo start, and follow the instructions to view the app in your browser or device.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/DJc6gXLraAX2iWP7w9DJ5_screenshot-2024-10-31-at-134200.png)
:::

## Troubleshooting

Some common issues and solutions:

### **Metro has encountered an error: while trying to resolve module “idb-keyval’ from file**

Solution: Go to the metro.conf.js file and change it to this one:

```javascript
1   const { getDefaultConfig } = require("@expo/metro-config");
2   const defaultConfig = getDefaultConfig(__dirname);
3   defaultConfig.resolver.assetExts.push("cjs");
4   module.exports = defaultConfig;
```

### **Unable to resolve module ‘EventEmitter’**

Solution: Go to the file: node\_modules\parse\lib\react-native\EventEmitter.js and change this row:

:::BlockQuote
&#x20;var EventEmitter = require('../../../react-native/Libraries/vendor/emitter/EventEmitter');
:::

to this:

:::BlockQuote
&#x20;import EventEmitter from 'react-native/Libraries/vendor/emitter/EventEmitter';
:::

In the same file EventEmitter.js, change the following row:

:::BlockQuote
module.exports = EventEmitter;
:::

to this:

:::BlockQuote
export default EventEmitter;
:::

### Issues with babel

In case you face any issues with babel, consider updating your `babel.config.js` to the following:

:::BlockQuote
module.exports = function (api) \{
&#x20; api.cache(true);
&#x20; return \{
&#x20;   presets: \['babel-preset-expo'],
&#x20;   plugins: \[
&#x20;     '@babel/plugin-proposal-export-namespace-from',
&#x20;     'react-native-reanimated/plugin',
&#x20;   ],
&#x20; };
};
:::

## Next Steps

This guide covers the basic setup and data storage with Back4App. Explore Parse features, including data storage, real-time capabilities, local data storage, cloud functions, authentication, and file storage.

