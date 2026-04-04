# Source: https://docs-containers.back4app.com/docs/android/push-notifications/parse-server-push-notifications.md

---
title: via Dashboard
slug: docs/android/push-notifications/parse-server-push-notifications
description: In this guide you learn how to setup push notifications on your Android project
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-14T15:47:50.638Z
updatedAt: 2025-01-17T01:32:41.455Z
---

# Parse Server push notifications setup

## Introduction

This section explains how you can send push notifications using Firebase Cloud Messaging and Parse Dashboard through Back4App.

This is how it will look like:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/qgiN9Mi67yrzjVKNjEgE5_push-dashboard.gif" signedSrc size="50" width="296" height="580" position="center" caption}

:::hint{type="success"}
At any time, you can access the complete Android Project built with this tutorial at our Github repositories

- [**Kotlin Example Repository**](https://github.com/templates-back4app/Android-Parse-Sdk-Kotlin)
- [**Java Example Repository**](https://github.com/templates-back4app/Android-Parse-Sdk-Java)
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

## **1 - Link your Firebase Project with your Android Studio Project**

To send push notifications through your Dashboard, you will have to create a Project at [**Firebase Website**](https://firebase.google.com/) and link it to your Android Studio Project. To do so, follow the steps described below:

:::hint{type="danger"}
Pay attention to the steps below because you are not going to follow exactly the same steps that Firebase suggests.
:::

1. Go to [**Firebase Website&#x20;**](https://firebase.google.com/)and log in with a Google Account.
2. At Firebase Website, in the right corner click on GO TO CONSOLE and click on Add Project, then give your Project a name follow the steps to create a new project.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/I3KkZ46BVYCT6f5UOYDnt_screenshot-2024-05-28-at-145828.png)



&#x20;    3\. Then, connect your Android Studio Project to the Firebase Project you created. To do so, click on the Android icon, as shown in the following image.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/odAIcQRq04N36D_9J7mJr_screenshot-2024-05-28-at-150040.png)

&#x20;    4\. You will be asked to inform the package name of your Android Studio Project, as shown in the following image.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/ZKZpUf_WbXD_-YHI7CF4X_screenshot-2024-05-28-at-150111.png)

&#x20;    5\. To discover the package name of your Android Studio Project, leave the Firebase page opened and go to your Project in Android Studio and go to app > manifest > AndroidManifest.xml. In your manifest file you will be able to find the package name of your project, as you can see in the image below.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/m-lB5DO7DC2sTHUwgYaQz_image.png)

&#x20;    6\. Copy the package name in the required box at the Firebase page. You can also fill the other fields, but they are optional. After that, click on the Register app button.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/1A7UC2lK1q11Na87mvzyp_screenshot-2024-05-28-at-150207.png)

7\. Now, you have to download google-services.json file and move it to your Android Studio project module root directory.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/wqNQs8uAMWr_HWf3U3RDi_screenshot-2024-05-28-at-150237.png)

:::BlockQuote
1    classpath 'com.google.gms\:google-services\:latest.version.here'
:::

&#x20;    9\. After that, go to the build.gradle (Module\:app) file and, on the top of the file, add the code below.

:::BlockQuote
1    apply plugin: 'com.google.gms.google-services'
:::

&#x20;   10\. Continue on the build.gradle (Module\:app)\` file and add these lines of code

:::BlockQuote
*1   // Don't forget to change the line below with the latest versions of Firebase SDKs*
2     implementation 'com.google.firebase\:firebase-core\:latest.version.here'
3     implementation 'com.google.firebase\:firebase-messaging\:latest.version.here'
:::

:::hint{type="danger"}
Don’t forget to change these lines with the latest versions of Firebase SDKs.
:::

## 2 - Link your Firebase Project with Back4App

To link your Firebase Project with Back4App and easily send push notification through your Dashboard, simply follow these steps:

1. Go to [**Back4App Website**](https://www.back4app.com/), log in, find your app and click on Server Settings.
2. Find the “Android Push notification” block and click on SETTINGS > EDIT. The “Android Push notification” block looks like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/WtdLo5lTTQjr61nyGZnps_image.png)

&#x20;    3\. Leave the *Back4App Android Push Notification&#x20;*&#x70;age you visited opened and go to your project on the [**Firebase Website.**](https://firebase.google.com/)

&#x20;    4\. Click on the settings icon and then the Project Settings button, as shown below.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/rt8h-mSbpZzytrp05JixG_screenshot-2024-05-28-at-150316.png)

5\. Click on CLOUD MESSAGING and then on `Manage Service Accounts`.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/vEgYzTj2KGfZ5YGi1-D_Z_screenshot-2024-05-28-at-150402.png)

&#x20;    6\. Click on `Manage details` (under Actions).

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/u-2oRp7O1LzRYd5O9TUrE_screenshot-2024-05-28-at-150721.png)

&#x20;    7\. Go to `Keys` > `ADD KEY` > `Create new key`.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/mCdi_aNLu47qzDfncy_J6_screenshot-2024-05-28-at-150842.png)

&#x20;    8\. Choose the JSON Format and create.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/0nTbeaA_qfR2sYpNobZp8_screenshot-2024-05-28-at-151008.png)

&#x20;    9\. To set up your Service Account Configuration, click on the `Set Up Push Settings` button

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/uMbwX3vw5KoDzzfqtcsOV_screenshot-2024-05-28-at-151227.png)

&#x20;    10\. To finish the configuration, click on the Choose File button and select the JSON file you got from Firebase and NEXT.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/19Dpf38IqJtWvGvUHsAEv_screenshot-2024-05-28-at-151547.png)



## 3 - Set up the Manifest File

1. Open your Project at Android Studio and go to app > manifest > AndroidManifest.xml. In this file, use the code below right after the meta-data tags that are inside the application tag:

