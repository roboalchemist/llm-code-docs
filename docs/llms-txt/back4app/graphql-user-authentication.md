# Source: https://docs-containers.back4app.com/docs/parse-graphql/graphql-user-authentication.md

---
title: Authenticating a user
slug: docs/parse-graphql/graphql-user-authentication
description: This is a recipe for authenticating a logged user in Parse Server backend through the GraphQL API.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-02-27T13:08:02.390Z
updatedAt: 2025-01-27T20:05:10.995Z
---

# Authenticating a logged user through the Parse GraphQL API

## Problem

You want to authenticate a logged user in your backend through the Parse GraphQL API.

## Solution

Using the Parse GraphQL API, you can authenticate a logged user just by sending the user’s sessionToken (that you may have acquired by [**signing up**](https://www.back4app.com/docs/parse-graphql/graphql-sign-up) or [**logging in**](https://www.back4app.com/docs/parse-graphql/graphql-login) this user) through the X-Parse-Session-Token header. This header can be sent in any operation and it will make this operation to be run in the behavior of the authenticated user.

The X-Parse-Session-Token can be easily set in the Parse Dashboard GraphQL Playground through the HTTP HEADERS option in the bottom left side of this tool.



![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/zJ-w--S3pZaInDW9En-qZ_image.png)

