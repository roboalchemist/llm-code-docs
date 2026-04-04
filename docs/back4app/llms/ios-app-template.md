# Source: https://docs-containers.back4app.com/docs/ios/ios-app-template.md

---
title: Start from Swift Template
slug: docs/ios/ios-app-template
description: In this guide you learn how to install and connect the Parse Server SDK to your iOS-Swift project and get ready to use Parse in 3 easy steps.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-11T17:46:40.700Z
updatedAt: 2025-01-16T20:59:39.622Z
---

# Start your iOS project from an App Template - Swift

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
[**Back4App’s GitHub repository**](https://github.com/templates-back4app/ios-template-todo-list/archive/refs/heads/main.zip), and unzip files in your project folder.

You can do that using the following command line:

:::BlockQuote
&#x20; $ curl -LOk https\://github.com/templates-back4app/ios-template-todo-list/archive/refs/heads/main.zip && unzip swiftProjectBranch.zip
:::

## 2 - Open the project template

1. Open Xcode.
2. Click on File->Open.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/A5mL0Y6kXcp7SwjDxvB5O_image.png)

&#x20;   3\. Navigate to the project folder and double click on Todo\_List\_Back4app.xcworkspace.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/2-72Dv2ut08ip11-amMpf_image.png)

&#x20;    4\. Wait for Xcode to open the project.

## 3 - Setup app’s credentials

Update your App Delegate’s Parse Client Configuration values to set up the app’s credentials. Parse iOS SDK uses these settings to connect to the Back4App servers.

1. Open your App Delegate file: .../Todo\_List\_Back4app/AppDelegate.swift

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/SMDZnK9wIC023MSdnJu8b_image.png)

&#x20;    2\. Go to your App Dashboard at Back4App website.&#x20;

&#x20;    3\. Navigate to app's settings: Click on Features > Core Settingsblock > Server.

&#x20;    4\.  Return to your AppDelegate.swift file and paste your applicationId and clientKey.

:::hint{type="success"}
See more at our [**New Parse App guide**](https://www.back4app.com/docs/get-started/new-parse-app#creating-new-app-find-your-appid).
:::

## 4 - Test your connection

1. Build your app in a device or simulator (+R).

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/YjQGAPgH3G1EnV6GlRsV9_image.png)

&#x20;    2\. Wait until the Hello World! screen appears.

&#x20;    3\. Login at [**Back4App Website**](https://www.back4app.com/).

&#x20;    4\. Find your app and click on Dashboard.

&#x20;    5\. Click on Core.

&#x20;    6\. Go to Browser.

If everything works properly, you should find a class named Installation as follows:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Od2UtqcYrHV0g4J2Xcnzp_image.png)

## Next Steps

At this point, you have learned how to get started with iOS apps.

:::hint{type="info"}
Learn more by walking around our[**&#x20;iOS Tutorials**](https://www.back4app.com/docs/ios/ios-app-template) or check [**Parse open source documentation for iOS SDK**](https://docs.parseplatform.org/ios/guide/).
:::

