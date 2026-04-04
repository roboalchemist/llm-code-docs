# Source: https://docs-containers.back4app.com/docs/ios/twitter-login-ios-swift.md

---
title: Twitter login
slug: docs/ios/twitter-login-ios-swift
description: In this tutorial you learn how to add Twitter login to your ios app using Swift.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-12T11:20:36.945Z
updatedAt: 2025-01-16T21:00:17.553Z
---

# Add Twitter login to your iOS App using Swift

## Introduction

This section explains how you can create an app with user registration using Twitter Login and [**Parse Server core features**](https://www.back4app.com/product/parse-server) through Back4App.

## Prerequisites

:::hint{type="info"}
**To complete this quickstart, you need:**

- [**Xcode**](https://developer.apple.com/xcode/).
- An app created at Back4App.
  - Follow the [**New Parse App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse app at Back4App.
- An iOS app connected to Back4App.
  - **Note:&#x20;**&#x46;ollow the [**Install Parse SDK (ObjC) Tutorial**](https://www.back4app.com/docs/ios/parse-objc-sdk) to create an Xcode Project connected to Back4App.
:::

## 1 - Twitter Set up

To start using Twitter functions, you need to:

1. Go to [**Twitter Application Management Website**](https://twitter.com/login?redirect_after_login=https%3A%2F%2Fdeveloper.twitter.com%2Fapps), sign in with a Twitter account and click on Create New App.
2. Add your application’s Twitter consumer key on your Parse application’s settings page.
3. When asked to specify a “Callback URL” for your Twitter app, please insert a valid URL likehttp\://twitter-oauth.callback. This value will not be used by your iOS or Android application, but is necessary in order to enable authentication through Twitter.
4. Add the  and Social.framework libraries to your Xcode project.
5. Add the following where you initialize the Parse SDK, such as  inapplication\:didFinishLaunchingWithOptions:

```swift
1   PFTwitterUtils.initializeWithConsumerKey("YOUR CONSUMER KEY",  consumerSecret:"YOUR CONSUMER SECRET")
```

## 2 - Login and SignUP

PFTwitterUtils provides a way to allow your PFUsers to log in or sign up through Twitter. This is accomplished using the logInWithBlock or logInWithTarget messages:

```swift
1   PFTwitterUtils.logInWithBlock {
2     (user: PFUser?, error: NSError?) -> Void in
3     if let user = user {
4       if user.isNew {
5         print("User signed up and logged in with Twitter!")
6       } else {
7         print("User logged in with Twitter!")
8       }
9     } else {
10      print("Uh oh. The user cancelled the Twitter login.")
11    }
12  }
```

When this code is run, the following happens:

1. The user is shown the Twitter login dialog.
2. The user authenticates via Twitter, and your app receives a callback.
3. Our SDK receives the Twitter data and saves it to a PFUser. If it’s a new user based on the Twitter handle, then that user is created.
4. Yourblock is called with the user.

## 3 - Twitter Linking

If you want to associate an existing PFUser with a Twitter account, you can link it like so:

```swift
1   if !PFTwitterUtils.isLinkedWithUser(user) {
2     PFTwitterUtils.linkUser(user, {
3       (succeeded: Bool?, error: NSError?) -> Void in
4       if PFTwitterUtils.isLinkedWithUser(user) {
5         print("Woohoo, user logged in with Twitter!")
6       }
7     })
8   }
```

The steps that happen when linking are very similar to log in. The difference is that on successful login, the existing PFUser is updated with the Twitter information. Future logins via Twitter will now log the user into their existing account.

If you want to unlink Twitter from a user, simply do this:

```swift
1   PFTwitterUtils.unlinkUserInBackground(user, {
2     (succeeded: Bool?, error: NSError?) -> Void in
3     if error == nil && succeeded {
4       print("The user is no longer associated with their Twitter account.")
5     }
6   })
```

## 6 - Twitter API calls

Our SDK provides a straightforward way to sign your API HTTP requests to the [**Twitter REST API**](https://dev.twitter.com/rest/public) when your app has a Twitter-linked PFUser. To make a request through our API, you can use the PF\_Twitter singleton provided by PFTwitterUtils:

```swift
1   let verify = NSURL(string: "https://api.twitter.com/1.1/account/verify_credentials.json")
2   var request = NSMutableURLRequest(URL: verify!)
3   PFTwitterUtils.twitter()!.signRequest(request)
4   let task = NSURLSession.sharedSession().dataTaskWithRequest(request) { data, response, error in
5     // Check for error
6     // Data will contain the response data
7   }
8   task.resume()
```

