# Source: https://docs-containers.back4app.com/docs/platform/instagram-basic-display-api.md

---
title: Instagram Basic Display
slug: docs/platform/instagram-basic-display-api
description: In this tutorial you will learn the steps to set up Instagram Basic Display API with Parse
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-02-02T15:12:31.669Z
updatedAt: 2025-01-27T19:45:42.712Z
---

# Instagram Basic Display API Tutorial

## Introduction

The Instagram Basic Display API is an HTTP-based API that apps can use to get an Instagram user’s profile, images, videos, and albums.
Since October 15, 2019, new client registration and permission review on Instagram API platform are discontinued in favor of the Instagram Basic Display API and you should use this method from now on.

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- An app created at Back4App
- See the [**Create New App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create an app at Back4App.
- Set up a Subdomain for your Back4app app
- See [**Activating your Web Hosting and Live Query**](https://www.back4app.com/docs/platform/activating-web-hosting) to learn how to create a subdomain in Back4App.
- An [**Instagram Developer account**](https://developers.facebook.com/docs/instagram).
:::

## 1 - Create a New Back4App App

First of all, it’s necessary to make sure that you have an existing app created at Back4App. However, if you are a new user, you can check [**this tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create one.

## 2 - Present the Authorization Window

The Authorization Window allows app users to grant your app permissions and short-lived Instagram User Access Tokens. After a user logs in and chooses which data to allow your app to access, we will redirect the user to your app and include an Authorization Code, which you can then exchange for a short-lived access token.

To begin the process, get the Authorization Window and present it to the user:

:::BlockQuote
1   https\://api.instagram.com/oauth/authorize
2     ?client\_id=\{instagram-app-id}
3     \&redirect\_uri=\{redirect-uri}
4     \&scope=\{scope}
5     \&response\_type=code
6     \&state=\{state}        //Optional
:::

All parameters except state are required.

If authorization is successful, we will redirect the user to your redirect\_uri and pass you an Authorization Code through the code query string parameter. Capture the code so your app can exchange if for a short-lived Instagram User Access Token.

Authorization Codes are valid for 1 hour and can only be used once.

A sample Authorization Code would be:

:::BlockQuote
**https\://myapp.back4app.io/auth/?code=AQBx-hBsH3...#\_**
:::

Note that #\_ will be appended to the end of the redirect URI, but it is not part of the code itself, so strip it out.

## 3 - Retrieve your Token

Once you receive a code, exchange it for a short-lived access token by sending a POST request to the following endpoint:

:::BlockQuote
1   POST https\://api.instagram.com/oauth/access\_token
:::

A sample request would be like this:

```curl
1   curl -X POST \
2     https://api.instagram.com/oauth/access_token \
3     -F client_id=990602627938098 \
4     -F client_secret=eb8c7... \
5     -F grant_type=authorization_code \
6     -F redirect_uri=https://socialsizzle.herokuapp.com/auth/ \
7     -F code=AQBx-hBsH3...
```

and a successful response will look similar to this:

```json
1   {
2     "access_token": "IGQVJ...",
3     "user_id": 17841405793187218
4   }
```

## 4 - Start the development

Now that the Sign In with Instagram is configured, you can start the development process passing the Access Token you retrieved for authentication.
The format for AUTHDATA is:

```json
1   {
2     "instagram": {
3       "id": "user's Instagram id (string)",
4       "access_token": "an authorized Instagram access token for the user"
5     }
6   }
```

Here is the method for the iOS SDK:

```swift
1   PFUser.logInWithAuthType(inBackground: "instagram", authData: ["access_token":tokenString, "id": user]).continueWith { task -> Any? in
2    
3   }
```

And here for the Android SDK:

```java
1   Map<string, string> authData = new HashMap<string, string>(); 
2   authData.put("access_token", tokenString);
3   authData.put("id", user);
4   ParseUser.logInWithInBackground("instagram", authData){
5
6   }
```

