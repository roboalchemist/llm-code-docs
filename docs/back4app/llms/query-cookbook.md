# Source: https://docs-containers.back4app.com/docs/android/data-objects/query-cookbook.md

# Source: https://docs-containers.back4app.com/docs/ios/parse-swift-sdk/data-objects/query-cookbook.md

---
title: Query Cookbook
slug: docs/ios/parse-swift-sdk/data-objects/query-cookbook
description: In this guide, you'll learn how to use every query method in ParseSwift
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-11T13:37:31.100Z
updatedAt: 2025-01-16T20:59:11.242Z
---

# Query Cookbook for ParseSwift

## Introduction

In the [**basic queries**](https://www.back4app.com/docs/ios/parse-swift-sdk/data-objects/basic-queries) guide, we introduced some of the basic methods to construct queries and retrieve data from a **Back4App** Database.
The ParseSwift SDK offers practical ways to construct more complex queries for real-world applications.

In this guide, you will dive deep into the Query\<U> (generic) class and see all the methods you can use to build your queries. You will use a simple database class (named Profile) with some mocked data to perform queries using swift.

Before getting started, we should establish a couple of concepts about objects and data types. In this guide, we refer as objects to any data type (like structs) that can be stored in a database. In some situations, they are also referred as items or elements.
Properties are the members of a data type (mostly structs). However, in here, we usually call them fields. ParseSwift uses the term ‘key’, to indicate the properties’ name. Thus, any parameter labeled as ‘key’ in any method from the ParseSwift SDK indicates that its value has to match a field’s name.

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- An App [**created on Back4App**](https://www.back4app.com/docs/get-started/new-parse-app).
- A basic iOS App to test queries
:::

## Goal

To explore the different methods theQuery\<U> class provide to execute queries.

## The Query\<U> class

For this guide, we will query information about a person’s contact. These data is stored under the class Profile on the **Back4App** Database. In order to retrieve profiles via an iOS App, we need to create the Profile struct that will contain such information

```swift
1   import ParseSwift
2   ...
3
4   struct Profile: ParseObject {
5       ...
6    
7       // Custom properties to organize the person's information
8       var name: String?
9       var birthday: Date?
10      var numberOfFriends: Int?
11      var favoriteFoods: [String]?
12      var luckyNumbers: [Int]?
13      var lastLoginLocation: ParseGeoPoint? // A data type to store coordinates for geolocation
14      var isActive: Bool?
15      var membership: Pointer<Membership>? // More details about Membership below
16    
17      ...
18  }
```

Additionally, we use the object Membership to show how queries between Profile and Membership interact with each other. The Membership struct is implemented in the following way

```swift
1   import ParseSwift
2   ...
3
4   struct Membership: ParseObject {
5       ...
6    
7       // Custom properties to organize the membership's information
8       var typeDescription: String?
9       var expirationDate: Date?
10
11      ...
12  }
```

Any query operation on a Back4App Database is performed by the generic class Query\<Profile> where the generic type Profile (conforming to the ParseSwift protocol) is the object we are trying to retrieve. After instantiating a Query\<Profile> object, we must call one of its find(\_) methods (see the [**basic queries guide**](https://www.back4app.com/docs/ios/parse-swift-sdk/data-objects/basic-queries)) to handle the result returned from the query.

You can read more about the Query\<U> class [**here at the official documentation**](https://github.com/parse-community/Parse-Swift).

## Saving Data Objects

With the following snippet we create and save some data to test miscellaneous queries

```swift
1   let adamSandler = Profile(
2     name: "Adam Sandler",
3     birthday: Date(string: "09/09/1996"),
4     numberOfFriends: 2,
5     favoriteFoods: ["Lobster", "Bread"],
6     luckyNumbers: [2, 7],
7     lastLoginLocation: try? ParseGeoPoint(latitude: 37.38412167489413, longitude: -122.01268034622319),
8     isActive: false,
9     membership: nil
10  )
11
12  let britneySpears = Profile(
13    name: "Britney Spears",
14    birthday: Date(string: "12/02/1981"),
15    numberOfFriends: 52,
16    favoriteFoods: ["Cake", "Bread"],
17    luckyNumbers: [22, 7],
18    lastLoginLocation: try? ParseGeoPoint(latitude: 37.38412167489413, longitude: -122.01268034622319),
19    isActive: true,
20    membership: nil
21  )
22  
23  let carsonKressley = Profile(
24    name: "Carson Kressley",
25    birthday: Date(string: "03/27/1975"),
26    numberOfFriends: 12,
27    favoriteFoods: ["Fish", "Cookies"],
28    luckyNumbers: [8, 7],
29    lastLoginLocation: try? ParseGeoPoint(latitude: 37.38412167489413, longitude: -122.01268034622319),
30    isActive: true,
31    membership: nil
32  )
33
34  // We create and save a Membership object
35  let premiumMembership = Membership(typeDescription: "Premium", expirationDate: Date(string: "10/10/2030"))
36  let savedPremiumMembership = try! premiumMembership.save() // Careful with the forced unwrap
37 
38  let danAykroyd = Profile(
39    name: "Dan Aykroyd",
40    birthday: Date(string: "07/01/1952"),
41    numberOfFriends: 66,
42    favoriteFoods: ["Jam", "Peanut Butter"],
43    luckyNumbers: [22, 77],
44    lastLoginLocation: try? ParseGeoPoint(latitude: 37.38412167489413, longitude: -122.01268034622319),
45    isActive: true,
46    membership: try? .init(savedPremiumMembership)
47  )
48
49  let eddyMurphy = Profile(
50    name: "Eddie Murphy",
51    birthday: Date(string: "04/03/1961"),
52    numberOfFriends: 49,
53    favoriteFoods: ["Lettuce", "Pepper"],
54    luckyNumbers: [6, 5],
55   lastLoginLocation: try? ParseGeoPoint(latitude: -27.104919974838154, longitude: -52.61428045237739),
56    isActive: false,
57    membership: nil
58  )
59
60  let fergie = Profile(
61    name: "Fergie",
62    birthday: Date(string: "03/27/1975"),
63    numberOfFriends: 55,
64    favoriteFoods: ["Lobster", "Shrimp"],
65    luckyNumbers: [12, 7],
66    lastLoginLocation: try? ParseGeoPoint(latitude: -27.104919974838154, longitude: -52.61428045237739),
67    isActive: false,
68    membership: nil
69  )
70 
71  do {
72    _ = try? adamSandler.save()
73    _ = try? britneySpears.save()        
74    _ = try? carsonKressley.save()
75    _ = try? danAykroyd.save()
76    _ = try? eddyMurphy.save()
77  } catch {
78    // Handle the errors here
79  }
```

Once the above code is executed, we should have a small database to work with.

:::hint{type="success"}
See more about how to save data with ParseSwift at [**iOS Data Objects**](https://www.back4app.com/docs/ios/parse-swift-sdk/data-objects/swift-crud-database-operations).
:::

## Query retrievers

These methods are responsible for running the query and retrieving its results, being always present in your query implementation.

:::CodeblockTabs
Find

```swift
//This is the basic method for retrieving your query results
1   let query = Profile.query() // Instantiate a Query<Profile> class with no additional constraints
2
3   let profiles = try? query.find() // Executes the query synchronously returns and array of Profiles. It throws an error if something happened
4
5   query.find { result in // Executes the query asynchronously
6     // Handle the result (of type Result<[Profile], ParseError>)
7   }
```

First

```swift
//Retrieves the first Profile instance that meets the query criteria.
1   let query = Profile.query()
2
3   let profile = try? query.first() // Executes the query synchronously
4
5   query.first { result in // Executes the query asynchronously
6     // Handle the result (of type Result<Profile, ParseError>)
7   }
```

Count

```swift
//Retrieves the number of elemets found by the query
1   let query = Profile.query() // Instantiate a Query<Profile> class with no additional constraints
2
3   let profiles = try? query.count() // Executes the query synchronously
4
5   query.count { result in // Executes the query asynchronously
6     // Handle the result (of type Result<Int, ParseError>)
7   }
```

Distinct

```swift
//Runs the query and returns a list of unique values from the results and the specified field, name in this case.
1   let query = Profile.query() // Instantiate a Query<Profile> class with no additional constraints
2
3   let profiles = try? query.distinct("name") // Executes the query synchronously
4
5   query.distinct("name") { result in // Executes the query asynchronously
6     // Handle the result (of type Result<[Profile], ParseError>)
7   }
```

Find all

```swift
//Retrieves a complete list of Profile’s that satisfy this query.
1   let query = Profile.query()
2
3   let profiles = try? query.findAll() // Executes the query synchronously
4        
5   query.findAll { result in // Executes the query asynchronously
6     // Handle the result (of type Result<[Profile], ParseError>)
7   }
```

Using the objectId

```swift
//When you need to retrieve an object with a specific objectId
1   let profile = try? Profile(objectId: "HuYfN4YXFD").fetch() // Retrieves synchronously the Profile with the given objectId. It throws an error if something happened
2
3   Profile(objectId: "HuYfN4YXFD").fetch { // Retrieves asynchronously the Profile with the given objectId
4     // Handle the result (of type Result<Profile, ParseError>)
5   }
```
:::

## Queries with constraints on string type fields

We now start applying specific constraints to queries. Firstly, we will impose constraints that select objects only when a String type field satisfies a given condition. This and any other type of constraint imposed on a Query\<Profile> object is done via the QueryConstraint object. Below and in the next sections we detail how to construct such constraints.

:::CodeblockTabs
Equal

```swift
//Used when we need to select all the objects which have a field equal to a given String. We use the == operator to construct the corresponding constraint. On the left-hand side goes the field’s name and on the right hand side goes the String to compare against
1   let constraint: QueryConstraint = "name" == "Fergie" // Selects all Profiles with name equals to Fergie
2   let query = Profile.query(constraint)
3
4   let profiles = try? query.find() // Executes the query synchronously
5
6   query.find { result in // Executes the query asynchronously
7     // Handle the result (of type Result<[Profile], ParseError>)
8   }
```

Regular expression

```swift
//Used when one of the fields contains a given String
1   let constraint: QueryConstraint = containsString(key: "name", substring: "ie")
2   // containsString(key:substring:) is a method provided by the ParseSwift SDK
3   let query = Profile.query(constraint)
4
5   let profiles = try? query.find() // Executes the query synchronously
6
7   query.find { result in // Executes the query asynchronously
8     // Handle the result (of type Result<[Profile], ParseError>)
9   }
```

Contains substring

```swift
//Retrieves the number of elemets found by the query
1   let query = Profile.query() // Instantiate a Query<Profile> class with no additional constraints
2
3   let profiles = try? query.count() // Executes the query synchronously
4
5   query.count { result in // Executes the query asynchronously
6     // Handle the result (of type Result<Int, ParseError>)
7   }
```

Matches text

```swift
//Similar to == but it has additional options like case sensite, language and diacritic sensitive
1   // Careful with the force unwrap!
2   let constraint: QueryConstraint = try! matchesText(key: "name", text: "fergie", options: [.caseSensitive: false]) 
3   // matchesText(key:text:,options:) is a method provided by the ParseSwift SDK
4
5   let query = Profile.query(constraint)
6
7   let profiles = try? query.find() // Executes the query synchronously
8
9   query.find { result in // Executes the query asynchronously
10    // Handle the result (of type Result<[Profile], ParseError>)
11  }
```
:::

## Queries with constraints on comparable-like fields

It is very common to try to select objects where a certain number type field has to be equal, distinct, larger or smaller than a given value. This is accomplished by using the following comparable operations

:::CodeblockTabs
Equal

```swift
//Use this constraint when you need to select objects where a certain number type field is equal to a given value.
1   let constraint: QueryConstraint = "numberOfFriends" == 2 // Selects all Profiles with number of friends = 2
2   let query = Profile.query(constraint)
3
4   let profiles = try? query.find() // Executes the query synchronously
5
6   query.find { result in // Executes the query asynchronously
7     // Handle the result (of type Result<[Profile], ParseError>)
8   }
```

Not equal

```swift
//The opposite constraint of equals to and it also works with Date type fields.
1   let constraint: QueryConstraint = "numberOfFriends" != 2 // Selects all Profiles where the number of friends is different from 2
2   let query = Profile.query(constraint)
3
4   let profiles = try? query.find() // Executes the query synchronously
5
6   query.find { result in // Executes the query asynchronously
7     // Handle the result (of type Result<[Profile], ParseError>)
8   }
```

Less than

```swift
//To construct this constraint we use the < operator. On the left-hand side goes the field’s name and on the right-hand side goes the value to compare against
1   let constraint: QueryConstraint = "numberOfFriends" < 49 // Selects all Profiles with a maximum of 48 friends
2   let query = Profile.query(constraint)
3
4   let profiles = try? query.find() // Executes the query synchronously
5
6   query.find { result in // Executes the query asynchronously
7     // Handle the result (of type Result<[Profile], ParseError>)
8   }
```

Less than or equal

```swift
//To construct this constraint we use the <= operator. On the left-hand side goes the field’s name (also referred as key) and on the right-hand side goes the value to compare against
1   let constraint: QueryConstraint = "numberOfFriends" <= 49 // Selects all Profiles with a maximum of 49 friends
2   let query = Profile.query(constraint)
3
4   let profiles = try? query.find() // Executes the query synchronously
5
6   query.find { result in // Executes the query asynchronously
7     // Handle the result (of type Result<[Profile], ParseError>)
8   }
```

Greater than

```swift
//Once again, for this constraint we use another operator to construct it, the > operator.
1   let constraint: QueryConstraint = "birthday" > Date(string: "08/19/1980") // Selects all Profiles who born after 08/19/1980
2   let query = Profile.query(constraint)
3
4   let profiles = try? query.find() // Executes the query synchronously
5
6   query.find { result in // Executes the query asynchronously
7     // Handle the result (of type Result<[Profile], ParseError>)
8   }
```

Greater than or equal

```swift
//Last but not least, the greater than or equal constraint are constructed using the >= operator.
1   let constraint: QueryConstraint = "numberOfFriends" >= 20 // Selects all Profiles with at least 20 number of friends
2   let query = Profile.query(constraint)
3
4   let profiles = try? query.find() // Executes the query synchronously
5
6   query.find { result in // Executes the query asynchronously
7     // Handle the result (of type Result<[Profile], ParseError>)
8   }
```
:::

These constraints also work on Date type fields. For instance, we can have

```swift
1   let constraint: QueryConstraint = "birthday" > Date(string: "08/19/1980") // Selects all Profiles who were born after 08/19/1980
2   let query = Profile.query(constraint)
3
4   let profiles = try? query.find() // Executes the query synchronously
5
6   query.find { result in // Executes the query asynchronously
7     // Handle the result (of type Result<[Profile], ParseError>)
8   }
```

For Bool type fields, we have the **Equal** and **Not equal** options. For instance

```swift
1   let constraint: QueryConstraint = "isActive" == true
2   let query = Profile.query(constraint) // Selects all active Profiles
3
4   let profiles = try? query.find() // Executes the query synchronously
5
6   query.find { result in // Executes the query asynchronously
7     // Handle the result (of type Result<[Profile], ParseError>)
8   }
```

## Queries with constraints involving geolocation

For fields containing location data (i.e., of type ParseGeoPoint) we have the following query options.

:::CodeblockTabs
Near

```swift
//In order to select objects where one of their ParseGeoPoint type fields is near to another given geopoint, we use
1   guard let geopoint = try? ParseGeoPoint(latitude: 37.38412167489413, longitude: -122.01268034622319) else {
2     return
3   }
4
5   let query = Profile.query(near(key: "lastLoginLocation", geoPoint: geopoint))
6   // near(key:geoPoint:) is a method provided by the ParseSwift SDK
7
8   let profiles = try? query.find() // Executes the query synchronously
9
10  query.find { result in // Executes the query asynchronously
11    // Handle the result (of type Result<[Profile], ParseError>)
12  }
```

Contains

```swift
//Given an object with a ParsePolygon type field, in order to select them in a query depending on what geopoints the field contains, we can use the following constraint
1   struct MyObject: ParseSwift {
2     ...
3  
4     var aPolygon: ParsePolygon?
5
6     ...
7   }
8
9   guard let geopoint = try? ParseGeoPoint(latitude: 37.38412167489413, longitude: -122.01268034622319) else {
10    return
11  }
12        
13  let query = MyObject.query(polygonContains(key: "aPolygon", point: geopoint))
14  // polygonContains(key:point:) is a method provided by the ParseSwift SDK
15
16  let myObjects = try? query.find() // Executes the query synchronously
17
18  query.find { result in // Executes the query asynchronously
19    // Handle the result (of type Result<[MyObject], ParseError>)
20  }
```

Within geo box

```swift
//Used to select objects where a ParseGeoPoint type field is inside of a given geopoint box. This box is described by its northeastPoint and southwestPoint geopoints.
1   guard let southwestPoint = try? ParseGeoPoint(latitude: 37.38412167489413, longitude: -122.01268034622319),
2         let northeastPoint = try? ParseGeoPoint(latitude: 37.28412167489413, longitude: -121.91268034622319) else {
3     return
4   }
5        
6   let query = Profile.query(withinGeoBox(key: "lastLoginLocation", fromSouthWest: southwestPoint, toNortheast: northeastPoint))
7   // withinGeoBox(key:fromSouthWest:toNortheast:) is a method provided by the ParseSwift SDK
8
9   let profiles = try? query.find() // Executes the query synchronously
10
11  query.find { result in // Executes the query asynchronously
12    // Handle the result (of type Result<[Profile], ParseError>)
13  }
```

Within km/mph

```swift
//Used to select objects according to whether or not a ParseGeoPoint type field value is near a given geopoint. Additionally, we should provide the maximum distance for how far the field value can be from the geopoint.
1   guard let geopoint = try? ParseGeoPoint(latitude: 37.38412167489413, longitude: -122.01268034622319) else {
2     return
3   }
4        
5   let query1 = Profile.query(withinKilometers(key: "lastLoginLocation", geoPoint: geopoint, distance: 100))
6   // withinKilometers(key:geoPoint:distance:) is a method provided by the ParseSwift SDK
7
8   let query2 = Profile.query(withinMiles(key: "lastLoginLocation", geoPoint: geopoint, distance: 100))
9   // withinMiles(key:geoPoint:distance:) is a method provided by the ParseSwift SDK
10
11  ... // Execute the corresponding query
```

Within Polygon

```swift
//Used to select objects with a ParseGeoPoint type field in a given polygon. The vertices of the polygon are represented by ParseGeoPoint objects.
1   // Create the vertices of the polygon (4 in this case)
2   guard let geopoint1 = try? ParseGeoPoint(latitude: 37.48412167489413, longitude: -122.11268034622319),
3         let geopoint2 = try? ParseGeoPoint(latitude: 37.48412167489413, longitude: -121.91268034622319),
4         let geopoint3 = try? ParseGeoPoint(latitude: 37.38412167489413, longitude: -121.91268034622319),
5         let geopoint4 = try? ParseGeoPoint(latitude: 37.38412167489413, longitude: -122.01268034622319) else {
6     return
7   }
8        
9   let constraint: QueryConstraint = withinPolygon(
10    key: "lastLoginLocation",
11    points: [geopoint1, geopoint2, geopoint3, geopoint4]
12  )
13  // withinPolygon(key:points:) is a method provided by the ParseSwift SDK
14        
15  let query = Profile.query(constraint)
16
17  let profiles = try? query.find() // Executes the query synchronously
18
19  query.find { result in // Executes the query asynchronously
20    // Handle the result (of type Result<[Profile], ParseError>)
21  }
```

Within radians

```swift
//Similar to ‘within kilometers’ or ‘within miles’ but the distance is expressed in radians.
1   guard let geopoint = try? ParseGeoPoint(latitude: 37.48412167489413, longitude: -122.11268034622319) else {
2     return
3   }
4
5   let query = Profile.query(withinRadians(key: "lastLoginLocation", geoPoint: geopoint, distance: 1.5))
6   // withinRadians(key:geoPoint:distance:) is a method provided by the ParseSwift SDK
7
8   let profiles = try? query.find() // Executes the query synchronously
9
10  query.find { result in // Executes the query asynchronously
11    // Handle the result (of type Result<[Profile], ParseError>)
12  }
```
:::

## Queries with constraints involving array type fields

When the objects we want to retrieve need to satisfy a given condition on any of their array type fields, ParseSwift SDK provides the following alternatives to accomplish that

:::CodeblockTabs
Contained in

```swift
//Add a constraint to the query that requires a particular field to be contained in the provided array.
1   let constraint: QueryConstraint = containedIn(key: "luckyNumbers", array: [2, 7])
2   // containedBy(key:array:) is a method provided by the ParseSwift SDK
3
4   let query = Profile.query(constraint)
5
6   let profiles = try? query.find() // Executes the query synchronously
7
8   query.find { result in // Executes the query asynchronously
9     // Handle the result (of type Result<[Profile], ParseError>)
10  }
```

Contained by

```swift
//Add a constraint to the query that requires a particular field to be contained by the provided array. It retrieves objects where all the elements of their array type field match.
1   let constraint: QueryConstraint = containedBy(key: "luckyNumbers", array: [2, 7])
2   // containedBy(key:array:) is a method provided by the ParseSwift SDK
3
4   let query = Profile.query(constraint)
5
6   let profiles = try? query.find() // Executes the query synchronously
7
8   query.find { result in // Executes the query asynchronously
9     // Handle the result (of type Result<[Profile], ParseError>)
10  }
```

Contains all

```swift
//Add a constraint to the query that requires a particular array type field to contain every element of the provided array.
1   let constraint: QueryConstraint = containsAll(key: "luckyNumbers", array: [2, 7])
2   // containsAll(key:array:) is a method provided by the ParseSwift SDK
3
4   let query = Profile.query(constraint)
5
6   let profiles = try? query.find() // Executes the query synchronously
7
8   query.find { result in // Executes the query asynchronously
9     // Handle the result (of type Result<[Profile], ParseError>)
10  }
```
:::

## Advanced queries

Until now we introduced the main conditions we can apply on a given field to select objects from a Back4App Database using ParseSwift SDK. In this section we continue with the composition of queries and advanced queries.

:::CodeblockTabs
Exists

```swift
//It is used to select objects depending on the value of a given field not being nil.
1   let constraint: QueryConstraint = exists(key: "membership")
2   // exists(key:) is a method provided by the ParseSwift SDK
3
4   let query = Profile.query(constraint) // Will retrieve all Profiles which have a membership
5
6   let profiles = try? query.find() // Executes the query synchronously
7
8   query.find { result in // Executes the query asynchronously
9     // Handle the result (of type Result<[Profile], ParseError>)
10  }
```

Does not exists

```swift
//It is used to select objects depending on the value of a given field being nil.
1   let constraint: QueryConstraint = doesNotExist(key: "membership")
2   // doesNotExist(key:) is a method provided by the ParseSwift SDK
3
4   let query = Profile.query(constraint) // Will retrieve all Profiles which do not have a membership
5
6   let profiles = try? query.find() // Executes the query synchronously
7
8   query.find { result in // Executes the query asynchronously
9     // Handle the result (of type Result<[Profile], ParseError>)
10  }
```

Matches key in query

```swift
//When we need to retrieve objects using the result from a different query as a condition, we make use of the method doesNotMatchKeyInQuery(key:queryKey:query:) to construct the corresponding condition. To illustrate this in more detail, we first introduce a new object Friend which has a property numberOfContacts of type Int
1   struct Friend: ParseSwift {
2     ...
3     var numberOfContacts: Int? 
4     ...
5   }
```

Does not match key in query

```swift
//This case is the opposite of Matches key in query. It is useful when we want to select all the Profile objects where their numberOfFriends field does not match with the numberOfContacts field in all Friend objects. The method we use to compose this query is doesNotMatchKeyInQuery(key:queryKey:query:)
1   let friendQuery = Friend.query() // Selects all Friends objects
2
3   let constraint: QueryConstraint = doesNotMatchKeyInQuery(
4     key: "numberOfFriends",
5     queryKey: "numberOfContacts",
6     query: friendQuery
7   )
8   // doesNotMatchKeyInQuery(key:queryKey:query:) is a method provided by the ParseSwift SDK
9
10  let query = Profile.query(constraint)
11
12  let profiles = try? query.find() // Executes the query synchronously
13
14  query.find { result in // Executes the query asynchronously
15    // Handle the result (of type Result<[Profile], ParseError>)
16  }
```
:::

## Query ordering

Sorting the results from a query is key before starting to display or manipulate those results. The ParseSwift SDK provides the following options to accomplish that.

:::CodeblockTabs
Ascending

```swift
//Sort the results in ascending order, overwrites previous orderings. Multiple fields can be used to solve ordering ties. By calling the order(_:) method on a Query<Profile> object, we obtain a new query which implements the given order option. The argument for the order(_:) method is an Array of Query<Profile>.Order items. These enumerations contain the name of the field to be used for the sort algorithm. For ascending order we use Query<Profile>.Order.ascending("nameOfTheField").
1   let query = Profile.query().order([.ascending("numberOfFriends")])
2
3   let profiles = try? query.find() // Executes the query synchronously
4
5   query.find { result in // Executes the query asynchronously
6     // Handle the result (of type Result<[Profile], ParseError>)
7   }
```

Descending

```swift
//Similar to the ascending order, the only diference is that instead of using Query<Profile>.Order.ascending("nameOfTheField") we should use Query<Profile>.Order.descending("nameOfTheField").
1   let query = Profile.query().order([.descending("numberOfFriends")])
2
3   let profiles = try? query.find() // Executes the query synchronously
4
5   query.find { result in // Executes the query asynchronously
6     // Handle the result (of type Result<[Profile], ParseError>)
7   }
```

Text Score

```swift
//This kind of sorting procedure relies on a score metric. In order to use this option, the Profile object must conform to the ParseQueryScorable protocol. Once the protocol is implemented, we call the sortByTextScore() method on the Query<Profile> object to obtain a new one that implements the required sorting method.
1   extension Profile: ParseQueryScorable {
2     var score: Double? {
3       // Add the corresponding implementation
4     }  
5   }
6
7   let query = Profile.query().sortByTextScore()
8 
9   let profiles = try? query.find() // Executes the query synchronously
10
11  query.find { result in // Executes the query asynchronously
12    // Handle the result (of type Result<[Profile], ParseError>)
13  }
```
:::

## Field selecting

Depending on what data is required during a query, this can take more or less time. In some scenarios it may be enough to retrieve certain fields from an object and ignore the unnecessary fields. Furthermore, by selecting only the fields we need from a query, we avoid over-fetching and improve performance on the fetching process.

:::CodeblockTabs
Exclude

```swift
//Calling the exclude(_:) method on a query returns a new query that will exclude the fields passed (in variadic format) as the argument.
1   let query = Profile.query().exclude("name", "numberOfFriends")
2
3   let profiles = try? query.find() // Executes the query synchronously
4
5   query.find { result in // Executes the query asynchronously
6     // Handle the result (of type Result<[Profile], ParseError>)
7   }
```

Include

```swift
//It is used to retrieve the fields whose data type conforms to the ParseObject protocol (i.e., objects stored in the same Database under its corresponding class name). Calling the include(_:) method on a query returns a new query that will include the fields passed (in variadic format) as the argument. For instance, the membership field in Profile will not be fetched unless we include it manually.
1   let query = Profile.query().include("membership")
2
3   let profiles = try? query.find() // Executes the query synchronously
4
5   query.find { result in // Executes the query asynchronously
6     // Handle the result (of type Result<[Profile], ParseError>)
7   }
```

Include all

```swift
//When we need to retrieve the fields that conforms to the ParseObject we call the includeAll() method on the query.
1   let query = Profile.query().includeAll()
2
3   let profiles = try? query.find() // Executes the query synchronously
4
5   query.find { result in // Executes the query asynchronously
6     // Handle the result (of type Result<[Profile], ParseError>)
7   }
```

Select

```swift
//It returns only the specified fields in the returned objects. Calling the select(_:) method on a query returns a new query which will select only the fields passed (in variadic format) as argument.
1   let query = Profile.query().select("name", "birthday")
2
3   let profiles = try? query.find() // Executes the query synchronously
4
5   query.find { result in // Executes the query asynchronously
6     // Handle the result (of type Result<[Profile], ParseError>)
7   }
```
:::

## Pagination

In large Databases pagination, is a fundamental feature for querying and handling a large amount of results. the ParseSwift SDK provides the following methods to manage those situations.

:::CodeblockTabs
Limit

```swift
//Determines the maximum number of results a query is able to return, the default value is 100. We call the limit(_:) method on the query in question to change this value.
1   let query = Profile.query().limit(2)
2
3   let profiles = try? query.find() // Executes the query synchronously
4
5   query.find { result in // Executes the query asynchronously
6     // Handle the result (of type Result<[Profile], ParseError>)
7   }
```

Skip

```swift
//Together with the previous option, the skip option allows us to paginate the results. We call the skip(_:) method on the query in question to change this value.
1   let query = Profile.query().skip(2)
2
3   let profiles = try? query.find() // Executes the query synchronously
4
5   query.find { result in // Executes the query asynchronously
6     // Handle the result (of type Result<[Profile], ParseError>)
7   }
```

With count

```swift
//When we need to know in advance the number of results retrieved from a query, we use the withCount(completion:) method instead of the usual find(...). In this way, the result is composed by the objects found together with an integer indicating the length of the array.
1   let query = Profile.query()
2
3   query.withCount { result in // Executes the query asynchronously
4     // Handle the result (of type Result<([Profile], Int), ParseError>)
5   }
```
:::

## Compound queries

These methods will create compound queries, which can combine more than one Query\<Profile> instance to achieve more complex results.

:::CodeblockTabs
And

```swift
//Compose a compound query that is the AND of the passed queries. This is accomplished by first instantiating the queries to be used for the AND operation. The and(queries:) method provided by the ParseSwift SDK allows us to perform the AND operation and embed the result in a QueryConstraint object. This constraint is then used to instantiate the final query to be used for retrieveing the results.
1   let query1 = Profile.query("numberOfFriends" > 10)
2   let query2 = Profile.query("numberOfFriends" < 50)
3
4   let query = Profile.query(and(queries: query1, query2))
5   // and(queries:) is a method provided by the ParseSwift SDK. It takes an array of queries and applies the AND op. on them.
6
7   let profiles = try? query.find() // Executes the query synchronously
8   
9   query.find { result in // Executes the query asynchronously
10    // Handle the result (of type Result<[Profile], ParseError>)
11  }
```

Nor

```swift
//In this case, we apply a NOR operation on a set of queries. We use the nor(queries:) method provided by the ParseSwift SDK to perform such operation. We handle the result in a similar way as the AND operation.
1   let query1 = Profile.query("numberOfFriends" > 10)
2   let query2 = Profile.query("numberOfFriends" < 50)
3        
4   let query = Profile.query(nor(queries: query1, query2))
5
6   let profiles = try? query.find() // Executes the query synchronously
7
8   query.find { result in // Executes the query asynchronously
9     // Handle the result (of type Result<[Profile], ParseError>)
10  }
```

Or

```swift
//Similar to previous cases, we apply an OR operation on a set of queries. We use the or(queries:) method provided by the ParseSwift SDK to perform such operation. We handle the result in a similar way as the AND (or NOR) operation.
1   let query1 = Profile.query("numberOfFriends" > 10)
2   let query2 = Profile.query("numberOfFriends" < 50)
3        
4   let query = Profile.query(or(queries: query1, query2))
5
6   let profiles = try? query.find() // Executes the query synchronously
7
8   query.find { result in // Executes the query asynchronously
9     // Handle the result (of type Result<[Profile], ParseError>)
10  }
```
:::

## Database related

These methods are related to the database preferences and operations.

:::CodeblockTabs
aggregate

```swift
//Executes an aggregate query, retrieving objects over a set of input values. To use this feature, instead of executing the query with find(...), we call the aggregate(_:completion:). The first argument of this function is a dictionary containing the information about the pipeline. For more details, refer to MongoDB documentation on aggregate.
1   let query = Profile.query()
2
3   query.aggregate([["pipeline": 5]]) { result in
4     // Handle the result (of type Result<[Profile], ParseError>)
5   }
```

explain

```swift
//Investigates the query execution plan, related to MongoDB explain operation. This option requires a new object (conforming to the Decodable protocol) to handle the results.
1   struct AnyCodable: Decodable {
2  // Implement the corresponding properties
3}
4
5let query = Profile.query()
6
7let results = try? query.findExplain() // Executes the option synchronously
8
9// Instantiate the completion block explicitely in order for the method findExplain(completion:) to infer the type of the returning results
10  let completion: (Result<[AnyCodable], ParseError>) -> Void = { result in
11    // Handle the result
12  }
13
14  // Executes the option asynchronously
15  query.findExplain(completion: completion)
```

readPreference

```swift
//When using a MongoDB replica set, use this method to choose from which replica the objects will be retrieved. The possible values are PRIMARY (default), PRIMARY_PREFERRED, SECONDARY, SECONDARY_PREFERRED, or NEAREST.
1   let query = Profile.query().readPreference("NEAREST")
2
3   let profiles = try? query.find() // Executes the query synchronously
4
5   query.find { result in // Executes the query asynchronously
6     // Handle the result (of type Result<[Profile], ParseError>)
7   }
```
:::

## Conclusion

Using the different methods, objects and operators provided by the ParseSwift SDK, we were able to understand how to construct and retrieve objects from a **Back4App** Database. With this cookbook you should be able to perform queries with very flexible constraints and manage the results according to your use case. For more details about any of the above topics, you can refer to the [**ParseSwift repository**](https://github.com/parse-community/Parse-Swift).
