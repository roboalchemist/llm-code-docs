# Source: https://docs-containers.back4app.com/docs/security/multi-factor-authentication.md

---
title: MFA- User Account
slug: docs/security/multi-factor-authentication
description: In this guide you learn how to configure and use the Multi-factor Authentication
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-02-26T18:26:05.762Z
updatedAt: 2025-01-17T01:09:27.327Z
---

# How to Implement Multi-Factor Authentication in your Back4App Account

## Introduction

This section explains how you can setup and configure MFA to your Back4App Account. After completing this, step-by-step, you will be one step closer to secure your accounts and data.

## Prerequisites

:::hint{type="info"}
**To get started with this tutorial, you will need:**

- An account created in [**Back4App**](https://www.back4app.com/)
- You can download the app from [**Google Play Store**](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2\&hl=en)[**&#x20;or App Store**](https://itunes.apple.com/us/app/google-authenticator/id388497605?mt=8)
:::

# What is MFA?

MFA is the abbreviation for Multi-Factor Authentication that is a method to confirm a user’s identify by validating several (two or more) authentication stages. We deliver strong authentication with the simple sign-in process to provide an extra layer of security to our clients. Also, we add additional layers of protection not just on top of clients’ username and password, but also on their sensitive information that only they need to know.

## Why is this necessary?

This newly implemented method will assegure more security for your account and prevent attackers to bypass the security filter. For example, if your account and password are compromised, you will have another layer of protection to keep cybercriminals at bay.

# 3 Steps to enable MFA on your device

After creating your account in Back4App and downloading the Google Authentication app (see [**prereqs**](https://www.back4app.com/docs/security/multi-factor-authentication#content-prerequisites)), you can easily configure it on your device.

## 1 - log in to your Back4App account and generate an access token

After successfully accessing your account with credentials, go to the menu and hover your cursor over theHello, \< username >button in the top-right corner, and then click on Multi-Factor Authentication:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Wc0AskPqaDaP5hHAYJUMO_image.png" signedSrc size="60" width="262" height="219" position="center" caption}

## 2 - Scan the generated access token

Next, you will need to click on the red button ‘+’ in your device and scan the code generated on the screen from Back4App. After scanning the code, it will auto-generate a six-digit number, like the image below:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/WWOihZDG3ws8JJ8OOeJCU_image.png" signedSrc size="80" width="600" height="338" position="center" caption}

Then, you need to insert into Multi-Factor Authentication in your Back4App Account and click on the button Confirm Multi-Factor Authorization.

## 3 - MFA Activated

If you follow all the above mentioned steps and enter the correct code, you will be redirected to a Back4App success page!

**Now, we’re ready to test it!**

Hover your cursor over the Hello, \< username > button in the top-right corner of your device and click on the Logout link. Afterward, when you’ll try to login to your account, you’ll be able to see a new field like in the image below:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/FcnG0Gr_xzXqgWVDFMcSj_image.png" signedSrc size="40" width="351" height="515" position="center" caption}

Are you able to Log in? If yes, then congratulations! It seems like that you’ve followed this tutorial and all the steps splendidly. If you are facing any error or need any help to configure MFA on your device, please contact our Support Team!
