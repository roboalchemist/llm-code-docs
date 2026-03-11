# Source: https://docs-containers.back4app.com/docs/react-native/parse-sdk/data-objects/react-native-geolocation.md

---
title: Geoqueries
slug: docs/react-native/parse-sdk/data-objects/react-native-geolocation
description: In this guide, you'll learn how to perform GeoPoint querying in Parse on a React Native application
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-19T13:37:42.193Z
updatedAt: 2025-01-28T13:50:48.344Z
---

# Using React Native geolocation to perform geoqueries using Parse

## Introduction

In this guide, you will perform geoqueries in Parse using the React Native geolocation. You will implement a React Native component using these queries and learn how to set up and query realistic data using Back4App and React Native.

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- A React Native App created and connected to [**Back4App**](https://www.back4app.com/docs/react-native/parse-sdk/react-native-sdk).
- If you want to test/use the screen layout provided by this guide, you should set up thereact-native-paper[**library**](https://github.com/callstack/react-native-paper) and also react-native-geolocation-service.
:::

## Goal

Perform Geoqueries using geopoints stored on Back4App and React Native geolocation.

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

Let’s create a City class, which will be the target of our queries in this guide. On Parse JS Console is possible to run JavaScript code directly, querying and updating your application database contents using the JS SDK commands. Run the code below from your JS Console and insert the data on Back4App.

Here is how the JS Console looks like in your dashboard:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/zWAvl3tCT22AsXFJx2QD8_image.png)

Go ahead and create the City class with the following example content:

```javascript
1	// Add City objects and create table
2	// Note how GeoPoints are created, passing latitude and longitude as arguments
3	// Montevideo
4	City = new Parse.Object('City');
5	City.set('name', 'Montevideo - Uruguay');
6	City.set('location', new Parse.GeoPoint(-34.85553195363169, -56.207280375137955));
7	await City.save();
8	
9	// Brasília
10	City = new Parse.Object('City');
11	City.set('name', 'Brasília - Brazil');
12	City.set('location', new Parse.GeoPoint(-15.79485821477289, -47.88391074690196));
13	await City.save();
14	
15	// Bogotá
16	City = new Parse.Object('City');
17	City.set('name', 'Bogotá - Colombia');
18	City.set('location', new Parse.GeoPoint(4.69139880891712, -74.06936691331047));
19	await City.save();
20	
21	// Mexico City
22	City = new Parse.Object('City');
23	City.set('name', 'Mexico City - Mexico');
24	City.set('location', new Parse.GeoPoint(19.400977162618933, -99.13311378164776));
25	await City.save();
26	
27	// Washington, D.C.
28	City = new Parse.Object('City');
29	City.set('name', 'Washington, D.C. - USA');
30	City.set('location', new Parse.GeoPoint(38.930727220189944, -77.04626261880388));
31	await City.save();
32	
33	// Ottawa
34	City = new Parse.Object('City');
35	City.set('name', 'Ottawa - Canada');
36	City.set('location', new Parse.GeoPoint(45.41102167733425, -75.695414598736));
37	await City.save();
38	
39	console.log('Success!');
```

## 3 - Query the data

Now that you have a populated class, we can now perform some GeoPoint queries in it. Let’s begin by ordering City results by the nearest from Kingston in Jamaica (latitude 18.01808695059913 and longitude -76.79894232253473), using the Parse.Query.near method:

```javascript
1	// Create your query
2	let parseQuery = new Parse.Query('City');
3	
4	// Create our GeoPoint for the query
5	let kingstonGeoPoint = new Parse.GeoPoint(18.018086950599134, -76.79894232253473);
6	
7	// `near` will order results based on distance between the GeoPoint type field from the class and the GeoPoint argument
8	parseQuery.near('location', kingstonGeoPoint);
9	
10	// The query will resolve only after calling this method, retrieving
11	// an array of `Parse.Objects`
12	let queryResults = await parseQuery.find();
13	
14	// Let's show the results
15	for (let result of queryResults) {
16	  // You access `Parse.Objects` attributes by using `.get`
17	  console.log(result.get('name'));
18	};
```

Let’s now query using the methodParse.Query.withinKilometers, which will retrieve all results whose GeoPoint field is located within the max distance. Kingston will be used once again as a reference and the distance limit will be 3000 km.

```javascript
1	// Create your query
2	let parseQuery = new Parse.Query('City');
3	
4	// Create our GeoPoint for the query
5	let kingstonGeoPoint = new Parse.GeoPoint(18.018086950599134, -76.79894232253473);
6	
7	// You can also use `withinMiles` and `withinRadians` the same way,
8	// but with different measuring unities
9	parseQuery.withinKilometers('location', kingstonGeoPoint, 3000);
10	
11	// The query will resolve only after calling this method, retrieving
12	// an array of `Parse.Objects`
13	let queryResults = await parseQuery.find();
14	
15	// Let's show the results
16	for (let result of queryResults) {
17	  // You access `Parse.Objects` attributes by using `.get`
18	  console.log(result.get('name'));
19	};
```

Another useful query method isParse.Query.withinPolygon, which will query results whose GeoPoint field value is within the specified polygon, composed of an array of GeoPoints (at least three). If the polygon path is open, it will be closed automatically by Parse connecting the last and first points.

For this example, you will be using a simple polygon that roughly contains the South American continent, composed of 5 distant GeoPoints in the ocean.

```javascript
1	// Create your query
2	let parseQuery = new Parse.Query('City');
3	
4	// Create our GeoPoint polygon for the query
5	let geoPoint1 = new Parse.GeoPoint(15.822238344514378, -72.42845934415942);
6	let geoPoint2 = new Parse.GeoPoint(-0.7433770196268968, -97.44765968406668);
7	let geoPoint3 = new Parse.GeoPoint(-59.997149373299166, -76.52969196322749);
8	let geoPoint4 = new Parse.GeoPoint(-9.488786415007201, -18.346101586021952);
9	let geoPoint5 = new Parse.GeoPoint(15.414859532811047, -60.00625459569375);
10	
11	// Note that the polygon is merely an array of GeoPoint objects and that the first and last are not connected, so Parse connects them for you
12	parseQuery.withinPolygon('location', [geoPoint1, geoPoint2, geoPoint3, geoPoint4, geoPoint5]);
13	
14	// The query will resolve only after calling this method, retrieving
15	// an array of `Parse.Objects`
16	let queryResults = await parseQuery.find();
17	
18	// Let's show the results
19	for (let result of queryResults) {
20	  // You access `Parse.Objects` attributes by using `.get`
21	  console.log(result.get('name'));
22	};
```

## 4 - Query from a React Native component

Let’s now use our example queries inside a component in React Native, with a simple interface having a list showing results and also 3 buttons for calling the queries. The component also retrieves the device’s current location using react-native-geolocation-service, so the queries will be using real data.

This is how the component code is laid out, note the doQuery functions, containing the example code form before.

:::CodeblockTabs
JavaScript

```javascript
1	import React, {useState} from 'react';
2	import {
3	  Alert,
4	  Image,
5	  View,
6	  PermissionsAndroid,
7	  Platform,
8	  ScrollView,
9	  StyleSheet,
10	} from 'react-native';
11	import Parse from 'parse/react-native';
12	import {
13	  List,
14	  Title,
15	  Button as PaperButton,
16	  Text as PaperText,
17	} from 'react-native-paper';
18	import Geolocation from 'react-native-geolocation-service';
19	
20	export const QueryList = () => {
21	  // State variable
22	  const [queryResults, setQueryResults] = useState(null);
23	
24	  // This function asks for location permission on iOS and Android
25	  const requestLocationPermissions = async () => {
26	    if (Platform.OS === 'ios') {
27	      // iOS can be asked always, since the OS handles if user already gave permission
28	      await Geolocation.requestAuthorization('whenInUse');
29	    } else if (Platform.OS === 'android') {
30	      let permissionCheck = await PermissionsAndroid.check(
31	        PermissionsAndroid.PERMISSIONS.ACCESS_FINE_LOCATION,
32	      );
33	      // Only asks for permission on Android if not given before
34	      if (permissionCheck !== true) {
35	        await PermissionsAndroid.request(
36	          PermissionsAndroid.PERMISSIONS.ACCESS_FINE_LOCATION,
37	          {
38	            title: 'Location Permission Request',
39	            message:
40	              'This app needs you permission for using your location for querying GeoPoints in Parse!',
41	            buttonPositive: 'OK',
42	          },
43	        );
44	      }
45	    }
46	  };
47	
48	  const doQueryNear = async function () {
49	    // Request location permissions
50	    await requestLocationPermissions();
51	    // Get current location and create the GeoPoint for the query
52	    Geolocation.getCurrentPosition(
53	      async (currentPosition) => {
54	        // Create our GeoPoint
55	        let currentLocationGeoPoint = new Parse.GeoPoint(
56	          currentPosition.coords.latitude,
57	          currentPosition.coords.longitude,
58	        );
59	
60	        // Create our query
61	        let parseQuery = new Parse.Query('City');
62	
63	        // `near` will order results based on distance between the GeoPoint type field from the class and the GeoPoint argument
64	        parseQuery.near('location', currentLocationGeoPoint);
65	
66	        try {
67	          let results = await parseQuery.find();
68	          // Set query results to state variable
69	          setQueryResults(results);
70	        } catch (error) {
71	          // Error can be caused by lack of Internet connection
72	          Alert.alert('Error!', error.message);
73	        }
74	      },
75	      _error => {
76	        Alert.alert(
77	          'Error!',
78	          'This app needs your location permission to query this!',
79	        );
80	      },
81	      {enableHighAccuracy: true, timeout: 15000, maximumAge: 10000},
82	    );
83	    return true;
84	  };
85	
86	  const doQueryWithinKilometers = async function () {
87	    // Request location permissions
88	    await requestLocationPermissions();
89	    // Get current location and create the GeoPoint for the query
90	    Geolocation.getCurrentPosition(
91	      async (currentPosition) => {
92	        // Create our GeoPoint
93	        let currentLocationGeoPoint = new Parse.GeoPoint(
94	          currentPosition.coords.latitude,
95	          currentPosition.coords.longitude,
96	        );
97	
98	        // Create our query
99	        let parseQuery = new Parse.Query('City');
100	
101	        // You can also use `withinMiles` and `withinRadians` the same way,
102	        // but with different measuring unities
103	        parseQuery.withinKilometers('location', currentLocationGeoPoint, 3000);
104	
105	        try {
106	          let results = await parseQuery.find();
107	          // Set query results to state variable
108	          setQueryResults(results);
109	        } catch (error) {
110	          // Error can be caused by lack of Internet connection
111	          Alert.alert('Error!', error.message);
112	        }
113	      },
114	      _error => {
115	        Alert.alert(
116	          'Error!',
117	          'This app needs your location permission to query this!',
118	        );
119	      },
120	      {enableHighAccuracy: true, timeout: 15000, maximumAge: 10000},
121	    );
122	    return true;
123	  };
124	
125	  const doQueryWithinPolygon = async function () {
126	    // Create our GeoPoint polygon points
127	    let geoPoint1 = new Parse.GeoPoint(15.822238344514378, -72.42845934415942);
128	    let geoPoint2 = new Parse.GeoPoint(-0.7433770196268968, -97.44765968406668);
129	    let geoPoint3 = new Parse.GeoPoint(-59.997149373299166, -76.52969196322749);
130	    let geoPoint4 = new Parse.GeoPoint(-9.488786415007201, -18.346101586021952);
131	    let geoPoint5 = new Parse.GeoPoint(15.414859532811047, -60.00625459569375);
132	
133	    // Create our query
134	    let parseQuery = new Parse.Query('City');
135	
136	    // Note that the polygon is merely an array of GeoPoint objects and that the first and last are not connected, so Parse connects them for you
137	    parseQuery.withinPolygon('location', [
138	      geoPoint1,
139	      geoPoint2,
140	      geoPoint3,
141	      geoPoint4,
142	      geoPoint5,
143	    ]);
144	
145	    try {
146	      let results = await parseQuery.find();
147	      // Set query results to state variable
148	      setQueryResults(results);
149	    } catch (error) {
150	      // Error can be caused by lack of Internet connection
151	      Alert.alert('Error!', error.message);
152	    }
153	  };
154	
155	  const clearQueryResults = async function () {
156	    setQueryResults(null);
157	    return true;
158	  };
159	
160	  return (
161	    <>
162	      <View style={Styles.header}>
163	        <Image
164	          style={Styles.header_logo}
165	          source={ {
166	            uri:
167	              'https://blog.back4app.com/wp-content/uploads/2019/05/back4app-white-logo-500px.png',
168	          } }
169	        />
170	        <PaperText style={Styles.header_text}>
171	          <PaperText style={Styles.header_text_bold}>
172	            {'React Native on Back4App - '}
173	          </PaperText>
174	          {' GeoPoint Queries'}
175	        </PaperText>
176	      </View>
177	      <ScrollView style={Styles.wrapper}>
178	        <View>
179	          <Title>{'Result List'}</Title>
180	          {/* Query list */}
181	          {queryResults !== null &&
182	            queryResults !== undefined &&
183	            queryResults.map((result) => (
184	              <List.Item
185	                key={result.id}
186	                title={result.get('name')}
187	                titleStyle={Styles.list_text}
188	                style={Styles.list_item}
189	              />
190	            ))}
191	          {queryResults === null ||
192	          queryResults === undefined ||
193	          (queryResults !== null &&
194	            queryResults !== undefined &&
195	            queryResults.length <= 0) ? (
196	            <PaperText>{'No results here!'}</PaperText>
197	          ) : null}
198	        </View>
199	        <View>
200	          <Title>{'Query buttons'}</Title>
201	          <PaperButton
202	            onPress={() => doQueryNear()}
203	            mode="contained"
204	            icon="search-web"
205	            color={'#208AEC'}
206	            style={Styles.list_button}>
207	            {'Query Near'}
208	          </PaperButton>
209	          <PaperButton
210	            onPress={() => doQueryWithinKilometers()}
211	            mode="contained"
212	            icon="search-web"
213	            color={'#208AEC'}
214	            style={Styles.list_button}>
215	            {'Query Within KM'}
216	          </PaperButton>
217	          <PaperButton
218	            onPress={() => doQueryWithinPolygon()}
219	            mode="contained"
220	            icon="search-web"
221	            color={'#208AEC'}
222	            style={Styles.list_button}>
223	            {'Query Within Polygon'}
224	          </PaperButton>
225	          <PaperButton
226	            onPress={() => clearQueryResults()}
227	            mode="contained"
228	            icon="delete"
229	            color={'#208AEC'}
230	            style={Styles.list_button}>
231	            {'Clear Results'}
232	          </PaperButton>
233	        </View>
234	      </ScrollView>
235	    </>
236	  );
237	};
238	
239	// These define the screen component styles
240	const Styles = StyleSheet.create({
241	  header: {
242	    alignItems: 'center',
243	    paddingTop: 30,
244	    paddingBottom: 50,
245	    backgroundColor: '#208AEC',
246	  },
247	  header_logo: {
248	    height: 50,
249	    width: 220,
250	    resizeMode: 'contain',
251	  },
252	  header_text: {
253	    marginTop: 15,
254	    color: '#f0f0f0',
255	    fontSize: 16,
256	  },
257	  header_text_bold: {
258	    color: '#fff',
259	    fontWeight: 'bold',
260	  },
261	  wrapper: {
262	    width: '90%',
263	    alignSelf: 'center',
264	  },
265	  list_button: {
266	    marginTop: 6,
267	    marginLeft: 15,
268	    height: 40,
269	  },
270	  list_item: {
271	    borderBottomWidth: 1,
272	    borderBottomColor: 'rgba(0, 0, 0, 0.12)',
273	  },
274	  list_text: {
275	    fontSize: 15,
276	  },
277	});
```

```typescript
1	import React, {FC, ReactElement, useState} from 'react';
2	import {
3	  Alert,
4	  Image,
5	  View,
6	  PermissionsAndroid,
7	  Platform,
8	  ScrollView,
9	  StyleSheet,
10	} from 'react-native';
11	import Parse from 'parse/react-native';
12	import {
13	  List,
14	  Title,
15	  Button as PaperButton,
16	  Text as PaperText,
17	} from 'react-native-paper';
18	import Geolocation from 'react-native-geolocation-service';
19	
20	export const QueryList: FC<{}> = ({}): ReactElement => {
21	  // State variable
22	  const [queryResults, setQueryResults] = useState(null);
23	
24	  // This function asks for location permission on iOS and Android
25	  const requestLocationPermissions = async () => {
26	    if (Platform.OS === 'ios') {
27	      // iOS can be asked always, since the OS handles if user already gave permission
28	      await Geolocation.requestAuthorization('whenInUse');
29	    } else if (Platform.OS === 'android') {
30	      let permissionCheck: boolean = await PermissionsAndroid.check(
31	        PermissionsAndroid.PERMISSIONS.ACCESS_FINE_LOCATION,
32	      );
33	      // Only asks for permission on Android if not given before
34	      if (permissionCheck !== true) {
35	        await PermissionsAndroid.request(
36	          PermissionsAndroid.PERMISSIONS.ACCESS_FINE_LOCATION,
37	          {
38	            title: 'Location Permission Request',
39	            message:
40	              'This app needs you permission for using your location for querying GeoPoints in Parse!',
41	            buttonPositive: 'OK',
42	          },
43	        );
44	      }
45	    }
46	  };
47	
48	  const doQueryNear = async function (): Promise<boolean> {
49	    // Request location permissions
50	    await requestLocationPermissions();
51	    // Get current location and create the GeoPoint for the query
52	    Geolocation.getCurrentPosition(
53	      async (currentPosition: {
54	        coords: {latitude: number; longitude: number};
55	      }) => {
56	        // Create our GeoPoint
57	        let currentLocationGeoPoint: Parse.GeoPoint = new Parse.GeoPoint(
58	          currentPosition.coords.latitude,
59	          currentPosition.coords.longitude,
60	        );
61	
62	        // Create our query
63	        let parseQuery: Parse.Query = new Parse.Query('City');
64	
65	        // `near` will order results based on distance between the GeoPoint type field from the class and the GeoPoint argument
66	        parseQuery.near('location', currentLocationGeoPoint);
67	
68	        try {
69	          let results: [Parse.Object] = await parseQuery.find();
70	          // Set query results to state variable
71	          setQueryResults(results);
72	        } catch (error) {
73	          // Error can be caused by lack of Internet connection
74	          Alert.alert('Error!', error.message);
75	        }
76	      },
77	      _error => {
78	        Alert.alert(
79	          'Error!',
80	          'This app needs your location permission to query this!',
81	        );
82	      },
83	      {enableHighAccuracy: true, timeout: 15000, maximumAge: 10000},
84	    );
85	    return true;
86	  };
87	
88	  const doQueryWithinKilometers = async function (): Promise<boolean> {
89	    // Request location permissions
90	    await requestLocationPermissions();
91	    // Get current location and create the GeoPoint for the query
92	    Geolocation.getCurrentPosition(
93	      async (currentPosition: {
94	        coords: {latitude: number; longitude: number};
95	      }) => {
96	        // Create our GeoPoint
97	        let currentLocationGeoPoint: Parse.GeoPoint = new Parse.GeoPoint(
98	          currentPosition.coords.latitude,
99	          currentPosition.coords.longitude,
100	        );
101	
102	        // Create our query
103	        let parseQuery: Parse.Query = new Parse.Query('City');
104	
105	        // You can also use `withinMiles` and `withinRadians` the same way,
106	        // but with different measuring unities
107	        parseQuery.withinKilometers('location', currentLocationGeoPoint, 3000);
108	
109	        try {
110	          let results: [Parse.Object] = await parseQuery.find();
111	          // Set query results to state variable
112	          setQueryResults(results);
113	        } catch (error) {
114	          // Error can be caused by lack of Internet connection
115	          Alert.alert('Error!', error.message);
116	        }
117	      },
118	      _error => {
119	        Alert.alert(
120	          'Error!',
121	          'This app needs your location permission to query this!',
122	        );
123	      },
124	      {enableHighAccuracy: true, timeout: 15000, maximumAge: 10000},
125	    );
126	    return true;
127	  };
128	
129	  const doQueryWithinPolygon = async function (): Promise<boolean> {
130	    // Create our GeoPoint polygon points
131	    let geoPoint1: Parse.GeoPoint = new Parse.GeoPoint(
132	15.822.238.344.514.300,00
133	-7.242.845.934.415.940,00
134	    );
135	    let geoPoint2: Parse.GeoPoint = new Parse.GeoPoint(
136	      -0.7433770196268968,
137	-9.744.765.968.406.660,00
138	    );
139	    let geoPoint3: Parse.GeoPoint = new Parse.GeoPoint(
140	-59.997.149.373.299.100,00
141	-7.652.969.196.322.740,00
142	    );
143	    let geoPoint4: Parse.GeoPoint = new Parse.GeoPoint(
144	-9.488.786.415.007.200,00
145	-18.346.101.586.021.900,00
146	    );
147	    let geoPoint5: Parse.GeoPoint = new Parse.GeoPoint(
148	15.414.859.532.811.000,00
149	-6.000.625.459.569.370,00
150	    );
151	
152	    // Create our query
153	    let parseQuery: Parse.Query = new Parse.Query('City');
154	
155	    // Note that the polygon is merely an array of GeoPoint objects and that the first and last are not connected, so Parse connects them for you
156	    parseQuery.withinPolygon('location', [
157	      geoPoint1,
158	      geoPoint2,
159	      geoPoint3,
160	      geoPoint4,
161	      geoPoint5,
162	    ]);
163	
164	    try {
165	      let results: [Parse.Object] = await parseQuery.find();
166	      // Set query results to state variable
167	      setQueryResults(results);
168	    } catch (error) {
169	      // Error can be caused by lack of Internet connection
170	      Alert.alert('Error!', error.message);
171	    }
172	  };
173	
174	  const clearQueryResults = async function (): Promise<boolean> {
175	    setQueryResults(null);
176	    return true;
177	  };
178	
179	  return (
180	    <>
181	      <View style={Styles.header}>
182	        <Image
183	          style={Styles.header_logo}
184	          source={ {
185	            uri:
186	              'https://blog.back4app.com/wp-content/uploads/2019/05/back4app-white-logo-500px.png',
187	          } }
188	        />
189	        <PaperText style={Styles.header_text}>
190	          <PaperText style={Styles.header_text_bold}>
191	            {'React Native on Back4App - '}
192	          </PaperText>
193	          {' GeoPoint Queries'}
194	        </PaperText>
195	      </View>
196	      <ScrollView style={Styles.wrapper}>
197	        <View>
198	          <Title>{'Result List'}</Title>
199	          {/* Query list */}
200	          {queryResults !== null &&
201	            queryResults !== undefined &&
202	            queryResults.map((result: Parse.Object) => (
203	              <List.Item
204	                key={result.id}
205	                title={result.get('name')}
206	                titleStyle={Styles.list_text}
207	                style={Styles.list_item}
208	              />
209	            ))}
210	          {queryResults === null ||
211	          queryResults === undefined ||
212	          (queryResults !== null &&
213	            queryResults !== undefined &&
214	            queryResults.length <= 0) ? (
215	            <PaperText>{'No results here!'}</PaperText>
216	          ) : null}
217	        </View>
218	        <View>
219	          <Title>{'Query buttons'}</Title>
220	          <PaperButton
221	            onPress={() => doQueryNear()}
222	            mode="contained"
223	            icon="search-web"
224	            color={'#208AEC'}
225	            style={Styles.list_button}>
226	            {'Query Near'}
227	          </PaperButton>
228	          <PaperButton
229	            onPress={() => doQueryWithinKilometers()}
230	            mode="contained"
231	            icon="search-web"
232	            color={'#208AEC'}
233	            style={Styles.list_button}>
234	            {'Query Within KM'}
235	          </PaperButton>
236	          <PaperButton
237	            onPress={() => doQueryWithinPolygon()}
238	            mode="contained"
239	            icon="search-web"
240	            color={'#208AEC'}
241	            style={Styles.list_button}>
242	            {'Query Within Polygon'}
243	          </PaperButton>
244	          <PaperButton
245	            onPress={() => clearQueryResults()}
246	            mode="contained"
247	            icon="delete"
248	            color={'#208AEC'}
249	            style={Styles.list_button}>
250	            {'Clear Results'}
251	          </PaperButton>
252	        </View>
253	      </ScrollView>
254	    </>
255	  );
256	};
257	
258	// These define the screen component styles
259	const Styles = StyleSheet.create({
260	  header: {
261	    alignItems: 'center',
262	    paddingTop: 30,
263	    paddingBottom: 50,
264	    backgroundColor: '#208AEC',
265	  },
266	  header_logo: {
267	    height: 50,
268	    width: 220,
269	    resizeMode: 'contain',
270	  },
271	  header_text: {
272	    marginTop: 15,
273	    color: '#f0f0f0',
274	    fontSize: 16,
275	  },
276	  header_text_bold: {
277	    color: '#fff',
278	    fontWeight: 'bold',
279	  },
280	  wrapper: {
281	    width: '90%',
282	    alignSelf: 'center',
283	  },
284	  list_button: {
285	    marginTop: 6,
286	    marginLeft: 15,
287	    height: 40,
288	  },
289	  list_item: {
290	    borderBottomWidth: 1,
291	    borderBottomColor: 'rgba(0, 0, 0, 0.12)',
292	  },
293	  list_text: {
294	    fontSize: 15,
295	  },
296	});
```
:::

This is how the component should look like after rendering and querying one of the query functions:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Xea6zYcy8-Pe1W1Tob3J3_image.png" signedSrc size="50" width="355" height="750" position="center" caption}

## Conclusion

At the end of this guide, you learned how GeoPoint data queries work on Parse and how to perform them on Back4App from a React Native App. In the next guide, you will check how to create and manage users in Parse.
