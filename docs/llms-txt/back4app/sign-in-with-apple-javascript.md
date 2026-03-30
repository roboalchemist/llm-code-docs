# Source: https://docs-containers.back4app.com/docs/javascript/sign-in-with-apple-javascript.md

---
title: Sign In with Apple
slug: docs/javascript/sign-in-with-apple-javascript
description: In this tutorial you learn how to support Sign In with Apple to your Javascript project in a few easy steps.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-07T13:15:25.174Z
updatedAt: 2025-01-17T01:06:27.029Z
---

# Sign In with Apple - Javascript

## Introduction

In this section you learn how to get started with an Javascript template in a few easy steps.

## Prerequisites

:::hint{type="info"}
**To complete this quickstart, you need:**

- Set up Sign In with Apple in your Apple Developer account.
  - Follow the [**Sign In with Apple Tutorial**](https://www.back4app.com/docs/platform/sign-in-with-apple) to learn how to set up Sign In with Apple in your Apple Developer account.
:::

## 1 - Get the template

Clone or download the template at
[**Back4App’s GitHub repository**](https://github.com/back4app/SignInWithApple), open the Javascript foder.

## 2 - Open the project template

1. Open your editor choice.
2. Click on File=>Open
3. Navigate to the project folder and open the fileindex.html

## 3 - Edit the template

Find in the template the following function

```swift
1   AppleID.auth.init({
2       clientId : 'com.back4app.app.servicesid',
3       scope : 'email',
4       redirectURI: 'https://example-app.com/redirect',
5       state = random
6   });
```

and replace the values for the clientID and redirectURI for the values you set in your Services ID in your Apple Developer account.&#x20;

Save and close.

:::hint{type="info"}
See more at our [**New Parse App guide**](https://www.back4app.com/docs/get-started/new-parse-app#creating-new-app-find-your-appid).
:::

## 4 - Test your App

1. Open your browser of choice
2. Click onFile->Open
3. Wait until theSign in with Apple screen appears.
4. Click the button and do the login process.

If everything works properly, you should be redirected to your URI.

## Next Steps

At this point, you have learned how to get started with Javascript.

:::hint{type="success"}
Learn more by walking around our [**iOS Tutorials**](https://www.back4app.com/docs/ios/ios-app-template) or check [**Parse open source documentation for iOS SDK**](https://docs.parseplatform.org/ios/guide/).
:::

