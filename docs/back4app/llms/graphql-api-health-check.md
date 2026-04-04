# Source: https://docs-containers.back4app.com/docs/parse-graphql/graphql-api-health-check.md

---
title: Checking the API health
slug: docs/parse-graphql/graphql-api-health-check
description: This is a recipe for checking the Parse Server backend health through the GraphQL API.
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-02-15T20:22:57.755Z
updatedAt: 2025-01-27T20:04:42.439Z
---

# Checking the Parse GraphQL API health

## Problem

You want to check the Parse Server backend health through the GraphQL API.

## Solution

Using the Parse GraphQL API, you can check the backend health by calling the health query.

Example:

:::BlockQuote
**&#x20;  query** Health \{
&#x20;  health
&#x20;  }
:::

Result:

:::BlockQuote
&#x20;  \{
&#x20;  "data": \{
&#x20;  "health": **true**
&#x20;  }
&#x20;  }
:::

