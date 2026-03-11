# Source: https://docs-containers.back4app.com/docs/platform/parse-cron-job.md

---
title: Cron Job
slug: docs/platform/parse-cron-job
description: In this guide you learn how to create a cron job in javascript in a free online platform.
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-02-01T13:25:55.166Z
updatedAt: 2025-01-27T19:45:18.872Z
---

# How to create your Parse Cron Job

## Introduction

This section explains how you can schedule a cron job using [**Parse Server core features**](https://www.back4app.com/product/parse-server) through Back4App.

For this tutorial, as an example, you will build a cron job that removes users of your Parse Dashboard that haven’t verified their emails some time after they have signed up.

:::hint{type="info"}
**At any time, you can access the complete Project built for this tutorial at our&#x20;**[**GitHub repository**](https://github.com/back4app/android-background-jobs)**.**
:::

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you need:**

- An app created on Back4App.
  - Note: Follow the [**New Parse App Tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse App on Back4App
- Knowledge about Cloud Code.
  - Note: Follow the [**Cloud Code for Android Tutorial**](https://www.back4app.com/docs/android/parse-cloud-code) or the [**Cloud Code for iOS Tutorial**](https://www.back4app.com/docs) for more information.
  - A device (or [**virtual device**](https://developer.android.com/studio/run/managing-avds?hl=pt-br)) running Android 4.0 (Ice Cream Sandwich)or newer.
:::

## 1 - Create your cron job code

1. Create a .js file to put your cron job code into. In this example, a main.js file is created in a cloud\_code directory.
2. Define a job function using Parse.Cloud.job. In this example, the following code verifies every user in your Parse Dashboard, then query the ones that still have their email unverified after some time and destroy them:

:::CodeblockTabs
Parse Server 3.X main.js

```javascript
1   Parse.Cloud.job("removeInvalidLogin", async (request) => {
2     let date = new Date();
3     let timeNow = date.getTime();
4     let intervalOfTime = 3*60*1000;  // the time set is 3 minutes in milliseconds
5     let timeThen = timeNow - intervalOfTime;
6
7     // Limit date
8     let queryDate = new Date();
9     queryDate.setTime(timeThen);
10
11    // The query object
12    let query = new Parse.Query(Parse.User);
13
14    // Query the users that still unverified after 3 minutes
15    query.equalTo("emailVerified", false);
16    query.lessThanOrEqualTo("createdAt", queryDate);
17
18    const results = await query.find({useMasterKey:true});
19
20    results.forEach(object => {
21        object.destroy({useMasterKey: true}).then(destroyed => {
22            console.log("Successfully destroyed object" + JSON.stringify(destroyed));
23        }).catch(error => {
24            console.log("Error: " + error.code + " - " + error.message);
25        })
26    });
27    
28    return ("Successfully retrieved " + results.length + " invalid logins."); 
29  });
```

Parse Server 2.X main.js

```javascript
1   Parse.Cloud.job("removeInvalidLogin", function (request, response) {
2     var date = new Date();
3     var timeNow = date.getTime();
4     var intervalOfTime = 3*60*1000;  // the time set is 3 minutes in milliseconds
5     var timeThen = timeNow - intervalOfTime;
6
7     // Limit date
8     var queryDate = new Date();
9     queryDate.setTime(timeThen);
10
11    // The query object
12    var query = new Parse.Query(Parse.User);
13
14    // Query the users that still unverified after 3 minutes
15    query.equalTo("emailVerified", false);
16    query.lessThanOrEqualTo("createdAt", queryDate);
17
18    query.find({
19        success: function (results) {
20        console.log("Successfully retrieved " + results.length + " invalid logins.");
21
22        // Destroying the invalid users
23        query.each(function (object, err) {
24          object.destroy({
25            success: function (object) {
26              response.success("Successfully destroyed object " + object.objectId);
27            },
28            error: function (error) {
29              response.error("Error: " + error.code + " - " + error.message);
30            },
31            useMasterKey: true  // VERY IMPORTANT!!
32          })
33        })
34      },
35      error: function (error) {
36        response.error("Error: " + error.code + " - " + error.message);
37      }
38    });
39  });
```
:::

:::hint{type="danger"}
It is required to use the **master key&#x20;**&#x69;n this operation.
:::

:::hint{type="info"}
You can modify the intervalOfTime content with the amount of time you think an unverified user can still have his account active without verifying it. Just don’t forget that to test your application, small time intervals are better. So, it’s suggested that you set the intervalOfTime content to three minutes to test if the cron job is working and then change the JavaScript code with the amount of time you actually want intervalOfTime to be.
:::

:::hint{type="danger"}
Don’t forget that changes to the JavaScript file are only computed in your application if you upload the file again on Back4app Cloud Code block. To do this, delete the .js file with the unwanted intervalOfTime content and follow Step 2 to upload the file with the correct intervalOfTime content.
:::

## 2 - Upload cron job to Cloud Code

:::hint{type="info"}
To know more about how to get started with Cloud Code look at [**Cloud Code for Android Tutorial**](https://www.back4app.com/docs/android/parse-cloud-code) or [**Cloud Code for iOS Tutorial**](https://www.back4app.com/docs).
:::

1. Go to your App at the [**Back4App**](https://www.back4app.com/) website and click on Dashboard.
2. Find the Cloud Code and click on Functions & Web Hosting. It looks like this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/gAqCZlMJvj1u1_2A82SEg_image.png" signedSrc size="80" width="810" height="578" position="center" caption}

&#x20;    3\. Upload or create a new file (you can also edit the current main.js file directly on the browser). Then, click on Deploy as shown here:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/cEJDTAvCqpLgcEwst1IYa_image.png)

## 3 - Schedule cron job on Back4App

1. Go to your app at the [**Back4App website**](https://www.back4app.com/) and click on Server Settings.
2. Find the “Background Jobs” block and click on SETTINGS. The “Background Jobs” block looks like this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/X18vSRO1Tvs7KSC0u6elV_image.png" signedSrc size="50" width="331" height="339" position="center" caption}

&#x20;    3\. A Background Jobs page will appear and two options will be displayed: Browser a job or Schedule a job. Click on Schedule a job, as shown below:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/t5AO9omCAxyHaiVXvcKUK_image.png" signedSrc size="70" width="786" height="551" position="center" caption}

:::hint{type="info"}
If you want to Edit, Run now, or Delete an existing cron job, click on the Browser a job button.
:::

&#x20;     4\. A Schedule a job page will appear and you have to fill in the Description field of your job with its description and also the field Cloud Job with the name you set to your cron job in the first line of its JavaScript code. In this example, the name of the cron job created is removeInvalidLogin.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/MJWhjahzgsKOjL0wJ_Apk_image.png" signedSrc size="70" width="672" height="755" position="center" caption}

&#x20;5\. You can also set other options for your cron job as what time it should start running, if it should repeat, and how often. After filling in these options with your preferences, click on the SAVE button.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/lbntJNDOU5GfmZr02WH6p_image.png)

## 4 - Test your app

1. Create some users with emailVerified column set as False at your Parse Dashboard, as shown below:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/pGu1s06Aow8ReNU_HLnuF_image.png)

&#x20; 2\. Run your application and refresh your Parse Dashboard. It should have destroyed the unverified users. For the Parse Dashboard shown above, this is the result:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/JAjqPNXa7wD-QLmm7VAbe_image.png)

:::hint{type="info"}
**You can also see if the cron job is working by accessing Back4App Logs. To do that, follow these steps:**

1. Go to your app at the [**Back4App website**](https://www.back4app.com/) and click on Server Settings.
2. Find the “Logs” block and click on SETTINGS. The “Logs” block looks like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/hWuI1nQOsjx9FfSr0qjbF_image.png)

&#x20;      3\. Scroll the page until you see the Server System Log. There you should find information about the cron job that is running, as shown below:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/c8KgYmpE5D3TtfKNQKXb3_image.png)
:::

## It’s done!

At this stage, you can schedule cron jobs in your application using Parse Server Core features through Back4App!
