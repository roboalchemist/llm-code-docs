# Source: https://docs-containers.back4app.com/docs/parse-dashboard/app-settings.md

# Source: https://docs-containers.back4app.com/docs/platform/app-settings.md

---
title: Core Settings
slug: docs/platform/app-settings
description: In this tutorial, you will learn how to find your unique identifiers to access this App.
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-01-31T12:36:10.957Z
updatedAt: 2025-01-27T19:45:02.100Z
---

# Manage the App Core Settings

## Introduction

Once your app is created on Back4app, you have a feature called Core Settings which allows to find/edit your keys, restart, transfer or delete the app.

This guide shows the main functionalities and what you can do at this page.

## Goal

- Know the page permits.

## Prerequisites

:::hint{type="info"}
**There are no pre-requisites to read this page, however, some functionalities are allowed only to the app’s owner**
:::

## 1 - Access your Core Settings and find your keys

Access your Back4App account, find your app and go to the Server Settings > Core Settings > Settings. This block looks like:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/VB5hamqzZtZZiOIKvYMU4_image.png" signedSrc size="30" width="243" height="304" position="center" caption}

On this page, you have access to your app details and keys to connect to it via SDK or REST.

## 2 - Page features

There are options like editing the details of your app, restarting, transferring, cloning, and deleting your app. All these functionalities are located at the end of the page:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/5QxsNXpWgsImGO6MUOhYY_image.png" signedSrc size="40" width="407" height="267" position="center" caption}

## **2.1 - Edit details**

The first button can be used to edit the name, description, keys, enable/disable properties, or even your application’s Connection String.

### **2.1.1 - App name and description**

Right after you click on this button, you will be able to edit the name and the descriptions of your app. For both options, you can click on the blanks and write as you think is the best for your app.

### **2.1.2 - Keys**

You can also edit the Client Key, Javascript Key, .NET key, REST API Key, Webhook Key, File Key, and Master Key. To do this, search on the page what you want to change, click in the box that there is the old one, and generate a new one.

### **2.1.3 - Connection String**

Be careful if you want to change the *Connection String* because you will finish the past references that were linked with the last URI. To do this, you must click on the change database URI and sequentially click on OK.

### **2.1.4 - Allow class creation and push notifications**

1. **Allow class creation:** By enabling this option, the user will be able to create a new class in the database without the administrator’s permission. In this case, you have to be careful with this action.
2. **Allow push notifications from client:** By enabling this option, the user will be able to send notifications to other users. This operation is hazardous because you allow users to break into the privacy of others. Consequently, you turn your app vulnerable to security problems.

### **2.1.5 - Applying changes**

After all this process you click in the box SAVE button to apply all the new modifications.

## **2.2 - Restart App**

By clicking on this button, you are restarting your app activity including a kill of the current process, and switch on it sequentially.

When you click on it, a box will appear asking if you want to do this; if yes, click on OK, otherwise, click on CANCEL.

## **2.3 - Transfer App**

After clicking on this option, you will transfer the possession of the app to another user, to do this you click in the blank and write the e-mail of this person. So, you will be asked to accept the transfer.

## **2.4 - Clone App**

You use this option to create a new app with the same database as the app that you are working on. To do this, you click in the blank to give a name to your new app, click on the box to clone the database, and click on the CLONE button to confirm the action.

## **2.5 - Delete App**

When you click on this option, you lose, irreversibly, the power of being the administrator of the app. After clicking on this option, you must write the application name and click on the red button (DELETE) to complete this action.
