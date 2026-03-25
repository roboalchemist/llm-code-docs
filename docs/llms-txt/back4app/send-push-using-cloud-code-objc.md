# Source: https://docs-containers.back4app.com/docs/ios/push-notifications/send-push-using-cloud-code-objc.md

---
title: using CC and ObjC
slug: docs/ios/push-notifications/send-push-using-cloud-code-objc
description: In this guide you learn how to setup push notifications on your iOS project
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-12T12:07:05.104Z
updatedAt: 2025-01-16T21:00:31.730Z
---

# Sending push notifications using cloud code with Objective-C

## Introduction

This section explains how you can send push notifications using Cloud Code through Back4App.

This is how it will look like:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/wKKlp6QQvyOFUTlwBBriR_image.png" signedSrc size="40" width="640" height="1136" position="flex-start" caption}

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
- An iOS app set up via [**Back4App Push Notifications via Dashboard tutorial**](https://www.back4app.com/docs/ios/push-notifications/best-ios-push-notification-service).
- An iOS device, iphone or ipad, running iOS 10 or newer.
- A paid Apple developer Account.
:::

## 1 - Set up your iOS app to receive push

Every Parse application installed on a device registered for push notifications has an associated Installation object. The Installation object is where you store all the data needed to target push notifications. For example, in your app, you could store which teams one of your users is interested in to send updates about their performance. Saving the Installation object is also required for tracking push-related app open events.

The simplest way to start sending notifications is using channels. This allows you to use a publisher-subscriber model for sending pushes. Devices start by subscribing to one or more channels, and notifications can later be sent to these subscribers. The channels subscribed to by a given Installation are stored in the channels field of the Installation object.

After that we will go over sending targeted push notifications to a single user or to a group of users based on a query.

:::hint{type="danger"}
Going forward we are going to assume you have completed all steps of the[**&#x20;Back4App Push Notifications via Dashboard tutorial**](https://www.back4app.com/docs/ios/push-notifications/best-ios-push-notification-service), even if you use the iOS Project built with this tutorial that is available at our [**GitHub repository**](https://github.com/mpc20001/ios-objc-push-cloud-code).
You should have basic push notifications working and also be able to send pushes out via the admin console.
:::

## 2 - Subscribe your device to the News channel

1. First we will add a channel to your installation object. We are going to do this by altering the method createInstallationOnParse in our App Delegate file. Open your project’s AppDelegate.m file, and add make sure your version of didRegisterForRemoteNotificationsWithDeviceToken is the same as the code below. We are adding one new line of code - ‘\[currentInstallation setObject:@\[@”News1”] forKey:@”channels”];’ - which will set the installation object’s channel array to contain one channel called ‘News’. This will allow us to send a message to everyone who subscribes to the channel called ‘News’ via cloud code.



:::BlockQuote
\- (void)application:(UIApplication \*)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData \*)deviceToken \{
&#x20;// Store the deviceToken in the current Installation and save it to Parse
&#x20;PFInstallation \*currentInstallation = \[PFInstallation currentInstallation];
&#x20;\[currentInstallation setDeviceTokenFromData\:deviceToken];
&#x20;\[currentInstallation setObject:@\[@"News1"] forKey:@"channels"];
&#x20;\[currentInstallation saveInBackgroundWithBlock:^(BOOL succeeded, NSError \*error) \{
&#x20;    if (!error) \{
&#x20;        NSLog(@"installation saved!!!");
&#x20;    }else\{
&#x20;        NSLog(@"installation save failed %@",error.debugDescription);
&#x20;    }
&#x20;}];
}
:::

&#x20;      2\. Test it by running your app on a physical device. You cannot run this on simulator. You’ll need an actual push token to update your installation record so a physical device is a must. After it runs successfully you should see this in the installation section of your dashboard. You can check by going to [**Back4App website**](https://www.back4app.com/) and click on your app’s dashboard and then check the installation table. Under the the channels column you should see ‘News’, showing you that you are now subscribed to the News push channel.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Go0-0G9rO_d1fosUKlDFm_image.png)

## 3 - Create your Cloud Code

:::hint{type="info"}
To know more about how to get started with **Cloud Code&#x20;**&#x6C;ook at [**Cloud Code for iOS Tutorial**](https://www.back4app.com/docs).
:::

1. Create a .js file to put your Cloud Code into. You need to call it main.js in order for Back4App to know this is where you store your cloud code.
2.
   Define a Cloud function, using Parse.Cloud.Define, to call the push notification. Inside the function we will call Parse.Push.Send to send a pushes to the ‘News’ channel.

:::hint{type="danger"}
It is required to use the **master key&#x20;**&#x69;n this operation.
:::

The following code executes these steps:

:::CodeblockTabs
Parse Server 3.X

```javascript
// main.js
1   Parse.Cloud.define("pushsample", (request) => {
2
3       return Parse.Push.send({
4           channels: ["News"],
5           data: {
6               title: "Hello from the Cloud Code",
7               alert: "Back4App rocks!",
8           }
9       }, { useMasterKey: true });
10  });
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
21  })
```
:::

## 4 - Upload to Cloud Code

1. Go to your App at[**&#x20;Back4App Website**](https://www.back4app.com/) and click on Dashboard.
2. Find the Cloud Code and click on Functions & Web Hosting. It looks like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/cM-hOeH2GGq04PhYwvKyS_image.png)

&#x20;    3\. Upload or create a new file (you can also edit the current main.js file directly on the browser). Then, click at Deploy as shown here:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/jdZ-bp3IcWh-8Qg42UJG9_image.png)

## 5 - Call Cloud Code from your iOS App

1. Next we are going to write some code to call this cloud function from your app. You will need both the simulator and a physical device to complete this task. You will call the cloud function from your app running in the simulator and you will see the push appear on your physical device. Your physical device should actually be closed with the lock screen on in order to see the push. A push will not appear on the screem if you are inside the app that is sending it when you receive the push.
2. Open your project’s ViewController.m file. We need to include Parse in the view controller by adding the following code - ‘#import \<Parse/Parse.h>’ at the top of the file.



:::BlockQuote
\#import "ViewController.h"
\#import \<Parse/Parse.h>
:::

&#x20;    3\. Next in the ViewController.m file we will call an alert function from the viewDidAppear method. The alert will allow you to trigger the cloud code code which will send a push to your device. Be sure to include the following block of code after the viewDidLoad function.

[`ViewController.m`](https://github.com/mpc20001/ios-objc-push-cloud-code/blob/master/AddingParseSDKObjc/AppDelegate.m#L29-L62)&#x20;

:::BlockQuote
\- (void)viewDidAppear:(BOOL)animated \{
&#x20;\[self askToSendPushnotifications];
}
\- (void)askToSendPushnotifications \{
&#x20;UIAlertController\* alert = \[UIAlertController alertControllerWithTitle:@"Send a push to the news channel"
&#x20;                                                               message\:nil
&#x20;                                                        preferredStyle\:UIAlertControllerStyleAlert];
&#x20;UIPopoverPresentationController \*popPresenter = \[alert popoverPresentationController];
&#x20;popPresenter.sourceView = self.view;
&#x20;UIAlertAction \*Okbutton = \[UIAlertAction actionWithTitle:@"Ok" style\:UIAlertActionStyleDefault handler:^(UIAlertAction \*action) \{
&#x20;    \[self sendPushNotifications];
&#x20;}];
&#x20;\[alert addAction\:Okbutton];
&#x20;UIAlertAction \*cancelbutton = \[UIAlertAction actionWithTitle:@"Cancel" style\:UIAlertActionStyleCancel handler:^(UIAlertAction \*action) \{

&#x20;}];
&#x20;\[alert addAction\:cancelbutton];
&#x20;popPresenter.sourceRect = self.view\.frame;
&#x20;alert.modalPresentationStyle = UIModalPresentationPopover;
&#x20;\[self presentViewController\:alert animated\:YES completion\:nil];
}
&#x20;      \- (void)sendPushNotifications \{
&#x20;\[PFCloud callFunctionInBackground:@"pushsample"
&#x20;                   withParameters:@\{}
&#x20;                            block:^(id object, NSError \*error) \{
&#x20;                                if (!error) \{
&#x20;                                    NSLog(@"PUSH SENT");
&#x20;                                }else\{
&#x20;                                    NSLog(@"ERROR SENDING PUSH: %@",error.localizedDescription);
&#x20;                                }
&#x20;                            }];
}
:::

&#x20;   4\. Run your app in the simulator and when the alert asking to send the push pops up hit “OK”. On your physical device you should see the push appear on the lock screen.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/ijZml6qcgZiYvbGwmfnWb_image.png" signedSrc size="40" width="640" height="1136" position="flex-start" caption}

## 6 - Call Cloud Code from REST API

The REST API provides a quick and easy way to test if your Cloud function is working.
Just use the code below in your terminal or command prompt:

:::hint{type="info"}
Click on to know more about how to get started with command line in [**Linux**](https://www.digitalocean.com/community/tutorials/an-introduction-to-the-linux-terminal), [**MacOS**](https://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line)
or [**Windows**](https://www.bleepingcomputer.com/tutorials/windows-command-prompt-introduction/).
:::

:::BlockQuote
curl -X POST -H "X-Parse-Application-Id: YOUR\_APP\_ID\_HERE" \\
-H "X-Parse-REST-API-Key: YOUR\_REST\_API\_KEY\_HERE" \\
-H "Content-Type: application/json" \\
-d ‘\{ // Put the function parameters here in JSON format }’ \\
https\://parseapi.back4app.com/functions/pushsample
:::

To test the push notifications, just use the REST code while the device is closed.

## 7 - Send Targeted Push Notifications Using a User Object

:::hint{type="info"}
Going forward we will be using a different iOS project that has a basic signup and signin features already built. We are going to be using this iOS project that we can show you how to detect if a user is logged in, and if so save their installation to with a link to their object id for querying in cloud code. You can download the complete iOS Project built with this section’s tutorial at our [**GitHub repository**](https://github.com/mpc20001/ios-objc-targeted-push-cloud-code) but you will still have to do all of the setup from the previous tutorial that explains how to send pushes fromt he Back4App dashboard.
:::

1. Get the new version of the app setup and signup or login to the app. First make sure you download the working template from Github at [**GitHub repository**](https://github.com/mpc20001/ios-objc-targeted-push-cloud-code). We are not going to walk through all the steps of building this app, instead we will focus on setting up the cloud code and why it works. Once you open this new app be sure to put your own app’s credentials in the AppDelegate.m file.&#x20;



:::BlockQuote
\- (BOOL)application:(UIApplication \*)application didFinishLaunchingWithOptions:(NSDictionary \*)launchOptions \{
&#x20;// Override point for customization after application launch.
&#x20;\[Parse initializeWithConfiguration:\[ParseClientConfiguration configurationWithBlock:^(id\<ParseMutableClientConfiguration> configuration) \{
&#x20;    configuration.applicationId = @"PASTE\_YOUR\_APPLICATION\_ID\_HERE";
&#x20;    configuration.clientKey = @"PASTE\_YOUR\_CLIENT\_ID\_HERE";
&#x20;    configuration.server = @"https\://parseapi.back4app.com/";
&#x20;}]];
&#x20;return YES;
}
:::

&#x20;    2\. This app has some major differences between the previous app. It features 2 sections, one for being logged into your app and one section when you are not logged in to your app. The next big change is the AppDelegate.m file’s function ‘didRegisterForRemoteNotificationsWithDeviceToken’. We’ve added 1 line that store’s the user’s object id as part of the installation object. That way we can know which user is associated with which installation object and can target them individually for pushes.

&#x20;

:::BlockQuote
\- (void)application:(UIApplication \*)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData \*)deviceToken \{
&#x20;// Store the deviceToken in the current Installation and save it to Parse
&#x20;PFInstallation \*currentInstallation = \[PFInstallation currentInstallation];
&#x20;\[currentInstallation setDeviceTokenFromData\:deviceToken];
&#x20;\[currentInstallation setObject:@\[@"News"] forKey:@"channels"];
&#x20;\[currentInstallation setObject\:PFUser.currentUser.objectId forKey:@"userId"];
&#x20;\[currentInstallation saveInBackgroundWithBlock:^(BOOL succeeded, NSError \*error) \{
&#x20;    if (!error) \{
&#x20;        NSLog(@"installation saved!!!");
&#x20;    }else\{
&#x20;        NSLog(@"installation save failed %@",error.debugDescription);
&#x20;    }
&#x20;}];
}
:::

&#x20;    3\. Since we are now storing the user’s object id as part of the installation object we do not want to request a new push token until the user is logged in. We do not want to request a token directly from AppDelegate.m file’s function ‘application didFinishLaunchingWithOptions’ instead we want to call it from the LoggedInViewController’s function ‘viewDidAppear’. In ‘viewDidAppear’ we call a function on the AppDelegate to request access to a push notification token from Apple. Since you can only view this section once you are logged in we can assume the user is logged in when we create the installation object and retrieve the object id.



:::BlockQuote
\- (void)viewDidAppear:(BOOL)animated \{
&#x20;AppDelegate \*delegate = (AppDelegate \*)\[\[UIApplication sharedApplication] delegate];
&#x20;\[delegate registerForRemoteNotifications];
}
:::



:::BlockQuote
\[currentInstallation setObject\:PFUser.currentUser.objectId forKey:@"userId"];
:::

&#x20;   4\. Ok, now to sign up or login. On your physical device - (iphone or ipad) start the app. You should see the image below. You should sign Up to create a new user or sign in if you have already created a user on your app.
This is how it will look like:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/nqoTbBkYjc1EgWNP83LsS_image.png" signedSrc size="30" width="750" height="1334" position="flex-start" caption}

You should now be able to see the LoggedInviewController. It should look like this.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/3His1rs0WHDoel_4J70sq_image.png" signedSrc size="28" width="750" height="1334" position="flex-start" caption}

If you try to send pushes to yourself it won’t work yet because we haven’t added those methods to cloud code. So that’s what we will do next.

## 8 - Add the targeted Push Methods to Cloud Code

Open your Main.js file that you created previously and add the following functions to target installations by user id.

:::hint{type="danger"}
It is required to use the **master key&#x20;**&#x69;n this operation.
:::

The following code executes these steps:

:::CodeblockTabs
Parse Server 3.X

```javascript
// main.js
1   Parse.Cloud.define('sendPushToYourself', (request) => {
2       let userId = request.user.id;
3
4       let query = new Parse.Query(Parse.Installation);
5       query.equalTo("userId", userId);
6       query.descending("updatedAt");
7       return Parse.Push.send({
8           where: query,
9        data: {
10              title: "Hello from the Cloud Code",
11              alert: "Back4App rocks! Single Message!",
12          }
13      }, { useMasterKey: true });    
14  });
15
16  Parse.Cloud.define('sendPushToAllUsers', (request) => {
17      let currentUser = request.user;
18      let userIds = [currentUser.id];
19
20      let query = new Parse.Query(Parse.Installation);
21      query.containedIn('userId', userIds);
22      return Parse.Push.send({
23          where: query,
24          data: {
25              title: "Hello from the Cloud Code",
26              alert: "Back4App rocks! Group Message!",
27          }
28      }, { useMasterKey: true });
29  });
```

Parse Server 2.X

```javascript
//main.js
1   Parse.Cloud.define('sendPushToYourself', function (request, response) {
2       var currentUser = request.user;
3       var userId = currentUser.id;
4
5       var query = new Parse.Query("Installation");
6       query.equalTo("userId", userId);
7       query.descending("updatedAt");
8       Parse.Push.send({
9           where: query,
10          data: {
11              title: "Hello from the Cloud Code",
12              alert: "Back4App rocks! Single Message!",
13          }
14      }, {
15          useMasterKey: true,
16          success: function () {
17             response.success("success sending a single push!");
18          },
19          error: function (error) {
20              response.error(error.code + " : " + error.description);
21          }
22      });
23  });
24
25  Parse.Cloud.define('sendPushToAllUsers', function (request, response) {
26      var currentUser = request.user;
27      var userIds = [currentUser.id];
28  
29      var query = new Parse.Query(Parse.Installation);
30      query.containedIn('userId', userIds);
31      Parse.Push.send({
32          where: query,
33          data: {
34              title: "Hello from the Cloud Code",
35              alert: "Back4App rocks! Group Message!",
36          }
37      }, {
38          useMasterKey: true,
39          success: function () {
40              response.success('Success sending a group push!');
41          },
42          error: function (message) {
43              response.error(error.code + " : " + error.description);
44          }
45      });
46  });
```
:::

## 9 - Upload to Cloud Code

1. Go to your App at [**Back4App website**](https://www.back4app.com/) and click on Dashboard.
2.
   Find the Cloud Code and click on Functions & Web Hosting. It looks like this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/6z28wpouFf6ElQsP37Ycg_image.png" signedSrc size="50" width="810" height="578" position="center" caption}

3\. Upload or create a new file (you can also edit the current main.js file directly on the browser). Then, click at Deploy as shown here:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/8b26jNv2FJ4uenFGTATwU_image.png)

## 10 - Test that you can send Targeted push Notifications to yourself

Open your app from the simulator while leaving your physical device closed with the lock screen on. You can test that both push functions are working by pressing the ‘send push to a yourself’ button and the ‘send push to a group of people’ button. You should see the pushes appear on your devices lock screen.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/np9ER977_OIFEYdd2XAdt_image.png" signedSrc size="30" width="640" height="1136" position="flex-start" caption}

## Final Thoughts

This concludes the tutorial. You should have a firm understanding of how to send pushes based on a user’s channel or a user’s object id or any other query that involves getting the user’s object id. Remember in order to store the user’s object id you must add it to the push installation and only request a push token when the user is logged in. When sending pushes via query be aware that it is limited by default to 100 results and some users may have more than one instllation object. Also it is not reccomended to send pushes to array of installation objects that are larger than 100 results. It could result in some pushes not getting sent. if you are dealing with large groups of people it is better to use channels or to send the pushes out in repeated requests.

## It’s done!

At this stage, you can send push notifications using Cloud Code through Back4App! Congratulations!
