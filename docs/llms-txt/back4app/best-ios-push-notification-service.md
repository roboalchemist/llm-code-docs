# Source: https://docs-containers.back4app.com/docs/ios/push-notifications/best-ios-push-notification-service.md

---
title: via Dashboard (ObjC)
slug: docs/ios/push-notifications/best-ios-push-notification-service
description: In this guide you learn how to send push notifications using Back4App Dashboard
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-12T11:31:37.915Z
updatedAt: 2025-01-16T21:00:24.043Z
---

# Send iOS push notifications using Back4App - Objective-C

## Introduction

This section explains how you can send push notifications using Cloud Code through Back4App.

This is how it will look like:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/OaAA5-WSsHA5Jb-pWGklu_image.png" signedSrc size="30" width="640" height="1136" position="flex-start" caption}

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

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/_GwawOnu-WdgjcvEr63aI_image.png)

&#x20;    2\. Go to the [**Apple Developer Center**](https://developer.apple.com/) and login to your account:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/9wE9u-m0vkfpsZvoqf9Re_image.png)

&#x20;    3\. Click on Certificates, Identifiers & Profiles.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/dxN0FXd_tUBjoaD6EZTo4_image.png)

&#x20;    4\. In the certificates section hit the plus sign. Choose to create a apple push notification certificate for sandboxes.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/6R8uln7MpDHUgS5ddTayA_image.png)

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/ucHJ4WkNhrlWTJc0vRUXv_image.png)

&#x20;    5\. Pick your app id that matches the app id used in your current Xcode project.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/2jveJXHlp-MV22CPDcnG8_image.png)

&#x20;    6\. Now you will be asked for a Certificate Signing Request or CSR. You will generate your CSR from your Mac computer.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/bkk99AOgUS2fkD3tAzZrf_image.png)

&#x20;    7\. On your Mac computer open your Keychain Access.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/EPe-aVTybJoNJeQPiQp_1_image.png)

&#x20;    8\. Next, request a certificate from a certificate authority.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/cf7mcKSSBIXK1anAdXYg0_image.png)

&#x20;    9\. Pick your user email, then make sure you save your certificate to disk - save it on a folder on your desktop called PushCerts.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/L6JwTQsXS8FMZMhQzrWCJ_image.png)

&#x20;     10\. Go back to the Apple Developer center. Upload your CSR and hit continue.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/QF92X7rvMfbo4lZbCJyhN_image.png)

&#x20;    11\. Download your Development APN certificate into the same folder called PushCerts. Call it apn\_dev.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/01-12Kn8cR5VFkOnVZGkm_image.png)

&#x20;    12\. Let’s start the process over. This time we will create production push certificates. You need both for testing and release. Select Apple Push Notification Service SSL (Sanbox & Production).

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/kVXMtRExD6Z7QY4qKi6rp_image.png)

&#x20;    13\. Upload your CSR your previously created and hit continue.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Z6lPgccNEzTCUuShtfann_image.png)

&#x20;    14\.  Download your Production APN certificate into the same folder called PushCerts. Call it apn\_prod.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/n9vcomDVcWKhd12aGWRrY_image.png)

&#x20;    15\. At this point you should have 3 files in your PushCerts folder. Double click on your apn\_prod and your apn\_dev files to add them to your keychain.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/2JXMV-9MfjrskIYdkouHr_image.png)

&#x20;      16\. Open the keychain and find the files in the keychain. Click on each on and hit export. You will want to export them as a .p12 file into your PushCerts Folder. Name the development one cert Dev\_PushCertificates.p12 and name the production cert as Prod\_PushCertificate.p12.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/BBab-cCZ28y62-gd5bDFd_image.png)

&#x20;       17\. It will ask you add a password to your exported file. Just leave it blank. You will have to enter your master key to sign the certificate though, and thats fine.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/HMEwrho_kZGim2f-5PW4m_image.png)

&#x20;      18\. Now that you have added your .p12 files your folder should look like this. If you have all these files in your folder you can go on to Step 2. If you don’t have any of these files go back to the beginning and figure out where you missed a step.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/i-YqeZKI8XofI4zCmKG2K_image.png)

## 2 - Adding Your .P12 certificates to Back4App

