# Source: https://docs-containers.back4app.com/docs/platform/custom-parse-options.md

---
title: Custom Parse Options
slug: docs/platform/custom-parse-options
description: In this tutorial, you will learn how to work with Custom Parse Options.
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-01-31T16:21:40.893Z
updatedAt: 2025-01-27T19:45:11.682Z
---

## Introduction

In this guide, you will learn how to add and edit your Custom Parse Options.

## Goal

- Configure the Parse Server Options.

## Prerequisites

:::hint{type="info"}
**There are no pre-requisites to read or edit this page.**
:::

## Parse Server Options

When you create a new application at Back4App, we will create all your application backend structure and it builds your database structure, your application layer, and your APIs. We do it all, thinking about scalability and security.

While your app is being created, a file called config.json will be generated with the options that contain the configuration like keys to starting the app in the JSON format.

This block looks like this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/NC3D9GCY83SL7CKJok3ZA_image.png" signedSrc size="40" width="239" height="305" position="center" caption}

## How to use it?

Now, we will show you some examples of properties that can be easily changed at this section.

:::hint{type="danger"}
Note that this is a **DANGER ZONE**. Your app can stop working if you do something wrong. If you are not sure, ask for support.
:::

Please, check the following topics about how to use each property below:

### **Property: allowCustomObjectId**

Enable (or disable) custom objectId.

```json
{
    "allowCustomObjectId": true
}
```

### **Property: customPages**

With this property, you will be able to add custom pages for password validation and reset.

**1 - Enable your Webhosting**

The first step that you need to take is to enable your web hosting following [**this guide**](https://www.back4app.com/docs/platform/parse-web-hosting).

**2 - Upload the HTML files**

At this step, You only need to deploy these static HTML pages in your “public” folder on cloud code. Please, download the following templates to edit them:

::File[]{src="https://api.archbee.com/api/presign/yD3zCY-NNBBIfd0uqcfR5/aNXpCyDvMy8bdzXoB9pXY_choose-password.html" label="choose_password.html"}

::File[]{src="https://api.archbee.com/api/presign/yD3zCY-NNBBIfd0uqcfR5/iyI0RtmQH0_LW5swCCuRw_invalid-link.html" label="invalid_link.html"}

::File[]{src="https://api.archbee.com/api/presign/yD3zCY-NNBBIfd0uqcfR5/_x0rDq9PPlCurkL2kOcZY_invalid-verification-link.html" label="invalid_verification_link.html"}

::File[]{src="https://api.archbee.com/api/presign/yD3zCY-NNBBIfd0uqcfR5/Q6viDQiA5zA7m5XfkRUcM_link-send-fail.html" label="link_send_fail.html"}

::File[]{src="https://api.archbee.com/api/presign/yD3zCY-NNBBIfd0uqcfR5/LY_amC4Mu6O5ilSOY9TP2_link-send-success.html" label="link_send_success.html"}

::File[]{src="https://api.archbee.com/api/presign/yD3zCY-NNBBIfd0uqcfR5/OJ8hRCzPvXJcfpF-nFCKU_password-reset-success.html" label="password_reset_success.html"}

::File[]{src="https://api.archbee.com/api/presign/yD3zCY-NNBBIfd0uqcfR5/2VtVz1ZbmW4pBoVoUWG_z_verify-email-success.html" label="verify_email_success.html"}

:::hint{type="danger"}
Before uploading these files, please make sure that your file name doesn’t have spaces.
:::

**3 - Configuring the custom pages**

The configuration will look like something below:

Example:

```json
{
    "customPages": {
        "invalidLink": "https://<subdomain>.b4a.app/invalid_link.html",
        "verifyEmailSuccess": "https://<subdomain>.b4a.app/verify_email_success.html",
        "choosePassword": "https://<subdomain>.b4a.app/choose_password.html",
        "passwordResetSuccess": "https://<subdomain>.b4a.app/password_reset_success.html",
        "invalidVerificationLink": "https://<subdomain>.b4a.app/invalid_verification_link.html",
        "linkSendFail": "https://<subdomain>.b4a.app/link_send_fail.html",
        "linkSendSuccess": "https://<subdomain>.b4a.app/link_send_success.html"
    }
}
```

Check how to [**create your subdomain here**](https://www.back4app.com/docs/platform/activating-web-hosting)

### **Property: sessionLength**

This property configures the expiration date of your sessions, in seconds (defaults to 1 year).

Example:

```json
{
    "sessionLength": 31622400
}
```

### &#x20;**Property: emailVerifyTokenValidityDuration**

This property configures the email verification token validity duration, in seconds.

Example:

```json
{
    "emailVerifyTokenValidityDuration": Number
}
```

### **Property: enableAnonymousUsers**

With this property, you will be able to enable (or disable) anon users, defaults to true.

&#x20;Example:

```json
{
    "enableAnonymousUsers": false
}
```

### **Property: enableSingleSchemaCache**

Use a single schema cache shared across requests. Reduces the number of queries made to \_SCHEMA, defaults to false, i.e. unique schema cache per request.

Example:

```json
{
    "enableSingleSchemaCache": true
}
```

### **Property: expireInactiveSessions**

Sets whether we should expire the inactive sessions, defaults to true.

Example:

```json
{
    "expireInactiveSessions": false
}
```

### **Property: objectIdSize**

Sets the number of characters in generated object IDs, default 10.

Example:

```json
{
    "objectIdSize": Number
}
```

### **Property: preserveFileName**

Enable (or disable) the addition of a unique hash to the file names.

Note that it is recommended to keep it as false to prevent errors while trying to delete the unused files!

Example:

```json
{
    "preserveFileName": Boolean
}
```

## Conclusion

At this point, you have learned how to customize your Parse Server Options.
