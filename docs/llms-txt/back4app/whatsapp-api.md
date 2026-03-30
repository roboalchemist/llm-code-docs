# Source: https://docs-containers.back4app.com/docs/cloud-code-functions/integrations/whatsapp-api.md

---
title: WhatsApp
slug: docs/cloud-code-functions/integrations/whatsapp-api
description: In this guide you learn how to use Twilio API in Back4App.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-02-28T14:24:00.087Z
updatedAt: 2025-01-17T14:25:15.596Z
---

# Using cloud functions to send WhatsApp messages through Twilio API

## Introduction

In this guide, we will explain how you can use Twilio’s streamlined REST API to send WhatsApp messages easily. After completing this tutorial, you can use a cloud code function to send WhatsApp messages to your customers. So, let’s get down to business.

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

As you may know, the Facebook-owned WhatsApp has recently rolled out its first version of API for businesses to integrate and communicate seamlessly with customers. By using WhatsApp this service to the Bussiness API, companies can send customized notifications with pertinent, non-promotional messages, such as booking confirmations, appointment reminders, and delivery alerts, to their opted-in customers.

Twilio is a cloud communication platform that offers a robust feature to communicate and prototype with WhatsApp Bussiness API immediately. For now, the Twilio API for WhatsApp is in BETA and only allows you to send text messages to a WhatsApp user. In other words with that service, it’s not yet possible to send images, audio, videos and pdf files to users.

The feature used to send or receive WhatsApp messages to the user is “Twilio Sandbox”. In order to send messages to a user’s WhatsApp number, you will need to activate the sandbox first, and need to activate the number that will join your sandbox. In step 1, we will explain how you can activate your Twilio Sandbox for WhatsApp.

:::hint{type="info"}
**Note:&#x20;**&#x54;he Twilio Sandbox has [**some limitations**](https://www.twilio.com/docs/whatsapp/api#sandbox-limitations), and the major one is that you can only send to or receive messages from those users who have joined your specific sandbox. However, this limitation can be overcome if you enable WhatsApp using your own Twilio number. In order to activate WhatsApp on your own number, you need to submit a request for approval directly at [**Twilio Console**](https://www.twilio.com/docs/whatsapp/api#enabling-whatsapp-with-a-twilio-number).
:::

In this guide, we will explain how you can use a simple REST API to send and receive messages directly on WhatsApp while employing as a middleware. We will write and implement a Cloud Function that will interact with a Twilio API to send those messages. Once this function will be triggered by a saving event, we call this function an AfterSave.

To create or access an Account in Twilio, check the links given below:

[**Create a new account**](https://www.twilio.com/try-twilio) - [**Log in to your account**](https://www.twilio.com/login)

## 1 - Activate your WhatsApp Beta

After logging in to an existing account, you will be redirected to your Project. But, if you are a new user, you’ll first need to create a project and select programmable SMS from products. You should now see the recently created project on your console. Next, you must click on the programmable SMS and select the 4th option WhatsApp Beta and then follow the Steps given in that section to activate the Twilio Sandbox for WhatsApp. Same as shown below:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Zh_JtnPvd9BXCUzForN8q_image.png)

## 2 - Get Account SID and Auth Token

To find your Account SID and Auth Token, log in to your Twilio Account, go to your Dashboard and click on Settings. All the important information about your Project will be available in that section. Make sure that all these instructions are followed as shown in the image below:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/kkaxBERJI8j7fUgZu6U8z_image.png" signedSrc size="70" width="450" height="425" position="center" caption}

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

In this section, we will show you know how to work with the [**Cloud Functions**](https://docs.parseplatform.org/cloudcode/guide/#cloud-functions).

We will build an afterSave Trigger function to activate and send the confirmation message that the object has been saved.

```javascript
1   Parse.Cloud.afterSave("Contact", (request) => {
2
3     // Requiring the values to send
4     var
5         getPhoneTo   = request.object.get("phone"),
6         getFirstName = request.object.get("firstName"),
7         getPhoneFrom = "+Your Phone number", //Remember to replace your number enable on Twilio Sandbox
8         accountSid = 'AccountSID',
9         authToken  = 'AuthToken',
10        getMessage   = "Welcome " + getFirstName +", to Twilio App! Thank you for your interest, our team will contact you ASAP! ;)";
11
12    //require the Twilio module and create a REST client
13    var client = require('twilio')(accountSid, authToken);
14
15    client.messages
16        .create(
17        {
18            from: "whatsapp:" + getPhoneFrom,
19            body: getMessage,
20            to: "whatsapp:" + getPhoneTo
21        })
22        .then(message => console.log(message.sid))
23        .done();  
24  });
```

## 5 - Test the AfterSave Trigger

Now that we have created and activated the afterSave trigger, it’s time to test the function whether it’s working faultlessly or not. You can also test the function in client SDKs, but for now, we will use the REST API command to save a new User:

```curl
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"firstName":"Natália", "phone":"+0000000000000"}' \
  https://parseapi.back4app.com/classes/Contact
```

And the result will be similar to the screenshot below.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/gxPyaasg1-D1aiHmAHNZ6_image.png" signedSrc size="50" width="338" height="600" position="center" caption}

## 6 - It’s done!

With the guide described above, you’ll be able to use Twilio with a Cloud Code Function in Back4App and send WhatsApp messages to your opted-in customers!

In case you need any help or a function/link doesn’t work, please contact our team via chat!
