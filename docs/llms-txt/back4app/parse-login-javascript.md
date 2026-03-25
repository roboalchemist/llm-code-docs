# Source: https://docs-containers.back4app.com/docs/javascript/parse-login-javascript.md

---
title: User Registration - login
slug: docs/javascript/parse-login-javascript
description: In this guide you learn how to add user registration and login to your Parse App
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-05T13:34:45.298Z
updatedAt: 2025-03-21T19:12:56.287Z
---

# Add JavaScript user registration and log in to your Parse App

## Introduction

This section explains how to do a basic user registration with email verification in a JavaScript environment through [**Back4app**](https://www.back4app.com/).

In this tutorial, you will use Parse.User object and will learn its most important functions.

:::hint{type="success"}
See more about Parse SDK at [**Parse JavaScript SDK API Reference**](https://parseplatform.org/Parse-SDK-JS/api/4.3.1/) and [**Parse open source documentation for JavaScript SDK**](https://docs.parseplatform.org/js/guide/).
:::

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- A basic JavaScript app connected with Back4app or JSBin connected with our Parse API.
- **Note:&#x20;**&#x59;ou can use the app created in our [**JavaScript Install Parse SDK tutorial**](https://www.back4app.com/docs/javascript/parse-javascript-sdk) or use the same online environment [**JSBin**](https://jsbin.com/?html,js,output) with the setup done in the J[**avaScript Database Operations tutorial**](https://www.back4app.com/docs/javascript/serverless-database).
:::

## 1 - Sign Up

The user sign-up function is similar to the create function used in the [**JavaScript Database Operations tutorial**](https://www.back4app.com/docs/javascript/serverless-database), but it has some additional benefits:

- Check if the username and email are unique.
- Securely hashes the password in the cloud. Not even the developer can see the user’s password.
- Requires at least a username and a password. You can use the email as a username if you want to.

:::hint{type="info"}
You can open the [**Back4app JavaScript Sign Up Function**](https://jsbin.com/guhikig/edit?html,js,console) to see the code that has already been implemented.
:::

To make your own signUp function, you need to repeat the same steps of the create function explained in the [**Javascript CRUD tutorial**](https://www.back4app.com/docs/javascript/serverless-database) but call the method user.signUp instead of the save method, as shown below:

:::CodeblockTabs
signUp.js

```javascript
signUp();

function signUp() {
    // Create a new instance of the user class
    var user = new Parse.User();
    user.set("username", "my name");
    user.set("password", "my pass");
    user.set("email", "email@example.com");

    // other fields can be set just like with Parse.Object
    user.set("phone", "415-392-0202");

    user.signUp().then(function(user) {
        console.log('User created successful with name: ' + user.get("username") + ' and email: ' + user.get("email"));
    }).catch(function(error){
        console.log("Error: " + error.code + " " + error.message);
    });
}
```
:::

:::hint{type="danger"}
- Be aware that **Error 202** or **Error 203** is likely to occur if you don’t change the username or the email.
-
  The **Error 209** *invalid season* token is also likely to occur when your browser cookies conflict
  &#x20;with your Parse’s Current Session. To bypass that, clear your browser cookies or open the
  &#x20;incognito mode of your browser.
  To confirm that the new user has been added to the database, you can access your Parse Dashboard or code the login function which will be provided ahead.
:::

## 2 - Email Verification

An important feature of a sign-up method is email verification.
Fortunately, it is easy to configure it using Back4App. To enable email verification, login to your account, find your app, and click on Server Settings.
Find the “Verification Emails” box and click on SETTINGS. Here’s how the “Verification Emails” box looks like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/NDs8FvH4tfewWxQZRzLaW_image.png)

Then enable the verification by checking the box below.

:::hint{type="info"}
If you are using the cloud environment of JSBin, then there is no need to complete this step.
:::

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/7W_ZO1xEu0wKLOd2IZZWH_image.png)

:::hint{type="info"}
By enabling this, the user’s class in your database receives one additional field: verifiedEmail.
This field is set to true when the email is verified, false if the email isn’t verified, and
undefined if the user was created before this setting was checked.
:::

On that page, you can also customize the email, change the subject, the body, and the sender’s email and name.

:::hint{type="info"}
To see how the email looks like, just create a user, using the signUp function,
with an email that you can access. You should receive an email for verification.
:::

## 3 - Login

The login function is very simple and just needs a password and a username to run.

:::hint{type="info"}
You can open the [**Back4app JavaScript Login Function**](https://jsbin.com/delazew/edit?html,js,console) to see the code that has already been implemented.
:::

You need to call the Parse.User.logIn method is as follows:

:::CodeblockTabs
login.js

```javascript
logIn();

function logIn() {
    // Create a new instance of the user class
    var user = Parse.User
        .logIn("myname", "mypass").then(function(user) {
            console.log('User created successful with name: ' + user.get("username") + ' and email: ' + user.get("email"));
    }).catch(function(error){
        console.log("Error: " + error.code + " " + error.message);
    });
}
```
:::

## 4 - Reset Password

It’s **very important** to add the **Reset Password** option as users are likely to forget their password in the future.
The configuration for the email that will be sent in the reset password function is on the same
page as in the **Email Verification step**. There you can change the body and the subject of the email.

:::hint{type="info"}
You can open the [**Back4app JavaScript Reset Password Function**](https://jsbin.com/guwuben/edit?html,js,console,output) to see the code that has already been implemented.
:::

To send the Reset Password email, just run the following code:

:::CodeblockTabs
resetpassword.js

```javascript
resetPassword();

function resetPassword() {
    Parse.User.requestPasswordReset("email@example.com").then(function() {
      console.log("Password reset request was sent successfully");
    }).catch(function(error) {
      console.log("The login failed with error: " + error.code + " " + error.message);
    });
}
```
:::

## It’s done!

At this point, you have learned not only how to do User Registration with JavaScript apps, but also how to send email verification and password reset emails.
