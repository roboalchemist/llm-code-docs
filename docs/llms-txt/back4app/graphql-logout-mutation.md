# Source: https://docs-containers.back4app.com/docs/parse-graphql/graphql-logout-mutation.md

---
title: Logging out
slug: docs/parse-graphql/graphql-logout-mutation
description: This is a recipe for logging out a logged user in Parse Server backend through the GraphQL API.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-02-27T13:25:14.560Z
updatedAt: 2025-01-27T20:05:22.754Z
---

# Logging out a logged user through the Parse GraphQL API

## Problem

You want to log out a logged user in your backend through the Parse GraphQL API.

## Solution

Using the Parse GraphQL API, you can log out a logged user just by sending the user’s sessionToken through the X-Parse-Session-Token header (as described in the [**authenticating a user**](https://www.back4app.com/docs/parse-graphql/graphql-user-authentication) recipe) and calling the logOut mutation. Parse Server will destroy the sessionToken and it will not be accepted for any other future request.

## Version Information

Depending on the version of Parse you choose to run, the GraphQL queries, mutations and results will be slightly different.
Please choose the correct example along with the Parse version you are running.

## **Parse Server 4.4.0 and later**

:::CodeblockTabs
Request

```graphql
//The headers for this operation are X-Parse-Application-Id, X-Parse-Client-Key and X-Parse-Session-Token
1   mutation logOutButton {
2	   logOut(input: { clientMutationId: "9vc3NljYHP" }) {
3		   clientMutationId
4	   }
5   }
```

Response

```graphql
1   {
2     "data": {
3       "logOut": {
4         "clientMutationId": "9vc3NljYHP"
5       }
6     }
7   }
8
```
:::

## Older Parse Server Versions

::::ExpandableHeading
**Parse Server 3.10.0 and 4.2.0**

:::CodeblockTabs
Request

```graphql
//With Parse 3.10.0 and 4.2.0 you must set a header called X-Parse-Session-Token containing the Session Token for the authenticated user. Once it is set, you can call:
1   mutation{
2     logOut(input: { clientMutationId: "sampleId"}){
3       viewer{
4         user{
5           id
6         }
7       }
8     }
9   }
```

Response

```graphql
1   {
2     "data": {
3       "logOut": {
4         "viewer": {
5           "user": {
6             "id": "X1VzZXI6UHNOUkJ3Y1YyRQ=="
7           }
8         }
9       }
10    }
11  }
```
:::
::::

::::ExpandableHeading
**Parse Server 3.9.0**

:::CodeblockTabs
Request

```graphql
//With Parse 3.9.0 you must set a header called X-Parse-Session-Token containing the Session Token for the authenticated user. Once it is set, you can call:
1   mutation{
2     logOut{
3       id
4     }
5   }
```

Response

```graphql
1   {
2     "data": {
3       "logOut": {
4         "id": "Gx2zW7yEnY"
5       }
6     }
7   }
```
:::


::::

::::ExpandableHeading
**Parse Server 3.8.0**

:::CodeblockTabs
Request

```graphql
1   mutation{
2     logOut{
3       objectId
4     }
5   }
```

Response

```graphql
1   {
2     "data": {
3       "logOut": {
4         "objectId": "KTznKVzto2"
5       }
6     }
7   }
```
:::
::::

::::ExpandableHeading
**Parse Server 3.7.2**

:::CodeblockTabs
Request

```graphql
1   mutation LogOut {
2     users {
3       logOut
4     }
5   }
```

Response

```graphql
1   {
2     "data": {
3       "users": {
4         "logOut": true
5       }
6     }
7   }
```
:::


::::

