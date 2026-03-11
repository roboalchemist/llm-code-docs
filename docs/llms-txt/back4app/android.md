# Source: https://docs-containers.back4app.com/docs/react-native/parse-sdk/push-notifications/android.md

---
title: Android Setup
slug: docs/react-native/parse-sdk/push-notifications/android
description: In this guide, you will learn how to send push notifications using Parse to your React Native App on Android
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-19T18:09:40.979Z
updatedAt: 2024-03-29T01:37:41.300Z
---

# Push Notifications for React Native on Android

## Introduction

This guide will teach you how to use Parse to send push notifications to your React Native application on Android. You will set up Firebase and configure your Back4App app to send them via dashboard and Cloud Code functions.

:::hint{type="success"}
At any time, you can access the complete Android Project built with this tutorial at our Github repositories

- [**JavaScript Example Repository**](https://github.com/templates-back4app/react-native-js-push-notifications)
- [**TypeScript Example Repository**](https://github.com/templates-back4app/react-native-ts-push-notifications)
:::

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- A React Native App created and [**connected to Back4App**](https://www.back4app.com/docs/react-native/parse-sdk/react-native-sdk).
- Understand how to [**deploy a cloud function**](https://www.back4app.com/docs/get-started/cloud-functions) on Back4App.
- An active account at Google, so you can use Google Firebase.
:::

## Goal

Send push notifications from Parse to a React Native application on Android, using Back4App’s dashboard and Cloud Code functions.

## 1 - Setting up Firebase

Firebase is the most used service provider for sending and receiving push notifications on Android. It’s used by a wide range of companies nowadays, together with the other various tools. Let’s start by creating a Firebase project for your app following steps 1 and 2 from [**this documentation**](https://firebase.google.com/docs/android/setup#console).

After creating your app and before exiting Firebase’s console, make sure to download and save the file google-services.json and also go to the project settings, over the “Cloud Messaging” tab and retrieve the following keys:

- **Server key;**
- **Sender ID.**

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/UX0EeTvU80dzhrLVfRPJW_image.png)

## 2 - Enabling Push Notifications on Back4App

To link your Firebase Project with Back4App and enable sending push notifications through your Dashboard and Cloud Code, follow these steps:

1. Go to [**Back4App Website**](https://www.back4app.com/), log in, find your app and click on Server Settings.
2. Find the “Android Push notification” block and click on SETTINGS > EDIT. The “Android Push notification” block looks like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/uytiokeM6FEsn1egTKByX_image.png)

&#x20;    3\. Add the FirebaseServer Keyto theAPI Keyfield and theSender IDto theGCM Sender IDfield.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/tUTrVpr6XQcBG2k4G-muV_image.png)

&#x20;    4\. Save it and you are done.

## 3 - Installing and Setting Up Dependencies

On your React Native project, let’s install the react-native-push-notification library, which will integrate the application with Firebase and enable you to handle any received notification. Run the following command on your project root directory:

:::BlockQuote
yarn add react-native-push-notification
:::

After installing it, you still need to add some configurations to the android/app/src/main/AndroidManifest.xml, android/build.gradle and android/app/build.gradle following the library [**docs**](https://github.com/zo0r/react-native-push-notification).

Make sure to also add in the AndroidManifest.xml file a meta-data containing the default notification channel id for your application(let’s use guideChannel as our example) . You can add the name directly to the directive or include it in the strings.xml file. Also, place your project’s google-services.json file at the android/app directory.

```xml
1	 <meta-data
2	      android:name="com.google.firebase.messaging.default_notification_channel_id"
3	      android:value="guideChannel" />
4	  <!-- OR -->
5	  <meta-data
6	      android:name="com.google.firebase.messaging.default_notification_channel_id"
7	      android:value="@string/default_notification_channel_id" />
```

In the next step, we will learn how to use this library and combine it with Parse.

## 4 - Handling Push Notifications

Let’s create a file with new methods related to push notifications called PushNotificationMethods.js (or PushNotificationMethods.tsx) and add the following function, that is responsible for initializing the react-native-push-notification, creating a notification channel, and also setting up Parse to recognize our device’s push configuration:

:::CodeblockTabs
JavaScript

```javascript
1	import PushNotification from 'react-native-push-notification';
2	import Parse from 'parse/react-native';
3	
4	const channelId = 'guideChannel';
5	
6	export async function configurePushNotifications() {
7	  // Initialize PushNotification
8	  await PushNotification.configure({
9	    // (required) Called when a remote is received or opened, or local notification is opened
10	    onNotification: function (notification) {
11	      // process the notification
12	      console.log('NOTIFICATION:', notification);
13	      // If notification is remote and has data, trigger local notification to show popup.
14	      // This is needed for Parse sent notifications because Firebase doesn't trigger popup
15	      // notifications with data by itself
16	      if (
17	        notification.data !== undefined &&
18	        notification.data.data !== undefined
19	      ) {
20	        try {
21	          // Notification data comes as a stringified JSON, so parsing is needed
22	          const notificationData = JSON.parse(notification.data.data);
23	          // JSON Parse notifications from the dashboard and Cloud Code
24	          // should contain the default `title` and `message` parameters
25	          let title = 'Notification Title';
26	          if (notificationData.title !== undefined) {
27	            title = notificationData.title;
28	          }
29	          let message = 'Noticiation Message';
30	          if (notificationData.message !== undefined) {
31	            message = notificationData.message;
32	          }
33	          // Text Parse notifications from the dashboard only have an `alert` parameter
34	          if (notificationData.alert !== undefined) {
35	            message = notificationData.alert;
36	          }
37	          PushNotification.localNotification({
38	            channelId: channelId,
39	            title: title,
40	            message: message,
41	          });
42	        } catch (error) {
43	          console.log(`Error triggering local notification ${error}`);
44	        }
45	      }
46	    },
47	
48	    onRegister: async function (token) {
49	      console.log(`Registered with device token ${token.token}`);
50	      let deviceToken = token.token;
51	
52	      // Create the notification channel, required for Android notifications
53	      await PushNotification.createChannel({
54	        channelId: channelId,
55	        channelName: 'Guide channel',
56	      });
57	      console.log('Notification channel created!');
58	
59	      // Create a Parse Installation, that will link our application's push notification
60	      // to the Parse server
61	      try {
62	        const installationId = await Parse._getInstallationId();
63	        const Installation = new Parse.Installation();
64	        // Make sure to change any needed value from the following
65	        Installation.set('deviceType', 'android');
66	        Installation.set('GCMSenderId', 'YOUR_GCM_SENDER_ID');
67	        Installation.set('pushType', 'gcm');
68	        Installation.set('appIdentifier', 'YOUR_APP_IDENTIFIER(PACKAGE_NAME)');
69	        Installation.set('parseVersion', '3.2.0');
70	        Installation.set('appName', 'Back4AppGuidePushNotifications');
71	        Installation.set('appVersion', '1.0');
72	        Installation.set('localeIdentifier', 'pt-BR');
73	        Installation.set('badge', 0); // Set initial notification badge number
74	        Installation.set('timeZone', 'America/Sao_Paulo');
75	        Installation.set('installationId', installationId);
76	        Installation.set('channels', [channelId]);
77	        Installation.set('deviceToken', deviceToken);
78	        await Installation.save();
79	        console.log(`Created new Parse Installation ${Installation}`);
80	      } catch (error) {
81	        console.log(error.message);
82	      }
83	    },
84	    popInitialNotification: true,
85	    requestPermissions: true,
86	  });
87	}
```

```typescript
1	import PushNotification from 'react-native-push-notification';
2	import Parse from 'parse/react-native';
3	
4	const channelId: string = 'guideChannel';
5	
6	export async function configurePushNotifications() {
7	  // Initialize PushNotification
8	  await PushNotification.configure({
9	    // (required) Called when a remote is received or opened, or local notification is opened
10	    onNotification: function (notification: object) {
11	      // process the notification
12	      console.log('NOTIFICATION:', notification);
13	      // If notification is remote and has data, trigger local notification to show popup.
14	      // This is needed for Parse sent notifications because Firebase doesn't trigger popup
15	      // notifications with data by itself
16	      if (
17	        notification.data !== undefined &&
18	        notification.data.data !== undefined
19	      ) {
20	        try {
21	          // Notification data comes as a stringified JSON, so parsing is needed
22	          const notificationData = JSON.parse(notification.data.data);
23	          // JSON Parse notifications from the dashboard and Cloud Code
24	          // should contain the default `title` and `message` parameters
25	          let title: string = 'Notification Title';
26	          if (notificationData.title !== undefined) {
27	            title = notificationData.title;
28	          }
29	          let message: string = 'Noticiation Message';
30	          if (notificationData.message !== undefined) {
31	            message = notificationData.message;
32	          }
33	          // Text Parse notifications from the dashboard only have an `alert` parameter
34	          if (notificationData.alert !== undefined) {
35	            message = notificationData.alert;
36	          }
37	          PushNotification.localNotification({
38	            channelId: channelId,
39	            title: title,
40	            message: message,
41	          });
42	        } catch (error: any) {
43	          console.log(`Error triggering local notification ${error}`);
44	        }
45	      }
46	    },
47	
48	    onRegister: async function (token: {os: string; token: string}) {
49	      console.log(`Registered with device token ${token.token}`);
50	      let deviceToken: string = token.token;
51	
52	      // Create the notification channel, required for Android notifications
53	      await PushNotification.createChannel({
54	        channelId: channelId,
55	        channelName: 'Guide channel',
56	      });
57	      console.log('Notification channel created!');
58	
59	      // Create a Parse Installation, that will link our application's push notification
60	      // to the Parse server
61	      try {
62	        const installationId = await Parse._getInstallationId();
63	        const Installation = new Parse.Installation();
64	        // Make sure to change any needed value from the following
65	        Installation.set('deviceType', 'android');
66	        Installation.set('GCMSenderId', 'YOUR_GCM_SENDER_ID');
67	        Installation.set('pushType', 'gcm');
68	        Installation.set('appIdentifier', 'YOUR_APP_IDENTIFIER(PACKAGE_NAME)');
69	        Installation.set('parseVersion', '3.2.0');
70	        Installation.set('appName', 'Back4AppGuidePushNotifications');
71	        Installation.set('appVersion', '1.0');
72	        Installation.set('localeIdentifier', 'pt-BR');
73	        Installation.set('badge', 0); // Set initial notification badge number
74	        Installation.set('timeZone', 'America/Sao_Paulo');
75	        Installation.set('installationId', installationId);
76	        Installation.set('channels', [channelId]);
77	        Installation.set('deviceToken', deviceToken);
78	        await Installation.save();
79	        console.log(`Created new Parse Installation ${Installation}`);
80	      } catch (error) {
81	        console.log(error.message);
82	      }
83	    },
84	    popInitialNotification: true,
85	    requestPermissions: true,
86	  });
87	}
```
:::

:::hint{type="info"}
**Open Source Documentation**
More information about the Parse.Installation class can be found [**here**](https://docs.parseplatform.org/js/guide/#push-notifications).
:::

Note that the event handler onNotification method has a code that triggers a local notification in the app after receiving a remote one. Parse requires this code because Firebase doesn’t trigger popup notifications with data by itself. More on that and Android notification types can be read [**here**](https://firebase.google.com/docs/cloud-messaging/concept-options#notifications_and_data_messages).

Call this configurePushNotifications method in your App.js (or App.tsx) file after initializing Parse and before declaring your App content.

:::CodeblockTabs
App.js

```javascript
1	// Other imports
2	// ...
3	import {configurePushNotifications} from './src/PushNotificationMethods';
4	
5	// Your Parse initialization configuration goes here
6	// ...
7	
8	// Initialize PushNotifications
9	configurePushNotifications();
```
:::

Build and run the application. You can now see an Installation table in your app’s Back4App dashboard with an entry corresponding to your app.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/ZC2-pd0RZQlBAl3DW7c9d_image.png)

## 5 - Sending Push Notifications via Dashboard

We are now ready to send the first push notification to our app. Follow the steps below to send a push message via Back4App’s Dashboard:

1. Go to [**Back4App Website**](https://www.back4app.com/), log in, find your app and click on Dashboard.
2. Click on Push > Send New Push and create an audience for your push notification.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/ily4bGb7Ftx038Bgvkmmc_image.png)

&#x20;    3\. Write your message and look at the preview by clicking on the Android option.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/0Pl7dwnpiZZgUlYcrwsD3_image.png)

&#x20;    4\. If you have already reviewed the push notification and you want to send it, click on Send push.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/iekjy_NEACTLvOjNUR-Yl_image.png)

:::hint{type="info"}
You may explore the other options for Push Notification at Parse Dashboard.
There, it’s also possible to look at Past Pushes you sent and the Audiences you created for them.
:::

## 6 - Sending Push Notifications via Cloud Code

Using [**Cloud functions starter guide**](https://www.back4app.com/docs/get-started/cloud-functions), you can detach reusable methods from your front-end and get complete control of all your backend resources via the master key.

Let’s use cloud code functions to send a push message. First, create a cloud function called sendPush which calls the Parse.Push.send method. There are two ways to select which users will receive the notification: querying the Parse.Installation class or via notification channel names. It’s more common in Android Apps to use channels to distinguish between the users, so let’s use it. Make sure to deploy this function on Back4App before go ahead.

:::hint{type="info"}
**Open Source Documentation**
Please check the [**open source documentation**](https://docs.parseplatform.org/js/guide/#sending-options) for more details about the send method.
:::

```javascript
1	Parse.Cloud.define('sendPush', async (request) => {
2	  try {
3	    await Parse.Push.send({
4	      channels: [ 'guideChannel' ],
5	      data: {
6	        message: 'Test message',
7	        title: 'Back4App Guide Notification'
8	      }
9	    }, { useMasterKey: true });
10	    return true;
11	  } catch (error) {
12	    return `Error: ${error}`
13	  }
14	});
```

Let’s now call the function from the React Native app. Add this function to the PushNotificationMethods.js (or PushNotificationMethods.tsx) file and call it in a button inside your application’s main screen:

```javascript
1	export async function sendNotification() {
2	  try {
3	    await Parse.Cloud.run('sendPush');
4	    console.log('Success!');
5	  } catch (error: any) {
6	    console.log(`Error: ${error}`);
7	  }
8	}
```

:::hint{type="info"}
Note that this case of allowing a user to trigger a push notification by himself is not common, we used it here just to show how simple it is to integrate the push notification sending with Parse.
:::

## Conclusion

At the end of this guide, you learned how to send Push Notifications using Parse to your React Native application on Android. In the next guide, you will learn how to send them on iOS.
