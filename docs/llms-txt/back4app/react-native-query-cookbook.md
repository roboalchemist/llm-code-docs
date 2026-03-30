# Source: https://docs-containers.back4app.com/docs/react-native/parse-sdk/data-objects/react-native-query-cookbook.md

---
title: Query Cookbook
slug: docs/react-native/parse-sdk/data-objects/react-native-query-cookbook
description: In this guide, you'll learn how to use every query method in Parse on a React Native application
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-19T12:17:38.853Z
updatedAt: 2025-01-28T13:50:41.091Z
---

# Parse Query Cookbook in React Native

## Introduction

We’ve already seen how a Parse.Query with get can retrieve a single Parse.Object from Back4App. There are many other ways to retrieve data with Parse.Query - you can retrieve many objects at once, use conditions on the objects you wish to retrieve, and more.

In this guide, you will ding deep into the Parse.Query class and see all the methods you can use to build your Queries. You will use a simple database class with some mocked data to perform the Queries using the Javascript Console on Back4App.

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- An App [**created on Back4App**](https://www.back4app.com/docs/get-started/new-parse-app).
:::

## Goal

Explore the Parse.Query class different methods.

## The Parse.Query class

Any query operation on Parse uses the Parse.Query object type, which will help you retrieve specific data from your Back4App throughout your app. To create a new Parse.Query, you need to pass as a parameter the desired Parse.Object subclass, which is the one that will contain your query results.

It is crucial to know that a Parse.Query will only resolve after calling a retrieve method (like Parse.Query.find or Parse.Query.get), so a query can be set up and several modifiers can be chained before actually being called.

You can read more about the Parse.Query class [**here at the official documentation**](https://parseplatform.org/Parse-SDK-JS/api/master/Parse.Query.html).

## Using the JS Console on Back4App

Inside your Back4App application’s dashboard, you will find a very useful API console in which you can run JavaScript code directly. In this guide you will use to store and query data objects from Back4App. On your App main dashboard go to Core->API Console->JS Console.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/wCOUHbylQUagFfnnZoMGa_image.png)

## Save your Data Objects

To run the queries on this guide you’ll need first to populate your App with some data. Let’s create a sample class called Profile, which mocks a social media profile class using famous people names and the following fields:

- string typename:
- Date typebirthDay:
- Number (integer) typefriendCount:
- Array (string array) typefavoriteFoods:
- Array (Number array) typeluckyNumbers:
- GeoPoint typelastLoginLocation:
- Nullable pointer typepremiumMembership, related to a Membership class containing string name and Date expirationDatefields.

Here is the Parse.Object classes creation code, so go ahead and run it in your API console:

```javascript
1	// Add Profile objects and create table
2	// Adam Sandler
3	let Profile = new Parse.Object('Profile');
4	Profile.set('name', 'Adam Sandler');
5	Profile.set('birthDay', new Date('09/09/1966'));
6	Profile.set('friendCount', 2);
7	Profile.set('favoriteFoods', ['Lobster', 'Bread']);
8	Profile.set('luckyNumbers', [2, 7]);
9	Profile.set('lastLoginLocation', new Parse.GeoPoint(37.38412167489413, -122.01268034622319));
10	await Profile.save();
11	
12	// Britney Spears
13	Profile = new Parse.Object('Profile');
14	Profile.set('name', 'Britney Spears');
15	Profile.set('birthDay', new Date('12/02/1981'));
16	Profile.set('friendCount', 52);
17	Profile.set('favoriteFoods', ['Cake', 'Bread']);
18	Profile.set('luckyNumbers', [22, 7]);
19	Profile.set('lastLoginLocation', new Parse.GeoPoint(37.38412167489413, -122.01268034622319));
20	await Profile.save();
21	
22	// Carson Kressley
23	Profile = new Parse.Object('Profile');
24	Profile.set('name', 'Carson Kressley');
25	Profile.set('birthDay', new Date('11/11/1969'));
26	Profile.set('friendCount', 12);
27	Profile.set('favoriteFoods', ['Fish', 'Cookies']);
28	Profile.set('luckyNumbers', [8, 2]);
29	Profile.set('lastLoginLocation', new Parse.GeoPoint(37.38412167489413, -122.01268034622319));
30	await Profile.save();
31	
32	// Dan Aykroyd
33	// Creates related object Membership for this user only
34	let Membership = new Parse.Object('Membership');
35	Membership.set('name', 'Premium');
36	Membership.set('expirationDate', new Date('10/10/2030'))
37	await Membership.save();
38	Profile = new Parse.Object('Profile');
39	Profile.set('name', 'Dan Aykroyd');
40	Profile.set('birthDay', new Date('07/01/1952'));
41	Profile.set('friendCount', 66);
42	Profile.set('favoriteFoods', ['Jam', 'Peanut Butter']);
43	Profile.set('luckyNumbers', [22, 77]);
44	Profile.set('lastLoginLocation', new Parse.GeoPoint(37.38412167489413, -122.01268034622319));
45	Profile.set('premiumMembership', Membership);
46	await Profile.save();
47	
48	// Eddie Murphy
49	Profile = new Parse.Object('Profile');
50	Profile.set('name', 'Eddie Murphy');
51	Profile.set('birthDay', new Date('04/03/1961'));
52	Profile.set('friendCount', 49);
53	Profile.set('favoriteFoods', ['Lettuce', 'Pepper']);
54	Profile.set('luckyNumbers', [6, 5]);
55	Profile.set('lastLoginLocation', new Parse.GeoPoint(-27.104919974838154, -52.61428045237739));
56	await Profile.save();
57	
58	// Fergie
59	Profile = new Parse.Object('Profile');
60	Profile.set('name', 'Fergie');
61	Profile.set('birthDay', new Date('03/27/1975'));
62	Profile.set('friendCount', 55);
63	Profile.set('favoriteFoods', ['Lobster', 'Shrimp']);
64	Profile.set('luckyNumbers', [13, 7]);
65	Profile.set('lastLoginLocation', new Parse.GeoPoint(-27.104919974838154, -52.61428045237739));
66	await Profile.save();
67	
68	console.log('Success!');
```

After running this code, you should now have a Profile class in your database with six objects created. Your new class should look like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/3N7_vbgwgh6HMao1XuEh3_image.png)

