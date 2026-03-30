# Source: https://docs-containers.back4app.com/docs/ios/sign-in-with-apple-ios.md

---
title: Sign In with Apple
slug: docs/ios/sign-in-with-apple-ios
description: In this tutorial you learn how to support Sign In with Apple to your iOS-Swift project and get ready to use Parse in a few easy steps.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-12T13:54:42.966Z
updatedAt: 2025-01-16T21:00:46.885Z
---

# Sign In with Apple - Swift

## Introduction

In this section you learn how to get started with Sign In with Apple using our Swift template and get ready to use Back4App in a few easy steps.

## Prerequisites

:::hint{type="info"}
**To complete this quickstart, you need:**

- Xcode 11
- Set up Sign In with Apple in your Apple Developer account.
  - Follow the [**Sign In with Apple Tutorial**](https://www.back4app.com/docs/platform/sign-in-with-apple) to learn how to set up Sign In with Apple in your Apple Developer account.
:::

## 1 - Get the template

Clone or download the template at
[**Back4App’s GitHub repository**](https://github.com/back4app/SignInWithApple), open the Swift foder.

## 2 - Open the project template

1. Open Xcode.
2. Click on File>Open.
3. Navigate to the project folder and double click on app.xcworkspace.
4. Wait for Xcode to open the project.

## 3 - Setup app’s credentials

Update your App Delegate’s Parse Client Configuration values to set up the app’s credentials. Parse iOS SDK uses these settings to connect to the Back4App servers.

1. Open your App Delegate file: AppDelegate.swift
2. Go to your App Dashboard at Back4App website.
3. Navigate to app’s settings: Click on Features>Core Settingsblock>Server
4. Return to your AppDelegate.swift file and paste your applicationId and clientKey.

:::hint{type="info"}
See more at our [**New Parse App guide**](https://www.back4app.com/docs/get-started/new-parse-app#creating-new-app-find-your-appid).
:::

## 4 - Replace the Bundle Identifier

In your target, replace the Bundle Identifier by the one you created when setting up Sign In with Apple in your Apple Developer account

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/uCKcoA_WBChh7qZpG2ShU_image.png)

Also add the Sign In with Apple in the Capabilities of your App

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/o-eW51KbTABmtE9tduXeb_image.png)

## 5 - Test your App

1. Build your app in a device or simulator (Command+R)

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/dXkrh-tGuuFhtkGlvSVvm_image.png)

&#x20;    2\. Wait until the Sign in with Apple screen appears.

&#x20;    3\. Click the button and do the login process.

&#x20;    4\. Find your app and click on Dashboard.

&#x20;    5\. Click on Core.

&#x20;    6\. Go to Browser.

If everything works properly, you should find a class named User as follows:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/QCW4CPWjJRms0Y3yHP7XH_image.png" signedSrc size="40" width="295" height="381" position="center" caption}

## Next Steps

At this point, you have learned how to get started with iOS apps.

:::hint{type="info"}
Learn more by walking around our[**&#x20;iOS Tutorials**](https://www.back4app.com/docs/ios/ios-app-template) or check [**Parse open source documentation for iOS SDK**](https://docs.parseplatform.org/ios/guide/).
:::

