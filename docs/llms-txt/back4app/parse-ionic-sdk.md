# Source: https://docs-containers.back4app.com/docs/js-framework/ionic/parse-ionic-sdk.md

---
title: Install SDK
slug: docs/js-framework/ionic/parse-ionic-sdk
description: In this guide you'll learn how to install and connect the Parse SDK to your Ionic project and get ready to use Parse in 3 easy steps.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-08T13:12:25.154Z
updatedAt: 2025-01-17T01:07:35.469Z
---

# Start your Ionic project using a pre built template

## Introduction

In this section you learn how to install Parse JavaScript SDK into your Ionic project.

:::hint{type="success"}
See more about Parse SDK at [**Parse JavaScript SDK API Reference**](https://parseplatform.org/Parse-SDK-JS/api/4.3.1/) and [**Parse open source documentation for JavaScript SDK**](https://docs.parseplatform.org/js/guide/).
:::

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- An app created at Back4App.
  - Follow the [**New Parse App tutorial&#x20;**](https://www.back4app.com/docs/get-started/new-parse-app)to learn how to create a Parse App at Back4App.
- An Ionic project started.
  - Follow the [**Getting Started&#x20;**](https://ionicframework.com/docs/intro/cli)tutorial if you don’t have it set up.
:::

## 1 - Install SDK

Since Ionic packages are managed by npm, all you have to do is to run the following command at your project folder level:

:::BlockQuote
$ npm install parse
:::

## 2 - Connect your Parse App

Import Parse in home.ts or in the page you want to make use of:

:::CodeblockTabs
home.ts

```typescript
1   import Parse from 'parse';
```
:::

UseParse.serverURL atrribute to set up the url for Back4app parse server.

:::CodeblockTabs
home.ts

```typescript
1   Parse.serverURL = 'https://parseapi.back4app.com/';
```
:::

UseParse.initialize method to set up the authentication token, connecting your page with Back4App servers.

:::CodeblockTabs
home.ts

```typescript
1   Parse.initialize("YOUR-APP-ID", "YOUR-JS-KEY");
```
:::

**Find your Application ID and your Client Key**

1. Go to your App Dashboard at Back4App website.
2. Navigate to app’s settings: Click on Server Settings > Core Settingsblock > Settings.
3. Return to your Parse.Initialize function and paste your applicationId and javaScriptKey.

## 3 - Test your conection

**Create a test code**

Test your initial setup with the following code which creates an Installation object.

First, go ahead and create a variable to show the result on your app Home page.

:::CodeblockTabs
home.ts

```typescript
1   result: string;
```
:::

Next, display that variable on your Home view.

:::CodeblockTabs
home.html

```html
1   <ion-content padding>
2     <h4>{{result}}</h4>
3   </ion-content>
```
:::

Finally, add the code that instanciates an Installation object and saves it.

Add this piece of code after setting up the communication.

:::CodeblockTabs
home.ts

```typescript
1     let install = new Parse.Installation();
2
3     install.save(null, {
4       success: (install) => {
5         // Execute any logic that should take place after the object is saved.
6         this.result = 'New object created with objectId: ' + install.id;
7       },
8       error: (install, error) => {
9         // Execute any logic that should take place if the save fails.
10        // error is a Parse.Error with an error code and message.
11        this.result = ('Failed to create new object, with error code:' + error.message.toString());
12     }
13   });
```
:::

1. Run your app on your browser.

:::BlockQuote
$ ionic serve
:::

&#x20;    2\. Wait until a new tab opens on your browser.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/bbUt7hk5KCSjQm23LtqNH_image.png)

:::hint{type="success"}
**I**n order to see the page in a phone frame, press F12.
:::

3\. Login at [**Back4App Website**](https://www.back4app.com/)

4\. Find your app and click on Dashboard.

5\. Click on Core.

6\. Go to Browser.



If everything works properly, you should find a class named Installation as follows:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/D-xCV3dRfrg3uRgGTcMru_image.png)

## It’s done!

At this point, you have learned how to get started with Ionic apps.
