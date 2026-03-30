# Source: https://docs-containers.back4app.com/docs/parse-graphql/graphql-mutation-update-object.md

---
title: Updating an object
slug: docs/parse-graphql/graphql-mutation-update-object
description: This is a recipe for updating an object in Parse Server backend through the GraphQL API.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-02-26T18:36:28.483Z
updatedAt: 2025-01-27T20:04:58.523Z
---

# Updating an object through the Parse GraphQL API

## Problem

You want to update an existing object in your database through the Parse GraphQL API.

## Solution

Using the parse GraphQL, there are two different ways to update an existing object in your database:

- [**Using generic mutation&#x20;**](https://www.back4app.com/docs/parse-graphql/graphql-mutation-update-object#mutation-generic)- this is the mutation that you must use if you want to set fields that do not belong to your object’s class yet.
- [**Using class mutation&#x20;**](https://www.back4app.com/docs/parse-graphql/graphql-mutation-update-object#mutation-class)- this is the recommended mutation if your object’s class already has all fields that you want to update.

## Version Information

Depending on the version of Parse you choose to run, the GraphQL queries, mutations and results will be slightly different.
Please choose the correct example along with the Parse version you are running.

### **Using generic mutation**

When you use the update generic mutation, Parse Server behaves like a schemaless database. It means that you do not need to define all fields of your object beforehand. You just need to send the fields that you want to update, and Parse Server will not only store it, but also learn from it, and automatically create any new field in this object’s class.

Therefore, the objects’ update generic mutation is the method that you must use for updating an existing object if you want to set fields that do not belong to your object’s class yet. You can actually use this mutation for updating any existing object, but we recommend using the [**class mutation**](https://www.back4app.com/docs/parse-graphql/graphql-mutation-update-object#mutation-class) if your object’s class already has all fields that you want to update.

:::hint{type="info"}
This example will only work if you use a className and an objectId of an existing object. You can create an object using the [**creating an object**](https://www.back4app.com/docs/parse-graphql/graphql-mutation-create-object) recipe.
:::

## **Parse 3.8.0**

:::CodeblockTabs
Request

```graphql
1   mutation UpdateObject {
2     update(className: "Hero", objectId: "rR8jmFRnkS", fields: { height: 5.6 }) {
3       updatedAt
4     }
5   }
```

Response

```graphql
1   {
2     "data": {
3       "updateHero": {
4        "updatedAt": "2019-11-04T13:28:44.150Z"
5       }
6     }
7   }
```
:::

### **Example Parse 3.9.0 and later:**

Parse 3.9.0 and later does not have the generic method UPDATE. You must use the specific methods below to update objects.

### **Using class mutation**

Once you have already created your object’s class in your application’s schema (for instance, using the [**creating an object**](https://www.back4app.com/docs/parse-graphql/graphql-mutation-create-object#mutation-generic) recipe), Parse Server instantly adds to your GraphQL API a new update\<ClassName> mutation to update an existing object of this class.

Therefore, the object’s class mutation is the recommended method for updating an existing object if your object’s class already has all fields that you want to update. Since this mutation knows your class’ data, it will automatically make available for you additional features like code auto-complete and validation. You also don’t need to specify the data types when sending dates, pointers, relations, files, geo points, polygons, or bytes through the class update mutation.

:::hint{type="info"}
This example will only work if you use a class’ mutation and objectId or id of an existing object. You can create an object using the [**creating an object**](https://www.back4app.com/docs/parse-graphql/graphql-mutation-create-object) recipe. The object’s class must have all fields that you are trying to update. You can create new fields using the [**generic mutation**](https://www.back4app.com/docs/parse-graphql/graphql-mutation-update-object#mutation-generic).
:::

## **Parse 3.10.0 and later**

:::CodeblockTabs
Request

```graphql
1   mutation UpdateObject {
2     updateHero(input: {
3       id: "SGVybzpVRm5TVDM1YnBp"
4       fields: {
5         height: 5.6
6       }
7     }){
8       hero{
9         updatedAt
10      }
11    }
12  }
```

Response

```graphql
1   {
2     "data": {
3       "updateHero": {
4         "hero": {
5           "updatedAt": "2020-02-06T13:31:49.866Z"
6         }
7       }
8     }
9   }
```
:::

## Older Parse Server Versions

::::ExpandableHeading
**Parse 3.9.0**

**Class mutation:**

:::CodeblockTabs
Parse Server 3.9.0

```graphql
1   mutation UpdateObject {
2     updateHero(id: "CkhurmMjZW" fields:{
3       height: 5.6
4     }){
5       updatedAt
6     }
7   }
```

Result Parse 3.9.0

```graphql
1   {
2     "data": {
3       "updateHero": {
4         "updatedAt": "2019-11-04T13:30:20.457Z"
5       }
6     }
7   }
```
:::
::::

::::ExpandableHeading
**Parse 3.8.0**

**Class mutation:**

:::CodeblockTabs
Request

```graphql
1   mutation UpdateObject {
2     updateHero(objectId: "rR8jmFRnkS" fields:{
3       height: 5.6
4     }){
5       updatedAt
6     }
7   }
```

Response

```graphql
1   {
2     "data": {
3       "updateHero": {
4         "updatedAt": "2019-11-04T13:38:46.343Z"
5       }
6     }
7   }
```
:::


::::

::::ExpandableHeading
**Parse 3.7.2**

**Generic mutation:**

:::CodeblockTabs
Parse Server 3.7.2

```graphql
1   mutation UpdateObject {
2     objects {
3       update(className: "Hero", objectId: "ffyOBOTk85", fields: { height: 5.6 }) {
4         updatedAt
5       }
6     }
7   }
```

Result Parse 3.7.2

```graphql
1   {
2     "data": {
3       "objects": {
4         "update": {
5           "updatedAt": "2019-07-15T05:57:14.416Z"
6         }
7       }
8     }
9   }
```
:::

**Class mutation:**

:::CodeblockTabs
Parse Server 3.7.2

```graphql
1   mutation UpdateHero {
2     objects {
3       updateHero(objectId: "jJH0aQQjfs", fields: { height: 3.6 }) {
4         updatedAt
5       }
6     }
7   }
```

Result Parse 3.7.2

```graphql
1   {
2     "data": {
3       "objects": {
4         "updateHero": {
5           "updatedAt": "2019-07-15T05:51:25.572Z"
6         }
7       }
8     }
9   }
```
:::
::::

