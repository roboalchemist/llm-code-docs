# Source: https://docs-containers.back4app.com/docs/platform/parse-live-query.md

---
title: Enable Live Query
slug: docs/platform/parse-live-query
description: In this guide you learn how to enable the Live query.
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-02-01T14:20:01.954Z
updatedAt: 2025-01-27T19:45:21.953Z
---

# Activating your Live Query

## Introduction

The Query is one of the key concepts for Parse Technology. It allows you to retrieve objects by specifying some conditions, making it easy to build apps such as social networks, dashboards, mobile commerce, and also amazing games. However, Parse.Query is based on a pull model, which is not suitable for apps that need real-time support.

Suppose you are building an app that needs real-time messages like a chat-app. Parse.Query would not be an ideal solution since a user app doesn’t know when another one updated a conversation with a new message. In this case, the database has a new update to inform the other to query from the server to get the updates.

**LiveQuery solves this problem.** This tool allows you to subscribe to a Parse.Query you are interested in. Once subscribed, the server will notify clients whenever a Parse.Object that matches the Parse.Query is created or updated, in real-time.

At this guide, we’re going to show you how to activate LiveQueries to your App.

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- A verified account at Back4App.
- An app created in Back4App.
  - Check this [**Create New App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create an app at Back4App.
:::

## How can I use this feature?

When you enable the Live Query feature is a guarantee that you can use more functionalities in Back4App side, so, it has the many different purposes that are described below. You will also learn the process of setting up a subdomain later, in the following instructions.

## 1 - Locate the feature block

To locate and enable your Live Query feature, log in to your Back4App account go to the My Apps option, and then click on Server Settings. After that, search for the Server URL and Live Query and select Settings. The Server URL and Live Query section looks like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/s0-t_ufZcSOI82tmZgpZ0_image.png)

## **2 - Use Live Query in your App**

To enable client-LiveQuery server interaction, it’s necessary to activate the Live Query in the Web Hosting box and select the Class that will allow communication between the client and server. The section related to this is shown below:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/CES9K-MM9MUICVUYqU3xj_image.png" signedSrc size="50" width="846" height="899" position="center" caption}

## **3 - Change the default serverURL**

You can change the default URL [**https://parseapi.back4app.com/**](https://parseapi.back4app.com/) to your subdomain [**\* .b4a.io/**](https://www.back4app.com/docs/platform/*.b4a.io/).

With the guide described above, you’ll be able to set a custom API address with Back4App and enable as well with various features, including using Live Query and changing your ServerURL!
