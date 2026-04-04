# Source: https://docs-containers.back4app.com/docs/parse-graphql/graphql-get-current-user.md

---
title: Getting a logged user
slug: docs/parse-graphql/graphql-get-current-user
description: This is a recipe for getting a logged user's data in Parse Server backend through the GraphQL API.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-02-27T13:09:10.249Z
updatedAt: 2025-01-27T20:05:13.917Z
---

# Getting a logged user through the Parse GraphQL API

## Problem

You want to get a logged user’s data from your backend through the Parse GraphQL API.

## Solution

Using the Parse GraphQL API, you can get a logged user’s data just by sending the user’s sessionToken through the X-Parse-Session-Token header (as described in the [**authenticating a user**](https://www.back4app.com/docs/parse-graphql/graphql-user-authentication) recipe) and calling the me query.

## Version Information

Depending on the version of Parse you choose to run, the GraphQL queries, mutations and results will be slightly different.
Please choose the correct example along with the Parse version you are running.

## **Parse Server 4.4.0 and later**

:::CodeblockTabs
Request

```graphql
//The headers for this query are X-Parse-Application-Id, X-Parse-Client-Key and X-Parse-Session-Token
1   query GetCurrentUser {
2     viewer {
3       sessionToken
4       user {
5         id
6         objectId
7       }
8     }
9   }
```

Response

```graphql
1   {
2     "data": {
3       "viewer": {
4         "sessionToken": "r:07dbfe8425d47d57c973bddce0df2ec9",
5         "user": {
6           "id": "X1VzZXI6OXZjM05sallIUA==",
7           "objectId": "9vc3NljYHP"
8         }
9       }
10    }
11  }
```
:::

::::ExpandableHeading
**Parse Server 3.10.0 and 4.2.0**

:::CodeblockTabs
Request

```graphql
1   query Me {
2     viewer {
3       user{
4         id
5         createdAt
6         updatedAt
7         username
8       }
9       sessionToken
10    }
11  }
```

Response

```graphql
1   {
2     "data": {
3       "viewer": {
4         "user": {
5           "id": "X1VzZXI6UHNOUkJ3Y1YyRQ==",
6           "createdAt": "2020-02-06T13:38:04.517Z",
7           "updatedAt": "2020-02-06T13:38:04.517Z",
8           "username": "somefolk"
9         },
10        "sessionToken": "r:00afa413b9cadd1007ad9ccd3c00f1c9"
11      }
12    }
13  }
```
:::
::::

::::ExpandableHeading
**Parse Server 3.9.0**

:::CodeblockTabs
Request

```graphql
1   query Me {
2     users {
3       results{
4         id,
5         createdAt,
6         updatedAt,
7         username
8       }
9     }
10  }
```

Response

```graphql
1   {
2     "data": {
3       "users": {
4         "me": {
5           "objectId": "NyU1lNlhPd",
6           "createdAt": "2019-07-29T09:09:58.222Z",
7           "updatedAt": "2019-07-29T09:09:58.222Z",
8           "username": "somefolk"
9         }
10      }
11    }
12  }
```
:::


::::

::::ExpandableHeading
**Parse Server 3.8.0**

:::CodeblockTabs
Request

```graphql
1   query Me{
2     viewer {
3       sessionToken
4       username
5     }
6   }
```

Response

```graphql
1   {
2     "data": {
3       "viewer": {
4         "sessionToken": "r:5c5024921339edf773b5b3e867d708be",
5         "username": "somefolk"
6       }
7     }
8   }
```
:::


::::

::::ExpandableHeading
**Parse Server 3.7.2**

:::CodeblockTabs
Request

```graphql
1   query Me {
2     users {
3       me {
4         objectId,
5         createdAt,
6         updatedAt,
7         username,
8         sessionToken
9       }
10    }
11  }
```

Response

```graphql
1   {
2     "data": {
3       "users": {
4         "me": {
5           "objectId": "NyU1lNlhPd",
6           "createdAt": "2019-07-29T09:09:58.222Z",
7           "updatedAt": "2019-07-29T09:09:58.222Z",
8           "username": "somefolk",
9           "sessionToken": "r:cbca71d29d7601761b48ed01bbe9638d"
10        }
11      }
12    }
13  }
```
:::


::::

