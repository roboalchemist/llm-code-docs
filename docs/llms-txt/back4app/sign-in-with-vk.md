# Source: https://docs-containers.back4app.com/docs/platform/sign-in-with-vk.md

---
title: Sign Up With VKontakte
slug: docs/platform/sign-in-with-vk
description: In this tutorial you will learn the steps to set up Sign In with VK (VKontakte).
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-02-05T13:24:02.649Z
updatedAt: 2025-01-27T19:45:56.550Z
---



# Sign In with VK (VKontakte) Tutorial

## Introduction

Sign In with VK (VKontakte) enables users to sign in to Apps using their VK accounts.

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- An app created at Back4App
- See the [**Create New App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create an app at Back4App.
- Set up a Subdomain for your Back4app app
- See [**Activating your Web Hosting and Live Query**](https://www.back4app.com/docs/platform/activating-web-hosting) to learn how to create a subdomain in Back4App.
- A [**VK account**](https://vk.com/).
:::

## 1 - Create a New Back4App App

First of all, it’s necessary to make sure that you have an existing app created at Back4App. However, if you are a new user, you can check [**this tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create one.

## 2 - Create a new VK App

Create a new VK Application by going to [**VK Developers**](https://vk.com/apps?act=manage) and clicking the `Create app button`

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Boa01ieeq3GJoROBAoueS_image.png)

Fill up the Title and choose the Platform as Standalone app, then click the Connect app button

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/oybDJT1inXp77Dcj1LsOh_image.png)

Choose a Category for your app and, if applicable, a Type of leaderboard, and Community. Click Save

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/P-epaj4HCCM_vQv1IUFpS_image.png)

Under the Settings tab of your VK Application, you will find your App ID, Secure key, and Service token among other useful info. Fill up your Website address and the Base domain for it. Save it.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/uLP5qA1wjra7VzRHISZkx_image.png)

## 3 - Retrieve your Code

Copy the App ID from your to use as the `YOUR_CLIENT_ID` and use your Website address as `YOUR_REDIRECT_URI`, and choose a [**scope**](https://vk.com/dev/permissions) to use in `YOUR_SCOPE` from the available options.

Then visit the following URL changing the parameters above:

:::BlockQuote
[**https://oauth.vk.com/authorize?client\_id=YOUR\_CLIENT\_ID\&scope=YOUR\_SCOPE\&redirect\_uri=https://localhost\&response\_type=token**](https://oauth.vk.com/authorize?client_id=YOUR_CLIENT_ID\&scope=YOUR_SCOPE\&redirect_uri=https://localhost\&response_type=token)
:::

It will ask you to log in to VK:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Ql80wj-_wGwQB1qn6pmRc_image.png)

Alternatively, you can use the following CURL command to retrieve your token:

```curl
curl -X POST \
    -F \'client_id=YOUR_CLIENT_ID' 
    -F 'scope=YOUR_SCOPE'
    -F 'redirect_uri=YOUR_REDIRECT_URI' 
    -F 'response_type=token' 
    https://oauth.vk.com/authorize?
```

Run it and you should retrieve your access token:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/t6SnGMgZ2kuOVQVKUHgQf_image.png)

**REMEMBER**: the code can be used only once. If you get an error or don’t use your token, you must re-generate your Code to be able to run it again.

## 4 - Configure your Back4app App

In your Back4app App, go to Server Settings and open the VKontakte Login box

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/pNdJNQzx_bpWot8RckzW2_image.png" signedSrc size="40" width="292" height="338" position="center" caption}

Fill up your Application Id and VKontakte Application Secret. Save it.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/OtzKpW-akzILuxLH5S2bA_image.png" signedSrc size="70" width="603" height="574" position="center" caption}

## 5 - Start the development

Now that the Sign-in with VK is configured, you can start the development process.
The format for AUTHDATA is:

```json
   {
     "vkontakte": {
       "id": "user's vkontakte id (string)",
       "access_token": "an authorized vkontakte access token for the user"
     }
   }
```

Here is the method for the iOS SDK:

```swift
1   PFUser.logInWithAuthType(inBackground: "vkontakte", authData: ["access_token":tokenString, "id": user]).continueWith { task -> Any? in
2    
3   }
```

And here for the Android SDK

```java
1   Map<string, string, bool> authData = new HashMap<string, string, bool>(); 
2   authData.put("access_token", tokenString);
3   authData.put("id", user);
4   ParseUser.logInWithInBackground("vkontakte", authData){
5
6   }
```