Let’s now take a look at examples from every Parse.Query method, along with brief explanations on what they do. Please note that some methods in this list can take options as an additional argument, but in most cases, it is only related to masterKey usage and not relevant to this guide content, so this possibility will be omitted whenever not relevant.

## Query retrievers

These methods are responsible for running the query and retrieving its results, being always present in your query implementation.

:::CodeblockTabs
cancel

```javascript
//Cancels the current network request.
1	let query = new Parse.Query('Profile');
2	let queryResult = await query.find();
3	// This is hard to test in small databases, since by the time
4	// "cancel" is called, the "find" request is already resolved
5	queryResult = query.cancel();
6	console.log(queryResult);
```

count

```javascript
//Retrieves the count of Parse.Object results that meet the query criteria.
1	let query = new Parse.Query('Profile');
2	let queryResult = await query.count();
3	console.log(queryResult);
```

distinct

```javascript
//Runs the query and returns a list of unique values from the results and the specified key.
1	let query = new Parse.Query('Profile');
2	let queryResult = await query.distinct('favoriteFoods');
3	console.log(queryResult);
```

find

```javascript
//This is the basic method for retrieving your query results, always returning an array of Parse.Object instances, being empty when none are found.
1	let query = new Parse.Query('Profile');
2	// When using .find() in a query without other operations, you will
3	// get every object saved in your class
4	let queryResult = await query.find();
5	console.log(queryResult);
```

findAll

```javascript
//Retrieves a complete list of Parse.Objects that satisfy this query.
1	let query = new Parse.Query('Profile');
2	// When using .findAll() in a query without other operations, you will
3	// get every object saved in your class
4	let queryResult = await query.findAll();
5	console.log(queryResult);
```

first

