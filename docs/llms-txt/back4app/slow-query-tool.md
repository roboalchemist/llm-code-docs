# Source: https://docs-containers.back4app.com/docs/parse-dashboard/analytics/slow-query-tool.md

---
title: Slow query report
slug: docs/parse-dashboard/analytics/slow-query-tool
description: Back4App automatically identifies inefficient and expensive queries so you know exactly where to make fixes and improvements to your app’s user experience.
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-02-09T13:37:20.353Z
updatedAt: 2025-01-27T20:04:29.082Z
---

# Eliminate app lag with our Slow Query Tool

## Introduction

This document defines our generic analytic **Slow requests report** that allows users to focus on response time and monitor the performance of their app requests. This report is designed to provide you with the important details about the problematic and slowest requests that have occurred in your application starting from 00:00 UTC of the current day. In this manner, you get a clear idea of the exact moment the unhandled request occurred. You can also ascertain parameters associated with the request as method and path, response status and response time (in milliseconds).

This report is exceptionally advantageous for developers as it helps them understand the precise cause of slow requests and eliminate the bottlenecks by identifying inefficient and expensive queries, thereby enabling them to improve app performance.

:::hint{type="danger"}
**This Analytic Report will work only if the Parse Server version of your app is equal to or greater than 2.8.4.**

**If you want to manage your Parse Server Version for 2.8.4, follow&#x20;**[**these instructions**](https://help.back4app.com/hc/en-us/articles/360016081032-Manage-Parse-Server-Version)**.**
:::

## Getting started

To start using the **Slow requests report** of your app, you need to:

1. Go to [**Back4App Website**](https://www.back4app.com/) and click on My Apps. Find your app and then click on DASHBOARD.2.  Select More > Analytics section and click on Slow Requests section under the Analytics tab.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/oR4bvfKpLt4rPu8cddE4S_image.png)

&#x20;    2\.  Select More > Analytics section and click on Slow Requests section under the Analytics tab.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/1ULpeW2XjtxORbGeAd5vB_image.png)

By now, you should be seeing a list on the right side of the Dashboard containing the slowest requests that have occurred in your app, starting from 00:00 UTC of the current day. This list will show all the vital information about the slow requests, including the exact date and time the request has occurred, its method and path, parameters associated with it, its response status, and also response time in milliseconds.

:::hint{type="info"}
**The list comprising slow requests is arranged from the request with the longest response time to the one with the shortest response time.**
:::

:::hint{type="info"}
**To see all the entries of the list, scroll down a little bit.**
:::

## Exploring the report

To explore the **Slow requests report** of your app, follow these steps:

1. If you don’t want to see all slow requests in the list at once, you can filter the necessary queries that are required in the report. To do so, you need to click on the Filterbutton located at the top right corner.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/TG90MqQdPFSZrSGpxGSbd_image.png)

&#x20;    2\. Select the filter you want to apply: Method, Path, or Response Status of your slow requests. On selecting one of the filters, you can already run a query. You can also pick multiple filter items from the options . After choosing the filter (or filters) you want, go to the bottom right corner of your Dashboard and click on the Run query button.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/b2aVagKHVWuR8NhZmu2JW_image.png)

:::hint{type="danger"}
Be aware that if you select a new filter, you can’t undo this selection, except if you click on Clear all. This option will automatically clear all your filter selections.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/9rUAgGfDAFzS70kP7mra0_image.png)
:::

&#x20;    3\. Now, your filtered query is done, as shown in the image below.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Ih4vSan8jN8vEnmaTp41N_image.png)

&#x20;    4\. If you want to download the report data, click on the Download button placed on the top right of the screen.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/-TeeRpTM5GAniUerqrW-c_image.png)

## It’s done!

Congratulations! Now, you can explore the **Slow requests report** of your app through Back4App and identify as well as optimize slow requests!
