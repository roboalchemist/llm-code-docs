# Source: https://docs-containers.back4app.com/docs/android/push-notifications/parse-push-notifications.md

---
title: using Cloud Code
slug: docs/android/push-notifications/parse-push-notifications
description: In this guide you learn how to send push notifications using a cloud function
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-14T16:22:20.876Z
updatedAt: 2025-01-16T20:45:22.787Z
---

# Send Parse push notifications using Cloud Code

## Introduction

This section explains how you can send push notifications using Cloud Code through Back4App.

This is how it will look like:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/EiFlOChZLMHV5aMdWSbrr_push-cloud-code.gif" signedSrc size="50" width="290" height="580" position="center" caption}

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
- Follow the **Steps 1** to **5** of [**Back4App Push Notification via Dashboard tutorial**](https://www.back4app.com/docs/android/push-notifications/parse-server-push-notifications) carefully to set up Push Notifications to your app.
- A device (or[**&#x20;virtual device**](https://developer.android.com/studio/run/managing-avds.html)) running API level 27 or newer.
:::

## 1 - Set up Android to receive push

Every Parse application installed on a device registered for push notifications has an
associated Installation object. The Installation object is where you store all the data needed to target push notifications. For example, in your app, you could store which
teams one of your users is interested in to send updates about their performance. Saving the Installation object is also required for tracking push-related app open events.

The simplest way to start sending notifications is using channels. This allows you to use a
publisher-subscriber model for sending pushes. Devices start by subscribing to one or more channels, and notifications can later be sent to these subscribers. The channels subscribed to by a given Installation are stored in the channels field of the Installation object.

To start working with push notifications, the following steps are required:

:::hint{type="info"}
If you downloaded our [**project template**](https://github.com/back4app/android-cloud-code-push), don’t forget to change your credentials in the app/src/main/res/values/string.xml file and the GCMSenderId that you obtained at Firebase in the AndroidManifest.xml file.
:::

1. Import the following dependecies:

:::BlockQuote
*1   // Java Dependencies*
2   import java.util.ArrayLis&#x74;**;**
*3   // Parse Dependencies*
4   import com.parse.Pars&#x65;**;**
5   import com.parse.ParseInstallatio&#x6E;**;**
:::

&#x20;    2\. Initialize Parse with Parse.initialize(this).

&#x20;    3\. Create a new array of channels and put the channels you would like to subscribe. In this example, the News channel is created.

&#x20;   4\.  Add to your installation your GCMSenderId, obtained from the [**Firebase Console**](https://console.firebase.google.com/?pli=1), through the command installation.put("GCMSenderId", "YOUR\_FIREBASE\_GCM\_SENDER\_ID\_HERE").

:::hint{type="info"}
To know how you can obtain that key, look at **Step 1** of [**Push Notifications via Dashboard tutorial**](https://www.back4app.com/docs/android/push-notifications/parse-server-push-notifications).
:::

&#x20;    5\. Add the channels object to the installation through the command installation.put("channels", channels).

&#x20;    6\. Save the installation to your database through installation.saveInBackground().

The following code executes these steps:

```java
1   Parse.initialize(this);
2   ArrayList<String> channels = new ArrayList<>();
3   channels.add("News");
4   ParseInstallation installation = ParseInstallation.getCurrentInstallation();
5   // don't forget to change the line below with the sender ID you obtained at Firebase
6   installation.put("GCMSenderId", "YOUR_FIREBASE_GCM_SENDER_ID_HERE");
7   installation.put("channels", channels);
8   installation.saveInBackground();
```

## 2 - Create your Cloud Code

:::hint{type="info"}
To know more about how to get started with **Cloud Code&#x20;**&#x6C;ook at [**Cloud Code for Android Tutorial**](https://www.back4app.com/docs/get-started/cloud-functions).
:::

1. Create a .jsfile to put your Cloud Code into. In this example, a main.js file is created.
2. Define a Cloud function, using Parse.Cloud.Define, to call the push notification. In this example, this function is called Parse.Push.Send.

:::hint{type="danger"}
It is required to use the **master key&#x20;**&#x69;n this operation.
:::

The following code executes these steps:

:::CodeblockTabs
Parse Server 3.X

```javascript
//main.js
1   Parse.Cloud.define("pushsample", (request) => {
2
3       return Parse.Push.send({
5           channels: ["News"],
6           data: {
7               title: "Hello from the Cloud Code",
8               alert: "Back4App rocks!",
9           }
10      }, { useMasterKey: true });
11  });
```

Parse Server 2.X

```javascript
//main.js
1   Parse.Cloud.define("pushsample", function (request, response) {
2       Parse.Push.send({
3               channels: ["News"],
4               data: {
5                   title: "Hello from the Cloud Code",
6                   alert: "Back4App rocks!",
7               }
8          }, {
9               success: function () {
10                  // Push was successful
11                  response.success("push sent");
12                  console.log("Success: push sent");
13              },
14              error: function (error) {
15                  // Push was unsucessful
16                  response.error("error with push: " + error);
17                  console.log("Error: " + error);
18              },
19              useMasterKey: true
20         });
21  });
```
:::

## 3 - Upload to Cloud Code

1. Go to your App at [**Back4App website&#x20;**](https://www.back4app.com/)and click on Dashboard.
2. Find the Cloud Code and click on Functions & Web Hosting. It looks like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/ncvuU4Sq-UW5g8-GZWOBi_image.png)

3\. Upload or create a new file (you can also edit the current main.js file directly on the browser). Then, click at Deploy as shown here:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/8MGNrzcB4wdH4-klh9QcY_image.png)

## 4 - Call Cloud Code from Android App

1. Import the following dependencies:

:::BlockQuote
*1   // Java Dependencies*
2   import java.util.HashMa&#x70;**;** *// This includes the HasMap Object that the 4       Cloud function needs to call*
*3   // Parse Dependencies*
4   import com.parse.FunctionCallbac&#x6B;**;**
5   import com.parse.ParseClou&#x64;**;**
6   import com.parse.ParseExceptio&#x6E;**;**&#x20;
:::

&#x20;    2\. Call the ParseCloud.callFunctionInBackground on the pushsample cloud function:

```java
1   final HashMap<String, String> params = new HashMap<>();
2   // Calling the cloud code function
3   ParseCloud.callFunctionInBackground("pushsample", params, new FunctionCallback<Object>() {
4    @Override
5    public void done(Object response, ParseException exc) {
6        if(exc == null) {
7            // The function was executed, but it's interesting to check its response
8            alertDisplayer("Successful Push","Check on your phone the notifications to confirm!");
9        }
10       else {
11           // Something went wrong
12           Toast.makeText(MainActivity.this, exc.getMessage(), Toast.LENGTH_LONG).show();
13       }
14   }
15  });
```

::::hint{type="info"}
The alertDisplayer method used in the example above is the following:

:::BlockQuote
**1   private** **void** **alertDisplayer(String** titl&#x65;**,String** messag&#x65;**)\{**
2      **AlertDialog.**&#x42;uilder builder **=** **newAlertDialog.**&#x42;uilde&#x72;**(MainActivity.**&#x74;hi&#x73;**)**
3      **.**&#x73;etTitl&#x65;**(**&#x74;itl&#x65;**)**
4      **.**&#x73;etMessag&#x65;**(**&#x6D;essag&#x65;**)**
5      **.**&#x73;etPositiveButto&#x6E;**(**"OK"**,** **new** **DialogInterface.**&#x4F;nClickListene&#x72;**()** **\{**
6                 @Override
7                 **public** **void** **onClick(DialogInterface** dialo&#x67;**,** **int** whic&#x68;**)** **\{**
8                     dialo&#x67;**.**&#x63;ance&#x6C;**();**
9                 **}**
10             **});**
11     **AlertDialog** ok **=** builde&#x72;**.**&#x63;reat&#x65;**();**
12     o&#x6B;**.**&#x73;ho&#x77;**();**
13   **}**
:::
::::

&#x20;   3\. Test if the push notifications are being sent by calling the function above while the device is opened.

## 5 - Call Cloud Code from REST API

The REST API provides a quick and easy way to test if your Cloud function is working.
Just use the code below in your terminal or command prompt:

:::hint{type="info"}
Click on to know more about how to get started with command line in [**Linux**](https://www.digitalocean.com/community/tutorials/an-introduction-to-the-linux-terminal), [**MacOS**](https://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line) or [**Windows**](https://www.bleepingcomputer.com/tutorials/windows-command-prompt-introduction/).
:::

:::BlockQuote
curl -X POST -H "X-Parse-Application-Id: YOUR\_APP\_ID\_HERE" \\
-H "X-Parse-REST-API-Key: YOUR\_REST\_API\_KEY\_HERE" \\
-H "Content-Type: application/json" \\
-d '\{ // Put the function parameters here in JSON format }' \\
https\://parseapi.back4app.com/functions/pushsample
:::

To test the push notifications, just use the REST code while the device is opened.

## It’s done!

At this stage, you can send push notifications using Cloud Code through Back4App!
