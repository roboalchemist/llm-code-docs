# Source: https://docs-containers.back4app.com/docs/react-native/parse-sdk/working-with-users/react-native-querying-users.md

---
title: Querying Users
slug: docs/react-native/parse-sdk/working-with-users/react-native-querying-users
description: In this guide you'll learn how to query users in Parse on React Native
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-19T17:05:26.783Z
updatedAt: 2024-03-29T01:30:37.680Z
---

# Querying users in Parse on React Native

## Introduction

Some React Native apps need to directly manage your application users or at least be able to list a specific subset of them. Parse has powerful querying tools and they can also be used for your users in your social media app, for example.
In this guide, you’ll learn how to use Parse.Query to perform realistic user querying in your React Native App using Parse JS SDK.

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- A React Native App created and [**connected to Back4App**](https://www.back4app.com/docs/react-native/parse-sdk/react-native-sdk).
:::

## Goal

To build a user querying feature using Parse for a React Native App.

## 1 - Understanding the Parse.Query class

Any Parse query operation uses the Parse.Query object type, which will help you retrieve specific data from your database throughout your app. It is crucial to know that a Parse.Query will only resolve after calling a retrieve method (like Parse.Query.find or Parse.Query.get), so a query can be set up and several modifiers can be chained before actually being called.

To create a new Parse.Query, you need to pass as a parameter the desired Parse.Object subclass, which is the one that will contain your query results. An example for this guide use-case (Parse.User) can be seen below.

:::CodeblockTabs
JavaScript

```javascript
1   // This will create your query
2   const parseQuery = new Parse.Query(Parse.User);
3   // The query will resolve only after calling this method
5   const queryResult = await parseQuery.find();
```

```typescript
1   // This will create your query
2   const parseQuery: Parse.Query = new Parse.Query(Parse.User);
3   // The query will resolve only after calling this method
4   const queryResult: [Parse.User] = await parseQuery.find();
```
:::

You can read more about the Parse.Query class [**here at the official documentation**](https://parseplatform.org/Parse-SDK-JS/api/master/Parse.Query.html).

## 2 - Performing relevant user queries

Let’s now take a look at some relevant queries that you may need to perform when managing or displaying users in your app. First of all, let’s perform a text search query, searching for users whose usernames contain the search value.

:::CodeblockTabs
JavaScript

```javascript
1	const doUserQuery = async function () {
2	  // This value comes from a state variable
3	  const usernameSearchValue = usernameSearch;
4	  // This will create your user query
5	  const parseQuery = new Parse.Query(Parse.User);
6	  // Several query functions can be set to your Parse,Query, they will
7	  // only resolve when calling "find", for example
8	  if (usernameSearchValue !== '') {
9	    // "contains" will retrieve users whose username contain the searched value, case-sensitive
10	    parseQuery.contains('username', usernameSearchValue);
11	    // 
12	    // or 
13	    // 
14	    // for case-insensitive string search, use "matches", that will take into account
15	    // an regexp for matching, in this case use only "i", which is the regexp modifier
16	    // for case-insensitive
17	    parseQuery.matches('username', usernameSearchValue, 'i');
18	  }
19	  // Only after calling "find" all query conditions will resolve
20	  return await parseQuery
21	    .find()
22	    .then(async (queriedUsers => {
23	      // Set the query results to an state variable to retrieve it on your JSX
24	      // Be aware that empty or invalid queries return as an empty array
25	      setQueryResults(queriedUsers);
26	      return true;
27	    })
28	    .catch((error) => {
29	      // Error can be caused by lack of Internet connection, but in most
30	      // cases "find" will return as an empty array on "then"
31	      Alert.alert('Error!', error.message);
32	      setQueryResults([]);
33	      return false;
34	    });
35	};
```

```typescript
1	const doUserQuery = async function (): Promise<Boolean> {
2	  // This value comes from a state variable
3	  const usernameSearchValue: string = usernameSearch;
4	  // This will create your user query
5	  const parseQuery: Parse.Query = new Parse.Query(Parse.User);
6	  // Several query functions can be set to your Parse,Query, they will
7	  // only resolve when calling "find", for example
8	  if (usernameSearchValue !== '') {
9	    // "contains" will retrieve users whose username contain the searched value, case-sensitive
10	    parseQuery.contains('username', usernameSearchValue);
11	    // 
12	    // or 
13	    // 
14	    // for case-insensitive string search, use "matches", that will take into account
15	    // an regexp for matching, in this case use only "i", which is the regexp modifier
16	    // for case-insensitive
17	    parseQuery.matches('username', usernameSearchValue, 'i');
18	  }
19	  // Only after calling "find" all query conditions will resolve
20	  return await parseQuery
21	    .find()
22	    .then(async (queriedUsers: [Parse.User]) => {
23	      // Set the query results to an state variable to retrieve it on your JSX
24	      // Be aware that empty or invalid queries return as an empty array
25	      setQueryResults(queriedUsers);
26	      return true;
27	    })
28	    .catch((error: object) => {
29	      // Error can be caused by lack of Internet connection, but in most
30	      // cases "find" will return as an empty array on "then"
31	      Alert.alert('Error!', error.message);
32	      setQueryResults([]);
33	      return false;
34	    });
35	};
```
:::

Note that that are at least two different ways to search for a string, each one having its specific applications and advantages. In most cases, you will want to use Parse.Query.matches to ensure case-insensitive results and avoid unexpected behavior in your code.

After performing this query, your user list on your app should be showing something like this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/4vywdrYv0rn3auip-iLeS_image.png" signedSrc size="50" width="349" height="726" position="center" caption}

In addition to string querying, you can also perform “exact” queries, when you want to retrieve objects that contain an exact value, just as with boolean fields. The next example will show how to retrieve users that are verified by email, through the emailVerified field.

:::CodeblockTabs
JavaScript

```javascript
1	const doUserQuery = async function () {
2	  // This value comes from a state variable
3	  const showOnlyVerifiedValue: boolean = showOnlyVerified;
4	  // This will create your user query
5	  const parseQuery = new Parse.Query(Parse.User);
6	  // Several query functions can be set to your Parse,Query, they will
7	  // only resolve when calling "find", for example
8	  if (showOnlyVerifiedValue === true) {
9	    // "equalTo" will retrieve users whose "emailVerified" value is exactly "true"
10	    parseQuery.equalTo('emailVerified', true);
11	  }
12	  // Only after calling "find" all query conditions will resolve
13	  return await parseQuery
14	    .find()
15	    .then(async (queriedUsers) => {
16	      // Set the query results to an state variable to retrieve it on your JSX
17	      // Be aware that empty or invalid queries return as an empty array
18	      setQueryResults(queriedUsers);
19	      return true;
20	    })
21	    .catch((error) => {
22	      // Error can be caused by lack of Internet connection, but in most
23	      // cases "find" will return as an empty array on "then"
24	      Alert.alert('Error!', error.message);
25	      setQueryResults([]);
26	      return false;
27	    });
28	};
```

```typescript
1	const doUserQuery = async function (): Promise<Boolean> {
2	  // This value comes from a state variable
3	  const showOnlyVerifiedValue: boolean = showOnlyVerified;
4	  // This will create your user query
5	  const parseQuery: Parse.Query = new Parse.Query(Parse.User);
6	  // Several query functions can be set to your Parse,Query, they will
7	  // only resolve when calling "find", for example
8	  if (showOnlyVerifiedValue === true) {
9	    // "equalTo" will retrieve users whose "emailVerified" value is exactly "true"
10	    parseQuery.equalTo('emailVerified', true);
11	  }
12	  // Only after calling "find" all query conditions will resolve
13	  return await parseQuery
14	    .find()
15	    .then(async (queriedUsers: [Parse.User]) => {
16	      // Set the query results to an state variable to retrieve it on your JSX
17	      // Be aware that empty or invalid queries return as an empty array
18	      setQueryResults(queriedUsers);
19	      return true;
20	    })
21	    .catch((error: object) => {
22	      // Error can be caused by lack of Internet connection, but in most
23	      // cases "find" will return as an empty array on "then"
24	      Alert.alert('Error!', error.message);
25	      setQueryResults([]);
26	      return false;
27	    });
28	};
```
:::

Your app should now be updating your user list like this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/7NvaTct3a8HdR40C1Urec_image.png" signedSrc size="50" width="353" height="731" position="center" caption}

Another common example would be to apply orderings to your query. This can be done in two ways, either by using Parse.Query.ascending/Parse.Query.descending or Parse.Query.addAscending/Parse.Query.addDescending. The first case will override any other ordering and will be the only one that the query will take and the latter will concatenate with existing orderings, making multiple orderings possible.

:::CodeblockTabs
JavaScript

```javascript
1	const doUserQuery = async function () {
2	  // This value comes from a state variable
3	  const orderByValue = orderBy;
4	  // This will create your user query
5	  const parseQuery = new Parse.Query(Parse.User);
6	  // Several query functions can be set to your Parse,Query, they will
7	  // only resolve when calling "find", for example
8	  // For list ordering, you can use "addAscending" or "addDescending", passing as parameter
9	  // which object field should be the one to order by
10	  // Note that "usernameAsc", "usernameDesc" and so on are made up string values applied to a filter in
11	  // our example app, so change it by what is suitable to you
12	  if (orderByValue === 'usernameAsc') {
13	    parseQuery.ascending('username');
14	    //
15	    // or
16	    //
17	    parseQuery.addAscending('username');
18	  } else if (orderByValue === 'usernameDesc') {
19	    parseQuery.descending('username');
20	    //
21	    // or
22	    //
23	    parseQuery.addDescending('username');
24	  } else if (orderByValue === 'dateAsc') {
25	    parseQuery.ascending('createdAt');
26	    //
27	    // or
28	    //
29	    parseQuery.addAscending('createdAt');
30	  } else if (orderByValue === 'dateDesc') {
31	    parseQuery.descending('createdAt');
32	    //
33	    // or
34	    //
35	    parseQuery.addDescending('createdAt');
36	  }
37	  // Only after calling "find" all query conditions will resolve
38	  return await parseQuery
39	    .find()
40	    .then(async (queriedUsers) => {
41	      // Set the query results to an state variable to retrieve it on your JSX
42	      // Be aware that empty or invalid queries return as an empty array
43	      setQueryResults(queriedUsers);
44	      return true;
45	    })
46	    .catch((error) => {
47	      // Error can be caused by lack of Internet connection, but in most
48	      // cases "find" will return as an empty array on "then"
49	      Alert.alert('Error!', error.message);
50	      setQueryResults([]);
51	      return false;
52	    });
53	};
```

```typescript
1	const doUserQuery = async function (): Promise<Boolean> {
2	  // This value comes from a state variable
3	  const orderByValue: string = orderBy;
4	  // This will create your user query
5	  const parseQuery: Parse.Query = new Parse.Query(Parse.User);
6	  // Several query functions can be set to your Parse,Query, they will
7	  // only resolve when calling "find", for example
8	  // For list ordering, you can use "addAscending" or "addDescending", passing as parameter
9	  // which object field should be the one to order by
10	  // Note that "usernameAsc", "usernameDesc" and so on are made up string values applied to a filter in
11	  // our example app, so change it by what is suitable to you
12	  if (orderByValue === 'usernameAsc') {
13	    parseQuery.ascending('username');
14	    //
15	    // or
16	    //
17	    parseQuery.addAscending('username');
18	  } else if (orderByValue === 'usernameDesc') {
19	    parseQuery.descending('username');
20	    //
21	    // or
22	    //
23	    parseQuery.addDescending('username');
24	  } else if (orderByValue === 'dateAsc') {
25	    parseQuery.ascending('createdAt');
26	    //
27	    // or
28	    //
29	    parseQuery.addAscending('createdAt');
30	  } else if (orderByValue === 'dateDesc') {
31	    parseQuery.descending('createdAt');
32	    //
33	    // or
34	    //
35	    parseQuery.addDescending('createdAt');
36	  }
37	  // Only after calling "find" all query conditions will resolve
38	  return await parseQuery
39	    .find()
40	    .then(async (queriedUsers: [Parse.User]) => {
41	      // Set the query results to an state variable to retrieve it on your JSX
42	      // Be aware that empty or invalid queries return as an empty array
43	      setQueryResults(queriedUsers);
44	      return true;
45	    })
46	    .catch((error: object) => {
47	      // Error can be caused by lack of Internet connection, but in most
48	      // cases "find" will return as an empty array on "then"
49	      Alert.alert('Error!', error.message);
50	      setQueryResults([]);
51	      return false;
52	    });
53	};
```
:::

Your app must now be ordering your queries like this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/einf4n5_dzjeGfLJC65vj_image.png" signedSrc size="50" width="358" height="735" position="center" caption}

Remember that all of the query constraints mentioned above can be chained and performed in a single query, improving your app usability for creating different filters and orderings that will work altogether. Here is the full code presenting all the query methods used in this guide:

:::CodeblockTabs
JavaScript

```javascript
1	const doUserQuery = async function () {
2	  // This value comes from a state variable
3	  const usernameSearchValue = usernameSearch;
4	  const showOnlyVerifiedValue = showOnlyVerified;
5	  const orderByValue = orderBy;
6	  // This will create your user query
7	  const parseQuery = new Parse.Query(Parse.User);
8	  // Several query functions can be set to your Parse,Query, they will
9	  // only resolve when calling "find", for example
10	  if (usernameSearchValue !== '') {
11	    // "contains" will retrieve users whose username contain the searched value, case-sensitive
12	    parseQuery.contains('username', usernameSearchValue);
13	    //
14	    // or
15	    //
16	    // for case-insensitive string search, use "matches", that will take into account
17	    // an regexp for matching, in this case use only "i", which is the regexp modifier
18	    // for case-insensitive
19	    parseQuery.matches('username', usernameSearchValue, 'i');
20	  }
21	  if (showOnlyVerifiedValue === true) {
22	    // "equalTo" will retrieve users whose "emailVerified" value is exactly "true"
23	    parseQuery.equalTo('emailVerified', true);
24	  }
25	  // For list ordering, you can use "addAscending" or "addDescending", passing as parameter
26	  // which object field should be the one to order by
27	  if (orderByValue === 'usernameAsc') {
28	    parseQuery.ascending('username');
29	    //
30	    // or
31	    //
32	    parseQuery.addAscending('username');
33	  } else if (orderByValue === 'usernameDesc') {
34	    parseQuery.descending('username');
35	    //
36	    // or
37	    //
38	    parseQuery.addDescending('username');
39	  } else if (orderByValue === 'dateAsc') {
40	    parseQuery.ascending('createdAt');
41	    //
42	    // or
43	    //
44	    parseQuery.addAscending('createdAt');
45	  } else if (orderByValue === 'dateDesc') {
46	    parseQuery.descending('createdAt');
47	    //
48	    // or
49	    //
50	    parseQuery.addDescending('createdAt');
51	  }
52	  // Only after calling "find" all query conditions will resolve
53	  return await parseQuery
54	    .find()
55	    .then(async (queriedUsers) => {
56	      // Set the query results to an state variable to retrieve it on your JSX
57	      // Be aware that empty or invalid queries return as an empty array
58	      setQueryResults(queriedUsers);
59	      return true;
60	    })
61	    .catch((error) => {
62	      // Error can be caused by lack of Internet connection, but in most
63	      // cases "find" will return as an empty array on "then"
64	      Alert.alert('Error!', error.message);
65	      setQueryResults([]);
66	      return false;
67	    });
68	};
```

```typescript
1	const doUserQuery = async function (): Promise<Boolean> {
2	  // This value comes from a state variable
3	  const usernameSearchValue: string = usernameSearch;
4	  const showOnlyVerifiedValue: boolean = showOnlyVerified;
5	  const orderByValue: string = orderBy;
6	  // This will create your user query
7	  const parseQuery: Parse.Query = new Parse.Query(Parse.User);
8	  // Several query functions can be set to your Parse,Query, they will
9	  // only resolve when calling "find", for example
10	  if (usernameSearchValue !== '') {
11	    // "contains" will retrieve users whose username contain the searched value, case-sensitive
12	    parseQuery.contains('username', usernameSearchValue);
13	    //
14	    // or
15	    //
16	    // for case-insensitive string search, use "matches", that will take into account
17	    // an regexp for matching, in this case use only "i", which is the regexp modifier
18	    // for case-insensitive
19	    parseQuery.matches('username', usernameSearchValue, 'i');
20	  }
21	  if (showOnlyVerifiedValue === true) {
22	    // "equalTo" will retrieve users whose "emailVerified" value is exactly "true"
23	    parseQuery.equalTo('emailVerified', true);
24	  }
25	  // For list ordering, you can use "addAscending" or "addDescending", passing as parameter
26	  // which object field should be the one to order by
27	  if (orderByValue === 'usernameAsc') {
28	    parseQuery.ascending('username');
29	    //
30	    // or
31	    //
32	    parseQuery.addAscending('username');
33	  } else if (orderByValue === 'usernameDesc') {
34	    parseQuery.descending('username');
35	    //
36	    // or
37	    //
38	    parseQuery.addDescending('username');
39	  } else if (orderByValue === 'dateAsc') {
40	    parseQuery.ascending('createdAt');
41	    //
42	    // or
43	    //
44	    parseQuery.addAscending('createdAt');
45	  } else if (orderByValue === 'dateDesc') {
46	    parseQuery.descending('createdAt');
47	    //
48	    // or
49	    //
50	    parseQuery.addDescending('createdAt');
51	  }
52	  // Only after calling "find" all query conditions will resolve
53	  return await parseQuery
54	    .find()
55	    .then(async (queriedUsers: [Parse.User]) => {
56	      // Set the query results to an state variable to retrieve it on your JSX
57	      // Be aware that empty or invalid queries return as an empty array
58	      setQueryResults(queriedUsers);
59	      return true;
60	    })
61	    .catch((error: object) => {
62	      // Error can be caused by lack of Internet connection, but in most
63	      // cases "find" will return as an empty array on "then"
64	      Alert.alert('Error!', error.message);
65	      setQueryResults([]);
66	      return false;
67	    });
68	};
```
:::

## Conclusion

At the end of this guide, you learned how to perform queries on Parse users on React Native. In the next guide, we will show you how to save and read data on Parse.
