# Source: https://docs-containers.back4app.com/docs/js-framework/ionic/ionic-template.md

---
title: Start from template
slug: docs/js-framework/ionic/ionic-template
description: In this guide you learn how to download and start using a complete ionic app template.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-07T13:57:29.159Z
updatedAt: 2025-01-17T01:07:31.508Z
---

# Start your Ionic project from an App Template

## Introduction

In this section you learn how to get started with an Ionic template and get ready to use Back4App in 4 steps.

## Prerequisites

:::hint{type="info"}
**To complete this quickstart, you need:**

- [**Visual Studio Code&#x20;**](https://code.visualstudio.com/download)(or any web IDE you like).
- [**Ionic Framework&#x20;**](https://ionicframework.com/getting-started/)
- An app created at Back4App.
  - Follow the [**New Parse App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse app at Back4App.
:::

## 1 - Get the template

1. Download the template at our
   [**GitHub repository**](https://github.com/back4app/ionic-quickstart-example), and unzip files in your project folder. You can do that using the following command line:

:::BlockQuote
$ curl -LOk https\://github.com/back4app/ionic-quickstart-example/archive/master.zip && unzip master.zip
:::

&#x20;    2\. Navigate to the extracted folder and install the depedencies using the following command line:

:::BlockQuote
$ cd ionic-quickstart-example-master && npm install
:::

## 2 - Open the project template

1. Open Visual Studio Code.
2. Click on Open folder.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/2wqiTLb6yOllAInN6hwtU_image.png)

&#x20;   3\. Navigate to the project folder and click on OK.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/7gK4FOarlAUNlzxZjsWcK_image.png)

&#x20;    4\. Wait for Visual Studio to open.

## 3 - Set up app’s credentials

Update your strings values to set up the app’s credentials. Parse Javascript SDK uses these settings to connect to the Back4App servers. In order to do that, follow these steps:

1. Open your home typescript file:.../src/pages/home/home.ts

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/aNZ35hroSIRh5FjtO8cgu_image.png)

&#x20;     2\. Go to your App Dashboard at [**Back4App Website**](https://www.back4app.com/).

&#x20;     3\. Navigate to app’s settings: Click on Server Settings > Core Settingsblock > SETTINGS.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/cZKaNzJ7Ph1a5HSqsqQGb_image.png)

&#x20;       4\. Return to your home.ts file and paste your App Id and JavaScript Key.

:::hint{type="info"}
See more at our [**New Parse App guide**](https://www.back4app.com/docs/get-started/new-parse-app).
:::

## 4 - Testing your connection

1. Run your app on your browser.

:::BlockQuote
$ ionic serve
:::

&#x20;    1\. Wait until a new tab opens on your browser.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/HkOhB4Y0daIJcEi_InwSV_image.png)

:::hint{type="success"}
**I**n order to see the page in a phone frame, press F12.
:::

&#x20;    2\. Login at [**Back4App Website**](https://www.back4app.com/).

&#x20;    3\. Find your app and click on Dashboard.

&#x20;    4\. Click on Core.

&#x20;    5\. Go to Browser.

If everything works properly, you should find a class named Installation as follows:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/CKxmI6Y-djmpQBGVYjqMJ_image.png)

### It’s done!

At this point, you have learned how to get started with Ionic apps.