```javascript
//Retrieves the first Parse.Object instance that meets the query criteria.
1	let query = new Parse.Query('Profile');
2	// Pay attention to your query ordering when using .first
3	let queryResult = await query.first();
4	console.log(queryResult);
```

get

```javascript
//This quick method is used to retrieve a single Parse.Object instance when you know its objectId.
1	let query = new Parse.Query('Profile');
2	// Since objectId is randomly set in your database, make sure to inform a
3	// valid one when testing this method
4	let queryResult = await query.get('C6ENdLnFdQ');
5	console.log(queryResult);
```
:::

## Query conditioners

These methods give you the possibility of applying conditional constraints to your query, which are arguably the most important operations in querying. Remember that these operations can all be chained before the results are retrieved, so many combinations can be achieved to solve your querying needs.

:::CodeblockTabs
\_addCondition

```javascript
//  Helper that is called by Parse for filtering objects using conditional constants, such as “$gt”, “$eq” and so on. Only usable by users in very specific cases.
1	let query = new Parse.Query('Profile');
2	query._addCondition('friendCount', '$gt', 25);
3	let queryResult = await query.find();
4	console.log(queryResult);
```

\_regexStartWith

```javascript
//Helper used by Parse that converts string for regular expression at the beginning.
1	let query = new Parse.Query('Profile');
2	let result = query._regexStartWith('text');
3	console.log(result);
```

containedBy

```javascript
//Filters objects in which a key value must be contained by the provided array of values. Get objects where all array elements match.
1	let query = new Parse.Query('Profile');
2	query.containedBy('luckyNumbers', [2, 7]);
3	let queryResult = await query.find();
4	console.log(queryResult);
```

containedIn

```javascript
//Filters objects in which a key value is contained in the provided array of values.
1	let query = new Parse.Query('Profile');
2	// containedIn can be used on any data type such as numbers and strings
3	query.containedIn('luckyNumbers', [2, 7]);
4	let queryResult = await query.find();
5	console.log(queryResult);
```
:::

:::CodeblockTabs
contains

```javascript
//Filters objects in which a string key value contains the provided text value. Be aware that this condition is case-sensitive.
1	let query = new Parse.Query('Profile');
2	// This can be slow in large databases and are case sensitive
3	query.contains('name', 'da');
4	let queryResult = await query.find();
5	console.log(queryResult);
```

containsAll

```javascript
//Filters objects in which an array type key value must contain every value provided.
1	let query = new Parse.Query('Profile');
2	query.containsAll('luckyNumbers', [2, 7]);
3	let queryResult = await query.find();
4	console.log(queryResult);
```

containsAllStartingWith

```javascript
//Filters objects in which an array type key value must contain every string value provided.
1	let query = new Parse.Query('Profile');
2	// These should be string values
3	query.containsAllStartingWith('favoriteFoods', ['Shrimp', 'Lobster']);
4	let queryResult = await query.find();
5	console.log(queryResult);
```

doesNotExist

```javascript
//Filters objects in which a key value is not set.
1	let query = new Parse.Query('Profile');
2	query.doesNotExist('premiumMembership');
3	let queryResult = await query.find();
4	console.log(queryResult);
```
:::

:::CodeblockTabs
doesNotMatchKeyInQuery

```javascript
//  Requires that a key’s value does not match a value in an object returned by a different Parse.Query. Useful for multi-object querying.
1	let query = new Parse.Query('Profile');
2	// Multiple queries can be combined using this, useful when there are more objects
3	// related, not our example case
4	query.doesNotMatchKeyInQuery('friendCount', 'friendCount', new Parse.Query('Profile').lessThan('friendCount', 50));
5	query.greaterThan('friendCount', 10);
6	let queryResult = await query.find();
7	console.log(queryResult);
```

doesNotMatchQuery

```javascript
//Requires that an object contained in the given key does not match another query. Useful for multi-object querying.
1	let innerQuery = new Parse.Query('Membership');
2	innerQuery.greaterThan('expirationDate', new Date());
3	let query = new Parse.Query('Profile');
4	query.exists('premiumMembership');
5	query.doesNotMatchQuery('premiumMembership', innerQuery);
6	let queryResult = await query.find();
7	console.log(queryResult);
```

