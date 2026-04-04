# Source: https://docs-containers.back4app.com/docs/react-native/parse-sdk/data-objects/react-native-query.md

---
title: Basic Queries
slug: docs/react-native/parse-sdk/data-objects/react-native-query
description: In this guide, you'll learn how to perform basic data querying in Parse on a React Native application
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-19T12:08:37.341Z
updatedAt: 2025-01-28T13:50:36.508Z
---

# Query in React Native using Parse

## Introduction

In this guide, you will perform basic queries in Parse and implement a React Native component using these queries. You will learn how to set up and query realistic data using Back4App and React Native.

::embed[]{url="https://www.youtube.com/embed/IeQievfY-tM"}

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- A React Native App created and connected to [**Back4App**](https://www.back4app.com/docs/react-native/parse-sdk/react-native-sdk).
- If you want to test/use the screen layout provided by this guide, you should set up thereact-native-paper[**library**](https://github.com/callstack/react-native-paper).
:::

## Goal

Query data stored on Back4App from a React Native App.

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

Let’s create a Profile class, which will be the target of our queries in this guide. On Parse JS Console is possible to run JavaScript code directly, querying and updating your application database contents using the JS SDK commands. Run the code below from your JS Console and insert the data on Back4App.

Here is how the JS Console looks like in your dashboard:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/HRUb7bqUJv_QzXE2pjd4v_image.png)

Go ahead and create the user Profile class with the following example content:

```javascript
1	// Add Profile objects and create table
2	// Adam Sandler
3	let Profile = new Parse.Object('Profile');
4	Profile.set('name', 'Adam Sandler');
5	Profile.set('birthDay', new Date('09/09/1966'));
6	Profile.set('friendCount', 2);
7	Profile.set('favoriteFoods', ['Lobster', 'Bread']);
8	await Profile.save();
9	
10	// Adam Levine
11	Profile = new Parse.Object('Profile');
12	Profile.set('name', 'Adam Levine');
13	Profile.set('birthDay', new Date('03/18/1979'));
14	Profile.set('friendCount', 52);
15	Profile.set('favoriteFoods', ['Cake', 'Bread']);
16	await Profile.save();
17	
18	// Carson Kressley
19	Profile = new Parse.Object('Profile');
20	Profile.set('name', 'Carson Kressley');
21	Profile.set('birthDay', new Date('11/11/1969'));
22	Profile.set('friendCount', 12);
23	Profile.set('favoriteFoods', ['Fish', 'Cookies']);
24	await Profile.save();
25	
26	// Dan Aykroyd
27	Profile = new Parse.Object('Profile');
28	Profile.set('name', 'Dan Aykroyd');
29	Profile.set('birthDay', new Date('07/01/1952'));
30	Profile.set('friendCount', 66);
31	Profile.set('favoriteFoods', ['Jam', 'Peanut Butter']);
32	await Profile.save();
33	
34	// Eddie Murphy
35	Profile = new Parse.Object('Profile');
36	Profile.set('name', 'Eddie Murphy');
37	Profile.set('birthDay', new Date('04/03/1961'));
38	Profile.set('friendCount', 49);
39	Profile.set('favoriteFoods', ['Lettuce', 'Pepper']);
40	await Profile.save();
41	
42	// Fergie
43	Profile = new Parse.Object('Profile');
44	Profile.set('name', 'Fergie');
45	Profile.set('birthDay', new Date('03/27/1975'));
46	Profile.set('friendCount', 55);
47	Profile.set('favoriteFoods', ['Lobster', 'Shrimp']);
48	await Profile.save();
49	
50	console.log('Success!');
```

## 3 - Query the data

Now that you have a populated class, we can now perform some basic queries in it. Let’s begin by filtering Profile results by name, which is a string type field, searching for values that contain the name Adam using the Parse.Query.contains method:

```javascript
1	// Create your query
2	let parseQuery = new Parse.Query('Profile');
3	
4	// `contains` is a basic query method that checks if string field
5	// contains a specific substring
6	parseQuery.contains('name', 'Adam');
7	
8	// The query will resolve only after calling this method, retrieving
9	// an array of `Parse.Objects`
10	let queryResults = await parseQuery.find();
11	
12	// Let's show the results
13	for (let result of queryResults) {
14	  // You access `Parse.Objects` attributes by using `.get`
15	  console.log(result.get('name'));
16	};
```

Let’s now query by the number type field friendCount by using another common query method, Parse.Query.greaterThan. In this case, we want user Profiles in which the friend count is greater than 20.

```javascript
1	// Create your query
2	let parseQuery = new Parse.Query('Profile');
3	
4	// `greaterThan` is a basic query method that does what it
5	// says on the tin
6	parseQuery.greaterThan('friendCount', 20);
7	
8	// The query will resolve only after calling this method, retrieving
9	// an array of `Parse.Objects`
10	let queryResults = await parseQuery.find();
11	
12	// Let's show the results
13	for (let result of queryResults) {
14	  // You access `Parse.Objects` attributes by using `.get`
15	  console.log(`name: ${result.get('name')}, friend count: ${result.get('friendCount')}`);
16	};
```

Other recurring query methods are Parse.Query.ascending and Parse.Query.descending, responsible for ordering your queries. This ordering can be done in most data types, so let’s order a query by the date field birthDay by the youngest.

```javascript
1	// Create your query
2	let parseQuery = new Parse.Query('Profile');
3	
4	// `descending` and `ascending` can and should be chained
5	// with other query methods to improve your queries
6	parseQuery.descending('birthDay');
7	
8	// The query will resolve only after calling this method, retrieving
9	// an array of `Parse.Objects`
10	let queryResults = await parseQuery.find();
11	
12	// Let's show the results
13	for (let result of queryResults) {
14	  // You access `Parse.Objects` attributes by using `.get`
15	  console.log(`name: ${result.get('name')}, birthday: ${result.get('birthDay')}`);
16	};
```

As stated here before, you can and should chain query methods to achieve more refined results. Let’s then combine the previous examples in a single query request:

```javascript
1	// Create your query
2	let parseQuery = new Parse.Query('Profile');
3	
4	parseQuery.contains('name', 'Adam');
5	parseQuery.greaterThan('friendCount', 20);
6	parseQuery.descending('birthDay');
7	
8	// The query will resolve only after calling this method, retrieving
9	// an array of `Parse.Objects`
10	let queryResults = await parseQuery.find();
11	
12	// Let's show the results
13	for (let result of queryResults) {
14	  // You access `Parse.Objects` attributes by using `.get`
15	  console.log(`name: ${result.get('name')}, friend count: ${result.get('friendCount')}, birthday: ${result.get('birthDay')}`);
16	};
```

## 4 - Query from a React Native component

Let’s now use our example queries inside a component in React Native, with a simple interface having a list showing results and also 4 buttons for calling the queries. This is how the component code is laid out, note the doQuery functions, containing the example code form before.

:::CodeblockTabs
JavaScript

```javascript
1	import React, {useState} from 'react';
2	import {Alert, Image, View, ScrollView, StyleSheet} from 'react-native';
3	import Parse from 'parse/react-native';
4	import {
5	  List,
6	  Title,
7	  Button as PaperButton,
8	  Text as PaperText,
9	} from 'react-native-paper';
10	
11	export const BookList = () => {
12	  // State variable
13	  const [queryResults, setQueryResults] = useState(null);
14	
15	  const doQueryByName = async function () {
16	    // Create our Parse.Query instance so methods can be chained
17	    // Reading parse objects is done by using Parse.Query
18	    const parseQuery = new Parse.Query('Profile');
19	
20	    // `contains` is a basic query method that checks if string field
21	    // contains a specific substring
22	    parseQuery.contains('name', 'Adam');
23	
24	    try {
25	      let profiles = await parseQuery.find();
26	      setQueryResults(profiles);
27	      return true;
28	    } catch (error) {
29	      // Error can be caused by lack of Internet connection
30	      Alert.alert('Error!', error.message);
31	      return false;
32	    }
33	  };
34	
35	  const doQueryByFriendCount = async function () {
36	    // Create our Parse.Query instance so methods can be chained
37	    // Reading parse objects is done by using Parse.Query
38	    const parseQuery = new Parse.Query('Profile');
39	
40	    // `greaterThan` is a basic query method that does what it
41	    // says on the tin
42	    parseQuery.greaterThan('friendCount', 20);
43	
44	    try {
45	      let profiles = await parseQuery.find();
46	      setQueryResults(profiles);
47	      return true;
48	    } catch (error) {
49	      // Error can be caused by lack of Internet connection
50	      Alert.alert('Error!', error.message);
51	      return false;
52	    }
53	  };
54	
55	  const doQueryByOrdering = async function () {
56	    // Create our Parse.Query instance so methods can be chained
57	    // Reading parse objects is done by using Parse.Query
58	    const parseQuery = new Parse.Query('Profile');
59	
60	    // `descending` and `ascending` can and should be chained
61	    // with other query methods to improve your queries
62	    parseQuery.descending('birthDay');
63	
64	    try {
65	      let profiles = await parseQuery.find();
66	      setQueryResults(profiles);
67	      return true;
68	    } catch (error) {
69	      // Error can be caused by lack of Internet connection
70	      Alert.alert('Error!', error.message);
71	      return false;
72	    }
73	  };
74	
75	  const doQueryByAll = async function () {
76	    // Create our Parse.Query instance so methods can be chained
77	    // Reading parse objects is done by using Parse.Query
78	    const parseQuery = new Parse.Query('Profile');
79	
80	    parseQuery.contains('name', 'Adam');
81	    parseQuery.greaterThan('friendCount', 20);
82	    parseQuery.descending('birthDay');
83	
84	    try {
85	      let profiles = await parseQuery.find();
86	      setQueryResults(profiles);
87	      return true;
88	    } catch (error) {
89	      // Error can be caused by lack of Internet connection
90	      Alert.alert('Error!', error.message);
91	      return false;
92	    }
93	  };
94	
95	  const clearQueryResults = async function () {
96	    setQueryResults(null);
97	    return true;
98	  };
99	
100	  return (
101	    <>
102	      <View style={Styles.header}>
103	        <Image
104	          style={Styles.header_logo}
105	          source={ {
106	            uri:
107	              'https://blog.back4app.com/wp-content/uploads/2019/05/back4app-white-logo-500px.png',
108	          } }
109	        />
110	        <PaperText style={Styles.header_text}>
111	          <PaperText style={Styles.header_text_bold}>
112	            {'React Native on Back4App - '}
113	          </PaperText>
114	          {' Basic Queries'}
115	        </PaperText>
116	      </View>
117	      <ScrollView style={Styles.wrapper}>
118	        <View>
119	          <Title>{'Result List'}</Title>
120	          {/* Book list */}
121	          {queryResults !== null &&
122	            queryResults !== undefined &&
123	            queryResults.map((profile) => (
124	              <List.Item
125	                key={profile.id}
126	                title={profile.get('name')}
127	                description={`Friend count: ${profile.get(
128	                  'friendCount',
129	                )}, Birthday: ${profile.get('birthDay')}`}
130	                titleStyle={Styles.list_text}
131	                style={Styles.list_item}
132	              />
133	            ))}
134	          {queryResults === null ||
135	          queryResults === undefined ||
136	          (queryResults !== null &&
137	            queryResults !== undefined &&
138	            queryResults.length <= 0) ? (
139	            <PaperText>{'No results here!'}</PaperText>
140	          ) : null}
141	        </View>
142	        <View>
143	          <Title>{'Query buttons'}</Title>
144	          <PaperButton
145	            onPress={() => doQueryByName()}
146	            mode="contained"
147	            icon="search-web"
148	            color={'#208AEC'}
149	            style={Styles.list_button}>
150	            {'Query by name'}
151	          </PaperButton>
152	          <PaperButton
153	            onPress={() => doQueryByFriendCount()}
154	            mode="contained"
155	            icon="search-web"
156	            color={'#208AEC'}
157	            style={Styles.list_button}>
158	            {'Query by friend count'}
159	          </PaperButton>
160	          <PaperButton
161	            onPress={() => doQueryByOrdering()}
162	            mode="contained"
163	            icon="search-web"
164	            color={'#208AEC'}
165	            style={Styles.list_button}>
166	            {'Query by ordering'}
167	          </PaperButton>
168	          <PaperButton
169	            onPress={() => doQueryByAll()}
170	            mode="contained"
171	            icon="search-web"
172	            color={'#208AEC'}
173	            style={Styles.list_button}>
174	            {'Query by all'}
175	          </PaperButton>
176	          <PaperButton
177	            onPress={() => clearQueryResults()}
178	            mode="contained"
179	            icon="delete"
180	            color={'#208AEC'}
181	            style={Styles.list_button}>
182	            {'Clear Results'}
183	          </PaperButton>
184	        </View>
185	      </ScrollView>
186	    </>
187	  );
188	};
189	
190	// These define the screen component styles
191	const Styles = StyleSheet.create({
192	  header: {
193	    alignItems: 'center',
194	    paddingTop: 30,
195	    paddingBottom: 50,
196	    backgroundColor: '#208AEC',
197	  },
198	  header_logo: {
199	    height: 50,
200	    width: 220,
201	    resizeMode: 'contain',
202	  },
203	  header_text: {
204	    marginTop: 15,
205	    color: '#f0f0f0',
206	    fontSize: 16,
207	  },
208	  header_text_bold: {
209	    color: '#fff',
210	    fontWeight: 'bold',
211	  },
212	  wrapper: {
213	    width: '90%',
214	    alignSelf: 'center',
215	  },
216	  list_button: {
217	    marginTop: 6,
218	    marginLeft: 15,
219	    height: 40,
220	  },
221	  list_item: {
222	    borderBottomWidth: 1,
223	    borderBottomColor: 'rgba(0, 0, 0, 0.12)',
224	  },
225	  list_text: {
226	    fontSize: 15,
227	  },
228	});
```

```typescript
1	import React, {FC, ReactElement, useState} from 'react';
2	import {Alert, Image, View, ScrollView, StyleSheet} from 'react-native';
3	import Parse from 'parse/react-native';
4	import {
5	  List,
6	  Title,
7	  Button as PaperButton,
8	  Text as PaperText,
9	} from 'react-native-paper';
10	
11	export const QueryList: FC<{}> = ({}): ReactElement => {
12	  // State variable
13	  const [queryResults, setQueryResults] = useState(null);
14	
15	  const doQueryByName = async function (): Promise<boolean> {
16	    // Create our Parse.Query instance so methods can be chained
17	    // Reading parse objects is done by using Parse.Query
18	    const parseQuery: Parse.Query = new Parse.Query('Profile');
19	
20	    // `contains` is a basic query method that checks if string field
21	    // contains a specific substring
22	    parseQuery.contains('name', 'Adam');
23	
24	    try {
25	      let profiles: [Parse.Object] = await parseQuery.find();
26	      setQueryResults(profiles);
27	      return true;
28	    } catch (error) {
29	      // Error can be caused by lack of Internet connection
30	      Alert.alert('Error!', error.message);
31	      return false;
32	    }
33	  };
34	
35	  const doQueryByFriendCount = async function (): Promise<boolean> {
36	    // Create our Parse.Query instance so methods can be chained
37	    // Reading parse objects is done by using Parse.Query
38	    const parseQuery: Parse.Query = new Parse.Query('Profile');
39	
40	    // `greaterThan` is a basic query method that does what it
41	    // says on the tin
42	    parseQuery.greaterThan('friendCount', 20);
43	
44	    try {
45	      let profiles: [Parse.Object] = await parseQuery.find();
46	      setQueryResults(profiles);
47	      return true;
48	    } catch (error) {
49	      // Error can be caused by lack of Internet connection
50	      Alert.alert('Error!', error.message);
51	      return false;
52	    }
53	  };
54	
55	  const doQueryByOrdering = async function (): Promise<boolean> {
56	    // Create our Parse.Query instance so methods can be chained
57	    // Reading parse objects is done by using Parse.Query
58	    const parseQuery: Parse.Query = new Parse.Query('Profile');
59	
60	    // `descending` and `ascending` can and should be chained
61	    // with other query methods to improve your queries
62	    parseQuery.descending('birthDay');
63	
64	    try {
65	      let profiles: [Parse.Object] = await parseQuery.find();
66	      setQueryResults(profiles);
67	      return true;
68	    } catch (error) {
69	      // Error can be caused by lack of Internet connection
70	      Alert.alert('Error!', error.message);
71	      return false;
72	    }
73	  };
74	
75	  const doQueryByAll = async function (): Promise<boolean> {
76	    // Create our Parse.Query instance so methods can be chained
77	    // Reading parse objects is done by using Parse.Query
78	    const parseQuery: Parse.Query = new Parse.Query('Profile');
79	
80	    parseQuery.contains('name', 'Adam');
81	    parseQuery.greaterThan('friendCount', 20);
82	    parseQuery.descending('birthDay');
83	
84	    try {
85	      let profiles: [Parse.Object] = await parseQuery.find();
86	      setQueryResults(profiles);
87	      return true;
88	    } catch (error) {
89	      // Error can be caused by lack of Internet connection
90	      Alert.alert('Error!', error.message);
91	      return false;
92	    }
93	  };
94	
95	  const clearQueryResults = async function (): Promise<boolean> {
96	    setQueryResults(null);
97	    return true;
98	  };
99	
100	  return (
101	    <>
102	      <View style={Styles.header}>
103	        <Image
104	          style={Styles.header_logo}
105	          source={ {
106	            uri:
107	              'https://blog.back4app.com/wp-content/uploads/2019/05/back4app-white-logo-500px.png',
108	          } }
109	        />
110	        <PaperText style={Styles.header_text}>
111	          <PaperText style={Styles.header_text_bold}>
112	            {'React Native on Back4App - '}
113	          </PaperText>
114	          {' Basic Queries'}
115	        </PaperText>
116	      </View>
117	      <ScrollView style={Styles.wrapper}>
118	        <View>
119	          <Title>{'Result List'}</Title>
120	          {/* Book list */}
121	          {queryResults !== null &&
122	            queryResults !== undefined &&
123	            queryResults.map((profile: Parse.Object) => (
124	              <List.Item
125	                key={profile.id}
126	                title={profile.get('name')}
127	                description={`Friend count: ${profile.get(
128	                  'friendCount',
129	                )}, Birthday: ${profile.get('birthDay')}`}
130	                titleStyle={Styles.list_text}
131	                style={Styles.list_item}
132	              />
133	            ))}
134	          {queryResults === null ||
135	          queryResults === undefined ||
136	          (queryResults !== null &&
137	            queryResults !== undefined &&
138	            queryResults.length <= 0) ? (
139	            <PaperText>{'No results here!'}</PaperText>
140	          ) : null}
141	        </View>
142	        <View>
143	          <Title>{'Query buttons'}</Title>
144	          <PaperButton
145	            onPress={() => doQueryByName()}
146	            mode="contained"
147	            icon="search-web"
148	            color={'#208AEC'}
149	            style={Styles.list_button}>
150	            {'Query by name'}
151	          </PaperButton>
152	          <PaperButton
153	            onPress={() => doQueryByFriendCount()}
154	            mode="contained"
155	            icon="search-web"
156	            color={'#208AEC'}
157	            style={Styles.list_button}>
158	            {'Query by friend count'}
159	          </PaperButton>
160	          <PaperButton
161	            onPress={() => doQueryByOrdering()}
162	            mode="contained"
163	            icon="search-web"
164	            color={'#208AEC'}
165	            style={Styles.list_button}>
166	            {'Query by ordering'}
167	          </PaperButton>
168	          <PaperButton
169	            onPress={() => doQueryByAll()}
170	            mode="contained"
171	            icon="search-web"
172	            color={'#208AEC'}
173	            style={Styles.list_button}>
174	            {'Query by all'}
175	          </PaperButton>
176	          <PaperButton
177	            onPress={() => clearQueryResults()}
178	            mode="contained"
179	            icon="delete"
180	            color={'#208AEC'}
181	            style={Styles.list_button}>
182	            {'Clear Results'}
183	          </PaperButton>
184	        </View>
185	      </ScrollView>
186	    </>
187	  );
188	};
189	
190	// These define the screen component styles
191	const Styles = StyleSheet.create({
192	  header: {
193	    alignItems: 'center',
194	    paddingTop: 30,
195	    paddingBottom: 50,
196	    backgroundColor: '#208AEC',
197	  },
198	  header_logo: {
199	    height: 50,
200	    width: 220,
201	    resizeMode: 'contain',
202	  },
203	  header_text: {
204	    marginTop: 15,
205	    color: '#f0f0f0',
206	    fontSize: 16,
207	  },
208	  header_text_bold: {
209	    color: '#fff',
210	    fontWeight: 'bold',
211	  },
212	  wrapper: {
213	    width: '90%',
214	    alignSelf: 'center',
215	  },
216	  list_button: {
217	    marginTop: 6,
218	    marginLeft: 15,
219	    height: 40,
220	  },
221	  list_item: {
222	    borderBottomWidth: 1,
223	    borderBottomColor: 'rgba(0, 0, 0, 0.12)',
224	  },
225	  list_text: {
226	    fontSize: 15,
227	  },
228	});
```
:::

This is how the component should look like after rendering and querying by all the query functions:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Xrlx6Jf234xT-UHjkVBLs_image.png" signedSrc size="50" width="348" height="734" position="center" caption}

## Conclusion

At the end of this guide, you learned how basic data queries work on Parse and how to perform them on Back4App from a React Native App. In the next guide, you will explore the Parse.Query full potential using all the methods available on this class.
