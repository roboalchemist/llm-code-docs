# Source: https://docs-containers.back4app.com/docs/parse-graphql/graphql-mutation-create-object.md

---
title: Creating an object
slug: docs/parse-graphql/graphql-mutation-create-object
description: This is a recipe for creating an object in Parse Server backend through the GraphQL API.
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-02-16T13:10:31.766Z
updatedAt: 2025-01-27T20:04:47.423Z
---

# Creating an object through the Parse GraphQL API

## Problem

You want to create a new object in your database through the Parse GraphQL API.

## Solution

Using the parse GraphQL, there are two different ways to create a new object in your database:

- [**Using generic mutation&#x20;**](https://www.back4app.com/docs/parse-graphql/graphql-mutation-create-object#mutation-generic)- - this is the mutation that you must use if you do not have already created your object’s class.
- [**Using class mutation&#x20;**](https://www.back4app.com/docs/parse-graphql/graphql-mutation-create-object#mutation-class)- this is the recommended mutation if you have already created your object’s class.

## Version Information

Depending on the version of Parse you choose to run, the GraphQL queries, mutations and results will be slightly different.
Please choose the correct example along with the Parse version you are running.

### **Using generic mutation**

When you use the create generic mutation, Parse Server behaves like a schemaless database. It means that you do not need to define your object’s class in your application’s schema beforehand. You just need to send your object’s data, and Parse Server will not only store it, but also learn from it, and automatically create a new class in your application’s schema.

Therefore, the objects’ create generic mutation is the method that you must use for creating a new object if you do not have already created your object’s class. You can also use this mutation for creating an object of pre-existing classes, but, for these cases, we recommend using the [**class mutation**](https://www.back4app.com/docs/parse-graphql/graphql-mutation-create-object#mutation-class).

**Class:**

:::CodeblockTabs
Request

```graphql
     #In Parse 3.10.0 and later you must first create the Class itself:
1    mutation CreateClass {
2      createClass(input:{
3        name: "Hero"
4        schemaFields: {
5          addStrings: [{name: "name"}]
6          addNumbers: [{name: "height"}]
7        }
8      }){
9        class{
10         schemaFields{
11           name
12           __typename
13         }
14       }
15     }
16   }
```

Response

```graphql
1   {
2     "data": {
3       "createClass": {
4         "class": {
5           "schemaFields": [
6             {
7               "name": "objectId",
8               "__typename": "SchemaStringField"
9             },
10            {
11              "name": "updatedAt",
12              "__typename": "SchemaDateField"
13            },
14            {
15              "name": "createdAt",
16              "__typename": "SchemaDateField"
17            },
18            {
19              "name": "name",
20              "__typename": "SchemaStringField"
21            },
22            {
23              "name": "height",
24              "__typename": "SchemaNumberField"
25            },
26            {
27              "name": "ACL",
28              "__typename": "SchemaACLField"
29            }
30          ]
31        }
32      }
33    }
34  }
```
:::

**Object:**

:::CodeblockTabs
Request

```graphql
1   mutation CreateObject{
2     createHero(input: {fields: {name: "Luke Skywalker"}}){
3       hero{
4         id
5         name
6       }
7     }
8   }
```

Response

```graphql
1   {
2     "data": {
3       "createHero": {
4         "hero": {
5           "id": "SGVybzo5QjFPMUFxcXN1",
6           "name": "Luke Skywalker"
7         }
8       }
9     }
10  }
```
:::

### **Using class mutation**

Once you have already created your object’s class in your application’s schema (for instance, using the [**generic mutation**](https://www.back4app.com/docs/parse-graphql/graphql-mutation-create-object#mutation-generic)), Parse Server instantly adds to your GraphQL API a new create\<ClassName> mutation to create a new object of this class.

Therefore, the object’s class mutation is the recommended method for creating a new object if you have already created your object’s class. Since this mutation knows your class’ data, it will automatically make available for you additional features like code auto-complete and validation. You also don’t need to specify the data types when sending dates, pointers, relations, files, geo points, polygons, or bytes through the class create mutation.

:::hint{type="info"}
**This example will only work if you have already created your object’s class. You can create a class using the** [**generic mutation**](https://www.back4app.com/docs/parse-graphql/graphql-mutation-create-object#mutation-generic)**.**
:::

:::CodeblockTabs
Request

```graphql
1   mutation CreateObject{
2     createHero(input: {fields: {name: "R2-D2"}}){
3       hero{
4         id
5         createdAt
6       }
7     }
8   }
```

Response

```graphql
   #Notice the id property refers to the Global id in the Relay specification, not to confuse with the objectId from Parse.
1   {
2     "data": {
3       "createHero": {
4         "hero": {
5           "id": "SGVybzpVRm5TVDM1YnBp",
6           "createdAt": "2020-02-06T13:13:26.678Z"
7         }
8       }
9     }
10  }
```
:::

## Older Parse Server Versions

::::ExpandableHeading
**Parse Server 3.9.0**

**Generic mutation**

**Class:**

:::CodeblockTabs
Request

```graphql
     #In Parse 3.9.0 you also must first create the Class itself:
1   mutation CreateClass {
2     createClass(
3       name: "Hero"
4       schemaFields: {
5         addStrings: [{name: "name"}]
6         addNumbers: [{name: "height"}]
7       }){
8       schemaFields{
9         name
10        __typename
11      }
12    }
13  }
```

Response

```graphql

1   {
2     "data": {
3       "createClass": {
4         "schemaFields": [
5           {
6             "name": "objectId",
7             "__typename": "SchemaStringField"
8           },
9           {
10            "name": "updatedAt",
11            "__typename": "SchemaDateField"
12          },
13          {
14            "name": "createdAt",
15            "__typename": "SchemaDateField"
16          },
17          {
18            "name": "name",
19            "__typename": "SchemaStringField"
20          },
21          {
22            "name": "height",
23            "__typename": "SchemaNumberField"
24          },
25          {
26            "name": "ACL",
27            "__typename": "SchemaACLField"
28          }
29        ]
30      }
31    }
32  }
```
:::

**Object:**

:::CodeblockTabs
Request

```graphql
   #And then create the Object:
   #In Parse 3.9.0 you must first create the Class itself:
1   mutation CreateObject{
2     createHero(fields:{
3       name: "Luke Skywalker"
4     }){
5       id
6       createdAt
7     }
8   }
```

Response

```graphql
1   {
2     "data": {
3       "createHero": {
4         "id": "CkhurmMjZW",
5         "createdAt": "2019-11-04T12:37:22.462Z"
6       }
7     }
8   }
```
:::

**Class mutation**

:::CodeblockTabs
Parse Server 3.9.0

```graphql
1   mutation CreateObject{
2     createHero(fields:{
3       name: "R2-D2"
4     }){
5       id
6       createdAt
7     }
8   }
```

Result Parse 3.9.0

```graphql
1   {
2     "data": {
3       "createHero": {
4         "id": "n5GrpEi0iL",
5         "createdAt": "2019-11-04T12:45:00.882Z"
6       }
7     }
8   }
```
:::
::::

::::ExpandableHeading
**Parse Server 3.8.0**

**Generic mutation:**

:::CodeblockTabs
Parse Server 3.8.0

```graphql
1   mutation CreateObject {
2     create(className: "Hero" fields:{
3       name: "Luke Skywalker"
4     }){
5       objectId
6       createdAt
7     }
8   }
```

Result Parse 3.8.0

```graphql
1   {
2     "data": {
3       "objects": {
4         "create": {
5           "objectId": "ffyOBOTk85",
6           "createdAt": "2019-07-15T01:25:20.875Z"
7         }
8       }
9     }
10   }
```
:::

**Class mutation:**

:::CodeblockTabs
Parse Server 3.8.0

```graphql
1   mutation CreateHero {
2     createHero(fields: { name: "R2-D2" }) {
3       objectId,
4       createdAt
5     }
6   }
```

Result Parse 3.8.0

```graphql
1   {
2     "data": {
3       "createHero": {
4         "objectId": "tUEcddcgno",
5         "createdAt": "2019-11-04T12:44:10.951Z"
6       }
7     }
8   }
```
:::
::::

::::ExpandableHeading
**Parse Server 3.7.2**

**Generic mutation:**

:::CodeblockTabs
Parse Server 3.7.2

```graphql
1   mutation CreateObject {
2     objects {
3       create(className: "Hero", fields: { name: "Luke Skywalker" }) {
4         objectId,
5         createdAt
6       }
7     }
8   }
```

Result Parse 3.7.2

```graphql
1   {
2     "data": {
3       "objects": {
4         "create": {
5           "objectId": "Kr9aqnzfui",
6           "createdAt": "2019-07-15T01:25:20.875Z"
7         }
8       }
9     }
10  }
```
:::

**Class mutation:**

:::CodeblockTabs
Parse Server 3.7.2

```graphql
1   mutation CreateHero {
2     objects {
3       createHero(fields: { name: "R2-D2" }) {
4         objectId,
5         createdAt
6       }
7     }
8   }
```

Result Parse 3.7.2

```graphql
1   {
2     "data": {
3       "objects": {
4         "createHero": {
5           "objectId": "jJH0aQQjfs",
6           "createdAt": "2019-07-15T02:22:04.982Z"
7         }
8       }
9     }
10  }
```
:::
::::