```xml
1   <meta-data android:name="com.parse.push.gcm_sender_id"
2              android:value="INSERT_YOUR_SENDER_ID" />
```

:::hint{type="danger"}
Don’t forget to insert theGCM Sender IDyou obtained at Firebase in this line of code.
:::

&#x20;    2\. Use the following code right before the application tag ends:

:::CodeblockTabs
AndroidX

```xml
1   <service android:name="com.parse.fcm.ParseFirebaseMessagingService" android:exported="false">
2           <intent-filter>
3               <action android:name="com.google.firebase.MESSAGING_EVENT"/>
4           </intent-filter>
5       </service>
6
7       <receiver android:name="com.parse.ParsePushBroadcastReceiver" android:exported="false">
8          <intent-filter>
9              <action android:name="com.parse.push.intent.RECEIVE" />
10             <action android:name="com.parse.push.intent.OPEN" />
11             <action android:name="com.parse.push.intent.DELETE" />
12         </intent-filter>
13      </receiver>
```

Android

```xml
1   <service android:name="com.parse.fcm.ParseFirebaseInstanceIdService" android:exported="false">
2         <intent-filter>
3         <action android:name="com.google.firebase.INSTANCE_ID_EVENT" />
4         </intent-filter>
5      </service>
6
7      <service
8          android:name="com.parse.fcm.ParseFirebaseMessagingService" android:exported="false">
9          <intent-filter>
10              <action android:name="com.google.firebase.MESSAGING_EVENT"/>
11          </intent-filter>
12      </service>
13
14      <receiver android:name="com.parse.ParsePushBroadcastReceiver" android:exported="false">
15         <intent-filter>
16             <action android:name="com.parse.push.intent.RECEIVE" />
17             <action android:name="com.parse.push.intent.OPEN" />
18             <action android:name="com.parse.push.intent.DELETE" />
19         </intent-filter>
20      </receiver>    
```
:::

&#x20;Use the following permissions right after theuses-permission tags that you placed to allow your app to have access to internet.

```xml
1   <uses-permission android:name="android.permission.WAKE_LOCK" />
2   <uses-permission android:name="android.permission.VIBRATE" />
3   <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
4   <uses-permission android:name="android.permission.GET_ACCOUNTS" />
5   <uses-permission android:name="com.google.android.c2dm.permission.RECEIVE" />
```

:::hint{type="info"}
You added permissions to allow internet access in the [**Install Parse SDK Tutorial**](https://www.back4app.com/docs/android/parse-android-sdk) instructions. If you didn’t, access Install Parse SDK Tutorial and follow its steps.
:::

## 4 - Set up build.gradle (Module: app)

Install the Parse FCM SDK and the Parse Bolts SDK for Android. To do so, open build.gradle (Module: app) and add the code below in the dependecies\{} tag.

:::BlockQuote
*1    // Don't forget to change the lines belows with the latest versions these SDKs*
2    implementation "com.github.parse-community.Parse-SDK-Android\:fcm\:latest.version.here"
3    implementation 'com.parse.bolts\:bolts-android\:latest.version.here'
:::

:::hint{type="danger"}
Don’t forget to change these lines with the latest versions of these SDKs.
:::

:::hint{type="danger"}
If you are not using AndroidX, you cannot use the latest version. [**Check the changelog**](https://github.com/parse-community/Parse-SDK-Android/blob/master/CHANGELOG.md)
:::

## 5 - Create an installation

Every Parse application installed on a device registered for push notifications has an associated Installation object that stores all the data needed to target push notifications.

In Android, Installation objects are available through the ParseInstallation class. This class uses the same API for storing and retrieving data. To access the current Installation object from your Android app, use the ParseInstallation.getCurrentInstallation() method.

In the first time you save a ParseInstallation, Parse will add it to your Installation class and it will be available for targeting push notifications.

To create a ParseInstallation in your app, go to your Android Studio Project and in the Java file called App that extends Application that you created to initialize the Parse SDK, on its onCreate method, right after Parse.initialize() call, use the following code to create a ParseInstallation.

:::BlockQuote
**1    ParseInstallation** installation **=** **ParseInstallation.**&#x67;etCurrentInstallatio&#x6E;**();**
2    installatio&#x6E;**.**&#x70;u&#x74;**(**"GCMSenderId"**,** INSERT\_YOUR\_SENDER\_I&#x44;**);**
3    installatio&#x6E;**.**&#x73;aveInBackgroun&#x64;**();**
:::

:::hint{type="danger"}
Don’t forget to insert theGCM Sender IDyou obtained at Firebase in the code above.
:::

:::hint{type="danger"}
If you don’t have an App.java file as described in this step, access the [**Install Parse SDK for Android**](https://www.back4app.com/docs/android/parse-android-sdk) documentation and make sure that you have followed all the steps required to install Parse SDK correctly. If you do not install Parse SDK properly your facebook login with Parse will not work.
:::

## 6 - Test your app

1. Go to [**Back4App Website**](https://www.back4app.com/), log in, find your app and click on Dashboard.

2. Click on  > Push > Send New Push and create an audience for your push notification.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/9T7-Hr7t1iKy0CEKSUBVC_screenshot-2024-05-28-at-152236.png)

&#x20;    3\. Write your message and look at the preview by clicking at the Android option.

&#x20;    4\. If you already reviewed the push notification and you want to send it, click onSend push.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/nYqE52F-L0uOrmNsZnuzc_screenshot-2024-05-28-at-152459.png)

:::hint{type="info"}
You may explore the other options for Push Notification at Parse Dashboard.
There, it’s also possible to look at Past Pushes you sent and the Audiences you created for them.
:::

## It’s done!

At this stage, you can send push notifications using the Parse Dashboard through Back4App!