endsWith

```javascript
//Filters objects in which a string key’s value ends with the provided text value.
1	let query = new Parse.Query('Profile');
2	// This is faster than other string searches by using backend index
3	query.endsWith('name', 'ie');
4	let queryResult = await query.find();
5	console.log(queryResult);
```

equalTo

```javascript
//Filters objects in which a specific key’s value is equal to the provided value.
1	let query = new Parse.Query('Profile');
2	// equalTo can be used in any data type
3	query.equalTo('friendCount', 2);
4	let queryResult = await query.find();
5	console.log(queryResult);
```
:::

:::CodeblockTabs
exists

```javascript
//Filters objects in which a key value is set.
1	let query = new Parse.Query('Profile');
2	query.exists('premiumMembership');
3	let queryResult = await query.find();
4	console.log(queryResult);
```

fullText

```javascript
//Filters objects in which a string key’s value wrap matches the provided text value in it. It can have many customizable options to improve its results, like language specification and score order. Check the Parse docs to have a complete understanding of that.
1	let query = new Parse.Query('Profile');
2	// fullText can be very powerful in text search queries, but
3	// also slow in large datasets when its options are not optimized
4	query.fullText('name', 'Spears', { diacriticSensitive: false, caseSensitive: false });
5	// In order to sort you must use select and ascending ($score is required)
6	query.ascending('$score');
7	query.select('$score');
8	let queryResult = await query.find();
9	console.log(queryResult);
```

greaterThan

```javascript
//Filters objects in which a specific key’s value is greater than the provided value.
1	let query = new Parse.Query('Profile');
2	// greaterThan can be used on numbers and dates
3	query.greaterThan('birthDay', new Date('08/19/1980'));
4	let queryResult = await query.find();
5	console.log(queryResult);
```

greaterThanOrEqualTo

```javascript
//Filters objects in which a specific key’s value is greater than or equal to the provided value.
1	let query = new Parse.Query('Profile');
2	// greaterThanOrEqualTo can be used on numbers and dates
3	query.greaterThanOrEqualTo('friendCount', 49);
4	let queryResult = await query.find();
5	console.log(queryResult);
```
:::

:::CodeblockTabs
lessThan

```javascript
//  Filters objects in which a specific key’s value is lesser than the provided value.
1	let query = new Parse.Query('Profile');
2	// lessThan can be used on numbers and dates
3	query.lessThan('birthDay', new Date('08/19/1980'));
4	let queryResult = await query.find();
5	console.log(queryResult);
```

lessThanOrEqualTo

```javascript
//Filters objects in which a specific key’s value is lesser than or equal to the provided value.
1	let query = new Parse.Query('Profile');
2	// lessThanOrEqualTo can be used on numbers and dates
3	query.lessThanOrEqualTo('friendCount', 49);
4	let queryResult = await query.find();
5	console.log(queryResult);
```

matches

```javascript
//Filters objects in which a string type key value must match the provided regular expression and its modifiers.
1	let query = new Parse.Query('Profile');
2	// Using the "i" modifier is a quick way to achieve
3	// case insensitive string querying
4	query.matches('name', 'da', 'i');
5	let queryResult = await query.find();
6	console.log(queryResult);
```

matchesKeyInQuery

```javascript
//Requires that a key’s value matches a value in an object returned by a different Parse.Query. Useful for multi-object querying.
1	let query = new Parse.Query('Profile');
2	// Multiple queries can be combined using this, useful when there are more objects
3	// related, not our example case
4	query.matchesKeyInQuery('friendCount', 'friendCount', new Parse.Query('Profile').lessThan('friendCount', 50));
5	query.greaterThan('friendCount', 10);
6	let queryResult = await query.find();
7	console.log(queryResult);
```
:::

:::CodeblockTabs
matchesQuery

