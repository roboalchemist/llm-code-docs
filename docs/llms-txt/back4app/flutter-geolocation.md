# Source: https://docs-containers.back4app.com/docs/flutter/parse-sdk/data-objects/flutter-geolocation.md

---
title: Geoqueries
slug: docs/flutter/parse-sdk/data-objects/flutter-geolocation
description: In this guide, you'll learn about Geopoint datatype and how to perform queries in Parse on a Flutter application
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-18T12:33:18.194Z
updatedAt: 2025-01-16T20:36:58.911Z
---

# Using Flutter geolocation to perform geoqueries on Parse

## Introduction

In this guide, you will learn about GeoPoint data type on Parse and how to perform geo queries in Parse using the Flutter geolocation. You will create an application that will perform geo queries and retrieve records using Parse Geopoints.

We won’t explain the Flutter application code once this guide’s primary focus is on the Flutter with Parse.

## Prerequisites

**To complete this tutorial, you will need:**

:::hint{type="info"}
- An app created on Back4App.
  - **Note:&#x20;**&#x46;ollow the [**New Parse App Tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse App on Back4App.
- An Flutter app connected to Back4app.
  - **Note:&#x20;**&#x46;ollow the [**Install Parse SDK on Flutter project**](https://www.back4app.com/docs/flutter/parse-sdk/parse-flutter-sdk) to create an Flutter Project connected to Back4App.
- A device (or virtual device) running Android or iOS.
- In order to run this guide example you should set up the plugin [**Geolocator**](https://pub.dev/packages/geolocator) properly. Do not forget to add permissions for Android and iOS in order to access the device location \{: .btn target=”\_blank” rel=”nofollow noreferer noopener”} in the project. Carefully read the instructions for setting up the Android and iOS project.
:::

## Goal

Perform Geoqueries using geopoints stored on Back4App and Flutter geolocation.

## The GeoPoint datatype

Parse allows you to associate real-world latitude and longitude coordinates with an object. Adding a ParseGeoPoint to a ParseObject will enable queries to consider the proximity of an object to a reference point. This feature allows you to easily do things like finding out what user is closest to another user or which places are nearest to a user.

To associate a point with an object, you first need to create a ParseGeoPoint. Below you can find a geopoint with a latitude of 40.0 degrees and -30.0 degrees longitude.

:::BlockQuote
**final** point **=** ParseGeoPoint(latitude: 40.0, longitude: 30.0);
:::

This point is then stored in the object as a regular field, like any other data type (string, number, date, etc.)

:::BlockQuote
placeObjec&#x74;**.**&#x73;et("location", point);
**await** placeObjec&#x74;**.**&#x73;ave();
:::

\*\* Note: Currently only one key in a class may be a ParseGeoPoint

## 1 - The QueryBuilder class

Any Parse query operation uses the QueryBuilder object type, which will help you retrieve specific data from your database throughout your app. To create a new QueryBuilder, you need to pass as a parameter the desired ParseObject subclass, which is the one that will contain your query results.

It is crucial to know that a QueryBuilder will only resolve after calling a retrieve method query, so a query can be set up and several modifiers can be chained before actually being called. You can read more about the QueryBuilder class [**here at the official documentation**](https://github.com/parse-community/Parse-SDK-Flutter/tree/master/packages/flutter#complex-queries).

## Using the JavaScript Console on Back4App

Inside your Back4App application’s dashboard, you will find a very useful API console in which you can run JavaScript code directly. In this guide you will use to store data objects in Back4App. On your App main dashboard go to Core->API Console->Javascript.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/a_0axHyd4EviC1lkQUYl6_image.png)

## 2 - Save Data on Back4app

To run the queries on this guide you’ll need first to populate your App with some data. Let’s create a City class, which will be the target of our queries in this guide. Here is the Parse.Object classes creation code, so go ahead and run it in your API console:

```javascript
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
38
39  // Tokyo
40  City = new Parse.Object('City');
41  City.set('name', 'Tokyo - Japan');
42  City.set('location', new Parse.GeoPoint(35.6897, 139.6922));
43  await City.save();
44
45  // Mumbai
46  City = new Parse.Object('City');
47  City.set('name', 'Mumbai - India');
48  City.set('location', new Parse.GeoPoint(18.9667, 72.8333));
49  await City.save();
50
51  // Shanghai
52  City = new Parse.Object('City');
53  City.set('name', 'Shanghai - China');
54  City.set('location', new Parse.GeoPoint(31.1667, 121.4667));
55  await City.save();
56
57  // New York
58  City = new Parse.Object('City');
59  City.set('name', 'New York - USA');
60  City.set('location', new Parse.GeoPoint(40.6943, -73.9249));
61  await City.save();
62
63  // Moscow
64  City = new Parse.Object('City');
65  City.set('name', 'Moscow - Russia');
66  City.set('location', new Parse.GeoPoint(55.7558, 37.6178));
67  await City.save();
68 
69  // Paris
70  City = new Parse.Object('City');
71  City.set('name', 'Paris - France');
72  City.set('location', new Parse.GeoPoint(48.8566, 2.3522));
73  await City.save();
74
75  // Paris
76  City = new Parse.Object('City');
77  City.set('name', 'London - United Kingdom');
78  City.set('location', new Parse.GeoPoint(51.5072, -0.1275));
79  await City.save();
80  
81  // Luanda
82  City = new Parse.Object('City');
83  City.set('name', 'Luanda - Angola');
84  City.set('location', new Parse.GeoPoint(-8.8383, 13.2344));
85  await City.save();
86
87  // Johannesburg
88  City = new Parse.Object('City');
89  City.set('name', 'Johannesburg - South Africa');
90  City.set('location', new Parse.GeoPoint(-26.2044, 28.0416));
91  await City.save();
92
93  console.log('Success!');
```

After running this code, you should now have a City class in your database. Your new class should look like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/sgzV_xHxAqb687O4oBItc_image.png)

