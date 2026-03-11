# Source: https://docs-containers.back4app.com/docs/react-native/parse-sdk/data-objects/react-native-join-query.md

---
title: Join Queries
slug: docs/react-native/parse-sdk/data-objects/react-native-join-query
description: In this guide, you'll learn how to perform relational join queries in Parse
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-19T13:45:30.959Z
updatedAt: 2025-01-28T13:50:52.103Z
---

# Join Query using Parse

## Introduction

In this guide, you will perform relational queries in Parse mimicking the behavior of SQL JOIN queries using a NoSQL database.

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- An App [**created on Back4App**](https://www.back4app.com/docs/get-started/new-parse-app).
:::

## Goal

Query relational data stored on Back4App in SQL JOIN query fashion.

## 1 - Understanding the Parse.Query class

Any Parse query operation uses the Parse.Query object type, which will help you retrieve specific data from your database throughout your app. It is crucial to know that a Parse.Query will only resolve after calling a retrieve method (like Parse.Query.find or Parse.Query.get), so a query can be set up and several modifiers can be chained before actually being called.

To create a new Parse.Query, you need to pass as a parameter the desired Parse.Object subclass, which is the one that will contain your query results. An example query can be seen below, in which a fictional Profile subclass is being queried.

```javascript
1   // This will create your query
2   let parseQuery = new Parse.Query("Profile");
3   // The query will resolve only after calling this method
4   let queryResult = await parseQuery.find();
```

You can read more about the Parse.Query class [**here at the official documentation**](https://parseplatform.org/Parse-SDK-JS/api/master/Parse.Query.html).

## 2 - Save some data on Back4App

Let’s create two example classes, TableA and TableB, which will be the targets of our queries in this guide. On Parse JS Console it is possible to run JavaScript code directly, querying and updating your application database contents using the JS SDK commands. Run the code below from your JS Console and insert the data on Back4App.

Here is how the JS Console looks like in your dashboard:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/gwr8EqE21xS3619i4j7d__image.png)

Go ahead and create the classes with the following content:

```javascript
1	// Create TableA and its records
2	let TableARecord1 = new Parse.Object('TableA');
3	TableARecord1.set('FieldA', 'Value A 1');
4	TableARecord1 = await TableARecord1.save();
5	
6	let TableARecord2 = new Parse.Object('TableA');
7	TableARecord2.set('FieldA', 'Value A 2');
8	TableARecord2 = await TableARecord2.save();
9	
10	let TableARecord3 = new Parse.Object('TableA');
11	TableARecord3.set('FieldA', 'Value A 3');
12	TableARecord3 = await TableARecord3.save();
13	
14	// Create TableB and its records, some of them linked to TableA
15	let TableBRecord1 = new Parse.Object('TableB');
16	TableBRecord1.set('FieldB', 'Value B 1');
17	TableBRecord1.set('link', TableARecord1);
18	TableBRecord1 = await TableBRecord1.save();
19	
20	let TableBRecord2 = new Parse.Object('TableB');
21	TableBRecord2.set('FieldB', 'Value B 2');
22	TableBRecord2.set('link', TableARecord1);
23	TableBRecord2 = await TableBRecord2.save();
24	
25	let TableBRecord3 = new Parse.Object('TableB');
26	TableBRecord3.set('FieldB', 'Value B 3');
27	TableBRecord3.set('link', TableARecord3);
28	TableBRecord3 = await TableBRecord3.save();
29	
30	let TableBRecord4 = new Parse.Object('TableB');
31	TableBRecord4.set('FieldB', 'Value B 4');
32	TableBRecord4 = await TableBRecord4.save();
33	
34	console.log('Success!');
```

## 3 - Querying the data

Now that you have populated the classes, we can now perform the relational queries in it. Let’s begin by performing the INNER JOIN, introducing the join relational query that we will use in all of our examples. This query represents the results of two combined queries between tables A and B, returning all the records that are related by a specific condition using the Parse.Query.matchesQuery method.

```javascript
1	// JOIN query, get all records in TableA that have matching records in TableB
2	let innerQueryTableA = new Parse.Query("TableA");
3	// Limit to 10 results only for example so we don't fetch too much data
4	innerQueryTableA.limit(10);
5	let joinQueryTableB = new Parse.Query("TableB");
6	// Match the TableA query by the "link" property
7	joinQueryTableB.matchesQuery("link", innerQueryTableA);
8	// Include the "link" property so we have the content of TableA as well
9	joinQueryTableB.include("link");
10	let joinQueryResults = await joinQueryTableB.find();
11	
12	// INNER JOIN, get only the records in TableA that have matching records in TableB
13	console.log("INNER JOIN");
14	console.log("TABLE A ID | FIELD A | FIELD B");
15	for (let joinResult of joinQueryResults) {
16	  console.log(
17	    `${joinResult.get("link").id} | ${joinResult
18	      .get("link")
19	      .get("FieldA")} | ${joinResult.get("FieldB")}`
20	  );
21	}
```

The INNER JOIN SQL query behavior is exactly the one achieved in our generic join relational query, so we need to print its results in the console. Remember that with a Parse.Object you can use the get method to retrieve data by using the column name.

Let’s now perform a LEFT OUTER JOIN consisting of getting all the records on TableA and showing the relational data on TableB, when available:

```javascript
1	// JOIN query, get all records in TableA that have matching records in TableB
2	let innerQueryTableA = new Parse.Query("TableA");
3	// Limit to 10 results only for example so we don't fetch too much data
4	innerQueryTableA.limit(10);
5	let joinQueryTableB = new Parse.Query("TableB");
6	// Match the TableA query by the "link" property
7	joinQueryTableB.matchesQuery("link", innerQueryTableA);
8	// Include the "link" property so we have the content of TableA as well
9	joinQueryTableB.include("link");
10	let joinQueryResults = await joinQueryTableB.find();
11	
12	// LEFT OUTER JOIN, get records in TableA that have matching records in TableB and also every
13	// other TableA record
14	let queryTableA = new Parse.Query("TableA");
15	queryTableA.limit(10);
16	let queryTableAResults = await queryTableA.find();
17	console.log("LEFT JOIN");
18	console.log("TABLE A ID | FIELD A | FIELD B");
19	for (let result of queryTableAResults) {
20	  // Get all entries from JOIN query that have a link to this TableA entry
21	  let joinQueryResultsFiltered = joinQueryResults.filter(
22	    (joinQueryResult) =>
23	      joinQueryResult.get("link") !== undefined &&
24	      joinQueryResult.get("link").id == result.id
25	  );
26	  if (joinQueryResultsFiltered.length > 0) {
27	    for (let joinResult of joinQueryResultsFiltered) {
28	      let fieldBValue = joinResult.get("FieldB");
29	      console.log(`${result.id} | ${result.get("FieldA")} | ${fieldBValue}`);
30	    }
31	  } else {
32	    console.log(`${result.id} | ${result.get("FieldA")} | `);
33	  }
34	}
```

TheRIGHT OUTER JOINis the opposite of the left one, fetching the records fromTableB.

```mysql
1	// JOIN query, get all records in TableA that have matching records in TableB
2	let innerQueryTableA = new Parse.Query("TableA");
3	// Limit to 10 results only for example so we don't fetch too much data
4	innerQueryTableA.limit(10);
5	let joinQueryTableB = new Parse.Query("TableB");
6	// Match the TableA query by the "link" property
7	joinQueryTableB.matchesQuery("link", innerQueryTableA);
8	// Include the "link" property so we have the content of TableA as well
9	joinQueryTableB.include("link");
10	let joinQueryResults = await joinQueryTableB.find();
11	
12	// RIGHT OUTER JOIN, get records in TableA that have matching records in TableB and also every
13	// other TableB record
14	let queryTableB = new Parse.Query("TableB");
15	queryTableB.limit(10);
16	let queryTableBResults = await queryTableB.find();
17	console.log("RIGHT JOIN");
18	console.log("TABLE B ID | FIELD A | FIELD B");
19	for (let result of queryTableBResults) {
20	  // Get all entries from JOIN query that matches this TableB entry
21	  let joinQueryResultsFiltered = joinQueryResults.filter(
22	    (joinQueryResult) => joinQueryResult.id == result.id
23	  );
24	  if (joinQueryResultsFiltered.length > 0) {
25	    for (let joinResult of joinQueryResultsFiltered) {
26	      let fieldAValue = "";
27	      if (joinResult.get("link") !== undefined) {
28	        fieldAValue = joinResult.get("link").get("FieldA");
29	      }
30	      console.log(
31	        `${result.id} | ${fieldAValue} | ${joinResult.get("FieldB")}`
32	      );
33	    }
34	  } else {
35	    console.log(`${result.id} | | ${result.get("FieldB")}`);
36	  }
37	}
```

Finally, we have theFULL OUTER JOINwhich is the combination of the left and right inner joins:

```mysql
1	// JOIN query, get all records in TableA that have matching records in TableB
2	let innerQueryTableA = new Parse.Query("TableA");
3	// Limit to 10 results only for example so we don't fetch too much data
4	innerQueryTableA.limit(10);
5	let joinQueryTableB = new Parse.Query("TableB");
6	// Match the TableA query by the "link" property
7	joinQueryTableB.matchesQuery("link", innerQueryTableA);
8	// Include the "link" property so we have the content of TableA as well
9	joinQueryTableB.include("link");
10	let joinQueryResults = await joinQueryTableB.find();
11	
12	// FULL OUTER JOIN, combining LEFT and RIGHT OUTER JOIN results
13	console.log("FULL JOIN");
14	console.log("TABLE ID | FIELD A | FIELD B");
15	// First print all INNER JOIN results
16	for (let joinResult of joinQueryResults) {
17	  console.log(
18	    `${joinResult.get("link").id} | ${joinResult
19	      .get("link")
20	      .get("FieldA")} | ${joinResult.get("FieldB")}`
21	  );
22	}
23	// Print LEFT JOIN leftovers
24	let outerQueryTableA = new Parse.Query("TableA");
25	outerQueryTableA.limit(10);
26	let outerQueryTableAResults = await outerQueryTableA.find();
27	// Get all entries from query that doesn't match the JOIN query results
28	let filteredOuterQueryTableAResults = outerQueryTableAResults.filter(
29	  (outerQueryTableAResult) =>
30	    joinQueryResults.find(
31	      (joinQueryResult) =>
32	        joinQueryResult.get("link") !== undefined &&
33	        joinQueryResult.get("link").id === outerQueryTableAResult.id
34	    ) === undefined
35	);
36	for (let result of filteredOuterQueryTableAResults) {
37	  console.log(`${result.id} | ${result.get("FieldA")} | `);
38	}
39	// Print RIGHT JOIN leftovers
40	let outerQueryTableB = new Parse.Query("TableB");
41	outerQueryTableB.limit(10);
42	let outerQueryTableBResults = await outerQueryTableB.find();
43	// Get all entries from query that doesn't match the JOIN query results
44	let filteredOuterQueryTableBResults = outerQueryTableBResults.filter(
45	  (outerQueryTableBResult) =>
46	    joinQueryResults.find(
47	      (joinQueryResult) => joinQueryResult.id === outerQueryTableBResult.id
48	    ) === undefined
49	);
50	for (let result of filteredOuterQueryTableBResults) {
51	  console.log(`${result.id} | | ${result.get("FieldB")}`);
52	}
```

## Conclusion

At the end of this guide, you learned how to perform on Back4App relational queries using Parse and emulating the most common SQL JOIN queries in a NoSQL database.
