# Source: https://docs-containers.back4app.com/docs/parse-graphql/graphql-mutation-delete-object.md

---
title: Deleting an object
slug: docs/parse-graphql/graphql-mutation-delete-object
description: This is a recipe for deleting an object in Parse Server backend through the GraphQL API.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-02-26T18:55:29.131Z
updatedAt: 2025-01-27T20:05:01.272Z
---

# Deleting an object through the Parse GraphQL API

## Problem

You want to delete an existing object in your database through the Parse GraphQL API.

## Solution

Using the parse GraphQL, there are two different ways to delete an existing object in your database:

- [**Using generic mutation&#x20;**](https://www.back4app.com/docs/parse-graphql/graphql-mutation-delete-object#mutation-generic)- this is the mutation that you can use to delete an object of any class.
- [**Using class mutation&#x20;**](https://www.back4app.com/docs/parse-graphql/graphql-mutation-delete-object#mutation-class)- this is the recommended mutation that you should use to delete an object of a specific class.

## Version Information

Depending on the version of Parse you choose to run, the GraphQL queries, mutations and results will be slightly different.
Please choose the correct example along with the Parse version you are running.

### **Using generic mutation**

When you use the delete generic mutation, you send the object’s className and objectId, and Parse Server will delete this object.

Therefore, the objects’ delete generic mutation is the one that you can use for deleting an existing object of any class. If you want to delete an existing object of a specific class, we recommend using the [**class mutation**](https://www.back4app.com/docs/parse-graphql/graphql-mutation-delete-object#mutation-class).

:::hint{type="info"}
This example will only work if you use a className and an objectId of an existing object. You can create an object using the [**creating an object**](https://www.back4app.com/docs/parse-graphql/graphql-mutation-create-object) recipe.
:::

## **Parse 3.8.0**

:::CodeblockTabs
Request

```graphql
1   mutation DeleteObject {
2     delete(className: "Hero", objectId: "rR8jmFRnkS")
3   }
```

Response

```graphql
1   {
2     "data": {
3       "delete": true
4     }
5   }
```
:::

### **Example Parse 3.9.0 and later:**

Parse 3.9.0 and later does not have the generic method DELETE. You must use the specific methods below to delete objects.

### **Using class mutation**

Once you have already created your object’s class in your application’s schema (for instance, using the [**creating an object**](https://www.back4app.com/docs/parse-graphql/graphql-mutation-create-object#mutation-generic) recipe), Parse Server instantly adds to your GraphQL API a new delete\<ClassName> mutation to delete an existing object of this class.

Therefore, the object’s class mutation is the recommended method for deleting an existing object of a specific class.

:::hint{type="info"}
This example will only work if you use a objectId or id of an existing object. You can create an object using the [**creating an object**](https://www.back4app.com/docs/parse-graphql/graphql-mutation-create-object) recipe.
:::

## **Parse 3.10.0 and later**

:::CodeblockTabs
Request

```graphql
1   mutation DeleteObject {
2     deleteHero(input:{
3       id: "SGVybzpVRm5TVDM1YnBp"
4     }){
5       hero{
6         id
7       }
8     }
9   }
```

Response

```graphql
1   {
2     "data": {
3       "deleteHero": {
4         "hero": {
5           "id": "SGVybzpVRm5TVDM1YnBp"
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
Request

```graphql
1   mutation DeleteObject {
2     deleteHero(id: "CkhurmMjZW"){
3       id
4     }
5   }
```

Response

```graphql
1   {
2     "data": {
3       "deleteHero": {
4         "id": "CkhurmMjZW"
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
1   mutation DeleteObject {
2     deleteHero(objectId: "rR8jmFRnkS"){
3       objectId
4     }
5   }
```

Response

```graphql
1   {
2     "data": {
3       "deleteHero": {
4         "objectId": "rR8jmFRnkS"
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
1   mutation DeleteObject {
2     objects {
3       delete(className: "Hero", objectId: "ffyOBOTk85")
4     }
5   }
```

Result Parse 3.7.2

```graphql
1   {
2     "data": {
3       "objects": {
4         "delete": true
5       }
6     }
7   }
```
:::

**Class mutation:**

:::CodeblockTabs
Parse Server 3.7.2

```graphql
1   mutation DeleteHero {
2     objects {
3       deleteHero(objectId: "jJH0aQQjfs")
4     }
5   }
```

Result Parse 3.7.2

```graphql
1   {
2     "data": {
3       "objects": {
4         "delete": true
5       }
6     }
7   }
```
:::
::::