1. You’re almost done. Aren’t you excited? Go to [**Back4App Website**](https://www.back4app.com/), log in, find your app and click on iOS Push notification.

![](https://www.back4app.com/docs/assets/images/png/ios-push18.png)

&#x20;    2\. Upload the dev cert and the prod cert and hit send for each.

![](https://www.back4app.com/docs/assets/images/png/ios-push19.png)

&#x20;     3\. After you’ve uploaded both certificates your screen should look like this.

![](https://www.back4app.com/docs/assets/images/png/ios-push20.png)

## 3 - Setting up Your Xcode Project to receive Push Notifications

1. Open your project’s AppDelegate.M file to create a push installation object. Add the UserNotifications framework at the top of the file.

[**AppDelegate.m**](https://github.com/mpc20001/ios-objc-push-back4app/blob/master/AddingParseSDKObjc/AppDelegate.m#L11)

:::BlockQuote
\#import \<UserNotifications/UserNotifications.h>
:::

&#x20;     2\. Add the code below inside of the didFinishLaunchingWithOptions function, and make sure it is before ‘return true’ statement.

[**AppDelegate.m**](https://github.com/mpc20001/ios-objc-push-back4app/blob/master/AddingParseSDKObjc/AppDelegate.m#L27)

:::BlockQuote
&#x20;\[self registerForRemoteNotifications];
:::

&#x20;     3\. Add the following code snippets to your AppDelegate.m file below the didFinishLaunchingWithOptions function. This code will issue a request for push notifications permissions when the app first launches. Make sure to say yes to this request or your app will not be able to receive pushes. It will also handle the resulting token when the request is approved and save it as an installation object on Back4App.

[**AppDelegate.m**](https://github.com/mpc20001/ios-objc-push-back4app/blob/master/AddingParseSDKObjc/AppDelegate.m#L31-L55)

:::BlockQuote
\- (void)registerForRemoteNotifications \{
&#x20;UNUserNotificationCenter \*center = \[UNUserNotificationCenter currentNotificationCenter];
&#x20;\[center requestAuthorizationWithOptions:(UNAuthorizationOptionSound | UNAuthorizationOptionAlert | UNAuthorizationOptionBadge |     UNAuthorizationOptionCarPlay) completionHandler:^(BOOL granted, NSError \* \_Nullable error)\{
&#x20;    if(!error)\{
&#x20;        dispatch\_async(dispatch\_get\_main\_queue(), ^\{
&#x20;            \[\[UIApplication sharedApplication] registerForRemoteNotifications];
&#x20;        });
&#x20;    }else\{
&#x20;        NSLog(@"%@",error.description);
&#x20;    }
&#x20;}];
}
\- (void)application:(UIApplication \*)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData \*)deviceToken \{
&#x20;// Store the deviceToken in the current Installation and save it to Parse
&#x20;PFInstallation \*currentInstallation = \[PFInstallation currentInstallation];
&#x20;\[currentInstallation setDeviceTokenFromData\:deviceToken];;
&#x20;\[currentInstallation saveInBackgroundWithBlock:^(BOOL succeeded, NSError \*error) \{
&#x20;    if (!error) \{
&#x20;        NSLog(@"installation saved!!!");
&#x20;    }else\{
&#x20;        NSLog(@"installation save failed %@",error.debugDescription);
&#x20;    }
&#x20;}];
}
:::

&#x20;     4\. Test it by running your app. You should see this in your simulator.

::Image[]{src="https://www.back4app.com/docs/assets/images/png/ios-push21.png" size="60" width="562" height="1000" position="center" caption}

&#x20;    5\. From here on out you must use a physical device, an iphone or ipad. Push notifications do not work with the Xcode simulator. If you do not have a physical device you cannot go any further in the tutorial. Once you have your physical device attached to your Mac computer and Xcode, try running the app on your device through Xcode. When you see the push permissions request hit approve.

## 4 - Test your app

1. Go to [**Back4App Website&#x20;**](https://www.back4app.com/)log in, find your app and click on Dashboard.
2. First check that your device’s installation record is visible in Installation table.

![](https://www.back4app.com/docs/assets/images/png/ios-push22.png)

&#x20;    3\. Then Click on Push > Send New Push and create an audience for your push notification.

![](https://www.back4app.com/docs/assets/images/png/push-dashboard.png)

&#x20;   4\. Write your message and look at the preview by clicking at iOS option.

&#x20;   5\. If you have already reviewed the push notification and you want to send, click on Send push.

![](https://www.back4app.com/docs/assets/images/png/send-push.png)

:::hint{type="info"}
You may explore the other options for Push Notification at Parse Dashboard.&#x20;

There, it’s also possible to look at Past Pushes you sent and the Audiences you created for them.
:::

## It’s done!

At this stage, you can send push notifications using Parse Dashboard through Back4App!
