# Source: https://docs-containers.back4app.com/docs/ios/push-notifications/push-client-swift.md

---
title: from client side (Swift)
slug: docs/ios/push-notifications/push-client-swift
description: In this guide you learn how to send push notifications from your client
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-12T13:46:17.319Z
updatedAt: 2025-01-16T21:00:43.301Z
---

# Send push notifications from client side in Swift

## Introduction

This section explains how you can send push notifications through your iOS client with Back4App.

This is how it will look like:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/N6XcUW-VUuLNwzDiPqxOD_image.png" size="36" width="640" height="1136" position="flex-start" caption}

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

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/br0y9ydiIJ-MGcuigWBh9_image.png)

&#x20;    3\.  Scroll to the end of the page and click on the EDIT DETAILS button, as shown below:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/tA1g08ntmcgBz8DctuBWy_image.png)

&#x20;    4\. You will see a checkbox called Allow Push Notification from Client in the end of the edit page, tick that box and click on the SAVE button, as shown below:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/PBxZPk1qKAcGHdU4ODAQI_image.png)

## 2 - Subscribe your device to the News channel

1. Assuming you have completed the [**Back4App Push Notifications via Dashboard tutorial**](https://www.back4app.com/docs/ios/push-notifications/best-ios-push-notification-service), you will want to modify the completed project from that tutorial or download it from our [**GitHub repository**](https://github.com/back4app/ios-objc-push). First, you will add a channel to your Installation object. You are going to do this by altering the method createInstallationOnParse in your AppDelegate file. Open your project’s AppDelegate.swift file and add the following line of code - ‘**Installation setObject(\[”News1”] forKey:”channels”];**’ - which will set the installation object’s channel array to contain one channel called News.

:::CodeblockTabs
AppDelegate.m

```swift
1   func createInstallationOnParse(deviceTokenData:Data){
2       if let installation = PFInstallation.current(){
3           installation.setDeviceTokenFrom(deviceTokenData)
4           installation.setObject(["News"], forKey: "channels")
5           installation.saveInBackground {
6               (success: Bool, error: Error?) in
7               if (success) {
8                   print("You have successfully saved your push installation to Back4App!")
9               } else {
10                  if let myError = error{
11                      print("Error saving parse installation \(myError.localizedDescription)")
12                  }else{
13                      print("Uknown error")
14                  }
15              }
16          }
17      }
18  }
```
:::

:::hint{type="success"}
This will allow you to send a message to everyone who subscribes to the channel called News via cloud code
:::

:::hint{type="info"}
Make sure your version of didRegisterForRemoteNotificationsWithDeviceToken is the same as the code below.
:::

&#x20;      2\. Next, we will add a method to your app delegate to send a push to the News channel everytime the app launches. Open your project’s AppDelegate.swift file and the method below and make sure this method is fired off everytime the app launches by calling it from didFinishLaunchingWithOptions.

:::CodeblockTabs
AppDelegate.m

```swift
1   func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
2        let configuration = ParseClientConfiguration {
3            $0.applicationId = "PASTE_YOUR_APPLICATION_ID_HERE"
4            $0.clientKey = "PASTE_YOUR_CLIENT_ID_HERE"
5            $0.server = "https://parseapi.back4app.com"
6        }
7        Parse.initialize(with: configuration)
8
9        UNUserNotificationCenter.current().requestAuthorization(options: [.alert, .sound, .badge, .carPlay ]) {
10           (granted, error) in
11           print("Permission granted: \(granted)")
12           guard granted else { return }
13           self.getNotificationSettings()
14       }
15       sendPushOnLaunch()
16       return true
17   }
18   func sendPushOnLaunch(){
19       let push = PFPush()
20       push.setChannel("News")
21       push.setMessage("Push From Device")
22       push.sendInBackground()
23   }
```
:::

## 3 - Test that you can send targeted push notifications to yourself via the client

Open your app from the simulator while leaving your physical device closed with the lock screen on.

You should see the pushes appear on your device’s lock screen as soon as the app opens on the simulator.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/miCD1avjvfKiZPeDraEiY_image.png" signedSrc size="28" width="640" height="1136" position="flex-start" caption}

## Final Thoughts

You should have a firm understanding of how to send pushes from the client.

You can combine it with a pfquery to target users based on some sort of property like age, location, or object id.

:::hint{type="danger"}
Just remember that if client push is enabled it **can be exploited&#x20;**&#x61;nd **can’t be turned off without restricting all client pushes**. It’s **recommended that you tick to pushes from Cloud Code**, but it’s still good to know.
:::

## It’s done!

At this stage, you can send push notifications using Client Push through Back4App!
