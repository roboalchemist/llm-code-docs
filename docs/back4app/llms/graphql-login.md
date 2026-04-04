# Source: https://docs-containers.back4app.com/docs/parse-graphql/graphql-login.md

---
title: Logging in
slug: docs/parse-graphql/graphql-login
description: This is a recipe for logging in an existing user in Parse Server backend through the GraphQL API.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-02-26T19:18:47.038Z
updatedAt: 2025-01-27T20:05:08.222Z
---

# Logging in an existing user through the Parse GraphQL API

# Problem

You want to log in an existing user in your backend through the Parse GraphQL API.

## Solution

Using the Parse GraphQL API, you can log in an existing user just by sending the user’s credentials through the logIn mutation. The username and password arguments are mandatory. The mutation will return back all users’ fields, including the sessionToken.

After logging in an existing user, you can use the [**authenticating an user**](https://www.back4app.com/docs/parse-graphql/graphql-user-authentication) recipe to send the sessionToken in the following operations so they will be executed in the behavior of this user. You can also use the [**logging out**](https://www.back4app.com/docs/parse-graphql/graphql-logout-mutation) recipe to destroy the sessionToken.

## Version Information

Depending on the version of Parse you choose to run, the GraphQL queries, mutations and results will be slightly different.
Please choose the correct example along with the Parse version you are running.

## **Parse Server 3.10.0 and later**

:::CodeblockTabs
Request

```graphql
1   mutation LogIn{
2     logIn(input: {
3       username: "somefolk"
4       password: "somepassword"
5     }){
6       viewer{
7         user{
8           id
9           createdAt
10          updatedAt
11          username
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
3       "logIn": {
4         "viewer": {
5           "user": {
6             "id": "X1VzZXI6UHNOUkJ3Y1YyRQ==",
7             "createdAt": "2020-02-06T13:38:04.517Z",
8             "updatedAt": "2020-02-06T13:38:04.517Z",
9             "username": "somefolk"
10          },
11          "sessionToken": "r:a5318d28821a78069f5b618de35b57bb"
12        }
13      }
14    }
15  }
```
:::

::::ExpandableHeading
**Parse Server 3.9.0**

:::CodeblockTabs
Request

```graphql
1   mutation LogIn{
2     logIn(fields:{
3       username: "somefolk"
4       password: "somepassword"
5     }){
6       id,
7       createdAt,
8       updatedAt,
9       username,
10      sessionToken
11    }
12  }
```

Response

```graphql
1   {
2     "data": {
3       "viewer": {
4         "sessionToken": "r:1450d329038f876835fb7aac16742380",
5         "username": "somefolk"
6       }
7     }
8   }
```
:::
::::

::::ExpandableHeading
**Parse Server 3.8.0**

:::CodeblockTabs
Request

```graphql
1   mutation LogIn{
2     logIn(fields:{
3       username: "somefolk"
4       password: "somepassword"
5     }){
6       objectId,
7       createdAt,
8       updatedAt,
9       username,
10      sessionToken
11    }
12  }
```

Response

```graphql
1   {
2     "data": {
3       "logIn": {
4         "objectId": "KTznKVzto2",
5         "createdAt": "2019-11-04T14:23:46.014Z",
6         "updatedAt": "2019-11-04T14:23:46.014Z",
7         "username": "somefolk",
8         "sessionToken": "r:fe39d9de406d53d13e9af1efbbe967a8"
9       }
10    }
11  }
```
:::
::::

::::ExpandableHeading
**Parse Server 3.7.2**

:::CodeblockTabs
Request

```graphql
1   mutation LogIn {
2     users {
3       logIn(username: "somefolk", password: "somepassword") {
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
4         "logIn": {
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

