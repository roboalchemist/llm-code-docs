# Source: https://docs-containers.back4app.com/docs/parse-graphql/graphql-email-verification.md

---
title: Email verification
slug: docs/parse-graphql/graphql-email-verification
description: This is a recipe for creating an object in Parse Server backend through the GraphQL API.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-02-27T13:21:01.418Z
updatedAt: 2025-01-27T20:05:16.670Z
---

# Request Password Reset with Parse GraphQL API

## **Problem**

You want to send an email verification to a user in your database through the Parse GraphQL API.

## **Version Information**

It is only available for Parse Server 3.10.0 and later.&#x20;

:::CodeblockTabs
Request

```graphql
1   mutation sendVerificationEmail {
2     sendVerificationEmail(input: { email: "example@email.com" }) {
3       ok
4     }
5   }
```

Response

```graphql
1   {
2     "data": {
3       "sendVerificationEmail": {
4         "ok": true
5       }
6     }
7   }
```
:::

