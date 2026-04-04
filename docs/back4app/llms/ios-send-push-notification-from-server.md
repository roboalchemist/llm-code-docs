# Source: https://docs-containers.back4app.com/docs/ios/push-notifications/ios-send-push-notification-from-server.md

---
title: via Dashboard (Swift)
slug: docs/ios/push-notifications/ios-send-push-notification-from-server
description: In this guide you learn how to send push notifications from your Parse Server
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-12T12:02:03.333Z
updatedAt: 2025-01-16T21:00:27.587Z
---

# Send iOS push notifications from your Parse Server - Swift

## Introduction

This section explains how you can send push notifications using Parse Dashboard through Back4App.

This is how it will look like:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/wPGXE8KmF7QKYlOAywcYk_image.png" signedSrc size="40" width="640" height="1136" position="flex-start" caption}

:::hint{type="success"}
At any time, you can access the complete Project built with this tutorial at our [**GitHub repository**](https://github.com/templates-back4app/iOS-install-SDK).
:::

:::hint{type="info"}
**To complete this quickstart, you need:**

- [**Xcode**](https://developer.apple.com/xcode/).
- An app created at Back4App.
  - Follow the [**New Parse App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse app at Back4App.
- An iOS app connected to Back4App.
  - **Note:&#x20;**&#x46;ollow the [**Install Parse SDK (Swift) Tutorial**](https://www.back4app.com/docs/ios/parse-swift-sdk) to create an Xcode Project connected to Back4App.
- A paid Apple Developer Account.
:::

## 1 - Create Your Push Certificates In The Apple Developer Center

:::hint{type="danger"}
Pay attention to the steps below because you need to get them right in the exact order. If pushes are not being received there isn’t much we can do to debug besides going over the steps again
:::



1. Go to the target and go to Capabilities - click on push notifications - then turn push notifications on. This creates your app id and sets your entitlements.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/7wNJ8j4vdRag0IUNvZnCZ_image.png)

&#x20;    2\. Go to the [**Apple Developer Center**](https://developer.apple.com/) and login to your account:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Y-8oeYqh_a_EiIRQoj8e0_image.png)

&#x20;    3\. Click on Certificates, Identifiers & Profiles.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/PvQpClhDtBHjxgfnC5ZEr_image.png)

&#x20;    4\. In the certificates section hit the plus sign. Choose to create a apple push notification certificate for sandboxes.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/8oa7EHB0m3X1BIK8HGkzg_image.png)

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/rRNpoyltOVGnw2vGUXFrt_image.png)

&#x20;    5\. Pick your app id that matches the app id used in your current Xcode project.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/r8i8N1O28UncUyAiHkmSt_image.png)

&#x20;    6\. Now you will be asked for a Certificate Signing Request or CSR. You will generate your CSR from your Mac computer.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/N9gV9mIAVqHAiy-azI46c_image.png)

&#x20;    7\. On your Mac computer open your Keychain Access.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/2JpLjFss7mnJP3OeXT7hx_image.png)

&#x20;    8\. Next, request a certificate from a certificate authority.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/_m4lIxXE4-Y2AdAYZpmOT_image.png)

&#x20;    9\. Pick your user email, then make sure you save your certificate to disk - save it on a folder on your desktop called PushCerts.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/B87-lzvBzNx8a06WqkkJ8_image.png)

&#x20;     10\. Go back to the Apple Developer center. Upload your CSR and hit continue.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/XubdNcydnGGPG8XbXi0C3_image.png)

&#x20;    11\. Download your Development APN certificate into the same folder called PushCerts. Call it apn\_dev.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/JCEaJWTiF1FcP264UvJ9d_image.png)

&#x20;    12\. Let’s start the process over. This time we will create production push certificates. You need both for testing and release. Select Apple Push Notification Service SSL (Sanbox & Production).

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/qbQ6xY8_ZnHdWTbBupnyx_image.png)

&#x20;    13\. Upload your CSR your previously created and hit continue.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/r1LNpX7MKo2rn63oNb3lp_image.png)

&#x20;    14\.  Download your Production APN certificate into the same folder called PushCerts. Call it apn\_prod.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/m0g-xi-mZdHuGvveGAWCE_image.png)

&#x20;    15\. At this point you should have 3 files in your PushCerts folder. Double click on your apn\_prod and your apn\_dev files to add them to your keychain.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Q4IThevZAyapvDUyX_rwC_image.png)

&#x20;      16\. Open the keychain and find the files in the keychain. Click on each on and hit export. You will want to export them as a .p12 file into your PushCerts Folder. Name the development one cert Dev\_PushCertificates.p12 and name the production cert as Prod\_PushCertificate.p12.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/APa9QBL0sC6_j5MvPPAZ4_image.png)

&#x20;       17\. It will ask you add a password to your exported file. Just leave it blank. You will have to enter your master key to sign the certificate though, and thats fine.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/E3eRjL8lfXLaH8OhJV_b4_image.png)

