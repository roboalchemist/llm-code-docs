# Source: https://docs-containers.back4app.com/docs/parse-dashboard/api-reference.md

---
title: API Reference
slug: docs/parse-dashboard/api-reference
description: In this tutorial, you will learn what is and how to use the API Reference.
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-02-05T13:34:41.040Z
updatedAt: 2025-01-27T20:04:07.252Z
---

# API Reference

## Introduction

In this tutorial, you will learn what is and how to use the API Reference.

## Goal

- Access and use the API Reference.

## Prerequisites

:::hint{type="info"}
**There are no pre-requisites to read or edit this page.**
:::

### API Reference

The API Documentation tool generates docs for any objects saved in your database and with this tool, we provide code snippets for each of the supported programming languages, so your documentation lives right alongside your data. Your API keys are provided in the docs so you don’t need to jump back and forth between two different things.

Back4App’s API Documentation tool creates this dynamic environment for any project.

You can access it going to: Dashboard > API Reference or you can find the button in any class to the API Reference panel.

**How it works?**

We’ll briefly go through each of the sections.

**Introduction**

Contains background information on the Back4App API.

**Getting Started**

The main sections that we need to highlight are:

- **Installing Parse SDK&#x20;**&#x70;rovides links to each of the Parse SDKs. These are libraries for integrating the frontend of your project with your Back4App server.
- **Initializing Parse SDK** presents your keys. You’ll also notice on the left you can page between different languages to see how to initialize your project. This is great because you can copy this code directly, and not have to track down your keys separately!
  api-reference-initializing-sdk
- **Objects API&#x20;**&#x74;his section provides detailed information on what Parse Objects are and how the API works. It also explains how to create classes on the fly- unlike what we did with the data browser. I highly recommend reading this section!&#x20;
- **User API&#x20;**&#x61;nother important section with API calls for interacting with the special User class. It has the same methods as normal objects but adds some authentication items.
- **Queries&#x20;**&#x63;an be used to explore the Query capabilities.
- **Errors&#x20;**&#x69;f your server sends back an error, this is where you can find out what the numeric code means.

Read more about it in this [**post blog**](https://blog.back4app.com/2018/12/14/the-api-reference-tool/).

