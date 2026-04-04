# Source: https://docs-containers.back4app.com/docs/js-framework/angular-template.md

---
title: Angular
slug: docs/js-framework/angular-template
description: In this guide you learn how to download and start using an Angular app template.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-07T13:24:34.029Z
updatedAt: 2025-01-17T01:07:21.998Z
---

# Start your Angular project using a pre built template

## Introduction

In this section you will learn how to get install Parse and started with an **Angular 8** App in 5 easy steps.

At any time, you can test the app built with this tutorial by clicking [**here**](https://angulardocs.back4app.io/).

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- An app created on Back4App.
  - **Note: &#x20;**&#x46;ollow the [**New Parse App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse App on Back4Ap&#x70;**.**
- Node Package Manager installed in your system.
  - Look at the [**get npm guide**](https://docs.npmjs.com/getting-started) for more info.
- Basic knowledge in [**Angular**](https://angular.io/).
:::

## 1 - Install the Angular CLI

You’re first going to need to install the Angular CLI (Command Line Interface) tool. The CLI helps you to start new Angular project as well as assist you during development. In your terminal, please type the following line:

:::BlockQuote
npm install -g @angular/cli
:::

## 2 - Get the template

Download the template at our GitHub repository. You can do that using the following command line:

:::BlockQuote
curl -LOk https\://github.com/templates-back4app/angular-integration/archive/master.zip && unzip master.zip
:::

Navigate to the folder of your project and install all dependencies by running the following command:

:::BlockQuote
cd angular-integration-master/ && npm i
:::

## 3 - Update the app’s credentials

Update the strings values for App ID and JavaScript Key to set up the app’s credentials. Parse JavaScript SDK uses these settings to connect your app to Back4App servers.

1. Go to your app Dashboard at [**Back4App Website&#x20;**](https://www.back4app.com/)and click on *Server Settings*.
2. Find the *Core Settings&#x20;*&#x62;lock and click on *Settings.&#x20;*&#x4E;eed Help? Take a look at [**these steps**](https://www.back4app.com/docs/platform/app-settings) to find your keys
3. Copy your *App Id* and *Javascript Key* and return to your project's folder.
4. Go to src > environments > environment.ts and paste your keys.

## 4 - Test your connection locally

1. Start the project by running ng serve.
2. Navigate to http\://localhost:4200/.
3. Wait until the login screen appears.
4. Create an example user by clicking on the register button.

## 5 - Upload your code to the Back4App server

To deploy your app with Back4App, you first need to proper build your app. Use the following command to compile and build your app to a dist directory:

:::BlockQuote
$ ng build
:::

Then, you need to upload the created dist directory to the public folder of your Cloud Code. In order to do that, choose one of the options to deploy:

### **5.1 - Deploy via CLI**

To upload through Back4App Command Line Interface, you take a look at [**these steps**](https://www.back4app.com/docs/command-line-tool/how-to-use).

### **5.2 - Deploy via Dashboard**

In order to upload the code via Back4App visual interface, go to your App’s Dashboard at [**Back4App website**](https://www.back4app.com/) and click on *Cloud Code Functions*.

Click on +ADD button and select all the files of the dist directory. Move them to public and then click SAVE, as shown here:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/7anZ_trqrQ4ZylbCDfFUd_image.png)

Finally, to deploy your app, see the [**Back4App Web Hosting Tutorial**](https://www.back4app.com/docs/platform/parse-web-hosting).

## It’s done!

At this point, you have learned how to get started with Angular apps.