&#x20;      18\. Now that you have added your .p12 files your folder should look like this. If you have all these files in your folder you can go on to Step 2. If you don’t have any of these files go back to the beginning and figure out where you missed a step.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/pk2CgaobB5-NZ_5QXCRGD_image.png)

## 2 - Adding Your .P12 certificates to Back4App

1. You’re almost done. Aren’t you excited? Go to [**Back4App Website**](https://www.back4app.com/), log in, find your app and click on iOS Push notification.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/SLmWrZTJEgVVUozfnm_C4_image.png)

&#x20;    2\. Upload the dev cert and the prod cert and hit send for each.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Ohzrd_mYOlDFd2audt9_2_image.png)

&#x20;     3\. After you’ve uploaded both certificates your screen should look like this.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/xf8nNjmA1KOa6IYiqUf_m_image.png)

## 3 - Setting up Your Xcode Project to receive Push Notifications

1. Open your project’s AppDelegate.swift file to create a push installation object. Add the UserNotifications framework at the top of the file.

[**AppDelegate.swift**](https://github.com/mpc20001/ios-swift-push-back4app/blob/master/AddingParseSDK/AppDelegate.swift#L10-L11)

:::BlockQuote
\#import UserNotifications
:::

&#x20;     2\. Add the code below inside of the didFinishLaunchingWithOptions function, and make sure it is before ‘return true’ statement.

[**AppDelegate.swift**](https://github.com/mpc20001/ios-swift-push-back4app/blob/master/AddingParseSDK/AppDelegate.swift#L25-L30)

:::BlockQuote
&#x20;**UNUserNotificationCenter.current**()**.requestAuthorization**(options: \[**.**&#x61;lert, **.**&#x73;ound, **.**&#x62;adge, **.**&#x63;arPlay ]) \{
&#x20;        (granted, error) **in**
&#x20;        **print**("Permission granted: \\(granted)")
&#x20;        **guard** granted **else** \{ **return** }
&#x20;        **self.getNotificationSettings**()
&#x20;    }
:::

&#x20;     3\. Add the following code snippets to your AppDelegate.swift file below the didFinishLaunchingWithOptions function. This code will issue a request for push notifications permissions when the app first launches. Make sure to say yes to this request or your app will not be able to receive pushes. It will also handle the resulting token when the request is approved and save it as an installation object on Back4App.

:::CodeblockTabs
AppDelegate.swift

```swift
1   func getNotificationSettings() {
2        UNUserNotificationCenter.current().getNotificationSettings { (settings) in
3            print("Notification settings: \(settings)")
4            guard settings.authorizationStatus == .authorized else { return }
5            UIApplication.shared.registerForRemoteNotifications()
6        }
7    }
8
9    func application(_ application: UIApplication,
10                    didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
11       createInstallationOnParse(deviceTokenData: deviceToken)
12   }
13
14   func application(_ application: UIApplication,
15                    didFailToRegisterForRemoteNotificationsWithError error: Error) {
16       print("Failed to register: \(error)")
17   }
18
19   func createInstallationOnParse(deviceTokenData:Data){
20       if let installation = PFInstallation.current(){
21           installation.setDeviceTokenFrom(deviceTokenData)
22           installation.saveInBackground {
23               (success: Bool, error: Error?) in
24               if (success) {
25                   print("You have successfully saved your push installation to Back4App!")
26               } else {
27                   if let myError = error{
28                       print("Error saving parse installation \(myError.localizedDescription)")
29                   }else{
30                       print("Uknown error")
31                   }
32               }
33           }
34       }
35   }
```
:::

&#x20;     4\. Test it by running your app. You should see this in your simulator.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/7hGkqv8WqWuac5Kyz8GSw_image.png" signedSrc size="40" width="562" height="1000" position="flex-start" caption}

&#x20;    5\. From here on out you must use a physical device, an iphone or ipad. Push notifications do not work with the Xcode simulator. If you do not have a physical device you cannot go any further in the tutorial. Once you have your physical device attached to your Mac computer and Xcode, try running the app on your device through Xcode. When you see the push permissions request hit approve.

## 4 - Test your app

1. Go to [**Back4App Website&#x20;**](https://www.back4app.com/)log in, find your app and click on Dashboard.
2. First check that your device’s installation record is visible in Installation table.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/g9nVfZ4aQO7raMj7Za6Iw_image.png)

&#x20;    3\. Then Click on Push > Send New Push and create an audience for your push notification.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/3EYkrPwt2dREgfM_244DV_image.png)

&#x20;   4\. Write your message and look at the preview by clicking at iOS option.

&#x20;   5\. If you have already reviewed the push notification and you want to send, click on Send push.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/fQ4huje7fM94tU8WYLPtq_image.png)

:::hint{type="info"}
You may explore the other options for Push Notification at Parse Dashboard.&#x20;

There, it’s also possible to look at Past Pushes you sent and the Audiences you created for them.
:::

## It’s done!

At this stage, you can send push notifications using Parse Dashboard through Back4App!