Let’s now take a look at examples from every QueryBuilder method, along with brief explanations on what they do.

## 3 - Query the data

Now that you have a populated class, we can now perform some GeoPoint queries in it.

Let’s begin by ordering City results by the nearest from Dallas in USA (latitude 32.779167, and longitude -96.808891), using the whereNear method:

```javascript
1       // Create your query
2       final QueryBuilder<ParseObject> parseQuery =
3           QueryBuilder<ParseObject>(ParseObject('City'));
4
5       // Create our GeoPoint for the query
6       final dallasGeoPoint =
7           ParseGeoPoint(latitude: 32.779167, longitude: -96.808891);
8
9       // `whereNear` will order results based on distance between the GeoPoint
10      // type field from the class and the GeoPoint argument
11      parseQuery.whereNear('location', dallasGeoPoint);
12
13      // The query will resolve only after calling this method, retrieving
14      // an array of `ParseObjects`, if success
15      final ParseResponse apiResponse = await parseQuery.query();
16
17      if (apiResponse.success && apiResponse.results != null) {
18        // Let's show the results
19        for (var o in apiResponse.results! as List<ParseObject>) {
20          print(
21              'City: ${o.get<String>('name')} - Location: ${o.get<ParseGeoPoint>('location')!.latitude}, ${o.get<ParseGeoPoint>('location')!.longitude}');
22        }
23      }
```

Let’s now query using the method whereWithinKilometers, which will retrieve all results whose GeoPoint field is located within the max distance in Kilometers.
Dallas will be used once again as a reference and the distance limit will be 3000 km.