```javascript
//Requires that an object contained in the given key matches another query. Useful for multi-object querying.
1	let innerQuery = new Parse.Query('Membership');
2	innerQuery.greaterThan('expirationDate', new Date());
3	let query = new Parse.Query('Profile');
4	query.exists('premiumMembership');
5	query.matchesQuery('premiumMembership', innerQuery);
6	let queryResult = await query.find();
7	console.log(queryResult);
```

notEqualTo

```javascript
//Filters objects in which a specific key’s value is not equal to the provided value.
1	let query = new Parse.Query('Profile');
2	// notEqualTo can be used in any data type
3	query.notEqualTo("friendCount", 2);
4	let queryResult = await query.find();
5	console.log(queryResult);
```

startsWith

```javascript
//Filters objects in which a string key’s value starts with the provided text value.
1	let query = new Parse.Query('Profile');
2	// This is faster than other string searches by using backend index
3	query.startsWith('name', 'Brit');
4	let queryResult = await query.find();
5	console.log(queryResult);
```
:::

## Query ordering

Essential in most queries, ordering can be easily achieved in Parse and even chained between two or more ordering constraints.

:::CodeblockTabs
addAscending

```javascript
//  Sort the results in ascending order, overwrites previous orderings. Multiple keys can be used to solve ordering ties.
1	let query = new Parse.Query('Profile');
2	query.addAscending('friendCount');
3	let queryResult = await query.find();
4	console.log(queryResult);
```

addDescending

```javascript
//Sort the results in descending order, overwrites previous orderings. Multiple keys can be used to solve ordering ties.
1	let query = new Parse.Query('Profile');
2	query.addDescending('friendCount');
3	let queryResult = await query.find();
4	console.log(queryResult);
```

ascending

```javascript
//Sort the results in ascending order, this can be chained without overwriting previous orderings. Multiple keys can be used to solve ordering ties.
1	let query = new Parse.Query('Profile');
2	query.ascending('friendCount');
3	let queryResult = await query.find();
4	console.log(queryResult);
```

descending

```javascript
//Sort the results in descending order, this can be chained without overwriting previous orderings. Multiple keys can be used to solve ordering ties.
1	let query = new Parse.Query('Profile');
2	query.descending('friendCount');
3	let queryResult = await query.find();
4	console.log(queryResult);
```

sortByTextScore

```javascript
//Sorts by text score when using Parse.Query.fullText
1	let query = new Parse.Query('Profile');
2	query.fullText('name', 'Dan', { diacriticSensitive: false, caseSensitive: false });
3	query.sortByTextScore();
4	let queryResult = await query.find();
5	console.log(queryResult);
```
:::

## Field selecting

These methods affect which field values can be in your query results.

:::CodeblockTabs
exclude

```javascript
//  Return all fields in the returned objects except the ones specified.
1	let query = new Parse.Query('Profile');
2	query.exclude('name');
3	let queryResult = await query.find();
4	console.log(queryResult[0].get('name') === undefined);
5	console.log(queryResult[0].get('birthDay'));
```

include

```javascript
//Includes nested Parse.Objects for the provided key.
1	let query = new Parse.Query('Profile');
2	query.exists('premiumMembership');
3	query.include('premiumMembership');
4	let queryResult = await query.find();
5	console.log(queryResult[0].get('premiumMembership'));
```

includeAll

```javascript
//Includes all nested Parse.Objects.
1	let query = new Parse.Query('Profile');
2	query.exists('premiumMembership');
3	query.includeAll();
4	let queryResult = await query.find();
5	console.log(queryResult[0].get('premiumMembership'));
```

select

```javascript
//Return only the specified fields in the returned objects.
1	let query = new Parse.Query('Profile');
2	query.select('name');
3	let queryResult = await query.find();
4	console.log(queryResult[0].get('birthDay') === undefined);
5	console.log(queryResult[0].get('name'));
```
:::

## Geopoint querying

These are methods specific to GeoPoint querying.

:::CodeblockTabs
near

```javascript
//  Order objects by how near the key value is from the given GeoPoint.
1	let query = new Parse.Query('Profile');
2	query.near('lastLoginLocation', new Parse.GeoPoint(37.38412167489413, -122.01268034622319));
3	let queryResult = await query.find();
4	console.log(queryResult);
```

