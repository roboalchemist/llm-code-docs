# Source: https://docs-containers.back4app.com/docs/platform/sign-in-with-github.md

---
title: Sign Up With GitHub
slug: docs/platform/sign-in-with-github
description: In this tutorial you will learn the steps to set up Sign In with Github.
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-02-05T13:14:51.899Z
updatedAt: 2025-01-27T19:45:53.203Z
---

# Sign In with Github Tutorial

## Introduction

Sign In with Github enables users to sign in to Apps using their Github accounts.

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- An app created at Back4App
- See the [**Create New App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create an app at Back4App.
- Set up a Subdomain for your Back4app app
- See [**Activating your Web Hosting and Live Query**](https://www.back4app.com/docs/platform/activating-web-hosting) to learn how to create an subdomain in Back4App.
- An [**Github account**](https://github.com/).
:::

## 1 - Create a New Back4App App

First of all, it’s necessary to make sure that you have an existing app created at Back4App. However, if you are a new user, you can check [**this tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create one.

## 2 - Create a new Github App

Create a new Github Application by going to [**Applications/New**](https://github.com/settings/applications/new)
Fill up the Application name, your Homepage URL, a quick Description and your Authorization callback URL\`

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Ld1eSVaG7slk55nMfTb39_image.png" signedSrc size="80" width="1178" height="1124" position="center" caption}

Then click Register Application. You should then see your App Secret and Client Secret

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Y-ycoPAFfoOZqBF0fG-u2_image.png" signedSrc size="80" width="1516" height="1584" position="center" caption}

## 3 - Retrieve your Code

Visit the following URL, changing the values for CLIENT\_ID for the one you created.

:::BlockQuote
https\://github.com/login/oauth/authorize scope=user\:email\&client\_id=CLIENT\_ID
:::

Log in with your GitHub account:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/k7oreeJEhLcTKa53B201E_image.png" signedSrc size="90" width="1130" height="1268" position="center" caption}

and the redirected website will have your code in the URL:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/s-OO81f3ZtNAzMDW9Zpo4_image.png)

Copy the Code part of the URL only and run the following CURL command replacing the values YOUR\_CODE, YOUR\_CLIENT\_ID, and YOUR\_CLIENT\_SECRET for the values of your application

```curl
1   curl -X POST \
2       -F \'client_id=YOUR_CLIENT_ID' 
3       -F 'client_secret=YOUR_CLIENT_SECRET' 
4       -F 'code=YOUR_CODE' 
5       -F 'accept=json' 
6       https://github.com/login/oauth/access_token
```

Run it and you should retrieve your access token:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/7pxb4bu-YmtkcXDt1kUlg_image.png)

**REMEMBER**: the code can be used only once. If you get an error or don’t use your token, you must re-generate your Code to be able to run it again.

## 4 - Start the development

Now that the Sign In with Github is configured, you can start the development process.
The format for AUTHDATA is:

```json
1   {
2     "github": {
3       "id": "user's Github id (string)",
4       "access_token": "an authorized Github access token for the user"
5     }
6   }
```

Here is the method for the iOS SDK:

```swift
1   PFUser.logInWithAuthType(inBackground: "github", authData: ["access_token":tokenString, "id": user]).continueWith { task -> Any? in
2    
3   }
```

And here for the Android SDK:

```java
1   Map<string, string, bool> authData = new HashMap<string, string, bool>(); 
2   authData.put("access_token", tokenString);
3   authData.put("id", user);
4   ParseUser.logInWithInBackground("github", authData){
5
6   }
```