```javascript
1       // Create your query
2       final QueryBuilder<ParseObject> parseQuery =
3           QueryBuilder<ParseObject>(ParseObject('City'));
4
5       // Create our GeoPoint for the query
6       final dallasGeoPoint =
7           ParseGeoPoint(latitude: 32.779167, longitude: -96.808891);
8
9       // You can also use `withinMiles` and `withinRadians` the same way,
10      // but with different measuring unities
11      parseQuery.whereWithinKilometers('location', dallasGeoPoint, 3000);
12     //parseQuery.whereWithinMiles('location', dallasGeoPoint, 3000);
13
14      // The query will resolve only after calling this method, retrieving
15      // an array of `ParseObjects`, if success
16      final ParseResponse apiResponse = await parseQuery.query();
17
18      if (apiResponse.success && apiResponse.results != null) {
19        // Let's show the results
20        for (var o in apiResponse.results! as List<ParseObject>) {
21          print(
22              'City: ${o.get<String>('name')} - Location: ${o.get<ParseGeoPoint>('location')!.latitude}, ${o.get<ParseGeoPoint>('location')!.longitude}');
23        }
24      }
```

Let’s now query using the method whereWithinMiles, which will retrieve all results whose GeoPoint field is located within the max distance in Miles.
Dallas will be used once again as a reference and the distance limit will be 3000 miles.

```javascript
1       // Create your query
2       final QueryBuilder<ParseObject> parseQuery =
3           QueryBuilder<ParseObject>(ParseObject('City'));
4
5       // Create our GeoPoint for the query
6       final dallasGeoPoint =
7           ParseGeoPoint(latitude: 32.779167, longitude: -96.808891);
8
9       // You can also use `whereWithinKilometers` and `whereWithinRadians` the same way,
10      parseQuery.whereWithinMiles('location', dallasGeoPoint, 3000);
11
12      // The query will resolve only after calling this method, retrieving
13      // an array of `ParseObjects`, if success
14      final ParseResponse apiResponse = await parseQuery.query();
15
16      if (apiResponse.success && apiResponse.results != null) {
17        // Let's show the results
18        for (var o in apiResponse.results! as List<ParseObject>) {
19          print(
20              'City: ${o.get<String>('name')} - Location: ${o.get<ParseGeoPoint>('location')!.latitude}, ${o.get<ParseGeoPoint>('location')!.longitude}');
21        }
22      }
```

## 4 - Query from Flutter

Let’s now use our example queries inside a Flutter App, with a simple interface having a list showing results and also 3 buttons for calling the queries.

