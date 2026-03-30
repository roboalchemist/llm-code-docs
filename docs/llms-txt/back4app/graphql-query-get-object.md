# Source: https://docs-containers.back4app.com/docs/parse-graphql/graphql-query-get-object.md

---
title: Getting an object
slug: docs/parse-graphql/graphql-query-get-object
description: This is a recipe for getting an object in Parse Server backend through the GraphQL API.
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-02-23T14:44:29.040Z
updatedAt: 2025-01-27T20:04:51.576Z
---

# Getting an object through the Parse GraphQL API

## Problem

You want to get an existing object from your database through the Parse GraphQL API.

## Solution

Using the parse GraphQL, there are two different ways to get an existing object from your database:

- [**Using generic query&#x20;**](https://www.back4app.com/docs/parse-graphql/graphql-query-get-object#query-generic)- this is the query that you can use to get an object of any class.
- [**Using class query&#x20;**](https://www.back4app.com/docs/parse-graphql/graphql-query-get-object#query-class)- this is the recommended query that you should use to get an object of a specific class.

## Version Information

Depending on the version of Parse you choose to run, the GraphQL queries, mutations and results will be slightly different.
Please choose the correct example along with the Parse version you are running.

### **Using generic query**

When you use the get generic query, Parse Server behaves like a schemaless database. It means that you do not need to specify which object’s fields you want to get. You just need to send the object’s className and objectId, and Parse Server will return all fields of this object.

Therefore, the objects’ get generic query is the query that you can use for getting an existing object of any class. If you want to get an existing object of a specific class, we recommend using the [**class query**](https://www.back4app.com/docs/parse-graphql/graphql-query-get-object#query-class).

:::hint{type="info"}
This example will only work if you use a className with existing object. You can create an object using the [**creating an object**](https://www.back4app.com/docs/parse-graphql/graphql-mutation-create-object) recipe.
:::

## **Parse Server 3.8.0**

:::CodeblockTabs
Request

```graphql
1   query GetObject {
2     get(className: "Hero", objectId: "rR8jmFRnkS")
3   }
```

Response

```graphql
1   {
2     "data": {
3       "get": {
4         "objectId": "rR8jmFRnkS",
5         "name": "Luke Skywalker",
6         "createdAt": "2019-11-04T12:42:40.723Z",
7         "updatedAt": "2019-11-04T12:42:40.723Z"
8       }
9     }
10  }
```
:::

## **Example Parse 3.9.0 and later:**

Parse 3.9 and later do not have the generic methods GET and FIND. You must use the specific methods below to retrieve objects.

### **Using class query**

Once you have already created your object’s class in your application’s schema (for instance, using the [**creating an object**](https://www.back4app.com/docs/parse-graphql/graphql-mutation-create-object#mutation-generic) recipe), Parse Server instantly adds to your GraphQL API a new get\<ClassName> query to get an existing object of this class.

Therefore, the object’s class query is the recommended method for getting an existing object of a specific class. Since this query knows your class’ data, it will automatically make available for you additional features like code auto-complete and validation.

:::hint{type="info"}
This example will only work if you use a className and an objectId of an existing object. You can create an object using the [**creating an object**](https://www.back4app.com/docs/parse-graphql/graphql-mutation-create-object) recipe.
:::

## **Parse Server 3.10.0 and later**

:::CodeblockTabs
Request

```graphql
1   query GetHero {
2     hero(id: "SGVybzpVRm5TVDM1YnBp") {
3       id,
4       name,
5       createdAt,
6       updatedAt
7     }
8   }
```

Response

```graphql
1   {
2     "data": {
3       "hero": {
4         "id": "SGVybzpVRm5TVDM1YnBp",
5         "name": "R2-D2",
6         "createdAt": "2020-02-06T13:13:26.678Z",
7         "updatedAt": "2020-02-06T13:13:26.678Z"
8       }
9     }
10  }
```
:::

## Older Parse Server Versions

::::ExpandableHeading
**Parse 3.9.0**

**Class query**

:::CodeblockTabs
Request

```graphql
1   query GetHero {
2     hero(id: "CkhurmMjZW") {
3       id,
4       name,
5       createdAt,
6       updatedAt
7     }
8   }
```

Response

```graphql
1   {
2     "data": {
3       "hero": {
4         "id": "CkhurmMjZW",
5         "name": "Luke Skywalker",
6         "createdAt": "2019-11-04T12:37:22.462Z",
7         "updatedAt": "2019-11-04T12:37:22.462Z"
8       }
9     }
10  }
```
:::


::::

:::ExpandableHeading
**Parse Server 3.8.0**

**Class queryParse Server 3.7.2**
:::

::::ExpandableHeading
**Parse Server 3.7.2**

**Generic query**

:::CodeblockTabs
Request

```graphql
1   query GetObject {
2     objects {
3       get(className: "Hero", objectId: "ffyOBOTk85")
4     }
5   }
```

Response

```graphql
1   {
2     "data": {
3       "objects": {
4         "get": {
5           "objectId": "ffyOBOTk85",
6           "name": "Luke Skywalker",
7           "createdAt": "2019-07-15T01:25:20.875Z",
8           "updatedAt": "2019-07-15T01:25:20.875Z"
9         }
10      }
11    }
12  }
```
:::

**Class query**

:::CodeblockTabs
Parse Server 3.7.2

```graphql
1   query GetHero {
2     objects {
3       getHero(objectId: "ffyOBOTk85") {
4         objectId,
5         name,
6         createdAt,
7         updatedAt
8       }
9     }
10  }
```

Result Parse 3.7.2

```graphql
1   {
2     "data": {
3       "objects": {
4         "getHero": {
5           "objectId": "ffyOBOTk85",
6           "name": "Luke Skywalker",
7           "createdAt": "2019-07-15T01:25:20.875Z",
8           "updatedAt": "2019-07-15T01:25:20.875Z"
9         }
10      }
11    }
12  }
```
:::
::::



