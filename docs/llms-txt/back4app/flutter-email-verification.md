# Source: https://docs-containers.back4app.com/docs/flutter/parse-sdk/users/flutter-email-verification.md

---
title: Email Verification
slug: docs/flutter/parse-sdk/users/flutter-email-verification
description: In this guide you learn how to use implement Flutter user registration with email verification
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-18T14:49:51.701Z
updatedAt: 2025-01-16T20:37:14.514Z
---

# User email verification for Flutter

## Introduction

Enabling email verification in an application’s settings allows the application to reserve part of its experience for users with confirmed email addresses.

Email verification adds the emailVerified key to the ParseUser object. When a ParseUseremail is set or modified, emailVerified is set to false.

Parse then emails the user a link which will set emailVerified to true.

There are three emailVerified states to consider:

1. true - the user confirmed his or her email address by clicking on the link Parse emailed them.
2. false - at the time the ParseUser object was last fetched, the user had not confirmed his or her email address. If emailVerified is false. If emailVerified is false, consider calling getUpdatedUser() on the ParseUser.
3. missing - the&#x20;

In this guide, you will learn how to set up a user email verification process to a user registration feature (Sign Up).

You will create an app that includes user registration with email verification using [**Parse Server core features**](https://www.back4app.com/product/parse-server) through Back4App.

You will use the same method you used to implement the user registration, but instead of redirecting the user to a logged screen, you will ask the user to verify their email to log in.

## Goal

Build a User verification email process feature using Parse for a Flutter App.

## Prerequisites

**To complete this tutorial, you will need:**

:::hint{type="info"}
- [**Flutter version 2.2.x or later**](https://flutter.dev/docs/get-started/install)
- [**Android Studio&#x20;**](https://developer.android.com/studio)or [**VS Code installed**](https://code.visualstudio.com/) (with [**Plugins**](https://docs.flutter.dev/get-started/editor) Dart and Flutter)
- A Flutter app created in previous guide
  - **Note:&#x20;**&#x46;ollow the [**How to implement user password reset**](https://app.archbee.com/docs/_roxIyUMXoBue9I7uv49e/3uUNUqP0K0awBtYuIl4ES)
- Complete the previous guide so ou can have a better understanding of the ParseUser class.
- A device (not Simulator) running Android or iOS.
:::

## Understanding Email verification function

To better understand Email verification function, we will continue the development of the application started in the previous guide and implement the function.

We won’t explain the Flutter application code once this guide’s primary focus is using the Flutter with Parse. Following the next steps, you will build a Login e Logout App at Back4App Database.

## Let’s get started!

In the following steps, you will be able to build a Email verification function in App.

## 1 - Enable Email Verification

Let’s now enable the email verification on Back4App Dashboard. The email verification page has two properties: Verify User Emails and Prevent login if the email is not verified.
If you enable only the Verify User Emails option, the user will receive the verification email but will be able to log in and use the application normally. If you also enable the Prevent login if email is not verified option, the user will only log in after concluding the email verification process.

1. Go to your App at [**Back4App Website&#x20;**](https://www.back4app.com/)and click on Server Settings.
2. Find the Verification emails card and click on Settings\`.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/wr9xlDI1N7Nc4Vy5ofv4k_image.png)

&#x20;    3\. Click on Verify User Email and Prevent login if the email is not verified.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/_9JbI7rA6mvuVSNrdpjKt_image.png)

&#x20;    4\. Optional: Fill the empty fields and modify the ones that have already been filled based on your preferences.

&#x20;    5\. Click on the SAVE button.

## 2 - Update the Login/Logout/Reset Password App

Open Flutter project from the previous guide [**How to add user reset password to a Flutter App**](https://www.back4app.com/docs/flutter/parse-sdk/users/flutter-reset-password).

Search for the function doUserRegistration in the file main.dart.

After call function user.signUp();, call the user.logout() function, to ensure that the user does not log in until the email is confirmed.
Update the message informing the user to check the mailbox e redirect the user to Home Screen.

Replace the code inside doUserRegistration with:

```dart
1     void doUserRegistration() async {
2       final username = controllerUsername.text.trim();
3       final email = controllerEmail.text.trim();
4       final password = controllerPassword.text.trim();
5   
6       final user = ParseUser.createUser(username, password, email);
7  
8       var response = await user.signUp();
9
10      if (response.success) {
11        Message.showSuccess(
12            context: context,
13            message: 'User was successfully created! Please verify your email before Login',
14            onPressed: () async {
15              Navigator.pop(context);          
16            });
17      } else {
18        Message.showError(context: context, message: response.error!.message);
19      }
20    }
```

Note: The code for SignUp function has been explained previously.

## 3 - Test Sign Up

To test it, click on the Run button in Android Studio/VSCode.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/iNh3vr_XzZCIlbsEmBIUC_image.png" signedSrc size="50" width="325" height="636" position="center" caption}

Perform the registration process, clicking in button Sign Up.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/pDtStKebbW_WqtIxYUndH_image.png" signedSrc size="50" width="328" height="637" position="center" caption}

After SignUp we will receieve an email like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/kYovPCgzCVE_Ctjv40sTC_image.png)

After click in link to verify the email, the property will be setted to true in Parse Dashboard:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/e749HwlRRhsSWP_tU0tgv_image.png)

## 4 - Log in

To implement the Log In with Email Verification, you have just to implement a Parse User Logins just as described on [**User LogIn guide**](https://www.back4app.com/docs/flutter/parse-sdk/users/flutter-login).

If you have enabled the ‘Prevent login if email is not verified’ option in Step 2, you will get the following error if you try to login without verifying your email.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/1KdIfOJ1iG_hASdIqt-Rr_image.png" signedSrc size="50" width="328" height="637" position="center" caption}

## It’s done!

At this stage, you can Log in, Sign Up or Log out of your app using email verification with Parse Server core features through Back4App!
