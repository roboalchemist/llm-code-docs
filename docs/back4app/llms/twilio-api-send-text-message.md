# Source: https://docs-containers.back4app.com/docs/cloud-code-functions/integrations/twilio-api-send-text-message.md

---
title: Twilio
slug: docs/cloud-code-functions/integrations/twilio-api-send-text-message
description: In this guide you learn how to use Twilio in Back4App.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-02-28T14:15:56.628Z
updatedAt: 2025-01-15T19:38:08.909Z
---

# Using cloud functions and Twilio API to send Text Message

## Introduction

This guide explains how you can use the Twilio REST API to send SMS. After completing this step-by-step tutorial, you can use your cloud code function to send SMS to your device.

## Prerequisites

:::hint{type="info"}
To complete this tutorial, you will need:




- An app created at Back4App.
- Follow the [**Create New App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create an app at Back4App.
- Back4App Command Line Configured with the project.
- Follow the [**Setting up Cloud Code tutorial**](https://www.back4app.com/docs/local-development/parse-cli) to learn how to set up cloud code for a project.
- Account created in [**Twilio**](https://login.twilio.com/u/signup?state=hKFo2SBSTHoyUXZ1NnUzTjZaMHk2Q3EtaXV5LUtnUlhaMzdtN6Fur3VuaXZlcnNhbC1sb2dpbqN0aWTZIE9JTzFKSU9LaVMzTV9fYVo0VDM0a2pnSEpZM09SYUo4o2NpZNkgTW05M1lTTDVSclpmNzdobUlKZFI3QktZYjZPOXV1cks).
:::

## Let’s get started!

Below are some steps you need to follow when writing a function to send SMS to a User and phone number.

To learn how to create or access an Account in Twilio, check the links given below:

[**Create a new account**](https://www.twilio.com/try-twilio) - [**Log in to your account**](https://www.twilio.com/login)

## 1 - Activate your Phone Number

After logging in or creating a new account, you will be redirected to your Project. There, on the left, you need to click on the #Phone Numbers. Next, tap on the last link ‘Getting Started’, and then click on the button ‘Get your first Twilio phone number’. Same as shown below:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/zWncYRIV74NXGLPTimCVF_image.png)

After that you will receive your first Phone Number for your Twilio Account. If you can’t find your phone number, go to #Phone Numbers and Manage Numbers.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/z11IgD_ew9-O-CQxq67t3_image.png)

## 2 - Get Account SID and Auth Token

To find your Account SID and Auth Token, log in to your Account, go to your Dashboard and click on Settings. All the important information about your Project will be available in that section; as shown in the image below:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/fBwxRTxumzqViO6-afJb6_image.png" signedSrc size="70" width="450" height="425" position="center" caption}

Now, you can Copy your SID and Authentication Token for the Cloud Code.

## 3 - Install Module from Twilio

After configuring the environment for the Command Line Interface in your computer, create a file called package.json, and inside this file, you need to install the Twilio module, like:

```json
1   {
2     "dependencies": {
3       "twilio": "*"
4     }
5   }
```

## 4 - Implement Cloud Code

:::CodeblockTabs
Parse Server 3.X

```javascript
1   Parse.Cloud.define("SendSMS", async(request) => {
2
3	   // Requiring the values to send
4	   let
5		   getMessage = request.params.message,
6		   getPhoneTo = '+Target test Phone number',
7		   getPhoneFrom = "+Your first Phone number",
8		   accountSid = 'AccountSID',
9		   authToken  = 'AuthToken';
10
11	  //require the Twilio module and create a REST client
12	  let client = require('twilio')(accountSid, authToken);
13
14	  return await client.messages
15		  .create({
16		  body: getMessage, // Any number Twilio can deliver to
17		  from: getPhoneFrom, // A number you bought from Twilio and can use for outbound communication
18		  to: getPhoneTo // body of the SMS message
19	  });
20  });
```

Parse Server 2.X

```javascript
1   Parse.Cloud.define("SendSMS",function(request,response){
2
3	   // Requiring the values to send
4	   var
5		   getMessage = request.params.message,
6		   getPhoneTo = '+Target test Phone number',
7		   getPhoneFrom = "+Your first Phone number",
8		   accountSid = 'AccountSID',
9		   authToken  = 'AuthToken';
10
11
12	  //require the Twilio module and create a REST client
13	  var client = require('twilio')(accountSid, authToken);
14
15	  client.messages
16	  .create({
17		  body: getMessage, // Any number Twilio can deliver to
18		  from: getPhoneFrom, // A number you bought from Twilio and can use for outbound communication
19		  to: getPhoneTo // body of the SMS message
20	  })
21	  .then(function(results) {
22		  response.success(results.sid);
23	  })
24	  .catch(function(error) {
25		  response.error(error);
26	  })
27  });
```
:::

## 5- Test the function “sendSMS”

You can also test the function in client SDKs, but for now, we will use the REST API command to send it:

```curl
curl -X POST \
  	-H "X-Parse-Application-Id: APP_ID" \
  	-H "X-Parse-REST-API-Key: REST_KEY" \
  	-H "Content-Type: application/json" \
  	-d '{ "message": "Now, I can send SMS from Cloud Code using Twilio", "phone": "+Target test Phone number" }' \
https://parseapi.back4app.com/functions/SendSMS
```

And the result will be something like as this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/fUVk4Kb6xIhjLpQHTvmgV_image.png" signedSrc size="60" width="500" height="889" position="center" caption}

## 6 - It’s done!

With the guide described above, you’ll be able to use Twilio with a Cloud Code Function in Back4App and send SMS to your customers!

In case you need any help or a function/link doesn’t work, please contact our team via chat!
