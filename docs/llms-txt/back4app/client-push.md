# Source: https://docs-containers.back4app.com/docs/ios/push-notifications/client-push.md

---
title: from client side (ObjC)
slug: docs/ios/push-notifications/client-push
description: In this guide you learn how to send push notifications from your client
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-12T13:21:59.665Z
updatedAt: 2025-01-16T21:00:38.541Z
---

# Send push notifications from client side in Objective-C

## Introduction

This section explains how you can send push notifications through your iOS client with Back4App.

This is how it will look like:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/I1AU-eH4ONf-ogYS7R_8B_image.png" signedSrc size="30" width="640" height="1136" position="flex-start" caption}

:::hint{type="success"}
At any time, you can access the complete Project built with this tutorial at our [**GitHub repository**](https://github.com/templates-back4app/iOS-install-SDK).
:::

## Prerequisites

:::hint{type="info"}
**To complete this quickstart, you need:**

- [**Xcode**](https://developer.apple.com/xcode/).
- An app created at Back4App.
  - Follow the [**New Parse App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse app at Back4App.
- An iOS app connected to Back4App.
  - **Note:&#x20;**&#x46;ollow the [**Install Parse SDK (Swift) Tutorial**](https://www.back4app.com/docs/ios/parse-swift-sdk) to create an Xcode Project connected to Back4App.
- An iOS app set up via [**Back4App Push Notifications via Dashboard tutorial**](https://www.back4app.com/docs/ios/push-notifications/best-ios-push-notification-service).
- An iOS device, iphone or ipad, running iOS 10 or newer.
- A paid Apple developer Account.
:::

:::hint{type="danger"}
Going forward we are going to assume you have completed all steps of the[**&#x20;Back4App Push Notifications via Dashboard tutorial**](https://www.back4app.com/docs/ios/push-notifications/best-ios-push-notification-service), even if you use the iOS Project built with this tutorial that is available at our [**GitHub repository**](https://github.com/mpc20001/ios-objc-push-cloud-code).
You should have basic push notifications working and also be able to send pushes out via the admin console.
:::

## 1 - Enable Client Push

1. Go to [**Back4App Website.&#x20;**](https://www.back4app.com/)log in, find your app and click on Server Settings.
2. Find the “Core Settings” block and click on SETTINGS. The “Core Settings” block looks like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/PuXmcH_B8_A-BdxssHm6n_image.png)

&#x20;    3\.  Scroll to the end of the page and click on the EDIT DETAILS button, as shown below:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/fLsT6XfjxNTSJO1pGuPxC_image.png)

&#x20;    4\. You will see a checkbox called Allow Push Notification from Client in the end of the edit page, tick that box and click on the SAVE button, as shown below:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/0XGl4x5H8n2BX_LdQ-2EF_image.png)

## 2 - Subscribe your device to the News channel

1. Assuming you have completed the [**Back4App Push Notifications via Dashboard tutorial**](https://www.back4app.com/docs/ios/push-notifications/best-ios-push-notification-service), you will want to modify the completed project from that tutorial or download it from our [**GitHub repository**](https://github.com/back4app/ios-objc-push). First, you will add a channel to your Installation object. You are going to do this by altering the method createInstallationOnParse in your AppDelegate file. Open your project’s AppDelegate.m file and add the following line of code - ‘**\[currentInstallation setObject:@\[@”News1”] forKey:@”channels”];**’ - which will set the installation object’s channel array to contain one channel called News.

[****](https://github.com/mpc20001/ios-objc-push-client/blob/master/AddingParseSDKObjc/AppDelegate.m#L52-L63)

:::BlockQuote
\- (void)application:(UIApplication \*)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData \*)deviceToken \{
&#x20;// Store the deviceToken in the current Installation and save it to Parse
&#x20;PFInstallation \*currentInstallation = \[PFInstallation currentInstallation];
&#x20;\[currentInstallation setDeviceTokenFromData\:deviceToken];
&#x20;\[currentInstallation setObject:@\[@"News"] forKey:@"channels"];
&#x20;\[currentInstallation saveInBackgroundWithBlock:^(BOOL succeeded, NSError \*error) \{
&#x20;    if (!error) \{
&#x20;        NSLog(@"installation saved!!!");
&#x20;    }else\{
&#x20;        NSLog(@"installation save failed %@",error.debugDescription);
&#x20;    }
&#x20;}];
}
:::

:::hint{type="success"}
This will allow you to send a message to everyone who subscribes to the channel called News via cloud code
:::

:::hint{type="info"}
Make sure your version of didRegisterForRemoteNotificationsWithDeviceToken is the same as the code below.
:::

&#x20;      2\. Next, we will add a method to your app delegate to send a push to the News channel everytime the app launches. Open your project’s AppDelegate.m file and the method below and make sure this method is fired off everytime the app launches by calling it from didFinishLaunchingWithOptions.



:::BlockQuote
\- (BOOL)application:(UIApplication \*)application didFinishLaunchingWithOptions:(NSDictionary \*)launchOptions \{
&#x20;// Override point for customization after application launch.
&#x20;\[Parse initializeWithConfiguration:\[ParseClientConfiguration configurationWithBlock:^(id\<ParseMutableClientConfiguration> configuration) \{
&#x20;    configuration.applicationId = @"7Ez7z1DfvGFFAXFi8pjhYBOtTGqeU89eSccLBBVN";
&#x20;    configuration.clientKey = @"fySO7DEPIC39LmWJLvugLMTKdlWsLVOmsSZGksqq";
&#x20;    configuration.server = @"https\://parseapi.back4app.com/";
&#x20;}]];
&#x20;\[self registerForRemoteNotifications];
&#x20;\[self sendPushOnLaunch];
&#x20;return YES;
}
\- (void)sendPushOnLaunch \{
&#x20;PFPush \*push = \[\[PFPush alloc] init];
&#x20;\[push setChannel:@"News"];
&#x20;\[push setMessage:@"Push From Device"];
&#x20;\[push sendPushInBackground];
}
:::

## 3 - Test that you can send targeted push notifications to yourself via the client

Open your app from the simulator while leaving your physical device closed with the lock screen on.

You should see the pushes appear on your device’s lock screen as soon as the app opens on the simulator.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/ZzLbDQRGFIwqM__UDcxqP_image.png" signedSrc size="30" width="640" height="1136" position="flex-start" caption}

## Final Thoughts

You should have a firm understanding of how to send pushes from the client.

You can combine it with a pfquery to target users based on some sort of property like age, location, or object id.

:::hint{type="danger"}
Just remember that if client push is enabled it **can be exploited&#x20;**&#x61;nd **can’t be turned off without restricting all client pushes**. It’s **recommended that you tick to pushes from Cloud Code**, but it’s still good to know.
:::

## It’s done!

At this stage, you can send push notifications using Client Push through Back4App!
