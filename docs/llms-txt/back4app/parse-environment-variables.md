# Source: https://docs-containers.back4app.com/docs/platform/parse-environment-variables.md

---
title: Environment Variables
slug: docs/platform/parse-environment-variables
description: In this tutorial, you will learn how to configure environment variables and use them.
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-01-31T16:35:39.161Z
updatedAt: 2025-01-27T19:45:15.473Z
---

# Setting up Environment Variables on Parse

## Introduction

In this guide, you will learn how to configure Environment variables.

## Goal

- Learn how to set and use Environment Variables page.

## Prerequisites

:::hint{type="info"}
**There are no pre-requisites to read or edit this page.**
:::

## Environment Variables

They are variables that describes your environment. While constants cannot be reassigned during the execution, an *Environment Variables* may change.

One of the most popular *Environment Variable* is **PATH** which contains path to the folders that might contain the executables.

In a few words, an environment variable consists of a name / value pair and any number can be created and available for reference at any given time.

Here at Back4App, this block looks like:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/YCzjuWr4srI06MPUbYNzj_image.png" signedSrc size="40" width="238" height="303" position="center" caption}

### **How to use it?**

In this section, we are going to show you how to set an *Environment Variable* and use it on our Cloud Code.

The first step, what you need to is to access Server Settings > Environment Variables > Settings and set *environment variables* using KEY=VALUE format. Please, put each variable in one line. Something like the example below:

:::BlockQuote
1    NODE\_ENV=PRODUCTION
:::

To use it on your Cloud Code, you can test it following the guide below:

:::::Tabs
::::Tab{title="Parse Server 3.X"}
:::CodeblockTabs
main.js

```javascript
1   Parse.Cloud.define("getEnvironmentVariable", (request) => {
2     const NODE_ENV = process.env.NODE_ENV;
3  
4     return `NODE_ENV = ${NODE_ENV}`
5   });
```
:::
::::

::::Tab{title="Parse Server 2.X"}
:::CodeblockTabs
main.js

```javascript
1   Parse.Cloud.define("getEnvironmentVariable", function(request, response) {
2      var NODE_ENV = process.env.NODE_ENV;
3
4      response.success(NODE_ENV);
5   });
```
:::
::::
:::::

To test it, you can use API Console to call this Cloud Code function and test it.
