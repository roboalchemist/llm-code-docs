# Source: https://docs-containers.back4app.com/docs/ios/parse-objc-sdk.md

---
title: Install Parse SDK (ObjC)
slug: docs/ios/parse-objc-sdk
description: Learn how to install Parse iOS SDK into your Xcode project
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-11T18:17:22.224Z
updatedAt: 2025-01-16T20:59:54.282Z
---

## Install Parse SDK on your iOS Objective-C Project

## Introduction

In this section you will learn how to install Parse iOS SDK into your Xcode project.

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

## 1 - Install SDK

:::hint{type="info"}
Follow this step if you haven’t yet installed Parse iOS SDK.
:::

Xcode can use [**CocoaPods**](https://cocoapods.org/) as dependency manager for Swift and Objective-C Cocoa projects.

You can refer to [**CocoaPods Getting Started Guide**](https://guides.cocoapods.org/using/getting-started.html) for additional details.

To install CocoaPods, open your terminal, copy the following code snippet and paste it in to your terminal and hit return:

:::BlockQuote
$ sudo gem install cocoapods
:::

CocoaPods should install automatically after you enter your password. If there’s a problem you may need to upgrade your local version of Ruby.

Next open up the Xcode Project folder and open a terminal window in that folder.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/leelNtzDVafWX_AkS5rwE_image.png)

Now you are going to create a Podfile. Copy the following code snippet and paste it in to your terminal and hit return:

:::BlockQuote
$ pod init
:::

If your folder now shows your Podfile you did it correctly.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/V-VPF_KBpi5r6BnxTbH5B_image.png)

:::hint{type="danger"}
**Be careful,&#x20;**&#x49;f you don’t see the podfile make sure your terminal is actually inside the project folder..
:::

Next open your Podfile with Xcode or any text editor and under each target add “pod ‘Parse’”.

:::BlockQuote
pod 'Parse'
:::

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/mhHx0L5FFRUqJvJL0ihxO_image.png)

Now you are going to add Parse to your project. Make sure your terminal is opened to your project folder. Copy the following code snippet and paste it in to your terminal and hit return:

:::BlockQuote
$ pod install
:::

CocoaPods will rebuild the project as a workspace and your project will now look like this.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/gRP51g1lUdtePoOQcaaXh_image.png)

If you have already opened your Xcode project close it. From now on you’ll open the workspace file instead of the project file. Double click on the workspace file to open it.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/WFWQGDFa8aopZ8nbeipCx_image.png)

Congratulations! You have now installed the Parse iOS SDK

## 2 - Connect your Parse App

1. Open your project’s AppDelegate.swift file to set up the app’s credentials.
2. Parse iOS SDK uses these settings to connect to the Back4App servers.
3. At the top of the file you should see a function called ‘didFinishLaunchingWithOptions’.
4. Paste the following code snippet inside this function, and make sure it is above the line that says ‘return true’.

:::BlockQuote
\[Parse initializeWithConfiguration:\[ParseClientConfiguration configurationWithBlock:^(id\<ParseMutableClientConfiguration> configuration) \{
&#x20;       configuration.applicationId = @"PASTE\_YOUR\_APPLICATION\_ID\_HERE";
&#x20;       configuration.clientKey = @"PASTE\_YOUR\_CLIENT\_ID\_HERE";
&#x20;       configuration.server = @"https\://parseapi.back4app.com/";
&#x20;   }]];
:::

At the top of your AppDelegate.m file make sure to include Parse as a module by including the follwing code snippet right below ‘#import “AppDelegate.h”’.

:::BlockQuote
\#import \<Parse/Parse.h>
:::

Your AppDelegate.m file should now look like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/_mQQyeFPAgq7YoKyRJJP1_image.png)

:::hint{type="danger"}
**Be careful**, If Xcode tells you there is **No Such Module ‘Parse’** there’s an easy solution. In Xcode open ‘Target > Build Settings > Search Paths > Framework Search Paths’ and then add two values: ‘$(PROJECT\_DIR)’ and ‘$(inherited)’. Xcode will now be able to find your Parse module.
:::

1. Go to your App Dashboard at Back4App website.
2. Navigate to app’s settings: Click on Features>Core Settings block>Server
3. Return to your AppDelegate.m file and paste your applicationId and clientKey.

:::hint{type="success"}
See more at our [**New Parse App guide**](https://www.back4app.com/docs/get-started/new-parse-app#creating-new-app-find-your-appid).
:::

## 3 - Test your connection

Open your AppDelgate.m file. Inside the function called ‘didFinishLaunchingWithOptions’ add a snippet of code below the code that configures parse.

:::BlockQuote
&#x20;\[self saveInstallationObject];
:::

Then add a snippet of code to AppDelegate.m file just below ‘didFinishLaunchingWithOptions’to create a new parse installation object upon your app loading.

:::BlockQuote
-(void)saveInstallationObject\{
&#x20;   PFInstallation \*currentInstallation = \[PFInstallation currentInstallation];
&#x20;   \[currentInstallation saveInBackgroundWithBlock:^(BOOL succeeded, NSError \*error) \{
&#x20;       if (!error) \{
&#x20;           NSLog(@"You have successfully connected your app to Back4App!");
&#x20;       }else\{
&#x20;           NSLog(@"installation save failed %@",error.debugDescription);
&#x20;       }
&#x20;   }];
}
}
:::

Your finished AppDelegate.m file should look like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/jW2_eqRvoii12BtgxOrrx_image.png)



1. Build your app in a device or simulator (Command+R).

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/tJ-6lAOYOkBloVSVg-2DX_image.png)

&#x20;    2\. Wait until the main screen appears.

&#x20;    3\. Login at [**Back4App Website**](https://www.back4app.com/).

&#x20;    4\. Find your app and click on Dashboard.

&#x20;    5\. Click on Core.

&#x20;    6\. Go to Browser

If everything works properly, you should find a class named Installation as follows:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/716sk5uPu9oUIfgV8wtKg_image.png)

## Next Steps

At this point, you have learned how to get started with iOS apps. You are now ready to explore [**Parse Server core features**](https://www.back4app.com/product/parse-server) and [**Back4App add-ons**](https://www.back4app.com/product/addons).

:::hint{type="info"}
Learn more by walking around our[**&#x20;iOS Tutorials**](https://www.back4app.com/docs/ios/ios-app-template) or check [**Parse open source documentation for iOS SDK**](https://docs.parseplatform.org/ios/guide/).
:::

