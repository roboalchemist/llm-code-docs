# Source: https://docs-containers.back4app.com/docs/platform/instagram-oauth-tutorial.md

---
title: Sign Up With Instagram
slug: docs/platform/instagram-oauth-tutorial
description: In this tutorial you will learn the steps to set up Instagram OAuth
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-02-02T15:01:20.780Z
updatedAt: 2025-01-27T19:45:38.762Z
---

# Instagram OAuth Tutorial

## Introduction

Instagram OAuth enables users to sign in to Apps using their Instagram account through OAuth.

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

## 2 - Create a new Instagram App Client

Log into your [**Instagram Developer account**](https://www.instagram.com/developer/) and sign up as a Developer.
Enter your website, telephone, and a description for your App. Accept the terms to proceed.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/aIWmarBXNbPdz-1h9hO6v_image.png)

Go to Overview. Click on Register Your Application

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/TDggEpHxpjBU33oNixvMs_image.png)

Click on Register a New Client

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/dptSWcpQlFihQbHFfKBP__image.png)

Fill up the Application Name, Description, Company Name, Website URL, Redirect URIs, Privacy Policy URL, and Contact email.

For the Valid redirect URIs, if you are only trying to retrieve your access token, you can leave it as

:::BlockQuote
http\://localhost
:::

Otherwise, you should use the production URI for redirection

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/gVVpnnKcOyxplyY56_Ukl_image.png)

At this point, you should have a Client like the image below

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/XkrJesJQlIIZh-rmdtKrc_image.png)

Click on Manage and under the Security tab, uncheck the Disable Implicit OAuth

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/t_7wOB9BSdgKKzkJLaPhd_image.png)

## 3 - Retrieve your Token

If you left your Redirect URIs as localhost, there are two ways you can retrieve your token.
The first one is using your Browser of choice, and going to the following URL:

[**https://api.instagram.com/oauth/authorize/?client\_id=CLIENT-ID\&redirect\_uri=REDIRECT-URI\&response\_type=code**](https://api.instagram.com/oauth/authorize/?client_id=CLIENT-ID\&redirect_uri=REDIRECT-URI\&response_type=code)

just change the CLIENT-ID and REDIRECT-URI using the values you got from your newly created Client.
This will redirect you to an invalid page, but show you the access token in the URL:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/2nRBVpsrA9fmD2Lh62jn6_image.png)

The other way to retrieve such a token is to run the following CURL command, replacing the CLIENT-ID, CLIENT-SECRET, and REDIRECT-URI for your values:

```curl
1   curl \-F 'client_id=CLIENT-ID' \
2       -F 'client_secret=CLIENT-SECRET' \
3       -F 'grant_type=authorization_code' \
4       -F 'redirect_uri=REDIRECT-URI' \
5       -F 'code=CODE' \
6       https://api.instagram.com/oauth/access_token
```

That command will also output your Access Token.

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

