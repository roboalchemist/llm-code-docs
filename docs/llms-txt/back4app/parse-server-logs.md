# Source: https://docs-containers.back4app.com/docs/platform/parse-server-logs.md

---
title: Logs
slug: docs/platform/parse-server-logs
description: In this tutorial, you will learn how to find your App logs.
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-01-31T12:48:04.764Z
updatedAt: 2025-01-27T19:45:08.566Z
---

# Parse Server Logs

## Introduction

In this guide, you will learn about the logs that you can find at the Back4App dashboard.

## Goal

- Understand the logs:
- System
- Info
- Error
- Access

## Prerequisites

:::hint{type="info"}
**There are no pre-requisites to read this page.**
:::

## Logs

Searching for logs? You’re in the right place :)

Logs are essential for development or production apps, it is an important way to understand what is happening with an aggregate output of the running processes. You must be able to track the app’s behaviors.

Application event logging is critical for understanding the requests and identifying possible loops or bugs in your code.

You can check them at the left menu, on Cloud Code > Logs. It looks like the image below:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/EbMZJzpBLUz4XsysY8K5i_image.png" signedSrc size="50" width="296" height="339" position="center" caption}

### **System**

The *System Log* shows the logs of console.log() and console.error() and all general logs of everything that happens with your app.

### **Info**

Here will appear the warnings about Cloud Code functions and triggers, as well as Live Query status.

### **Error**

Errors related to your Cloud Code functions or the database.

### **Access**

This block contains information about the [**requests**](https://help.back4app.com/hc/en-us/articles/115001377071-What-is-an-API-request-) that are coming into the server. The information is essential to understand where the data is being accessed from, as well as how it’s being accessed, by whom, and the status of requests.

## Sample Logs

Here you can find some examples of Back4App Logs:

::::ExpandableHeading
### System

:::BlockQuote
1   (node:19) \[DEP0066] DeprecationWarning: OutgoingMessage.prototype.\_headers is deprecated
2   (node:19) DeprecationWarning: The option \`reconnectInterval\` is incompatible with the unified topology, please read more by visiting http\://bit.ly/2D8WfT6
3   (node:18) DeprecationWarning: The option \`reconnectTries\` is incompatible with the unified topology, please read more by visiting http\://bit.ly/2D8WfT6
:::

At Back4App, the parse-cache module is set by default at versions higher than 2.8.4. Therefore, it’s also possible to see some warnings from Parse Server initialization:

:::BlockQuote
1   Using redis cache for query.cache() methods
2   Using memory cache for query.cache() methods
3   The server is listening on port 3000
:::

Cloud code syntax errors:

:::BlockQuote
1   Warning: main.js not found: to run any cloud code functions you need first to create a main.js file
2   Error loading your cloud code:
3    /usr/src/app/data/cloud/main.js:186
:::

And also console.log from Cloud Code triggers:

:::BlockQuote
1   This is the log from beforeSave trigger
:::
::::

::::ExpandableHeading
### Info

When the Server URL and Live Query are enabled for a class, a message will appear in this section:

:::BlockQuote
1   Parse LiveQuery Server starts running
:::

Calling a Cloud Code function will also be logged here:

:::BlockQuote
1   Ran cloud function helloWorld for user undefined with:
2   Input: \{}
:::

Running a Cloud Code function without a return statement:

:::BlockQuote
1   Ran cloud function helloWorld for user undefined with:
2   Input: \{}
3   Result: undefined
:::
::::

::::ExpandableHeading
### Error

Timeout errors:

:::BlockQuote
1   Uncaught internal server error. timeout of 1000ms exceeded
:::

Cloud Code triggers errors (see the example below):

```markdown
1  beforeSave failed for myClass for user undefined:
2    Input: {"Name":"Person","createdAt":"2021-06-16T17:12:54.863Z","updatedAt":"2021-06-16T17:17:14.717Z","objectId":"AsWn26ns4Q"}
3    Error: {"message":"You cannot save a person with age under 18!","code":141}
```
::::

:::ExpandableHeading
### Access

```markdown
1   2974:431:c7dc:5bb0:51ec:6258:6a16:e12b - - [2021-06-16T16:48:32.352Z] "POST /serverInfo"  200  1 ms  217 bytes_in  732 bytes_out
2   2974:431:c7dc:5bb0:51ec:6258:6a16:e12b - - [2021-06-16T16:47:26.879Z] "GET /classes/MyFirstClass"  200  50 ms  248 bytes_in  24 bytes_out
3   2974:431:c7dc:5bb0:51ec:6258:6a16:e12b - - [2021-06-16T16:46:57.068Z] "PUT /classes/MyFirstClass/Ao2ezFUQrS"  200  9 ms  240 bytes_in  40 bytes_out

```

After the endpoints, we can verify the response status code. Check some examples below:

```markdown
1   200 = The request has succeeded.
2   201 = The request has succeeded and a new resource has been created as a result. This is typically the response sent after POST or PUT requests.
3   204 = No content
4   400 = Bad request
5   401 = Unauthorized
6   404 = Not found
7   408 = Request timeout
8   500 = Internal server error
9   502 = Bad gateway
```

Calling Cloud Code functions will appear here too:

```markdown
1   2804:431:c7dc:5bb0:51ec:6258:6a16:e12b - - [2021-06-16T17:10:16.245Z] "POST /functions/hello"  200  2 ms  2 bytes_in  32 bytes_out
```
:::

