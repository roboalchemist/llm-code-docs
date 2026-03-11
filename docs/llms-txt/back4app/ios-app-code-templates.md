# Source: https://docs-containers.back4app.com/docs/ios/ios-app-code-templates.md

---
title: Start from ObjC Template
slug: docs/ios/ios-app-code-templates
description: In this guide you learn how to download and start using a complete(frontend and backend) iOS Objective-C app template.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-11T17:57:34.569Z
updatedAt: 2025-01-17T18:55:11.436Z
---

# Start your iOS project from an App Template - ObjC

## Introduction

In this section you learn how to get started with an Xcode template and get ready to use Back4App in 3 easy steps.

## Prerequisites

:::hint{type="info"}
**To complete this quickstart, you need:**

- Xcode.
- An app created at Back4App.
  - Follow the [**New Parse App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse app at Back4App.
:::

## 1 - Get the template

Download the template at
[**Back4App’s GitHub repository**](https://github.com/back4app/ios-objective-c-quickstart-example/archive/master.zip), and unzip files in your project folder.

You can do that using the following command line:

:::BlockQuote
$ curl -LOk [**https://github.com/back4app/ios-objective-c-quickstart-example/archive/master.zip**](https://github.com/back4app/ios-objective-c-quickstart-example/archive/master.zip) && unzip master.zip
:::

### Step 2 - Open the project template

1. Open Xcode.
2. Click on File->Open.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/VlzfoMHxymrGCXz7VBH7a_image.png)

1. Navigate to the project folder and double click on QuickStartObjcExampleApp.xcworkspace.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/O6NlutV2l4eA0SrnALcNk_image.png)

1. Wait for Xcode to open the project.

## 3 - Setup app’s credentials

Update your App Delegate’s Parse Client Configuration values to set up the app’s credentials. Parse iOS SDK uses these settings to connect to the Back4App servers.

1. Open your App Delegate file: .../QuickStartObjcExampleApp/AppDelegate.m

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/eucd2dITD5J6IDSBNpdRF_image.png)

1. Go to your App Dashboard at Back4App website.&#x20;
2. Navigate to app's settings: Click on Features > Core Settingsblock > Server.
3. Return to your AppDelegate.swift file and paste your applicationId and clientKey.

:::hint{type="success"}
See more at our [**New Parse App guide**](https://www.back4app.com/docs/get-started/new-parse-app#creating-new-app-find-your-appid).
:::

## 4 - Test your connection

1. Build your app in a device or simulator (Command+R).

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/PUaUGxCIyzbqcPvPsZE42_image.png)

1. Wait until the Hello World! screen appears.
2. Login at [**Back4App Website**](https://www.back4app.com/).
3. Find your app and click on Dashboard.
4. Click on Core.
5. Go to Browser.

If everything works properly, you should find a class named Installation as follows:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/253dXzdiCT6_BMH1h1R8n_image.png)

## Next Steps

At this point, you have learned how to get started with iOS apps.

:::hint{type="info"}
Learn more by walking around our[**&#x20;iOS Tutorials**](https://www.back4app.com/docs/ios/ios-app-template) or check [**Parse open source documentation for iOS SDK**](https://docs.parseplatform.org/ios/guide/).
:::

