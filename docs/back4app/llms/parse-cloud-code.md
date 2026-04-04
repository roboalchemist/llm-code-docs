# Source: https://docs-containers.back4app.com/docs/android/parse-cloud-code.md

---
title: Cloud Code Functions
slug: docs/android/parse-cloud-code
description: In this guide you learn how to implement twitter login on your Android project
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-14T15:40:49.359Z
updatedAt: 2025-01-16T20:45:13.488Z
---

# How to create and deploy your Parse Cloud Code

## Introduction

For complex apps, sometimes you need a bit of logic that isn’t running on the mobile device. **Cloud Code** makes it possible.

Cloud Code is built on the same JavaScript SDK that powers thousands of apps. The only
difference is that this code runs in your Parse Server rather than running on the user’s
mobile device. When you update the Cloud Code, it becomes available to all mobile environments
instantly and you don’t have to wait until a new release of your application comes up. This lets you change
app behavior on the fly and also lets you add new features on your app faster.

This section explains how to create and deploy Cloud Code, followed by how to call a cloud function
in Android projects through Back4App.

Even if you’re only familiar with mobile development, we hope you’ll find Cloud Code
straightforward and easy to use.

:::hint{type="info"}
You can find more in-depth information in [**Parse Official Cloud Code Documentation**](https://docs.parseplatform.org/cloudcode/guide/).
:::

:::hint{type="info"}
**To complete this tutorial, we need:**

- [**Android Studio**](https://developer.android.com/studio/index.html)
- An app created on Back4App.
  - **Note:&#x20;**&#x46;ollow the [**New Parse App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse App on Back4App.
- An android app connected to Back4App.
  - **Note:&#x20;**&#x46;ollow the [**Install Parse SDK tutoria**](https://www.back4app.com/docs/android/parse-android-sdk)l to create an Android Studio Project connected to Back4App.
- A device (or[**&#x20;virtual device**](https://developer.android.com/studio/run/managing-avds.html)) running Android 4.0 (Ice Cream Sandwich) or newer.
:::

## 1 - Create a Cloud Code File

Create a new file and name it main.js and add the following Parse.Cloud.define function, which has its name and a callback as arguments.

:::hint{type="info"}
You can pass parameters to your Cloud function from your Android App and access then within the
&#x20;request.params object.
:::

:::CodeblockTabs
Parse Server 3.X

```javascript
//main.js
1   Parse.Cloud.define("test", (request) => {
2       var text = "hello world";
3       var jsonObject = {
4           "answer": text
5       };
6       return jsonObject
7   });
```

Parse Server 2.X

```javascript
//main.js
1   Parse.Cloud.define("test", function(request, response) {
2       var text = "hello world";
3       var jsonObject = {
4           "answer": text
5       };
6       response.success(jsonObject);
7   });
```
:::

## 2 - Upload to Cloud Code

1. Go to your App at [**Back4App website&#x20;**](https://www.back4app.com/)and click on Dashboard.
2. Find the Cloud Code and click on Functions & Web Hosting. It looks like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/0DZPwtZliAPrFFFKX5qZB_image.png)

3\. Upload or create a new file (you can also edit the current main.js file directly on the browser). Then, click at Deploy as shown here:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/AQkVxTJ2saNB_PnsEAvHs_image.png)

## 3 - Add Android Code

Import the following dependecies:

:::BlockQuote
*1   // Front End Dependencies*
2   import android.widget.Toas&#x74;**;**
*3   // Parse Dependencies*
4   import com.parse.FunctionCallbac&#x6B;**;**
5   import com.parse.ParseClou&#x64;**;**
6   import com.parse.ParseExceptio&#x6E;**;**
*7   // Java Dependencies*
8   import java.util.HashMa&#x70;**;**
9   import java.util.Ma&#x70;**;**
:::

To call your Cloud Code function, you need to call a special android function: ParseCloud.callFunctionInBackground.
Its first parameter is the **function name on Cloud Code** and the second one is the **HashMap**
that has every parameter that will be passed to the function. The third argument is the **callback**
that will be executed after the function has been called.

The following code calls the function:

```javascript
1   // Use this map to send parameters to your Cloud Code function
2   // Just push the parameters you want into it
3   Map<String, String> parameters = new HashMap<String, String>();
4
5   // This calls the function in the Cloud Code
6   ParseCloud.callFunctionInBackground("test", parameters, new FunctionCallback<Map<String, Object>>() {
7       @Override
8       public void done(Map<String, Object> mapObject, ParseException e) {
9           if (e == null) {
10              // Everything is alright
11              Toast.makeText(MainActivity.this, "Answer = " + mapObject.get("answer").toString(), Toast.LENGTH_LONG).show();
12          }
13          else {
14              // Something went wrong
15          }
16      }
17  });
```

:::hint{type="info"}
In this function, the mapObject has a key called answer, which contains the value hello world,
which will be printed on the screen by the Toast class when the code is executed.
:::

## It’s done!

At this stage, you are able to code and call your own Cloud Code in your Android App using Parse Server Core features through Back4App!
