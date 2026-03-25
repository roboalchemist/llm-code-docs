# Source: https://docs-containers.back4app.com/docs/platform/parse-email-verification.md

---
title: Verification emails
slug: docs/platform/parse-email-verification
description: In this tutorial, you will learn how to use Verification emails.
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-02-01T14:41:23.430Z
updatedAt: 2025-01-27T19:45:32.848Z
---

# Setup Parse email verification

## Introduction

In this guide, you will learn how to use Verification emails.

## Goal

- Change the Parse Server version.

## Prerequisites

:::hint{type="info"}
**There are no pre-requisites to read this page, however, to edit it you should be the owner.**
:::

## Verification emails

Enabling email verification in an application’s settings allows the application to reserve part of its experience for users with confirmed email addresses.

Email verification adds the emailVerified key to the Parse.User object. When a Parse User’s email is set or modified, then emailVerified is set to false. Parse then emails the user a link that will automatically set emailVerified to true.

This block looks like this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/tkAfOXlJZrkP9Eik1x_WR_image.png" signedSrc size="50" width="240" height="303" position="center" caption}

To edit and enable the Email Verification, please take a look at the following steps:

1. Go to your App at [**Back4App Website&#x20;**](https://www.back4app.com/)and click on Server Settings.
2. Find the “Verification emails” block and click on Settings.
3. Click on the Verify User Email box.
4. Fill in the empty fields and modify the ones that have already been filled based on your preferences.
5. Click on the SAVE button.

:::hint{type="danger"}
Note that you need to reach us in our live chat if you wish to edit the email body.
:::

## Would you like to use your email verification tool?

If you want to use an alternative service, take a look at one of which guides below:

- [**SendGrid**](https://help.back4app.com/hc/en-us/articles/360032214231-How-can-I-use-my-own-verification-email-tool-SENDGRID-)
- [**Mailgun**](https://help.back4app.com/hc/en-us/articles/360028152251-How-can-I-use-my-own-verification-email-tool-MAILGUN-)

## Conclusion

At this point, you have learned how to enable your email verification and customize it.