polygonContains

```javascript
//Find objects whose key value contains the specified GeoPoint.
1	let query = new Parse.Query('Profile');
2	query.polygonContains('lastLoginLocation', new Parse.GeoPoint(37.38412167489413, -122.01268034622319));
3	let queryResult = await query.find();
4	console.log(queryResult);
```

withinGeoBox

```javascript
//Find objects whose key value is contained within the specified bounding box, composed by two GeoPoint values that set the lower-left and upper-right corner values.
1	let query = new Parse.Query('Profile');
2	query.withinGeoBox('lastLoginLocation', new Parse.GeoPoint(37.48412167489413, -122.11268034622319), new Parse.GeoPoint(37.28412167489413, -121.91268034622319));
3	let queryResult = await query.find();
4	console.log(queryResult);
```

withinKilometers

```javascript
//Find objects whose key value is near the given GeoPoint and within the maxDistance value. The sorted boolean value determines if the results should be sorted by distance ascending.
1	let query = new Parse.Query('Profile');
2	query.withinKilometers('lastLoginLocation', new Parse.GeoPoint(37.38412167489413, -122.01268034622319), 100, true);
3	let queryResult = await query.find();
4	console.log(queryResult);
```
:::

:::CodeblockTabs
withinMiles

```javascript
//Find objects whose key value is near the given GeoPoint and within the maxDistance value. The sorted boolean value determines if the results should be sorted by distance ascending.
1	let query = new Parse.Query('Profile');
2	query.withinMiles('lastLoginLocation', new Parse.GeoPoint(37.38412167489413, -122.01268034622319), 60, true);
3	let queryResult = await query.find();
4	console.log(queryResult);
```

withinPolygon

```javascript
//Find objects whose key value is contained within the specified polygon, composed of an array of GeoPoints (at least three). If the polygon path is open, it will be closed automatically by Parse connecting the last and first points.
1	let query = new Parse.Query('Profile');
2	query.withinPolygon('lastLoginLocation', [new Parse.GeoPoint(37.48412167489413, -122.11268034622319), new Parse.GeoPoint(37.48412167489413, -121.91268034622319), new Parse.GeoPoint(37.28412167489413, -121.91268034622319), new Parse.GeoPoint(37.28412167489413, -122.01268034622319)]);
3	let queryResult = await query.find();
4	console.log(queryResult);
```

withinRadians

```javascript
//Find objects whose key value is near the given GeoPoint and within the maxDistance value. The sorted boolean value determines if the results should be sorted by distance ascending.
1	let query = new Parse.Query('Profile');
2	query.withinRadians('lastLoginLocation', new Parse.GeoPoint(37.38412167489413, -122.01268034622319), 1.5, true);
3	let queryResult = await query.find();
4	console.log(queryResult);
```
:::

## Pagination

These methods are related to pagination utilities, useful for queries that will retrieve a large number of results.

:::CodeblockTabs
limit

```javascript
//  Sets the maximum value of returned results, the default value is 100.
1	let query = new Parse.Query('Profile');
2	query.limit(2);
3	let queryResult = await query.find();
4	console.log(queryResult);
```

skip

```javascript
//Skips the first n results in the query, essential for pagination.
1	let query = new Parse.Query('Profile');
2	query.skip(2);
3	let queryResult = await query.find();
4	console.log(queryResult);
```

withCount

```javascript
//Sets a flag that will wrap or not the query response in an object containing results, holding the array of Parse.Object and count integer holding the total number of results.
1	let query = new Parse.Query('Profile');
2	query.withCount(true);
3	let queryResult = await query.find();
4	console.log(queryResult);
```
:::

## Response handling

These methods are helpers for handling the query responses, making it possible to queue callbacks that will be called after your query is resolved. They act as query resolvers as well, like find and first.

:::CodeblockTabs
each

```javascript
//  Iterates over each result from the query and calls a callback for each one, in an unspecified order. Note that execution will halt on a rejected promise, so make sure to handle this case if using promises.
1	let query = new Parse.Query('Profile');
2	let queryResult = await query.each((result) => console.log(result));
3	console.log(queryResult);
```

