# Source: https://docs-containers.back4app.com/docs/ios/instagram-clone-download.md

---
title: Instagram Clone (SwiftUI)
slug: docs/ios/instagram-clone-download
description: In this tutorial you learn how to create an Instagram clone App from a Template.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-11T18:02:18.482Z
updatedAt: 2025-01-16T20:59:46.046Z
---

# Download an Instagram Clone App Template (SwiftUI)

## Introduction

In this tutorial you learn how to get started with an Xcode template and get an Instagram clone App in a few quick steps.

## Tutorial

:::hint{type="info"}
**You can find a series of step by step blog posts about this template here:**

- [**Part 1 - An Instagram clone using SwiftUI and GraphQL**](https://blog.back4app.com/2019/08/27/instagram-clone/)
- [**Part 2 - An Instagram clone using SwiftUI and GraphQL – Login**](https://blog.back4app.com/2019/09/03/swift-instagram-clone/)
- [**Part 3 - An Instagram clone using SwiftUI and GraphQL – ProfileView**](https://blog.back4app.com/2019/09/16/instagram-clone-profile/)
- [**Part 4 - Instagram Clone App using SwiftUI and GraphQL – HomeView**](https://blog.back4app.com/2019/09/26/instagram-clone-homeview/)
:::

## Prerequisites

:::hint{type="info"}
**To complete this quickstart, you need:**

- Xcode11 or above.
- An app created at Back4App.
  - Follow the [**New Parse App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse app at Back4App.
- [**Cocoapods**](https://cocoapods.org/) installed in your Mac.
:::

## 1 - Get the template

Download the template at
[**Back4App’s GitHub repository**](https://github.com/back4app/Back4Gram/archive/master.zip), and unzip files in your project folder.

You can do that using the following command line:

:::BlockQuote
&#x20; $ curl -LOk https\://github.com/back4app/Back4Gram/archive/master.zip && unzip master.zip
:::

## 2 - Install the Cocoapods dependencies

1. Open your Terminal.
2. Navigate to the project’s folder
3. Run this command:

   pod install
4. Wait for the process to complete.

## 3 - Open the project template

1. Open Xcode.
2. Click on File->Open.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Sc0UIbbA3OcXGzcXgS3Lf_image.png)

&#x20;     3\. Navigate to the project folder and double click on Back4Gram.xcworkspace
&#x20;     4\. Wait for Xcode to open the project.

## 4 - Setup app’s credentials

Update your App Delegate’s Parse Client Configuration values to set up the app’s credentials. Parse iOS SDK uses these settings to connect to the Back4App servers.

1. Open your App Delegate file: .../Back4Gram/AppDelegate.swift
2. Go to your App Dashboard at Back4App website.
3. Navigate to app’s settings: Click on Features > Core Settings block > Server.
4. Return to your AppDelegate.swift file and paste your applicationId and clientKey.

:::hint{type="success"}
See more at our [**New Parse App guide**](https://www.back4app.com/docs/get-started/new-parse-app#creating-new-app-find-your-appid).
:::

## 5 - Test your connection

1. Build your app in a device or simulator (Command+R)
2. Wait until the Back4Gram screen appears.

## Next Steps

At this point, you have your Back4Gram copy working with your Back4app App.

:::hint{type="info"}
Learn more by walking around our[**&#x20;iOS Tutorials**](https://www.back4app.com/docs/ios/ios-app-template) or check [**Parse open source documentation for iOS SDK**](https://docs.parseplatform.org/ios/guide/).
:::

