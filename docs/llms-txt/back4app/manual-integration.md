# Source: https://docs-containers.back4app.com/docs/ios/manual-integration.md

---
title: Manual SDK integration
slug: docs/ios/manual-integration
description: Learn how to manually integrate Parse iOS SDK into your Xcode project
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-11T18:26:47.679Z
updatedAt: 2025-01-17T14:23:32.050Z
---

# Manual Parse Integration

## Introduction

In this section you will learn how to manually install Parse iOS SDK into your Xcode project.

:::hint{type="success"}
At any time, you can access the complete Project built with this tutorial at our [**GitHub repository**](https://github.com/templates-back4app/iOS-install-SDK).
:::

## Prerequisites

In this tutorial we will use a basic app created in Objective-C with Xcode 9.1 and **iOS 11**.

:::hint{type="info"}
**To complete this tutorial, you need:**

- An app created at Back4App.
  - **Note:&#x20;**&#x46;ollow the [**New Parse App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create an app at Back4App.
- Xcode.
- Basic iOS app.
  - **Note:**&#x49;f you don’t have a basic app created you can open Xcode and hit **File-> New-> Project -> iOS**. Then select **App**. After you create your basic app you are ready to follow this guide.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/cNLdHv0CpMyIVzG3ZJa_v_image.png)



![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/BVaGv4xYWoLZlA-aWy8Q6_image.png)
:::

:::hint{type="danger"}
**Note:&#x20;**&#x50;arse iOS SDK works with iOS 7.0 or higher.
:::

## 1 - Download the SDK

Download [**Parse’s latest version**](https://github.com/parse-community/Parse-SDK-iOS-OSX/releases/latest) from Github.
Extract the file and keep the Parse.framework folder that you will be using soon.

## 2 - Download Bolts

Parse depends on [**Bolts Framework**](https://github.com/BoltsFramework) in order to work.
Download the latest version of Bolts, build it and keep the Bolts.framework folder.

If you have trouble building Bolts, you can download it pre-built from our website:

- [**Download Bolts 1.8 here**](https://www.back4app.com/docs/assets/downloads/Bolts_1.8.framework.zip)
- [**Download Bolts 1.9 (Objective C) here**](https://www.back4app.com/docs/assets/downloads/OBJC_Bolts_1.9.framework.zip)
- [**Download Bolts 1.9 (Swift) here**](https://www.back4app.com/docs/assets/downloads/Swift_Bolts_1.9.framework.zip)

Or if you prefer, we have the full projects running in Swift for IOS 13, Bolts 1.9 and Parse 1.17.3 here:

- [**Swift IOS 13, Parse 1.17.3, bolts 1.9 WITH Cocoapods**](https://www.back4app.com/docs/assets/downloads/Parse1.17.3_Bolts1.9_iOS13_WithPods.zip)
- [**Swift IOS 13, Parse 1.17.3, bolts 1.9 WITHOUT Cocoapods**](https://www.back4app.com/docs/assets/downloads/Parse1.17.3_Bolts1.9_iOS13_WithoutPods.zip)

## 3 - Add the Libraries to your Project

Parse relies in a number of libraries in order to work. Please add the following libraries to your project:

- **Parse.framework**
- **Bolts.framework**
- **libz.tbd**
- **libsqlite3.tbd**
- **Foundation.framework**
- **CFNetwork.framework**
- **SystemConfiguration.framework**
- **StoreKit.framework**
- **Security.framework**
- **QuartzCore.framework**
- **MobileCoreServices.framework**
- **CoreLocation.framework**
- **CoreGraphics.framework**
- **AudioToolbox.framework**

At the end, your project target must look like this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/g-y3ZZQbT1i2510p_gAhI_image.png" signedSrc size="50" width="504" height="612" position="center" caption}

## Next Steps

At this point, you have learned how to get started manually with iOS apps.

:::hint{type="info"}
Learn more by walking around our[**&#x20;iOS Tutorials**](https://www.back4app.com/docs/ios/ios-app-template) or check [**Parse open source documentation for iOS SDK**](https://docs.parseplatform.org/ios/guide/).
:::

