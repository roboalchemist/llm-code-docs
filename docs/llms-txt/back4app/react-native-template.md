# Source: https://docs-containers.back4app.com/docs/react-native/parse-sdk/react-native-template.md

---
title: Start your React Native Expo project using a pre-built template
slug: docs/react-native/parse-sdk/react-native-template
description: In this guide you learn how to install and connect the Parse Server SDK to your React Native project and get ready to use Parse in 4 easy steps
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-19T11:17:56.151Z
updatedAt: 2025-01-28T13:50:09.161Z
---

## Introduction

In this section, you will learn how to get started with **React Native** using an **Expo** template and how to connect it to Back4App in 4 easy steps.

## Prerequisites

:::hint{type="info"}
To complete this tutorial, you will need:


- A Backend Back4App App.
  - Note: Follow the [**New Parse App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse App on Back4App.
- [**NPM&#x20;**](https://www.npmjs.com/get-npm?utm_source=house\&utm_medium=homepage\&utm_campaign=free%20orgs\&utm_term=Install%20npm)or [**YARN&#x20;**](https://classic.yarnpkg.com/en/docs/install)installed on your system.
- Expo CLI installed following [**this guide**](https://docs.expo.io/get-started/installation/?redirected).
:::

## 1 - Get the template

To get the template project, download and unzip the source code at our [**GitHub repository**](https://github.com/templates-back4app/react-native-template) into your machine or clone the project with the git command line.

Run the following command to download and extract the template using CURL:

:::BlockQuote
curl -LOk https\://github.com/templates-back4app/react-native-template/archive/master.zip && unzip master.zip
:::

OR

Run the following command to clone the template using GIT:

:::BlockQuote
git clone https\://github.com/templates-back4app/react-native-template
:::

## 2 - Download the app’s dependencies

1. Make sure that you have installed npm or yarn in your system.

:::hint{type="info"}
&#x20;Look at the [**get npm**](https://docs.npmjs.com/getting-started) or [**get yarn**](https://classic.yarnpkg.com/en/docs/install#windows-stable) guides for more info.
:::

&#x20;    2\. On your terminal, run cd react-native-template-master and open the project's root directory.

&#x20;    3\. Run npm install to install dependencies.

In this tutorial, we are using *npm* to manage dependencies but you are free to use *yarn* instead.

## 3 - Set up the app’s credentials

To allow the App to securely connect to Back4App servers, you must provide Parse JavaScript SDK with the app’s credentials.

1. Locate your App ID and Javascript Key credentials by navigating to your app Dashboard > App Settings > Security & Keys.

On the project’s root directory, open the file at: app/(tabs)/index.tsx.

The file should look like this:

:::CodeblockTabs
index.tsx

```typescript
Parse.initialize(
  'YOUR APPLICATION ID HERE',     // Replace with your Parse Application ID
  'YOUR JAVASCRIPT KEY HERE'      // Replace with your Parse JavaScript key
);
Parse.serverURL = 'https://parseapi.back4app.com/'; 
```
:::

Copy and paste your App Id and Javascript Key on it.

## 4 - Test your connection

Inside the App.js of your template project, there is a function that creates a Person object and another for fetching People of your App to your Back4App Database.

:::CodeblockTabs
index.tsx

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
:::

To run and test your App connection:

1. Open your project’s terminal.
2. Runnpm run android or npm run ios or npm run start to open the application on your target platform



![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Ua5liIXkXvYN1gKWfmaPe_screenshot-2024-10-31-at-134200.png)

## It’s done!

At this point, you have learned how to get up and run a React Native application connected to Back4app.
