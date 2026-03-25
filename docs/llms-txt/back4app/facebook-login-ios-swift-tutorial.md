# Source: https://docs-containers.back4app.com/docs/ios/facebook-login-ios-swift-tutorial.md

---
title: Facebook login
slug: docs/ios/facebook-login-ios-swift-tutorial
description: In this tutorial you learn how to add facebook login to your ios app using Swift.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-11T19:01:35.653Z
updatedAt: 2025-01-16T21:00:13.753Z
---

# Add Facebook login to your iOS App using Swift tutorial

## Introduction

This section explains how you can create an app with user registration using Facebook Login and [**Parse Server core features**](https://www.back4app.com/product/parse-server) through Back4App.

## Prerequisites

:::hint{type="info"}
**To complete this quickstart, you need:**

- [**Xcode**](https://developer.apple.com/xcode/).
- An app created at Back4App.
  - Follow the [**New Parse App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse app at Back4App.
- An iOS app connected to Back4App.
  - **Note:&#x20;**&#x46;ollow the [**Install Parse SDK (ObjC) Tutorial**](https://www.back4app.com/docs/ios/parse-objc-sdk) to create an Xcode Project connected to Back4App.
:::

## 1 - Facebook Set up

To start using Facebook functions, you need to:

1. Go to the [**Facebook Developer Website&#x20;**](https://developers.facebook.com/)and create an account and an app.
2. Add your application’s Facebook Application ID on your Parse application’s settings page.
3. Follow Facebook’s instructions for [**getting started with the Facebook SDK&#x20;**](https://developers.facebook.com/docs/ios/getting-started)to create an app linked to the Facebook SDK.

## 2 - Link your Facebook App with Back4App

1. Go to your App dashboard at [**Back4App Website&#x20;**](https://www.back4app.com/)and click on Server Settings.
2. Find the “Facebook Login” block and click on Settings. The “Facebook Login” block looks like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/np6VzJ6Qoxfr8mKrVtYw4_image.png)

&#x20;    3\. Go back to your XCode Project, open your info.plist copy the code from [**Facebook Configuration**](https://developers.facebook.com/docs/facebook-login/ios), Step 4a, item 2, and paste it in the \<dict>...\</dict>  part of your info.plist.

&#x20;    4\. In order to use a dialog box from Facebook, also copy and paste the code from section 4a, item 3 into your info.plist file.

&#x20;    5\. Save&#x20;

## 3 - Setting up your App

1. Add the following to your application\:didFinishLaunchingWithOptions: method, after you’ve initialized the Parse SDK:

```swift
1    import FBSDKCoreKit
2    import Parse
3
4    // AppDelegate.swift
5    func application(application: UIApplicatiofunc application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
6    // Initialize Parse.
7    let parseConfig = ParseClientConfiguration {
8        $0.applicationId = "parseAppId"
9        $0.clientKey = "parseClientKey"
10       $0.server = "parseServerUrlString"
11   }
12   Parse.initialize(with: parseConfig)
13   PFFacebookUtils.initializeFacebook(applicationLaunchOptions: launchOptions)
14   }
```

&#x20;      2\. Add the following handlers in your app delegate:

```swift
1    func application(_ application: UIApplication, open url: URL, sourceApplication: String?, annotation: Any) -> Bool {
2
3    return FBSDKApplicationDelegate.sharedInstance().application(
4                application,
5                open: url,
6                sourceApplication: sourceApplication,
7                annotation: annotation
8        )
9  
10   }
11
12   func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey: Any] = [:]) -> Bool {
13
14   return FBSDKApplicationDelegate.sharedInstance().application(
15               app,
16               open: url,
17               sourceApplication: options[.sourceApplication] as? String,
18               annotation: options[.annotation]
19       )
20
21   }
22
23   //Make sure it isn't already declared in the app delegate (possible redefinition of func error)
24   func applicationDidBecomeActive(_ application: UIApplication) {
25   FBSDKAppEvents.activateApp()
26   }
```

## &#x20;4 - Log in & Sign Up

PFUser provides a way to allow your users to log in or sign up through Facebook. This is done by using the logInInBackgroundWithReadPermissions method like so:

```swift
1    PFFacebookUtils.logInInBackground(withReadPermissions: permissions) {
2    (user: PFUser?, error: Error?) in
3    if let user = user {
4        if user.isNew {
5        print("User signed up and logged in through Facebook!")
6        } else {
7        print("User logged in through Facebook!")
8        }
9     } else {
10        print("Uh oh. The user cancelled the Facebook login.")
11    }
12    }
```

When this code is run, the following happens:

1. The user is shown the Facebook login dialog.
2. The user authenticates via Facebook, and your app receives a callback using handleOpenURL
3. Our SDK receives the user’s Facebook access data and saves it to a PFUser. If no PFUser exists with the same Facebook ID, then a new PFUser is created.
4. Your code block is called with the user.
5. The current user reference will be updated to this user.

The permissions argument is an array of strings that specifies what permissions your app requires from the Facebook user. These permissions must only include read permissions.

To acquire publishing permissions for a user so that your app can, for example, post status updates on their behalf, you must call \[PFFacebookUtils logInInBackgroundWithPublishPermissions:]:

```swift
1   PFFacebookUtils.logInInBackgroundWithPublishPermissions(["publish_actions"], {
2     (user: PFUser?, error: NSError?) -> Void in
3     if user != nil {
4       // Your app now has publishing permissions for the user
5     }
6   })
```

## 5 - Linking

If you want to associate an existing PFUser to a Facebook account, you can link it like so:

```swift
1   if !PFFacebookUtils.isLinkedWithUser(user) {
2     PFFacebookUtils.linkUserInBackground(user, withReadPermissions: nil, {
3       (succeeded: Bool?, error: NSError?) -> Void in
4       if succeeded {
5         print("Woohoo, the user is linked with Facebook!")
6       }
7     })
8   }
```

## 6 - UnLinking

If you want to unlink Facebook from a user, simply do this:

```swift
1   PFFacebookUtils.unlinkUserInBackground(user, {
2     (succeeded: Bool?, error: NSError?) -> Void in
3     if succeeded {
4       print("The user is no longer associated with their Facebook account.")
5     }
6   })
```