The app also retrieves the device’s current location using [**Geolocator**](https://pub.dev/packages/geolocator) plugin (follow the instructions), so the queries will be using real data.

Open your Flutter project, go to the main.dart file, clean up all the code, and replace it with:

```dart
1   import 'package:flutter/cupertino.dart';
2   import 'package:flutter/material.dart';
3   import 'package:geolocator/geolocator.dart';
4   import 'package:parse_server_sdk_flutter/parse_server_sdk.dart';
5
6   void main() async {
7     WidgetsFlutterBinding.ensureInitialized();
8
9     final keyApplicationId = 'YOUR_APP_ID_HERE';
10    final keyClientKey = 'YOUR_CLIENT_KEY_HERE';
11
12    final keyParseServerUrl = 'https://parseapi.back4app.com';
13
14    await Parse().initialize(keyApplicationId, keyParseServerUrl,
15        clientKey: keyClientKey, debug: true);
16
17    runApp(MaterialApp(
18      title: 'Flutter - GeoPoint',
19      debugShowCheckedModeBanner: false,
20      home: HomePage(),
21    ));
22  }
23  
24  class HomePage extends StatefulWidget {
25    @override
26    _HomePageState createState() => _HomePageState();
27  }
28
29  class _HomePageState extends State<HomePage> {
30    List<ParseObject> results = <ParseObject>[];
31    double selectedDistance = 3000;
32
33    Future<Position> getCurrentPosition() async {
34      bool serviceEnabled;
35      LocationPermission permission;
36  
37      // Test if location services are enabled.
38      serviceEnabled = await Geolocator.isLocationServiceEnabled();
39      if (!serviceEnabled) {
40        return Future.error('Location services are disabled.');
41      }
42
43      permission = await Geolocator.checkPermission();
44      if (permission == LocationPermission.denied) {
45        permission = await Geolocator.requestPermission();
46        if (permission == LocationPermission.denied) {
47          return Future.error('Location permissions are denied');
48        }
49      }
50
51      if (permission == LocationPermission.deniedForever) {
52        return Future.error(
53            'Location permissions are permanently denied, we cannot request permissions.');
54      }
55
56      // When we reach here, permissions are granted and we can
57      // continue accessing the position of the device.
58      return await Geolocator.getCurrentPosition();
59    }
60  
61    void doQueryNear() async {
62      // Create your query
63      final QueryBuilder<ParseObject> parseQuery =
64          QueryBuilder<ParseObject>(ParseObject('City'));
65  
66      // Get current position from device
67      final position = await getCurrentPosition();
68
69      final currentGeoPoint = ParseGeoPoint(
70          latitude: position.latitude, longitude: position.longitude);
71
72      // `whereNear` will order results based on distance between the GeoPoint
73      // type field from the class and the GeoPoint argument
74      parseQuery.whereNear('location', currentGeoPoint);
75  
76      // The query will resolve only after calling this method, retrieving
77      // an array of `ParseObjects`, if success
78      final ParseResponse apiResponse = await parseQuery.query();
79  
80      if (apiResponse.success && apiResponse.results != null) {
81        // Let's show the results
82        for (var o in apiResponse.results! as List<ParseObject>) {
83          print(
84              'City: ${o.get<String>('name')} - Location: ${o.get<ParseGeoPoint>('location')!.latitude}, ${o.get<ParseGeoPoint>('location')!.longitude}');
85        }
86  
87        setState(() {
88          results = apiResponse.results as List<ParseObject>;
89        });
90      } else {
91        setState(() {
92          results.clear();
93        });
94      }
95   }
96  
97    void doQueryInKilometers() async {
98      // Create your query
99      final QueryBuilder<ParseObject> parseQuery =
100         QueryBuilder<ParseObject>(ParseObject('City'));
101 
102     // Get current position from device
103     final position = await getCurrentPosition();
104 
105     final currentGeoPoint = ParseGeoPoint(
106         latitude: position.latitude, longitude: position.longitude);
107 
108     // You can also use `whereWithinMiles` and `whereWithinRadians` the same way,
109     // but with different measuring unities
110     parseQuery.whereWithinKilometers(
111         'location', currentGeoPoint, selectedDistance);
112
113     // The query will resolve only after calling this method, retrieving
114     // an array of `ParseObjects`, if success
115     final ParseResponse apiResponse = await parseQuery.query();
116 
117     if (apiResponse.success && apiResponse.results != null) {
118       // Let's show the results
119       for (var o in apiResponse.results! as List<ParseObject>) {
120         print(
121             'City: ${o.get<String>('name')} - Location: ${o.get<ParseGeoPoint>('location')!.latitude}, ${o.get<ParseGeoPoint>('location')!.longitude}');
122       }
123
124       setState(() {
125         results = apiResponse.results as List<ParseObject>;
126       });
127     } else {
128       setState(() {
129         results.clear();
130       });
131     }
132   }
133
134   void doQueryInMiles() async {
135     // Create your query
136     final QueryBuilder<ParseObject> parseQuery =
137         QueryBuilder<ParseObject>(ParseObject('City'));
138 
139     // Get current position from device
140     final position = await getCurrentPosition();
141 
142     final currentGeoPoint = ParseGeoPoint(
143         latitude: position.latitude, longitude: position.longitude);
144 
145     // You can also use `whereWithinKilometers` and `whereWithinRadians` the same way,
146     parseQuery.whereWithinMiles('location', currentGeoPoint, selectedDistance);
147 
148     // The query will resolve only after calling this method, retrieving
149     // an array of `ParseObjects`, if success
150     final ParseResponse apiResponse = await parseQuery.query();
151 
152     if (apiResponse.success && apiResponse.results != null) {
153     // Let's show the results
154       for (var o in apiResponse.results! as List<ParseObject>) {
155         print(
156             'City: ${o.get<String>('name')} - Location: ${o.get<ParseGeoPoint>('location')!.latitude}, ${o.get<ParseGeoPoint>('location')!.longitude}');
157       }
158
159       setState(() {
160         results = apiResponse.results as List<ParseObject>;
161       });
162     } else {
163       setState(() {
164         results.clear();
165       });
166     }
167   }
168 
169   void doClearResults() async {
170     setState(() {
171       results = [];
172     });
173   }
174 
175   @override
176   Widget build(BuildContext context) {
177     return Scaffold(
178         body: Padding(
179       padding: const EdgeInsets.all(16.0),
180       child: Column(
181         crossAxisAlignment: CrossAxisAlignment.stretch,
182         children: [
183           Container(
184             height: 200,
185             child: Image.network(
186                 'https://blog.back4app.com/wp-content/uploads/2017/11/logo-b4a-1-768x175-1.png'),
187           ),
188           Center(
189             child: const Text('Flutter on Back4app - GeoPoint',
190                 style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
191           ),
192           SizedBox(
193             height: 8,
194           ),
195           Container(
196             height: 50,
197             child: ElevatedButton(
198                 onPressed: doQueryNear,
199                 child: Text('Query Near'),
200                 style: ElevatedButton.styleFrom(primary: Colors.blue)),
201           ),
202           SizedBox(
203             height: 16,
204           ),
205           Center(child: Text('Distance')),
206           Slider(
207             value: selectedDistance,
208             min: 0,
209             max: 10000,
210             divisions: 10,
211             onChanged: (value) {
212               setState(() {
213                 selectedDistance = value;
214               });
215             },
216             label: selectedDistance.toStringAsFixed(0),
217           ),
218           SizedBox(
219             height: 8,
220           ),
221           Container(
222             height: 50,
223             child: ElevatedButton(
224                 onPressed: doQueryInKilometers,
225                 child: Text('Query in Kilometers'),
226                 style: ElevatedButton.styleFrom(primary: Colors.blue)),
227           ),
228           SizedBox(
229             height: 8,
230           ),
231           Container(
232             height: 50,
233             child: ElevatedButton(
234                 onPressed: doQueryInMiles,
235                 child: Text('Query Miles'),
236                 style: ElevatedButton.styleFrom(primary: Colors.blue)),
237           ),
238           SizedBox(
239             height: 8,
240           ),
241           Container(
242             height: 50,
243             child: ElevatedButton(
244                 onPressed: doClearResults,
245                 child: Text('Clear results'),
246                 style: ElevatedButton.styleFrom(primary: Colors.blue)),
247           ),
248           SizedBox(
249             height: 8,
250           ),
251           Text(
252             'Result List: ${results.length}',
253           ),
254           Expanded(
255             child: ListView.builder(
256                 itemCount: results.length,
257                 itemBuilder: (context, index) {
258                   final o = results[index];
259                   return Container(
260                     padding: const EdgeInsets.all(4),
261                     decoration:
262                         BoxDecoration(border: Border.all(color: Colors.black)),
263                     child: Text(
264                         '${o.get<String>('name')} \nLocation: ${o.get<ParseGeoPoint>('location')!.latitude}, ${o.get<ParseGeoPoint>('location')!.longitude}'),
265                   );
266                 }),
267           )
268         ],
269       ),
270     ));
271   }
272 }
```

Find your Application Id and Client Key credentials navigating to your app Dashboard at [**Back4App Website**](https://www.back4app.com/).

Update your code in main.dart with the values of your project’s ApplicationId and ClientKey in Back4app.

- **keyApplicationId = App Id**
- **keyClientKey = Client Key**

Run the project, and the app will load as shown in the image.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/m8MRUzwQA1gerzIsCY8oA_image.png" signedSrc size="30" width="318" height="629" position="center" caption}

## Conclusion

At the end of this guide, you learned how GeoPoint data queries work on Parse and how to perform them on Back4App from a Flutter App.
