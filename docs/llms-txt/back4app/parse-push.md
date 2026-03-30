# Source: https://docs-containers.back4app.com/docs/android/push-notifications/parse-push.md

---
title: from client side
slug: docs/android/push-notifications/parse-push
description: In this guide you learn how to send parse push from the client side
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-14T16:56:12.333Z
updatedAt: 2025-01-16T20:45:25.651Z
---

# Send Parse push notifications from client side

## Introduction

Client Push is a feature that is available on Back4App’s Parse API, however it is not
enabled by default due to security issues.

Enabling Client Push and allowing your App to
use its features is quite simple, but not encouraged. The main function of Client Push is
for debugging and test purposes.

In this tutorial an example app will be built and this is how it will look like:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/MiXeAo_L2BZYYjyi7Re5o_client-push.gif" signedSrc size="50" width="298" height="578" position="center" caption}

:::hint{type="success"}
At any time, you can access the complete Android Project built with this tutorial at our [**Github repository.**](https://github.com/back4app/android-cloud-code-push)
:::

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, we need:**

- [**Android Studio**](https://developer.android.com/studio/index.html)
- An app created on Back4App.
  - **Note:&#x20;**&#x46;ollow the [**New Parse App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse App on Back4App.
- An android app connected to Back4App.
  - **Note:&#x20;**&#x46;ollow the [**Install Parse SDK tutoria**](https://www.back4app.com/docs/android/parse-android-sdk)l to create an Android Studio Project connected to Back4App.
- A device (or[**&#x20;virtual device**](https://developer.android.com/studio/run/managing-avds.html)) running Android 4.0 (Ice Cream Sandwich) or newer.
:::

## 1 - Enable Client Push

1. Go to [**Back4App Website**](https://www.back4app.com/), log in, find your app and click on Server Settings.
2. Find the “Core Settings” block and click on SETTINGS. The “Core Settings” block looks like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/nF_OiqB6hiRbYzmlexEDn_image.png)

&#x20;    3\. Scroll to the end of the page and click on the EDIT DETAILS button, as shown below:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/YsCu9POQ8kNSYOLmVbtDI_image.png)

&#x20;   4\. You will see a checkbox called Allow Push Notification from Client in the end of the edit page, tick that box and click on the SAVE button, as shown below:



![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/2fBoraTPhR0mXsezJeGDz_image.png)

## 2 - Push from your app

1. At the beginning of your activity, import the following dependencies:

:::BlockQuote
*// Imports to the JSONObject object, necessary for the push message*
**import** org.json.JSONException;
**import** org.json.JSONObject;
*// Parse Dependencies*
**import** com.parse.ParsePush;
:::

2\. Use ParsePush to send the push message, as shown in the following code:

:::hint{type="info"}
Remember to set up the channels and the message.
:::

```json
1   JSONObject data = new JSONObject();
2   // Put data in the JSON object
3   try {
4    data.put("alert", "Back4App Rocks!");
5    data.put("title", "Hello from Device");
6   } catch ( JSONException e) {
7    // should not happen
8    throw new IllegalArgumentException("unexpected parsing error", e);
9   }
10  // Configure the push
11  ParsePush push = new ParsePush();
12  push.setChannel("News");
13  push.setData(data);
14  push.sendInBackground();
```

&#x20;    3\. To test the push notifications, just call that function while the device is opened.

## It’s done!

At this stage, you can send push notifications using your own device with Client Push through Back4App!

:::hint{type="info"}
**To learn more about Android push notification, see&#x20;**[**Parse Android Push Notification Official Documentation**](http://docs.parseplatform.org/android/guide/#push-notifications)**.**
:::

