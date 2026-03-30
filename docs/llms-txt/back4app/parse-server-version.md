# Source: https://docs-containers.back4app.com/docs/platform/parse-server-version.md

---
title: Parse Server Version
slug: docs/platform/parse-server-version
description: In this tutorial, you will learn how to find the Parse Server versions and change it.
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-01-31T12:41:22.792Z
updatedAt: 2025-11-10T21:58:32.374Z
---

## Introduction

In this guide, you will learn how to change your Parse Server version.

## Goal

- Change the Parse Server version.

## Prerequisites

:::hint{type="info"}
**There are no pre-requisites to read this page, however, to change it, you should be the app owner.**
:::

## Parse Server

[**Parse Server**](https://blog.back4app.com/2020/03/17/managed-parse-server/) is an open-source framework that powers an application backend and it speeds up the time for developers by simplifying complicated programming tasks.

The Parse Server community is very active and often new versions [**are released**](https://github.com/parse-community/parse-server/releases). By changing the version of your app, you will be guaranteed to update to the latest version of Parse Server. All it takes is a single click on the Change Version option to upgrade or downgrade server versions.

It’s very simple, all you have to do is go to Manage Parse Server available at Server Settings, this block looks like below:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/JomXSrOdmsadkeBVMK2Az_image.png" signedSrc size="40" width="244" height="304" position="center" caption darkWidth="244" darkHeight="304"}

Now, you can select the version you’d like to have and click on the SAVE button.

## Breaking Changes

Before upgrading to a newer version of Parse Server, it is highly recommended that you keep a [**development app**](https://www.back4app.com/docs/platform/app-settings#clone-app) to apply this change.

Also, in this topic, you can check the most common errors to not stumble upon a breaking change. See:

### Parse Server 7.5.2&#x20;

**Live Queries — Parse Swift 5 compatibility**
Older Parse Server versions **are not fully compatible with Live Queries when using&#x20;**[**Parse Swift 5.**](https://swiftpackageindex.com/netreconlab/Parse-Swift)****

Upgrading to **Parse Server 7.5.2** is required to ensure compatibility.

### Parse Server 6.2.0&#x20;

In this version, there is a security implementation in terms of ACL for Users who are not set as public read anymore.&#x20;

However, in case you'd like to bypass it (not recommended, as this allows other users and unauthenticated users to read data such as `email`), you need to add the following configuration in your [**custom parse options**](https://www.back4app.com/docs/platform/custom-parse-options):

```json
{
    "enforcePrivateUsers": false
}
```

### Parse Server 5.2.3&#x20;

In this version, there is a security implementation in terms of uploading files to your app.

It’s required to add the following configuration in your [**custom parse options**](https://www.back4app.com/docs/platform/custom-parse-options) to make it work.

```json
{
    "fileUpload": {
        "enableForPublic": true,
        "enableForAnonymousUser": true,
        "enableForAuthenticatedUser": true
    }
}
```

- **enableForPublic**: Is true if file upload should be allowed for anyone, regardless of user authentication.
- **enableForAnonymousUser**: Is true if file upload should be allowed for anonymous users.
- **enableForAuthenticatedUser:** Is true if file upload should be allowed for authenticated users.

**Deprecation: Database HUB - Connection**
This version no longer supports connection with datasets from [**Database Hub**](https://back4app.com/database). Clone is still available.

### **Parse Server 3.7.2**

Before upgrading to a Parse Server version equal to or higher than 3.7.2, note that word id turned into a reserved field and it is related to GraphQL implementations. Note that you might not be able to manage your objects with Create, Read, Update, or Delete via REST API or SDK.

### **Parse Server 3.1.1**

&#x20;Two problems might happen:

1. There’s a breaking change through the upgrade from 2.x to 3.x related to the cloud code, and you can read more about the changes [**here**](https://www.back4app.com/docs/advanced-guides/parse-server-3). In other words, this update has cleaned up Cloud Code syntax.
2. Before you change to this version, there is a possibility provided by Parse Server which allows the user to save the audience for tracking and sending a Push notification, so you need to remove this class to prevent problems with the dashboard and database.

### Parse Server 2.6.5

**Before** upgrading to this version, you need to make sure that you don’t have any expired certificates added to your app, please go to Server Settings > iOS Push notification > Settings and check if there are any expired certificates.

To renew the certificate, you can upload a new one following [**this documentation**](https://www.back4app.com/docs/ios/push-notifications/best-ios-push-notification-service#step-1---create-your-push-certificates-in-the-apple-developer-center) about generating an iOS certificate.

### **Parse Server 2.2.14**

Revocable sessions were introduced in the middle of 2015 and it helped to improve the security for users. So, if it is your current version, you must be aware of a very common problem related to Legacy Token.

At this moment, if you are using Legacy Token, it’s necessary to change to Revocable Token before selecting a newer version. This link can help you with it:

[**Revocable Token migration tutorial**](https://web.archive.org/web/20170101001730/https://parse.com/tutorials/session-migration-tutorial)&#x20;

:::hint{type="info"}
If you got some error and the solutions above don’t work for you, please contact our support team via [**App Id**](https://www.back4app.com/docs/platform/parse-server-version) chat.
:::

## Conclusion

At this point, you have learned how to upgrade or downgrade your current Parse Server version and possible breaking changes based on the most common errors.
