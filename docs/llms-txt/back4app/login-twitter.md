# Source: https://docs-containers.back4app.com/docs/javascript/login-twitter.md

---
title: Twitter login
slug: docs/javascript/login-twitter
description: In this tutorial you learn how to configure Log In with Twitter to your Javascript project.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-06T14:38:32.598Z
updatedAt: 2025-01-17T01:06:22.876Z
---

# Twitter Login

## Introduction

This section explains how you can integrate Twitter Login into your Javascript project. After completing this step-by-step guide, you will be ready to upload your code to Cloud Code.

:::hint{type="danger"}
This project will use the newly released version 3.1 Parse Server. On your project dashboard, go to Server Settings > Manage Parse Server(settings) and select 3.1.1. For more information on migrating to Parse Server 3.1.x, see [**this guide**](https://www.back4app.com/docs/advanced-guides/parse-server-3).
See this guide if you do not understand the syntax of the cloud code for this project.
:::

## Prerequisites

:::hint{type="info"}
**To begin with this tutorial, you will need:**

- An app created at Back4App.
  - See the [**Create New App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create an app at Back4App.
- Set up a Subdomain for your Back4app app
  - See [**Activating your Web Hosting and Live Query**](https://www.back4app.com/docs/platform/activating-web-hosting) to learn how to create an subdomain in Back4App.
- A [**Twitter account**](https://twitter.com/) and you must apply for [**Developer access**](https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJyZWRpcmVjdF9hZnRlcl9sb2dpbiI6Imh0dHBzOi8vZGV2ZWxvcGVyLnR3aXR0ZXIuY29tL2VuL3BvcnRhbC9wZXRpdGlvbi9lc3NlbnRpYWwvYmFzaWMtaW5mbyJ9%22%7D).
:::

## 1 - Create a New Back4App App

First of all, it’s necessary to make sure that you have an existing app created at Back4App. However, if you are a new user, you can check [**this tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create one.

## 2 - Generate Access Tokens

In order for you to get the Twitter Login working in your project, you must have the Consumer Key and Consumer Secret.

To generate your access tokens keys, you must have a Twitter app. Basically, you have two options:

- If you have existing Twitter apps and you would like to edit them, please access the [**Twitter app dashboard**](https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJyZWRpcmVjdF9hZnRlcl9sb2dpbiI6Imh0dHBzOi8vZGV2ZWxvcGVyLnR3aXR0ZXIuY29tL2VuL2FwcHMifQ%3D%3D%22%7D).
- If you want to create a new app, you can access the same dashboard, but you must have an approved developer account.

:::hint{type="warning"}
**Hint:&#x20;**&#x57;hile you are requesting access for a developer account, you will certainly be asked to answer some questions, but don’t forget to agree with the terms of the contract.
:::

### **2.1 - Configure the app details**

In this topic, we’re going to configure the Twitter app credentials.

Note that it’s necessary to activate **WebHosting** to this application and to read more about WebHosting look at [**Back4App WebHosting Tutorial**](https://www.back4app.com/docs/platform/parse-web-hosting).

After that go to [**Twitter Dashboard**](https://developer.twitter.com/en/apps) and choose to Create an app or you can edit an existing app going to Details > Edit > Edit details.

Fill up the:

- *App name*
- *Application description*
- *Tell us how this app will be used*

For the **Website URL** you can leave it as your [**Back4App Subdomain**](https://www.back4app.com/docs/platform/parse-web-hosting) and the **Callback URLs** will be the [**subdomain**](https://www.back4app.com/docs/platform/parse-web-hosting) + /twitter-callback. It will looks something like this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/xULOFfw_M7P5-mgdnbnLO_image.png" signedSrc size="60" width="516" height="358" position="center" caption}

## 3 - Twitter Set up

To start using the Twitter Login for JavaScript, you need to follow these steps:

1. To link Back4app with your Twitter App and log in to your Back4App account;
2. Click on Server Settings of your App:
3. Then, click on SETTINGS of the **Twitter Login** block. It should look like this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/cKRrWzxdF3MDIKFsJGXMf_image.png" signedSrc size="40" width="260" height="322" position="center" caption}

## 4 - Get the template

Download the template at our GitHub repository. You can do that using the following command line:

:::BlockQuote
curl -LOk https\://github.com/templates-back4app/twitter-login-js/archive/master.zip && unzip master.zip
:::

## 5 - Replace keys

After downloading the project above, please open the ./cloud/app.js file and replace the following variables with the keys generated in step 2:

:::BlockQuote
**const** back4appWebhostDomain **=** 'YOUR\_BACK4APP\_WEBHOST\_DOMAIN';
**const** consumer\_key **=** 'YOUR\_CONSUMER\_KEY';
**const** consumer\_secret **=** 'YOUR\_CONSUMER\_SECRET';
:::

## 6 - Upload your code to Back4App server

To deploy your app with Back4App, you need to upload your code to Cloud Code. In order to do that, follow the steps below:

1. Go to your App at [**Back4App website&#x20;**](https://www.back4app.com/)and click on Server Settings.
2. Find the “Cloud Code” block and click on SETTINGS. The ''Cloud Code'' block looks like this:



::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/eSoaWd-txhLEZ-MXoo941_image.png" signedSrc size="70" width="810" height="578" position="center" caption}

&#x20;    3\. Click on Choose Files and select all the files imported by index.html. Move them to public, then click SAVE, as shown here:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/n4p1MR8rvvC-w07KAloLp_image.png)

&#x20;      4\. Your files will look like this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/_NIs0EluV1tao7gJH6mT__image.png" signedSrc size="70" width="533" height="538" position="center" caption}

## 7 - It’s done

After following the guide described above, you just need to open your browser with the Web Hosting address that you have created.

In case you need any help or a function/link doesn’t work, please contact our team via chat!
