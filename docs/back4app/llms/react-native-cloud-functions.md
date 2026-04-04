# Source: https://docs-containers.back4app.com/docs/react-native/parse-sdk/cloud-functions/react-native-cloud-functions.md

---
title: Triggers
slug: docs/react-native/parse-sdk/cloud-functions/react-native-cloud-functions
description: In this guide, you'll learn how to use Parse cloud code functions on a React Native application
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-19T17:33:30.675Z
updatedAt: 2025-01-17T14:12:48.483Z
---

# Using Cloud Functions in a React Native App

## Introduction

In this guide, you will learn how to use the Parse Cloud Code Functions from a React Native App. You will see examples of triggers implemented using cloud functinos, and also check how to implement a React Native component using these functions and Back4App.

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- A React Native App created and [**connected to Back4App**](https://www.back4app.com/docs/react-native/parse-sdk/react-native-sdk).
- Understand how to [**deploy a cloud function**](https://www.back4app.com/docs/get-started/cloud-functions) on Back4App.
- If you want to run this guide’s example application, you should set up thereact-native-paper[**library**](https://github.com/callstack/react-native-paper).
:::

## Goal

Run Parse Cloud Code on Back4App from a React Native App.

## 1 - Understanding Cloud Code Functions

In your applications, there will be times that you will need to perform certain data operations or heavy processing that shouldn’t be done on mobile devices. For these cases, you may use Cloud Code functions, that run directly on your Parse server and are called using Parse API. Note that this also enables changing some part of your app’s logic without needing to release a new version on the app stores, which can be useful in some cases.

There are two main types of Cloud Code functions, generic functions, using define and holding any type of code you want, and triggers, that are fired when certain events occur in your Parse server automatically.

In the next step, you will be presented with examples for most of these function types, which can be created and deployed directly in your Back4App dashboard or via CLI. You can check how to perform this in [**our Cloud functions starter guide**](https://www.back4app.com/docs/get-started/cloud-functions).

## 2 - Cloud Code Reference

### Cloud Functions

:::CodeblockTabs
Cloud Functions

```javascript
1	// This a generic cloud function that may contain any type of operation,
2	// these should be called via API in your app to be run
3	Parse.Cloud.define("getAverageMovieReviews", async (request) => {
4	  const query = new Parse.Query("Review");
5	  // Parameters can be passed in your request body and are accessed inside request.params
6	  query.equalTo("movie", request.params.movie);
7	  const results = await query.find();
8	  let sum = 0;
9	  for (let review of results) {
10	    sum += review.get("stars");
11	  }
12	  return {
13	    result: sum / results.length,
14	  }
15	});
```
:::

Response:

:::BlockQuote
1   \{ "result": 3.5 }
:::

### Save Triggers

:::CodeblockTabs
beforeSave

```javascript
1	// This will run every time an object of this class will be saved on the server
2	Parse.Cloud.beforeSave("Product", (request) => {
3	  // You can change any data before saving, can be useful for trimming text
4	  // or validating unique fields
5	  const name = request.object.get("description");
6	  if (description.length > 140) {
7	    // Truncate and add a ...
8	    request.object.set("description", comment.substring(0, 137) + "...");
9	  }
10	});
```

afterSave

```javascript
1	// This will always run after saving an object of this class
2	Parse.Cloud.afterSave("Comment", async (request) => {
3	  // You can use this method for changing other classes, like handling
4	  // a Comment counter for a Post
5	  const query = new Parse.Query("Post");
6	  try {
7	    let post = await query.get(request.object.get("post").id);
8	    post.increment("comments");
9	    return post.save();
10	  } catch (error) {
11	    console.error("Got an error " + error.code + " : " + error.message);
12	  }
13	});
```
:::

### Delete Triggers

:::CodeblockTabs
beforeDelete

```javascript
1	// This will be called before deleting an object, useful for checking
2	// for existing dependent conditions
3	Parse.Cloud.beforeDelete("Album", async (request) => {
4	  // This won't proceed deleting if the condition is not met, protection your
5	  // data
6	  const query = new Parse.Query("Photo");
7	  query.equalTo("album", request.object);
8	  const count = await query.count();
9	  if (count > 0) {
10	    throw "Can't delete album if it still has photos.";
11	  }
12	});
```

afterDelete

```javascript
1	// Called after deleting an object, useful for cascade deleting related
2	// objects
3	Parse.Cloud.afterDelete("Post", async (request) => {
4	  // Delete all post Comments after deleting the Post
5	  const query = new Parse.Query("Comment");
6	  query.equalTo("post", request.object);
7	  try {
8	    let results = await query.find();
9	    await Parse.Object.destroyAll(results);
10	  } catch (error) {
11	    console.error("Error finding related comments " + error.code + ": " + error.message);
12	  }
13	});
```
:::

### File Triggers

:::CodeblockTabs
beforeSaveFile

```javascript
1	// Can be called to change any file properties, like renaming it
2	Parse.Cloud.beforeSaveFile(async (request) => {
3	  const { file } = request;
4	  const fileData = await file.getData();
5	  // Note that the new file will be saved instead of the user submitted one
6	  const newFile = new Parse.File('a-new-file-name.txt', { base64: fileData });
7	  return newFile;
8	});
```

afterSaveFile

```javascript
1	// Can be called for managing file metadata and creating
2	// your file referencing object
3	Parse.Cloud.afterSaveFile(async (request) => {
4	  const { file, fileSize, user } = request;
5	  const fileObject = new Parse.Object('FileObject');
6	  fileObject.set('file', file);
7	  fileObject.set('fileSize', fileSize);
8	  fileObject.set('createdBy', user);
9	  const token = { sessionToken: user.getSessionToken() };
10	  await fileObject.save(null, token);
11	});
```

beforeDeleteFile

```javascript
1	// Useful for checking conditions in objects using the file to be deleted
2	Parse.Cloud.beforeDeleteFile(async (request) => {
3	  // Only deletes file if the object storing it was also deleted before
4	  const { file, user } = request;
5	  const query = new Parse.Query('FileObject');
6	  query.equalTo('fileName', file.name());
7	  const fileObjectCount = await query.count({ useMasterKey: true });
8	  if (fileObjectCount > 0) {
9	    throw 'The FileObject should be delete first!';
10	  }
11	});
```

afterDeleteFile

```javascript
1	// Useful for cleaning up objects related to the file
2	Parse.Cloud.afterDeleteFile(async (request) => {
3	  // Note that this example is the opposite of the beforeDeleteFile one,
4	  // this one will clean up FileObjects after deleting the file
5	  const { file } = request;
6	  const query = new Parse.Query('FileObject');
7	  query.equalTo('fileName', file.name());
8	  const fileObject = await query.first({ useMasterKey: true });
9	  await fileObject.destroy({ useMasterKey: true });
10	});
```
:::

### Find Triggers

:::CodeblockTabs
beforeFind

```javascript
1	// This will be called before any queries using this class
2	Parse.Cloud.beforeFind('MyObject', (request) => {
3	  // Useful for hard setting result limits or forcing
4	  // certain conditions
5	  let query = request.query;
6	  query.limit(5);
7	});
```

afterFind

```javascript
1	// This will be called after the query is done in the database
2	Parse.Cloud.afterFind('MyObject', (req) => {
3	  // Can be used in rare cases, like force reversing result ordering
4	  let results = req.objects;
5	  results = results.reverse();
6	  return req.objects;
7	});
```
:::

### Session Triggers

:::CodeblockTabs
beforeLogin

```javascript
1	// Can be used for checking for user permissions and state
2	Parse.Cloud.beforeLogin(async (request) => {
3	  // Doesn't allow banned users to login
4	  const { object: user } = request;
5	  if (user.get('isBanned') === true) {
6	    throw 'Access denied, you have been banned.';
7	  }
8	});
```

afterLogout

```javascript
1	// Can be used for cleaning up user actions after logging out
2	Parse.Cloud.afterLogout(async (request) => {
3	  // Sets custom online flag to false
4	  const { object: session } = request;
5	  const user = session.get('user');
6	  user.set('isOnline', false);
7	  await user.save(null, { useMasterKey: true } );
8	});
```
:::

## 3 - Using Cloud Code from a React Native component

Let’s now create an example Parse Cloud Code function and call it inside a component in React Native, with a simple interface having a label showing the function result and also a form for adding new objects.

Our cloud function will calculate the average of the ratings of every movie Review object in our app, which is a Parse.Object class composed of text, rate and movie fields. Here is the function code:

```javascript
1	Parse.Cloud.define("getMovieAverageRating", async (request) => {
2	  const query = new Parse.Query("Review");
3	  query.equalTo("movie", request.params.movie);
4	  const results = await query.find();
5	  let sum = 0;
6	  for (let review of results) {
7	    sum += review.get("rate");
8	  }
9	  return {
10	    result: sum / results.length,
11	  };
12	});
```

To call this cloud function in React Native, you need to use the Parse.Cloud.run method, passing as an argument the function name and also any necessary parameters inside an object.

:::CodeblockTabs
JavaScript

```javascript
1	const runGetMovieAverageRating = async function () {
2	  try {
3	    const params = {
4	      movie: 'Mission Very Possible',
5	    };
6	    let resultObject = await Parse.Cloud.run(
7	      'getMovieAverageRating',
8	      params,
9	    );
10	    // Set query results to state variable using state hook
11	    setRatingsAverage(resultObject.result.toFixed(1));
12	    return true;
13	  } catch (error) {
14	    // Error can be caused by lack of Internet connection
15	    // or by not having an valid Review object yet
16	    Alert.alert('Error!', error.message);
17	    return false;
18	  }
19	};
```

```typescript
1	const runGetMovieAverageRating = async function (): Promise<boolean> {
2	  try {
3	    const params: {movie: string} = {
4	      movie: 'Mission Very Possible',
5	    };
6	    let resultObject: {result: number} = await Parse.Cloud.run(
7	      'getMovieAverageRating',
8	      params,
9	    );
10	    // Set query results to state variable using state hook
11	    setRatingsAverage(resultObject.result.toFixed(1));
12	    return true;
13	  } catch (error) {
14	    // Error can be caused by lack of Internet connection
15	    // or by not having an valid Review object yet
16	    Alert.alert('Error!', error.message);
17	    return false;
18	  }
19	};
```
:::

We can also enforce that the reviews’ texts are kept short by using a beforeSave trigger function for the Review object. Here is the function code:

:::CodeblockTabs
JavaScript

```javascript
1	Parse.Cloud.beforeSave("Review", (request) => {
2	  const text = request.object.get("text");
3	  if (text.length > 20) {
4	    // Truncate and add a ...
5	    request.object.set("text", text.substring(0, 17) + "...");
6	  }
7	});
```
:::

This is how the full component code is laid out:

:::CodeblockTabs
JavaScript

```javascript
1	import React, {useState} from 'react';
2	import {
3	  Alert,
4	  Image,
5	  View,
6	  Platform,
7	  ScrollView,
8	  StyleSheet,
9	} from 'react-native';
10	import Parse from 'parse/react-native';
11	import {
12	  List,
13	  Title,
14	  TextInput as PaperTextInput,
15	  Button as PaperButton,
16	  Text as PaperText,
17	} from 'react-native-paper';
18	
19	export const MovieRatings = () => {
20	  // State variable
21	  const [queryResults, setQueryResults] = useState(null);
22	  const [ratingsAverage, setRatingsAverage] = useState('');
23	  const [reviewText, setReviewText] = useState('');
24	  const [reviewRate, setReviewRate] = useState('');
25	
26	  const runGetMovieAverageRating = async function () {
27	    try {
28	      const params = {
29	        movie: 'Mission Very Possible',
30	      };
31	      let resultObject = await Parse.Cloud.run(
32	        'getMovieAverageRating',
33	        params,
34	      );
35	      // Set query results to state variable using state hook
36	      setRatingsAverage(resultObject.result.toFixed(1));
37	      return true;
38	    } catch (error) {
39	      // Error can be caused by lack of Internet connection
40	      // or by not having an valid Review object yet
41	      Alert.alert(
42	        'Error!',
43	        'Make sure that the cloud function is deployed and that the Review class table is created',
44	      );
45	      return false;
46	    }
47	  };
48	
49	  const doReviewQuery = async function () {
50	    // Create our query
51	    let parseQuery = new Parse.Query('Review');
52	    try {
53	      let results = await parseQuery.find();
54	      // Set query results to state variable
55	      setQueryResults(results);
56	      return true;
57	    } catch (error) {
58	      // Error can be caused by lack of Internet connection
59	      Alert.alert('Error!', error.message);
60	      return false;
61	    }
62	  };
63	
64	  const createReview = async function () {
65	    try {
66	      // This values come from state variables linked to
67	      // the screen form fields
68	      const reviewTextValue = reviewText;
69	      const reviewRateValue = Number(reviewRate);
70	
71	      // Creates a new parse object instance
72	      let Review = new Parse.Object('Review');
73	
74	      // Set data to parse object
75	      // Simple title field
76	      Review.set('text', reviewTextValue);
77	
78	      // Simple number field
79	      Review.set('rate', reviewRateValue);
80	
81	      // Set default movie
82	      Review.set('movie', 'Mission Very Possible');
83	
84	      // After setting the values, save it on the server
85	      try {
86	        await Review.save();
87	        // Success
88	        Alert.alert('Success!');
89	        // Updates query result list
90	        doReviewQuery();
91	        runGetMovieAverageRating();
92	        return true;
93	      } catch (error) {
94	        // Error can be caused by lack of Internet connection
95	        Alert.alert('Error!', error.message);
96	        return false;
97	      }
98	    } catch (error) {
99	      // Error can be caused by lack of field values
100	      Alert.alert('Error!', error.message);
101	      return false;
102	    }
103	  };
104	
105	  return (
106	    <>
107	      <View style={Styles.header}>
108	        <Image
109	          style={Styles.header_logo}
110	          source={ {
111	            uri:
112	              'https://blog.back4app.com/wp-content/uploads/2019/05/back4app-white-logo-500px.png',
113	          } }
114	        />
115	        <PaperText style={Styles.header_text}>
116	          <PaperText style={Styles.header_text_bold}>
117	            {'React Native on Back4App - '}
118	          </PaperText>
119	          {' Cloud Code Movie Ratings'}
120	        </PaperText>
121	      </View>
122	      <ScrollView style={Styles.wrapper}>
123	        <View>
124	          <Title>{'Mission Very Possible Reviews'}</Title>
125	          <PaperText>{`Ratings Average: ${ratingsAverage}`}</PaperText>
126	          {/* Query list */}
127	          {queryResults !== null &&
128	            queryResults !== undefined &&
129	            queryResults.map((result) => (
130	              <List.Item
131	                key={result.id}
132	                title={`Review text: ${result.get('text')}`}
133	                description={`Rate: ${result.get('rate')}`}
134	                titleStyle={Styles.list_text}
135	                style={Styles.list_item}
136	              />
137	            ))}
138	          {queryResults === null ||
139	          queryResults === undefined ||
140	          (queryResults !== null &&
141	            queryResults !== undefined &&
142	            queryResults.length <= 0) ? (
143	            <PaperText>{'No results here!'}</PaperText>
144	          ) : null}
145	        </View>
146	        <View>
147	          <Title>Action Buttons</Title>
148	          <PaperButton
149	            onPress={() => runGetMovieAverageRating()}
150	            mode="contained"
151	            icon="search-web"
152	            color={'#208AEC'}
153	            style={Styles.list_button}>
154	            {'Calculate Review Average'}
155	          </PaperButton>
156	          <PaperButton
157	            onPress={() => doReviewQuery()}
158	            mode="contained"
159	            icon="search-web"
160	            color={'#208AEC'}
161	            style={Styles.list_button}>
162	            {'Query Reviews'}
163	          </PaperButton>
164	        </View>
165	        <View>
166	          <Title>Add new review</Title>
167	          <PaperTextInput
168	            value={reviewText}
169	            onChangeText={text => setReviewText(text)}
170	            label="Text"
171	            mode="outlined"
172	            style={Styles.form_input}
173	          />
174	          <PaperTextInput
175	            value={reviewRate}
176	            onChangeText={text => setReviewRate(text)}
177	            keyboardType={'number-pad'}
178	            label="Rate (1-5)"
179	            mode="outlined"
180	            style={Styles.form_input}
181	          />
182	          <PaperButton
183	            onPress={() => createReview()}
184	            mode="contained"
185	            icon="plus"
186	            style={Styles.submit_button}>
187	            {'Add'}
188	          </PaperButton>
189	        </View>
190	      </ScrollView>
191	    </>
192	  );
193	};
194	
195	// These define the screen component styles
196	const Styles = StyleSheet.create({
197	  header: {
198	    alignItems: 'center',
199	    paddingTop: 30,
200	    paddingBottom: 50,
201	    backgroundColor: '#208AEC',
202	  },
203	  header_logo: {
204	    height: 50,
205	    width: 220,
206	    resizeMode: 'contain',
207	  },
208	  header_text: {
209	    marginTop: 15,
210	    color: '#f0f0f0',
211	    fontSize: 16,
212	  },
213	  header_text_bold: {
214	    color: '#fff',
215	    fontWeight: 'bold',
216	  },
217	  wrapper: {
218	    width: '90%',
219	    alignSelf: 'center',
220	  },
221	  list_button: {
222	    marginTop: 6,
223	    marginLeft: 15,
224	    height: 40,
225	  },
226	  list_item: {
227	    borderBottomWidth: 1,
228	    borderBottomColor: 'rgba(0, 0, 0, 0.12)',
229	  },
230	  list_text: {
231	    fontSize: 15,
232	  },
233	  form_input: {
234	    height: 44,
235	    marginBottom: 16,
236	    backgroundColor: '#FFF',
237	    fontSize: 14,
238	  },
239	  submit_button: {
240	    width: '100%',
241	    maxHeight: 50,
242	    alignSelf: 'center',
243	    backgroundColor: '#208AEC',
244	  },
245	});
```

```typescript
1	import React, {FC, ReactElement, useState} from 'react';
2	import {
3	  Alert,
4	  Image,
5	  View,
6	  Platform,
7	  ScrollView,
8	  StyleSheet,
9	} from 'react-native';
10	import Parse from 'parse/react-native';
11	import {
12	  List,
13	  Title,
14	  TextInput as PaperTextInput,
15	  Button as PaperButton,
16	  Text as PaperText,
17	} from 'react-native-paper';
18	
19	export const MovieRatings: FC<{}> = ({}): ReactElement => {
20	  // State variable
21	  const [queryResults, setQueryResults] = useState(null);
22	  const [ratingsAverage, setRatingsAverage] = useState('');
23	  const [reviewText, setReviewText] = useState('');
24	  const [reviewRate, setReviewRate] = useState('');
25	
26	  const runGetMovieAverageRating = async function (): Promise<boolean> {
27	    try {
28	      const params: {movie: string} = {
29	        movie: 'Mission Very Possible',
30	      };
31	      let resultObject: {result: number} = await Parse.Cloud.run(
32	        'getMovieAverageRating',
33	        params,
34	      );
35	      // Set query results to state variable using state hook
36	      setRatingsAverage(resultObject.result.toFixed(1));
37	      return true;
38	    } catch (error) {
39	      // Error can be caused by lack of Internet connection
40	      // or by not having an valid Review object yet
41	      Alert.alert(
42	        'Error!',
43	        'Make sure that the cloud function is deployed and that the Review class table is created',
44	      );
45	      return false;
46	    }
47	  };
48	
49	  const doReviewQuery = async function (): Promise<boolean> {
50	    // Create our query
51	    let parseQuery: Parse.Query = new Parse.Query('Review');
52	    try {
53	      let results: [Parse.Object] = await parseQuery.find();
54	      // Set query results to state variable
55	      setQueryResults(results);
56	      return true;
57	    } catch (error) {
58	      // Error can be caused by lack of Internet connection
59	      Alert.alert('Error!', error.message);
60	      return false;
61	    }
62	  };
63	
64	  const createReview = async function (): Promise<boolean> {
65	    try {
66	      // This values come from state variables linked to
67	      // the screen form fields
68	      const reviewTextValue: string = reviewText;
69	      const reviewRateValue: number = Number(reviewRate);
70	
71	      // Creates a new parse object instance
72	      let Review: Parse.Object = new Parse.Object('Review');
73	
74	      // Set data to parse object
75	      // Simple title field
76	      Review.set('text', reviewTextValue);
77	
78	      // Simple number field
79	      Review.set('rate', reviewRateValue);
80	
81	      // Set default movie
82	      Review.set('movie', 'Mission Very Possible');
83	
84	      // After setting the values, save it on the server
85	      try {
86	        await Review.save();
87	        // Success
88	        Alert.alert('Success!');
89	        // Updates query result list
90	        doReviewQuery();
91	        runGetMovieAverageRating();
92	        return true;
93	      } catch (error) {
94	        // Error can be caused by lack of Internet connection
95	        Alert.alert('Error!', error.message);
96	        return false;
97	      }
98	    } catch (error) {
99	      // Error can be caused by lack of field values
100	      Alert.alert('Error!', error.message);
101	      return false;
102	    }
103	  };
104	
105	  return (
106	    <>
107	      <View style={Styles.header}>
108	        <Image
109	          style={Styles.header_logo}
110	          source={ {
111	            uri:
112	              'https://blog.back4app.com/wp-content/uploads/2019/05/back4app-white-logo-500px.png',
113	          } }
114	        />
115	        <PaperText style={Styles.header_text}>
116	          <PaperText style={Styles.header_text_bold}>
117	            {'React Native on Back4App - '}
118	          </PaperText>
119	          {' Cloud Code Movie Ratings'}
120	        </PaperText>
121	      </View>
122	      <ScrollView style={Styles.wrapper}>
123	        <View>
124	          <Title>{'Mission Very Possible Reviews'}</Title>
125	          <PaperText>{`Ratings Average: ${ratingsAverage}`}</PaperText>
126	          {/* Query list */}
127	          {queryResults !== null &&
128	            queryResults !== undefined &&
129	            queryResults.map((result: Parse.Object) => (
130	              <List.Item
131	                key={result.id}
132	                title={`Review text: ${result.get('text')}`}
133	                description={`Rate: ${result.get('rate')}`}
134	                titleStyle={Styles.list_text}
135	                style={Styles.list_item}
136	              />
137	            ))}
138	          {queryResults === null ||
139	          queryResults === undefined ||
140	          (queryResults !== null &&
141	            queryResults !== undefined &&
142	            queryResults.length <= 0) ? (
143	            <PaperText>{'No results here!'}</PaperText>
144	          ) : null}
145	        </View>
146	        <View>
147	          <Title>Action Buttons</Title>
148	          <PaperButton
149	            onPress={() => runGetMovieAverageRating()}
150	            mode="contained"
151	            icon="search-web"
152	            color={'#208AEC'}
153	            style={Styles.list_button}>
154	            {'Calculate Review Average'}
155	          </PaperButton>
156	          <PaperButton
157	            onPress={() => doReviewQuery()}
158	            mode="contained"
159	            icon="search-web"
160	            color={'#208AEC'}
161	            style={Styles.list_button}>
162	            {'Query Reviews'}
163	          </PaperButton>
164	        </View>
165	        <View>
166	          <Title>Add new review</Title>
167	          <PaperTextInput
168	            value={reviewText}
169	            onChangeText={text => setReviewText(text)}
170	            label="Text"
171	            mode="outlined"
172	            style={Styles.form_input}
173	          />
174	          <PaperTextInput
175	            value={reviewRate}
176	            onChangeText={text => setReviewRate(text)}
177	            keyboardType={'number-pad'}
178	            label="Rate (1-5)"
179	            mode="outlined"
180	            style={Styles.form_input}
181	          />
182	          <PaperButton
183	            onPress={() => createReview()}
184	            mode="contained"
185	            icon="plus"
186	            style={Styles.submit_button}>
187	            {'Add'}
188	          </PaperButton>
189	        </View>
190	      </ScrollView>
191	    </>
192	  );
193	};
194	
195	// These define the screen component styles
196	const Styles = StyleSheet.create({
197	  header: {
198	    alignItems: 'center',
199	    paddingTop: 30,
200	    paddingBottom: 50,
201	    backgroundColor: '#208AEC',
202	  },
203	  header_logo: {
204	    height: 50,
205	    width: 220,
206	    resizeMode: 'contain',
207	  },
208	  header_text: {
209	    marginTop: 15,
210	    color: '#f0f0f0',
211	    fontSize: 16,
212	  },
213	  header_text_bold: {
214	    color: '#fff',
215	    fontWeight: 'bold',
216	  },
217	  wrapper: {
218	    width: '90%',
219	    alignSelf: 'center',
220	  },
221	  list_button: {
222	    marginTop: 6,
223	    marginLeft: 15,
224	    height: 40,
225	  },
226	  list_item: {
227	    borderBottomWidth: 1,
228	    borderBottomColor: 'rgba(0, 0, 0, 0.12)',
229	  },
230	  list_text: {
231	    fontSize: 15,
232	  },
233	  form_input: {
234	    height: 44,
235	    marginBottom: 16,
236	    backgroundColor: '#FFF',
237	    fontSize: 14,
238	  },
239	  submit_button: {
240	    width: '100%',
241	    maxHeight: 50,
242	    alignSelf: 'center',
243	    backgroundColor: '#208AEC',
244	  },
245	});
```
:::

This is how the component should look like after rendering and querying by one of the query functions:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/TLxZDfyAWUhR-mxNfBSvB_image.png" signedSrc size="50" width="354" height="751" position="center" caption}

## Conclusion

At the end of this guide, you learned how Parse Cloud Code functions work and how to perform them on Back4App from a React Native App. In the next guide, you will learn how to work with Users in Parse.