eachBatch

```javascript
//Iterates over each result from the query and calls a callback for each batch of results, in an unspecified order. The batchSize value needs to be passed inside the options object parameter, being the default 100. Note that execution will halt on a rejected promise, so make sure to handle this case if using promises.
1	let query = new Parse.Query('Profile');
2	let queryResult = await query.eachBatch((result) => console.log(result), {batchSize: 2});
3	console.log(queryResult);
```

filter

```javascript
//Iterates over each result from the query and calls a callback for each one, in an unspecified order. Note that execution will halt on a rejected promise, so make sure to handle this case if using promises. Differs from each for passing more parameters down on callback execution.
1   let query = new Parse.Query('Profile');
2   let queryResult = await query.filter((currentObject, index, query) => console.log(`${index} - ${currentObject} - ${query}`));
3   console.log(queryResult);
```

map

```javascript
//Iterates over each result from the query and calls a callback for each one, in an unspecified order. Note that execution will halt on a rejected promise, so make sure to handle this case if using promises. Differs from each for passing more parameters down on callback execution.
1   let query = new Parse.Query('Profile');
2   let queryResult = await query.map((currentObject, index, query) => console.log(`${index} - ${currentObject} - ${query}`));
3   console.log(queryResult);
```

reduce

```javascript
//Iterates over each result from the query and calls a callback for each one, in an unspecified order. Note that execution will halt on a rejected promise, so make sure to handle this case if using promises. Differs from each for passing more parameters down on callback execution and by allowing direct accumulator handling. The initialValue is the value to use as the first argument to the first call of the callback. If no initialValue is supplied, the first object in the query will be used and skipped.
1   let query = new Parse.Query('Profile');
2   let queryResult = await query.reduce((accumulator, currentObject, index) => console.log(`${index} - ${currentObject} - ${accumulator}`));
3   console.log(queryResult);
```
:::

## Compound query

These methods will create compound queries, which can combine more than one Parse.Query instance to achieve more complex results.

:::CodeblockTabs
\_andQuery

```javascript
//  Helper that is used by Parse to add a constraint that all of passed in queries must match when using Parse.Query.and.
1	let query1 = new Parse.Query('Profile');
2	query1.greaterThan('friendCount', 10);
3	let query2 = new Parse.Query('Profile');
4	query1.lessThan('friendCount', 50);
5	let query = new Parse.Query('Profile');
6	query._andQuery([query1, query2]);
7	let queryResult = await query.find();
8	console.log(queryResult);
```

\_norQuery

```javascript
//Helper that is used by Parse when using Parse.Query.nor.
1	let query1 = new Parse.Query('Profile');
2	query1.greaterThan('friendCount', 10);
3	let query2 = new Parse.Query('Profile');
4	query1.lessThan('friendCount', 50);
5	let query = new Parse.Query('Profile');
6	query._norQuery([query1, query2]);
7	let queryResult = await query.find();
8	console.log(queryResult);
```

\_orQuery

```javascript
//Helper that is used by Parse to add a constraint that any of passed in queries must match when using Parse.Query.or.
1	let query1 = new Parse.Query('Profile');
2	query1.greaterThan('friendCount', 10);
3	let query2 = new Parse.Query('Profile');
4	query1.lessThan('friendCount', 50);
5	let query = new Parse.Query('Profile');
6	query._orQuery([query1, query2]);
7	let queryResult = await query.find();
8	console.log(queryResult);
```

and

```javascript
//Compose a compound query that is the AND of the passed queries.
1	let query1 = new Parse.Query('Profile');
2	query1.greaterThan('friendCount', 10);
3	let query2 = new Parse.Query('Profile');
4	query1.lessThan('friendCount', 50);
5	let query = Parse.Query.and(query1, query2);
6	let queryResult = await query.find();
7	console.log(queryResult);
```

nor

