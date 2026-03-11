# Source: https://docs-containers.back4app.com/docs/parse-graphql/graphql-password-reset.md

---
title: Password reset
slug: docs/parse-graphql/graphql-password-reset
description: This is a recipe for creating an object in Parse Server backend through the GraphQL API.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-02-27T13:23:53.269Z
updatedAt: 2025-01-27T20:05:19.844Z
---

# Request Password Reset with Parse GraphQL API&#x20;

## Problem

You want to request a reset password to a user in your database through the Parse GraphQL API.

## Version Information

It is only available for Parse Server 3.10.0 and later.

:::CodeblockTabs
Request

```graphql
1   mutation resetPassword {
2     resetPassword(input: { email: "example@email.com" }) {
3       ok
4     }
5   }
```

Response

```graphql
1   {
2     "data": {
3       "resetPassword": {
4         "ok": true
5       }
6     }
7   }
```
:::

