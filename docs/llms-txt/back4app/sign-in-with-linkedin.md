# Source: https://docs-containers.back4app.com/docs/platform/sign-in-with-linkedin.md

---
title: Sign Up With LinkedIn
slug: docs/platform/sign-in-with-linkedin
description: In this tutorial you will learn the steps to set up Sign In with LinkedIn.
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-02-02T15:29:44.156Z
updatedAt: 2025-01-27T19:45:49.928Z
---

# Sign In with LinkedIn Tutorial

## Introduction

Sign In with LinkedIn enables users to sign in to Apps using their LinkedIn accounts.

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- An app created at Back4App
- See the [**Create New App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create an app at Back4App.
- Set up a Subdomain for your Back4app app
- See [**Activating your Web Hosting and Live Query**](https://www.back4app.com/docs/platform/activating-web-hosting) to learn how to create a subdomain in Back4App.
- A [**LinkedIn Developer account**](https://www.linkedin.com/developers).
:::

## 1 - Create a New Back4App App

First of all, it’s necessary to make sure that you have an existing app created at Back4App. However, if you are a new user, you can check [**this tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create one.

## 2 - Create a new LinkedIn App

Log into your [**LinkedIn Developer account**](https://www.linkedin.com/developers) click Create App and choose OAuth client ID

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Se8FVnj5N-hwCKeFkccyQ_image.png)

Choose an App name and fill in the required fields such as Business email and App logo. Agree to the terms and click Create app

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/xAl9LVxEfGKKXPq3HUPgm_image.png" signedSrc size="80" width="519" height="916" position="center" caption}

In your newly created App, click Verify to verify the ownership of the App. You must be the owner or administrator of the LinkedIn page to verify.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/fQsUI-o0AjyznmSYsKPhB_image.png" signedSrc size="70" width="521" height="721" position="center" caption}

In the Verification page, click Generate URL

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/LgtvzoOBG_PB3MASZ-KQZ_image.png" signedSrc size="80" width="494" height="419" position="center" caption}

Visit the generated Verification URL using the admin or owner account of the company’s page on LinkedIn.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/cG24gUichkV2tSLLkRtri_image.png" signedSrc size="80" width="492" height="419" position="center" caption}

Click on Approve Verification

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/uuv4oVWSDAVSLudidLKgM_image.png)

Make sure your App is verified

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/HbiMmKh6v0UgmknjUBTLW_image.png)

In your App, go to the Auth tab, fill in the Redirect URLs field, and click Update

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/z_8wla-sJ34Dh8JcwOabQ_image.png" signedSrc size="70" width="517" height="676" position="center" caption}

## 3 - Retrieve your Code

Visit the following URL, changing the values for CLIENT\_ID, REDIRECT\_URL, and A\_RANDOM\_STRING for the ones you created.
The random string is to avoid CSRF attacks.

:::BlockQuote
https\://www\.linkedin.com/oauth/v2/authorization?response\_type=code\&client\_id=CLIENT\_ID\&redirect\_uri=REDIRECT\_URL\&state=A\_RANDOM\_STRING\&scope=r\_emailaddress
:::

Log in with your LinkedIn account and the redirected website will have your code in the URL:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/GjE0lzofVYRwFQXS5Fscc_image.png)

Copy the Code part of the URL only and run the following CURL command replacing the values YOUR\_CODE, YOUR\_CLIENT\_ID, YOUR\_CLIENT\_SECRET, and YOUR\_REDIRECT\_URI for the values of your application

```curl
1   curl -X POST \
2     https://www.linkedin.com/oauth/v2/accessToken \
3     -H 'cache-control: no-cache' \
4     -H 'content-type: application/x-www-form-urlencoded' \
5     -d 'client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&redirect_uri=YOUR_REDIRECT_URI&code=YOUR_CODE&grant_type=authorization_code'

```

Run it and you should retrieve your access token:

**REMEMBER**: the code can be used only once. If you get an error or don’t use your token, you must re-generate your Code to be able to run it again.

## 4 - Start the development

Now that the Sign-in with LinkedIn is configured, you can start the development process.
The format for AUTHDATA is:

```json
1   {
2     "linkedin": {
3       "id": "user's LinkedIn id (string)",
4       "access_token": "an authorized LinkedIn access token for the user",
5       "is_mobile_sdk": true|false // set to true if you acquired the token through LinkedIn mobile SDK
6     }
7   }
```

Here is the method for the iOS SDK:

```swift
1   PFUser.logInWithAuthType(inBackground: "linkedin", authData: ["access_token":tokenString, "id": user, "is_mobile_sdk": true]).continueWith { task -> Any? in
2    
3   }
```

And here for the Android SDK:

```java
1   Map<string, string, bool> authData = new HashMap<string, string, bool>(); 
2   authData.put("access_token", tokenString);
3   authData.put("id", user);
4   authData.put("is_mobile_sdk", true);
5   Task<ParseUser> t = ParseUser.logInWithInBackground("google", authData);
6				                    t.continueWith(new Continuation<ParseUser, Void>() {
7					                        public Void then(Task task) throws Exception {
8						                            if (task.isCancelled()) {
9							                                Log.w(TAG, "Task cancelled");
10						                            } else if (task.isFaulted()) {
11							                                Log.w(TAG, "Save FAIL" + task.getError());
12							                                Utilities.showToast(getResources().getString(R.string.errorLogin) + task.getError(), MainActivity.this);
13						                            } else {
14							                                // the object was saved successfully.
15							                                ParseUser user = (ParseUser)task.getResult();
16							                                Log.w(TAG, "Success " + user.getObjectId() + " " + user.getUsername() + " " + user.getEmail() + " " + user.getSessionToken());
17                  }
18               }
19            }
```