```javascript
//Compose a compound query that is the NOR of the passed queries.
1	let query1 = new Parse.Query('Profile');
2	query1.greaterThan('friendCount', 10);
3	let query2 = new Parse.Query('Profile');
4	query1.lessThan('friendCount', 50);
5	let query = Parse.Query.nor(query1, query2);
6	let queryResult = await query.find();
7	console.log(queryResult);
```

or

```javascript
//Compose a compound query that is the OR of the passed queries.
1	let query1 = new Parse.Query('Profile');
2	query1.greaterThan('friendCount', 10);
3	let query2 = new Parse.Query('Profile');
4	query1.lessThan('friendCount', 50);
5	let query = Parse.Query.or(query1, query2);
6	let queryResult = await query.find();
7	console.log(queryResult);
```
:::

## Database related

These methods are related to database preferences and operations.

:::CodeblockTabs
aggregate

```javascript
//  Executes an aggregate query, retrieving objects over a set of input values. Please refer to MongoDB documentation on aggregate for better understanding.
1   let query = new Parse.Query('Profile');
2   let queryResult = await query.aggregate({ limit: 5 });
3   console.log(queryResult);
```

explain

```javascript
//Investigates the query execution plan, related to MongoDB explain operation.
1	let query = new Parse.Query('Profile');
2	query.explain(true);
3	let queryResult = await query.find();
4	console.log(queryResult);
```

readPreference

```javascript
//SWhen using a MongoDB replica set, use this method to choose from which replica the objects will be retrieved. The possible values are PRIMARY (default), PRIMARY_PREFERRED, SECONDARY, SECONDARY_PREFERRED, or NEAREST.
1	let query = new Parse.Query('Profile');
2	query.readPreference(''PRIMARY'');
3	let queryResult = await query.find();
4	console.log(queryResult);
```
:::

## Local datastore

These methods enable selecting the source of the queries and using a local datastore.

:::CodeblockTabs
fromLocalDatastore

```javascript
//  Changes the source of this query to all pinned objects.
1	// This should be set before using fromLocalDatastore
2	Parse.enableLocalDatastore();
3	let query = new Parse.Query('Profile');
4	query.fromLocalDatastore();
5	let queryResult = await query.find();
6	console.log(queryResult);
```

fromNetwork

```javascript
//Changes the source of this query to your online server.
1	let query = new Parse.Query('Profile');
2	query.fromNetwork();
3	let queryResult = await query.find();
4	console.log(queryResult);
```

fromPin

```javascript
//Changes the source of this query to the default group of pinned objects.
1	let query = new Parse.Query('Profile');
2	query.fromPin();
3	let queryResult = await query.find();
4	console.log(queryResult);
```

fromPinWithName

```javascript
//Changes the source of this query to a specific group of pinned objects.
1	let query = new Parse.Query('Profile');
2	query.fromPinWithName('pinnedObjects');
3	let queryResult = await query.find();
4	console.log(queryResult);
```
:::

## JSON specifics

Methods that allow queries to be represented as JSON and retrieved.

:::CodeblockTabs
toJSON

```json
//  Returns a JSON representation of this query operations.
1	let query = new Parse.Query('Profile');
2	query.greaterThan('friendCount', 10);
3	let queryJSON = await query.toJSON();
4	console.log(queryJSON);
```

withJSON

```json
//Add a previously generated JSON representation of query operations to this query.
1	let query = new Parse.Query('Profile');
2	query.greaterThan('friendCount', 10);
3	let queryJSON = await query.toJSON();
4	let query2 = new Parse.Query('Profile');
5	query2.withJSON(queryJSON);
6	let queryResult = await query2.find();
7	console.log(queryResult);

//Static method to restore Parse.Query by JSON representation, internally calling Parse.Query.withJSON.
1	let query = new Parse.Query('Profile');
2	query.greaterThan('friendCount', 10);
3	let queryJSON = await query.toJSON();
4	let query2 = Parse.Query.withJSON('Profile', queryJSON);
5	let queryResult = await query2.find();
6	console.log(queryResult);
```
:::

## Conclusion

At the end of this guide, you learned how to perform every data query method in Parse. In the next guide, you will learn about complex Parse querying in React Native.
