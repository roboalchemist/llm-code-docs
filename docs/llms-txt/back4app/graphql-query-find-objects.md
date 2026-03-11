# Source: https://docs-containers.back4app.com/docs/parse-graphql/graphql-query-find-objects.md

---
title: Finding objects
slug: docs/parse-graphql/graphql-query-find-objects
description: This is a recipe for finding objects in Parse Server backend through the GraphQL API.
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-02-26T17:45:17.083Z
updatedAt: 2025-01-27T20:04:55.856Z
---

# Finding objects through the Parse GraphQL API

## Problem

You want to find objects from your database through the Parse GraphQL API.

## Solution

Using the parse GraphQL, there are two different ways to find objects from your database:

- [**Using generic query&#x20;**](https://www.back4app.com/docs/parse-graphql/graphql-query-find-objects#query-generic)-  this is the query that you can use to find objects of any class.
- [**Using class query&#x20;**](https://www.back4app.com/docs/parse-graphql/graphql-query-find-objects#query-class)- this is the recommended query that you should use to find objects of a specific class.

## Version Information

Depending on the version of Parse you choose to run, the GraphQL queries, mutations and results will be slightly different.
Please choose the correct example along with the Parse version you are running.

### **Using generic query**

When you use the find generic query, Parse Server behaves like a schemaless database. It means that you do not need to specify which object’s fields you want to retrieve. You just need to send the object’s className, and Parse Server will return all fields of the found objects.

Therefore, the objects’ find generic query is the query that you can use for finding objects of any class. If you want to find objects of a specific class, we recommend using the [**class query**](https://www.back4app.com/docs/parse-graphql/graphql-query-find-objects#query-class).

:::hint{type="info"}
This example will only work if you use a className with existing object. You can create an object using the [**creating an object**](https://www.back4app.com/docs/parse-graphql/graphql-mutation-create-object) recipe.
:::

## **Parse Server 3.8.0**

:::CodeblockTabs
Request

```graphql
1   query FindObject {
2     find(className: "Hero") {
3     count,
4     results      
5     }
6   }
```

Response

```graphql
1   {
2     "data": {
3       "find": {
4         "count": 2,
5         "results": [
6           {
7             "objectId": "rR8jmFRnkS",
8             "name": "Luke Skywalker",
9             "createdAt": "2019-11-04T12:42:40.723Z",
10            "updatedAt": "2019-11-04T12:42:40.723Z"
11          },
12          {
13            "objectId": "tUEcddcgno",
14            "name": "R2-D2",
15            "createdAt": "2019-11-04T12:44:10.951Z",
16            "updatedAt": "2019-11-04T12:44:10.951Z"
17          }
18        ]
19      }
20    }
21  }
```
:::

### **Example 3.9.0 and later:**

Parse 3.9.0 and later does not have the generic methods GET and FIND. You must use the specific methods below to retrieve objects.

### **Using class query**

Once you have already created your object’s class in your application’s schema (for instance, using the [**creating an object**](https://www.back4app.com/docs/parse-graphql/graphql-mutation-create-object#mutation-generic) recipe), Parse Server instantly adds to your GraphQL API a new find\<ClassName> query to find objects of this class.

Therefore, the object’s class query is the recommended method for finding objects of a specific class. Since this query knows your class’ data, it will automatically make available for you additional features like code auto-complete and validation.

:::hint{type="info"}
This example will only work if you use a class' query of existing object. You can create an object using the [**creating an object**](https://www.back4app.com/docs/parse-graphql/graphql-mutation-create-object) recipe.
:::

## **Parse Server 3.10.0 and later**

:::CodeblockTabs
Request

```graphql
1   query FindHero {
2     heroes{
3       count,
4       edges{
5         node{
6           name
7           createdAt
8           updatedAt
9         }
10      }
11    }
12  }
```

Response

```graphql
1   {
2     "data": {
3       "heroes": {
4         "count": 3,
5         "edges": [
6           {
7             "node": {
8               "name": "Luke Skywalker",
9               "createdAt": "2020-02-06T13:02:33.652Z",
10              "updatedAt": "2020-02-06T13:02:33.652Z"
11            }
12          },
13          {
14            "node": {
15              "name": "R2-D2",
16              "createdAt": "2020-02-06T13:13:26.678Z",
17              "updatedAt": "2020-02-06T13:13:26.678Z"
18            }
19          }
20        ]
21      }
22    }
23  }
```
:::

## Older Parse Server Versions

::::ExpandableHeading
**Parse 3.9.0**

**Class query:**

:::CodeblockTabs
Request

```graphql
1   query FindHero {
2     heroes{
3       count,
4       results {
5         id,
6         name,
7         createdAt,
8         updatedAt
9       }
10    }
11  }
```

Response

```graphql
1   {
2     "data": {
3       "heroes": {
4         "count": 2,
5         "results": [
6           {
7             "id": "CkhurmMjZW",
8             "name": "Luke Skywalker",
9             "createdAt": "2019-11-04T12:37:22.462Z",
10            "updatedAt": "2019-11-04T12:37:22.462Z"
11          },
12          {
13            "id": "n5GrpEi0iL",
14            "name": "R2-D2",
15            "createdAt": "2019-11-04T12:45:00.882Z",
16            "updatedAt": "2019-11-04T12:45:00.882Z"
17          }
18        ]
19      }
20    }
21  }
```
:::
::::

::::ExpandableHeading
**Parse Server 3.8.0**

**Class query:**

:::CodeblockTabs
Request

```graphql
1   query FindHero {
2     heroes{
3       count,
4       results {
5         objectId,
6         name,
7         createdAt,
8         updatedAt
9       }
10    }
11  }
```

Response

```graphql
1   "data": {
2       "objects": {
3         "findHero": {
4           "count": 2,
5           "results": [
6             {
7               "objectId": "ffyOBOTk85",
8               "name": "Luke Skywalker",
9               "createdAt": "2019-07-15T01:25:20.875Z",
10              "updatedAt": "2019-07-15T01:25:20.875Z"
11            },
12            {
13              "objectId": "jJH0aQQjfs",
14              "name": "R2-D2",
15              "createdAt": "2019-07-15T02:22:04.982Z",
16              "updatedAt": "2019-07-15T02:22:04.982Z"
17            }
18          ]
19        }
20      }
21    }
22  }
```
:::
::::

::::ExpandableHeading
**Parse Server 3.7.2**

**Generic query:**

:::CodeblockTabs
Request

```graphql
1   query FindObject {
2     objects {
3       find(className: "Hero") {
4         count,
5         results      
6       }
7     }
8   }
```

Response

```graphql
1   {
2     "data": {
3       "objects": {
4         "find": {
5           "count": 2,
6           "results": [
7             {
8               "objectId": "ffyOBOTk85",
9               "name": "Luke Skywalker",
10              "createdAt": "2019-07-15T01:25:20.875Z",
11             "updatedAt": "2019-07-15T01:25:20.875Z"
12            },
13            {
14              "objectId": "jJH0aQQjfs",
15              "name": "R2-D2",
16              "createdAt": "2019-07-15T02:22:04.982Z",
17              "updatedAt": "2019-07-15T02:22:04.982Z"
18            }
19          ]
20        }
21      }
22    }
23  }
```
:::

**Class query:**

:::CodeblockTabs
Request

```graphql
1   query FindHero {
2     objects {
3       findHero {
4         count,
5         results {
6           objectId,
7           name,
8           createdAt,
9           updatedAt
10        }
11      }
12    }
13  }
```

Response

```graphql
1   "data": {
2       "objects": {
3         "findHero": {
4           "count": 2,
5           "results": [
6             {
7               "objectId": "ffyOBOTk85",
8               "name": "Luke Skywalker",
9               "createdAt": "2019-07-15T01:25:20.875Z",
10              "updatedAt": "2019-07-15T01:25:20.875Z"
11            },
12            {
13              "objectId": "jJH0aQQjfs",
14              "name": "R2-D2",
15              "createdAt": "2019-07-15T02:22:04.982Z",
16              "updatedAt": "2019-07-15T02:22:04.982Z"
17            }
18          ]
19        }
20      }
21    }
22  }
```
:::
::::

