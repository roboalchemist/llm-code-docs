# Source: https://docs-containers.back4app.com/docs/ios/parse-swift-sdk/users/sign-in-with-google.md

# Source: https://docs-containers.back4app.com/docs/platform/sign-in-with-google.md

---
title: Sign Up With Google
slug: docs/platform/sign-in-with-google
description: In this tutorial you will learn the steps to set up Sign In with Google.
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-02-02T15:20:22.582Z
updatedAt: 2025-01-27T19:45:46.550Z
---

# Sign In with Google Tutorial

## Introduction

Sign In with Google enables users to sign in to Apps using their Google accounts.

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- An app created at Back4App
- See the [**Create New App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create an app at Back4App.
- Set up a Subdomain for your Back4app app
- See [**Activating your Web Hosting and Live Query**](https://www.back4app.com/docs/platform/activating-web-hosting) to learn how to create an subdomain in Back4App.
- An [**Google Developer account**](https://developers.google.com/?hl=pt-br).
:::

## 1 - Create a New Back4App App

First of all, it’s necessary to make sure that you have an existing app created at Back4App. However, if you are a new user, you can check [**this tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create one.

## 2 - Create a new Client Identifier

Log into your [**Google Developer account**](https://developers.google.com/) and go to Google API Console. Click Credentials and choose OAuth 2.0 Client IDs

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/OmNe9xVnQaAqqIy1Ft3zB_image.png)

If you do not have a Consent Screen, Google will ask you to create one. Click on Configure consent Screen, you will be redirected to the following page:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/ocXYNb6QjRzd8Y7kSfQrG_image.png)

Complete the screen consent configuration and hit Save

Pick the platform you will need. For this example, I am using Javascript (Web Application), but you should pick the one you will be using.

In Authorized JavaScript Origins, replace the URL with your subdomain.
In Authorized redirect URIs, insert your subdomain followed by /redirect. As shown in the image below:

:::hint{type="info"}
**Note**: If you do not have your subdomain enabled yet, please check the following guide to know how can you do this: [**Create your Subdomain**](https://www.back4app.com/docs/platform/activating-web-hosting)
:::

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/fHWYzVUltAqVN7gjrjURG_image.png)

After that you should have your Client ID and Secret:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/RutkaartvQC1wEC9kSXp2_image.png" signedSrc size="70" width="498" height="427" position="center" caption}

## 3 - Retrieve your Code

Visit the following URL, changing the values for REDIRECT\_URI and CLIENT\_ID for the ones you created:

:::BlockQuote
https\://accounts.google.com/o/oauth2/v2/auth?scope=https%3A//www\.googleapis.com/auth/drive.metadata.readonly\&access\_type=offline\&include\_granted\_scopes=true\&response\_type=code\&state=state\_parameter\_passthrough\_value\&redirect\_uri=REDIRECT-URL\&client\_id=CLIENT\_ID
:::

The scopes necessary to retrieve the auth\_token and later on the user\_id are:

https\://www\.googleapis.com/auth/userinfo.email
https\://www\.googleapis.com/auth/plus.me
https\://www\.googleapis.com/auth/userinfo.profile

Log in with your Google account and the redirected website will have your code in the URL:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Y9Z_gxHrgAdlx7qr3w3Y__image.png)

Copy the Code part of the URL only and run the following CURL command replacing the values YOUR\_CODE, CLIENT\_ID, CLIENT\_SECRET, and REDIRECT\_URI for the values of your application

```curl
1   curl -X POST \
2     https://oauth2.googleapis.com/token \
3     -F 'grant_type=authorization_code' \
4     -F 'code=YOUR_CODE' \
5     -F 'client_id=CLIENT_ID' \
6     -F 'client_secret=CLIENT_SECRET' \
7     -F 'redirect_uri=REDIRECT_URI'
```

Run it and you should retrieve your access token:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/E7bvJz86DXWcs42_9Zam7_image.png)

REMEMBER: the code can be used only once. If you get an error or don’t use your token, you must re-generate your Code to be able to run it again.

Now it is time to retrieve your Google's User ID. It is a numeric string that you will pass along as the id in step 4.
To do so, run the following command replacing the YOUR TOKEN string for the token you received in the previous command.

```curl
1   curl -X GET https://www.googleapis.com/userinfo/v2/me?access_token=YOUR_TOKEN
```

## 4 - Start the development

Now that the sign-in with Google is configured, you can start the development process.
The format for AUTHDATA is:

```json
1   {
2     "google": {
3       "id": "user's Google id (string)",
4       "id_token": "an authorized Google id_token for the user (use when not using access_token)",
5       "access_token": "an authorized Google access_token for the user (use when not using id_token)"
6     }
7   }
```

Here is the method for the iOS SDK:

```swift
1   PFUser.logInWithAuthType(inBackground: "google", authData: ["access_token":tokenString, "id": user]).continueWith { task -> Any? in
2    
3   }
```

And here for the Android SDK:

```java
1   Map<string, string> authData = new HashMap<string, string>(); 
2   authData.put("access_token", tokenString);
3   authData.put("id", user);
4   ParseUser.logInWithInBackground("google", authData){
5
6   }
```

Remember, this must be done at every login for every user.
