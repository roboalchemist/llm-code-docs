# Source: https://docs-containers.back4app.com/docs/flutter/parse-sdk/users/flutter-reset-password.md

---
title: Reset Password
slug: docs/flutter/parse-sdk/users/flutter-reset-password
description: In this guide you learn how implement Flutter user reset password
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-18T14:43:31.745Z
updatedAt: 2025-01-16T20:37:17.527Z
---

# How to add user reset password to a Flutter App

## Introduction

It’s a fact that as soon as you introduce passwords into a system, users will forget them. Parse Server provides a way to let them securely reset their password.
The password reset flow starts getting the user’s email address and calling the requestPasswordReset method from Parse.User class.
This will attempt to match the given email with the user’s email or username field and send them a password reset email. By doing this, you can opt to have users use their email as their username, or you can collect it separately and store it in the email field.

The flow for password reset is as follows:

1. **User requests that their password be reset by typing in their email.**
2. **Back4App sends an email to their address with a special password reset link.**
3. **User clicks on the reset link and is directed to a special Back4App page to type in a new password.**
4. **User types in a new password. Their password has now been reset to a value they specify.**

In this guide, you will learn how to use the **Flutter plugin for Parse Server** to implement user reset password feature using the ParseUser class for your Flutter App.

## Goal

Build a reset password feature using Parse for a Flutter App.

## Prerequisites

**To complete this tutorial, you will need:**

:::hint{type="info"}
- [**Flutter version 2.2.x or later**](https://flutter.dev/docs/get-started/install)
- [**Android Studio&#x20;**](https://developer.android.com/studio)or [**VS Code installed**](https://code.visualstudio.com/) (with [**Plugins**](https://docs.flutter.dev/get-started/editor) Dart and Flutter)
- A Flutter app created in previous guide
  - **Note:&#x20;**&#x46;ollow the [**Get current User**](https://app.archbee.com/docs/_roxIyUMXoBue9I7uv49e/HzbuRMIWCUKmJmsxuDirt) on session.
- Complete the previous guide so ou can have a better understanding of the ParseUser class.
- A device (not Simulator) running Android or iOS.
:::

## Understanding Reset Password process

To better understand Reset Password process, we will continue the development of the application started in the previous guide and implement the function.

We won’t explain the Flutter application code once this guide’s primary focus is using the Flutter with Parse. Following the next steps, you will build a Login e Logout App at Back4App Database.

## Let’s get started!

In the following steps, you will be able to build a reset password function in our application.

## 1 - Open the Login/Logout/Reset Password App Project

Open Flutter project from the previous guide [**Get current User on session**](https://www.back4app.com/docs/flutter/parse-sdk/flutter-current-user%22).

Go to the main.dart file.

## 2 - Code for Reset Password

To start the password reset flow, we need the user’s email. Search for the function doUserResetPassword in the file main.dart. Replace the code inside doUserResetPassword with:

```dart
1       final ParseUser user = ParseUser(null, null, controllerEmail.text.trim());
2       final ParseResponse parseResponse = await user.requestPasswordReset();
3       if (parseResponse.success) {
4         Message.showSuccess(
5             context: context,
6             message: 'Password reset instructions have been sent to email!',
7             onPressed: () {
8               Navigator.of(context).pop();
9             });
10      } else {
11        Message.showError(context: context, message: parseResponse.error!.message);
12      }
```

To build this function, follow these steps:

1. Create a newParseUser class instance with the command ParseUser(null, null, controllerEmail.text.trim());. The email field is required for the other fields you can use null.
2. Call theuser.requestPasswordReset function to send the recovery email.

The complete function should look like this:

```dart
1     void doUserResetPassword() async {
2       final ParseUser user = ParseUser(null, null, controllerEmail.text.trim());
3       final ParseResponse parseResponse = await user.requestPasswordReset();
4       if (parseResponse.success) {
5         Message.showSuccess(
6             context: context,
7             message: 'Password reset instructions have been sent to email!',
8             onPressed: () {
9               Navigator.of(context).pop();
10            });
11      } else {
12        Message.showError(context: context, message: parseResponse.error!.message);
13      }
14    }
```

:::hint{type="info"}
To test it, click on theRunbutton in Android Studio/VSCode.
:::

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/XYYxTqeltDKSytjtIrUL7_image.png" signedSrc size="50" width="321" height="635" position="center" caption}

Click on Reset Password button.

On the next screen enter the user’s email and click Reset Password again.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/IH_Bhhsw25tcslVOTp4Me_image.png" signedSrc size="50" width="325" height="636" position="center" caption}

## It’s done!

At the end of this guide, you can implement password reset function of your app using Parse Server core features through Back4App!
