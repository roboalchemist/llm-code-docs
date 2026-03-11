# Source: https://docs-containers.back4app.com/docs/ios/parse-swift-sdk/data-objects/geoqueries.md

---
title: Geoqueries
slug: docs/ios/parse-swift-sdk/data-objects/geoqueries
description: In this guide, you'll learn how to perform queries involving constraints on ParseGeoPoint data types
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-11T15:25:39.095Z
updatedAt: 2025-01-17T14:22:45.613Z
---

# Geoqueries

## Introduction

We use the term **Geoqueries** to refer to the type of queries where their conditions involve ParseGeoPoint type fields. It is recommended to use the ParseGeoPoint struct to store geographic location data in a Back4App Database. The ParseSwift SDK provides a set of methods that allows us to query data according to conditions applied on ParseGeoPointdata type.

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- An App [**created on Back4App**](https://www.back4app.com/docs/get-started/new-parse-app).
- A basic iOS App to test queries
:::

## Goal

To understand how to query data using conditions on geographic location data.

## 1 - Quick review about the **Query\<U>** class

Any query performed on a Back4App Database is done via the generic class Query\<U>. The generic parameter U (conforming to the ParseObject protocol) is the data type of the objects we are trying to retrieve from the database.

Given a data type like MyObject, we retrieve these objects from a Back4App Database in the following way

```swift
1   import ParseSwift
2
3   struct MyObject: ParseObject {
4     ...
5   }
6
7   let query = MyObject.query()
8
9   // Executes the query asynchronously
10  query.find { result in
11    // Handle the result (of type Result<[MyObject], ParseError>)
12  }
```

You can read more about the Query\<U> class [**here at the official documentation**](https://github.com/parse-community/Parse-Swift).

## 2 - Save some data on Back4App

Before we begin to execute queries, we should store some sample data on a Back4App Database. By following the [**Quickstart**](https://www.back4app.com/docs/ios/parse-swift-sdk/install-sdk) guide, you can configure and link your sample iOS App to your Back4App database. For this guide, we will store information about cities. We use the following struct to organize a city’s information:

```swift
1   import ParseSwift
2
3   struct City: ParseObject {
4       ...
5    
6       var name: String? // City's name
7       var location: ParseGeoPoint? // It will store the city's coordinate on Earth
8   }
```

Now, we proceed to store the sample data. This step can be implemented using **Swift** or directly from your app’s [**console**](https://www.youtube.com/watch?v=nVWRYRZbCmA) on the Back4App platform.&#x20;

:::CodeblockTabs
```swift
//After setting up your XCode project, calling the following method should save some sample data on your Back4App Database
1   import ParseSwift
2
3   func setupSampleData() {
4     do {
5       // Montevideo - Uruguay
6       _ = try City(
7         name: "Montevideo",
8         location: ParseGeoPoint(coordinate: CLLocationCoordinate2D(latitude: -34.85553195363169, longitude: -56.207280375137955))
9       ).save()
10            
11      // Brasília - Brazil
12      _ = try City(
13        name: "Brasília",
14        location: ParseGeoPoint(coordinate: CLLocationCoordinate2D(latitude: -15.79485821477289, longitude: -47.88391074690196))
15      ).save()
16              
17      // Bogotá - Colombia
18      _ = try City(
19        name: "Bogotá",
20        location: ParseGeoPoint(coordinate: CLLocationCoordinate2D(latitude: 4.69139880891712, longitude: -74.06936691331047))
21      ).save()
22            
23      // Mexico City - Mexico
24      _ = try City(
25        name: "Mexico City",
26        location: ParseGeoPoint(coordinate: CLLocationCoordinate2D(latitude: 19.400977162618933, longitude: -99.13311378164776))
27      ).save()
28            
29      // Washington, D.C. - United States
30        _ = try City(
31          name: "Washington, D.C.",
32          location: ParseGeoPoint(coordinate: CLLocationCoordinate2D(latitude: 38.930727220189944, longitude: -77.04626261880388))
33        ).save()
34            
35      // Ottawa - Canada
36      _ = try City(
37        name: "Ottawa",
38        location: ParseGeoPoint(latitude: 45.41102167733425, longitude: -75.695414598736)
39      ).save()
40    } catch let error as ParseError {
41      print("[ParseSwift ERROR]", error.message)
42    } catch {
43      print("[ERROR]", error.localizedDescription)
44    }
45  }
```

Back4App's console

```swift
//A quick way to insert elements on your Back4App Database is via the console located in your App’s API section. Once you are there, you can start running Javascript code to save the sample data
1   // Add City objects and create table
2   // Note how GeoPoints are created, passing latitude and longitude as arguments
3   // Montevideo
4   City = new Parse.Object('City');
5   City.set('name', 'Montevideo - Uruguay');
6   City.set('location', new Parse.GeoPoint(-34.85553195363169, -56.207280375137955));
7   await City.save();
8
9   // Brasília
10  City = new Parse.Object('City');
11  City.set('name', 'Brasília - Brazil');
12  City.set('location', new Parse.GeoPoint(-15.79485821477289, -47.88391074690196));
13  await City.save();
14
15  // Bogotá
16  City = new Parse.Object('City');
17  City.set('name', 'Bogotá - Colombia');
18  City.set('location', new Parse.GeoPoint(4.69139880891712, -74.06936691331047));
19  await City.save();
20
21  // Mexico City
22  City = new Parse.Object('City');
23  City.set('name', 'Mexico City - Mexico');
24  City.set('location', new Parse.GeoPoint(19.400977162618933, -99.13311378164776));
25  await City.save();
26
27  // Washington, D.C.
28  City = new Parse.Object('City');
29  City.set('name', 'Washington, D.C. - USA');
30  City.set('location', new Parse.GeoPoint(38.930727220189944, -77.04626261880388));
31  await City.save();
32
33  // Ottawa
34  City = new Parse.Object('City');
35  City.set('name', 'Ottawa - Canada');
36  City.set('location', new Parse.GeoPoint(45.41102167733425, -75.695414598736));
37  await City.save();
```
:::

## 3 - Query the data

**Sorting the results**

With the sample data saved, we can start performing different query types.

For our first example, we will select all the cities and sort them depending on how far they are from a reference geopoint. We implement this query by passing a constraint to the Query\<City> object. The method near(key\:geoPoint:) available via the ParseSwift SDK allows us to construct such constraint. As arguments, we pass the field’s name (usually referred to as key) containing the reference geoPoint.

```swift
1   // The reference geopoint will be Kingston city - Jamaica
2   guard let kingstonGeoPoint = try? ParseGeoPoint(latitude: 18.018086950599134, longitude: -76.79894232253473) else { return }
3
4   let query = City.query(near(key: "location", geoPoint: kingstonGeoPoint)) // The method near(key:geoPoint:) returns the constraint needed to sort the query
5
6   let sortedCities: [City]? = try? query.find() // Executes the query synchronosuly and returns an array containing the cities properly sorted
7
8   query.find { result in // Executes the query asynchronosuly and returns a Result<[City], ParseError> type object to handle the results
9     switch result {
10    case .success(let cities):
11      // cities = [Bogotá, Washington DC, Mexico City, Ottawa, Brasília, Montevideo]
12    case .failure(let error):
13      // Handle the error if something happened
14    }
15  }
```

**Selecting results within a given region**

Suppose we want to select cities within a certain region. We can achieve this with a constraint created by the method withinKilometers(key\:geoPoint\:distance:). As arguments, we pass the field’s name containing the city’s location, the region’s center (a ParseGeoPoint data type) and the maximum distance (in **km**) a city can be from this region’s center. To select all cities that are at most **3000km** away from Kingston - Jamaica, we can do it in the following way

```swift
1   let distance: Double = 3000 // km
2   guard let kingstonGeoPoint = try? ParseGeoPoint(latitude: 18.018086950599134, longitude: -76.79894232253473) else { return }
3
4   let query = City.query(withinKilometers(key: "location", geoPoint: kingstonGeoPoint, distance: distance))
5   // The method withinKilometers(key:geoPoint:distance:) returns the constraint we need for this case
6
7   let sortedCities: [City]? = try? query.find() // Executes the query synchronosuly and returns an array containing the cities we are looking for (Bogotá, Washington DC and Mexico city in this case)
8
9   query.find { result in // Executes the query asynchronosuly and returns a Result<[City], ParseError> type object to handle the results
10    switch result {
11    case .success(let cities):
12      // cities = [Bogotá, Washington DC, Mexico City]
13    case .failure(let error):
14      // Handle the error if something happened
15    }
16  }
```

Additionally, when the distance is given in miles instead of kilomenters, we can use the withinMiles(key\:geoPoint\:distance\:sorted:) method.

A less common method, withinRadians(key\:geoPoint\:distance\:sorted:), is also available if the distance is given in radians. Its use is very similar to the previous methods.

**Selecting results within a given polygon**

In the previous example, we selected cities within a region represented by a circular region. In case we require to have a non-circular shape for the region, the ParseSwift SDK does allow us to construct such regions from their vertices.

Now, the goal for this example is to select cities within a five vertex polygon. These vertices are expressed using the ParseGeoPoint struct. Once we have created the vertices, we instantiate a ParsePolygon. This polygon is then passed to the withinPolygon(key\:polygon:) method (provided by the ParseSwift SDK) to construct the constraint that will allow us to select cities within this polygon.

```swift
1   // The polygon where the selected cities are
2   let polygon: ParsePolygon? = {
3     do {
4       // We first instantiate the polygon vertices
5       let geoPoint1 = try ParseGeoPoint(latitude: 15.822238344514378, longitude: -72.42845934415942)
6       let geoPoint2 = try ParseGeoPoint(latitude: -0.7433770196268968, longitude: -97.44765968406668)
7       let geoPoint3 = try ParseGeoPoint(latitude: -59.997149373299166, longitude: -76.52969196322749)
8       let geoPoint4 = try ParseGeoPoint(latitude: -9.488786415007201, longitude: -18.346101586021952)
9       let geoPoint5 = try ParseGeoPoint(latitude: 15.414859532811047, longitude: -60.00625459569375)
10                
11      // Next we compose the polygon
12      return try ParsePolygon([geoPoint1, geoPoint2, geoPoint3, geoPoint4, geoPoint5])
13    } catch let error as ParseError {
14      print("Failed to instantiate vertices: \(error.message)")
15      return nil
16    } catch {
17      print("Failed to instantiate vertices: \(error.localizedDescription)")
18      return nil
19    }
20  }()
21        
22  guard let safePolygon = polygon else { return }
23        
24  let query = City.query(withinPolygon(key: "location", polygon: safePolygon))
25  // withinPolygon(key:polygon:) returns the required constraint to apply on the query
26        
27  let cities = try? query.find() // Executes the query synchronously
28        
29  query.find { result in // Executes the query asynchronously and returns a result of type Result<[], ParseError>
30    // Handle the result
31  }
```

## Conclusion

Nowadays doing operations on location data to offer custom services is very important. Back4App together with the ParseSwift SDK makes it easy to implement those kinds of operations.
