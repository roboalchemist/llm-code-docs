# Source: https://docs-containers.back4app.com/docs/parse-graphql/graphql-sign-up.md

---
title: Signing up
slug: docs/parse-graphql/graphql-sign-up
description: This is a recipe for signing up a user in Parse Server backend through the GraphQL API.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-02-26T19:07:29.126Z
updatedAt: 2025-01-27T20:05:05.089Z
---

# Signing up a user through the Parse GraphQL API

## Problem

You want to sign up a new user in your backend through the Parse GraphQL API.

## Solution

Using the Parse GraphQL API, you can sign up a new user just by sending the user’s data through the signUp mutation. The username and password fields are mandatory. The mutation will return back not only the objectId and createdAt fields (that are returned by default when [**creating an object**](https://www.back4app.com/docs/parse-graphql/graphql-mutation-create-object)), but also the sessionToken.

After signing up a new user, you can use the [**authenticating a user**](https://www.back4app.com/docs/parse-graphql/graphql-user-authentication) recipe to send the sessionToken in the following operations so they will be executed in the behavior of this user. You can also use the [**logging in**](https://www.back4app.com/docs/parse-graphql/graphql-login) recipe to log in the user by using the defined credentials and the [**logging out**](https://www.back4app.com/docs/parse-graphql/graphql-logout-mutation) recipe to destroy the sessionToken.

## Version Information

Depending on the version of Parse you choose to run, the GraphQL queries, mutations and results will be slightly different.

Please choose the correct example along with the Parse version you are running.

## &#x20;**Parse Server 4.2.0 and later**

:::CodeblockTabs
Request

```graphql
1   mutation SignUp{
2     signUp(input: {
3       fields: {
4         username: "somefolk"
5         password: "somepassword"
6       }
7     }){
8       viewer{
9         user{
10          id
11          createdAt
12        }
13        sessionToken
14      }
15    }
16  }
```

Response

```graphql
1   {
2     "data": {
3       "signUp": {
4         "viewer": {
5           "user": {
6             "id": "X1VzZXI6ckZWbDR3YlJucA==",
7             "createdAt": "2020-02-06T13:38:04.517Z"
8           },
9           "sessionToken": "r:3233bc3b6801a15bcda39ff250416143"
10        }
11      }
12    }
13  }
```
:::

## Older Parse Server Versions

::::ExpandableHeading
**Parse Server 3.10.0 and later**

:::CodeblockTabs
Request

```graphql
1   mutation SignUp{
2     signUp(input: {
3       userFields: {
4         username: "somefolk"
5         password: "somepassword"
6       }
7     }){
8       viewer{
9         user{
10          id
11          createdAt
12        }
13        sessionToken
14      }
15    }
16  }
```

Response

```graphql
1   {
2     "data": {
3       "signUp": {
4         "viewer": {
5           "user": {
6             "id": "X1VzZXI6UHNOUkJ3Y1YyRQ==",
7             "createdAt": "2020-02-06T13:38:04.517Z"
8           },
9           "sessionToken": "r:c7abf06d951e8087c00fa66d546d1fea"
10        }
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
1   mutation SignUp{
2     signUp(fields:{
3       username: "somefolk"
4       password: "somepassword"
5     }){
6       id
7       createdAt
8       sessionToken
9     }
10  }
```

Response

```graphql
1   {
2     "data": {
3       "signUp": {
4         "id": "Gx2zW7yEnY",
5         "createdAt": "2019-11-04T14:24:21.333Z",
6         "sessionToken": "r:6d5f75f0f2d9ee16077b0a0ff1e20eb2"
7       }
8     }
9   }
```
:::
::::

::::ExpandableHeading
**Parse Server 3.8.0**

:::CodeblockTabs
Request

```graphql
1   mutation SignUp{
2     signUp(fields:{
3       username: "somefolk"
4       password: "somepassword"
5     }){
6       objectId
7       createdAt
8     }
9   }
```

Response

```graphql
1   {
2     "data": {
3       "signUp": {
4         "objectId": "KTznKVzto2",
5         "createdAt": "2019-11-04T14:23:46.014Z",
6         "sessionToken": "r:2ca6914312ed16803cf3769a25934cdc"
7       }
8     }
9   }
```
:::


::::

::::ExpandableHeading
**Parse Server 3.7.2**

:::CodeblockTabs
Request

```graphql
1   mutation SignUp {
2     users {
3       signUp(fields: { username: "somefolk", password: "somepassword" }) {
4         objectId,
5         createdAt,
6         sessionToken
7       }
8     }
9   }
```

Response

```graphql
1   {
2     "data": {
3       "users": {
4         "signUp": {
5           "objectId": "NyU1lNlhPd",
6           "createdAt": "2019-07-29T09:09:58.222Z",
7           "sessionToken": "r:a86665f0b63d9d8f945e4b0f302a1655"
8         }
9       }
10    }
11  }
```
:::
::::



