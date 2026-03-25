# Source: https://docs-containers.back4app.com/docs/flutter/parse-sdk/flutter-save-file.md

---
title: Files
slug: docs/flutter/parse-sdk/flutter-save-file
description: In this guide you'll learn save and read files in Back4App on your Flutter App
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-18T15:10:02.884Z
updatedAt: 2025-01-16T20:37:35.493Z
---

# Save Files from a Flutter App

## Introduction

Sometimes applications need to store data that is often too large to be stored inside a ParseObject. The most common use case is storing images, but you can also use it for documents, videos, music, and other binary data.

To store a file on Parse, you should always associate the file with another data object so you can retrieve this file path when querying the object. If you do not associate, the file will be stored, but you will not find them on the Cloud.
Another important tip is to give a name to the file that has a file extension. This extension lets Parse figure out the file type and handle it accordingly. We should also mention that each upload gets a unique identifier, so there’s no problem uploading multiple files using the same name.

In Flutter, ParseFile and ParseWebFile let you store and retrieve application files in the Cloud that would. This guide explains how to store and retrieve files in your Flutter App to manage Back4app cloud storage.

:::hint{type="danger"}
- If you do not associate your file to a data object the file will become an orphan file and you wont be able to find it on Back4App Cloud.
:::

::embed[]{url="https://www.youtube.com/embed/C2XQGks2ivA"}

## Prerequisites

:::hint{type="info"}
- An app [**created**](https://www.back4app.com/docs/get-started/new-parse-app) on Back4App:
  - **Note:&#x20;**&#x46;ollow the [**New Parse App Tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse App on Back4App.
- An Flutter app connected to Back4app.
  - **Note:&#x20;**&#x46;ollow the [**Install Parse SDK on Flutter project**](https://www.back4app.com/docs/flutter/parse-sdk/parse-flutter-sdk) to create an Flutter Project connected to Back4App.
- A device (or virtual device) running Android or iOS.
- In order to run this guide example you should set up the plugin [**image\_picker**](https://pub.dev/packages/image_picker) properly. Do not forget to add permissions for iOS in order to access images stored in device. \{: .btn target=”\_blank” rel=”nofollow”}. Carefully read the instructions for setting up the Android and iOS project.
:::

## Goal

Create an Flutter Gallery App that uploads and displays images from Back4app.

## 1 - Understanding ParseFile and ParseWebFile class

There are three different file classes in this Parse SDK for Flutter

- ParseFileBaseis an abstract class, the foundation of every file class that this SDK can handle.
- ParseFileextends ParseFileBase and is by default used as the file class on every platform (not valid for web). This class uses a File from dart\:io for storing the raw file.
- ParseWebFileis the equivalent to ParseFile used at Flutter Web. This class uses an Uint8List for storing the raw file.

The methods available on ParseFileBase to manipulate files:

- save()or upload() for save file on Cloud
- download()for retrive file and store in local storage

There are properties to get information from the saved file:

- url: Gets the file url. It is only available after you save the file or after you get the file from a Parse.Object.
- name: Gets the file name. This is the filename given by the user before calling the save() method. After callint the method, the property receives a unique identifier.

## 2 - Uploading an Image

To upload an image, you will only need to create a ParseFileBase instance and then call the save method.

Let’s do that in our upload function:

```javascript
1         ParseFileBase? parseFile;
2
3         if (kIsWeb) {
4           //Flutter Web
5           parseFile = ParseWebFile(
6               await pickedFile!.readAsBytes(),
7               name: 'image.jpg'); //Name for file is required
8         } else {
9           //Flutter Mobile/Desktop
10          parseFile = ParseFile(File(pickedFile!.path));
11        }
12        await parseFile.save();
```

The above snippet creates and saves the image, and after the save completes, we associate it with a ParseObject called Gallery.

```javascript
1      final gallery = ParseObject('Gallery')
2        ..set('file', parseFile);
3      await gallery.save();
```

## 3 - Displaying Images

To display images, you need to get the image’s URL.

To upload an image, you will only need to create a ParseFileBase instance and then call the save method.

```javascript
1       ParseFileBase? varFile = parseObject.get<ParseFileBase>('file');
2
3       return Image.network(
4         varFile!.url!,
5         width: 200,
6         height: 200,
7         fit: BoxFit.fitHeight,
8       );
```

## 4 - Upload and Retrieve from Flutter App

Let’s now use our example for uploading and displaying images in Flutter App, with a simple interface.

Open your Flutter project, go to the main.dart file, clean up all the code, and replace it with:

```dart
1   import 'dart:io';
2
3   import 'package:flutter/cupertino.dart';
4   import 'package:flutter/foundation.dart';
5   import 'package:flutter/material.dart';
6   import 'package:image_picker/image_picker.dart';
7   import 'package:parse_server_sdk_flutter/parse_server_sdk.dart';
8
9   void main() async {
10    WidgetsFlutterBinding.ensureInitialized();
11
12    final keyApplicationId = 'YOUR_APP_ID_HERE';
13    final keyClientKey = 'YOUR_CLIENT_KEY_HERE';
14
15    final keyParseServerUrl = 'https://parseapi.back4app.com';
16
17    await Parse().initialize(keyApplicationId, keyParseServerUrl,
18        clientKey: keyClientKey, debug: true);
19
20    runApp(MaterialApp(
21      title: 'Flutter - Storage File',
22      debugShowCheckedModeBanner: false,
23      home: HomePage(),
24    ));
25  }
26  
27  class HomePage extends StatefulWidget {
28    @override
29    _HomePageState createState() => _HomePageState();
30  }
31  
32  class _HomePageState extends State<HomePage> {
33    PickedFile? pickedFile;
34 
35    List<ParseObject> results = <ParseObject>[];
36    double selectedDistance = 3000;
37
38    @override
39    Widget build(BuildContext context) {
40      return Scaffold(
41          body: Padding(
42        padding: const EdgeInsets.all(16.0),
43        child: Column(
44          crossAxisAlignment: CrossAxisAlignment.stretch,
45          children: [
46            Container(
47              height: 200,
48              child: Image.network(
49                  'https://blog.back4app.com/wp-content/uploads/2017/11/logo-b4a-1-768x175-1.png'),
50            ),
51            SizedBox(
52              height: 16,
53            ),
54            Center(
55              child: const Text('Flutter on Back4app - Save File',
56                  style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
57            ),
58            SizedBox(
59              height: 16,
60            ),
61            Container(
62              height: 50,
63              child: ElevatedButton(
64                child: Text('Upload File'),
65                style: ElevatedButton.styleFrom(primary: Colors.blue),
66                onPressed: () {
67                  Navigator.push(
68                    context,
69                    MaterialPageRoute(builder: (context) => SavePage()),
70                  );
71                },
72              ),
73            ),
74            SizedBox(
75              height: 8,
76            ),
77            Container(
78                height: 50,
79                child: ElevatedButton(
80                  child: Text('Display File'),
81                  style: ElevatedButton.styleFrom(primary: Colors.blue),
82                  onPressed: () {
83                    Navigator.push(
84                      context,
85                      MaterialPageRoute(builder: (context) => DisplayPage()),
86                    );
87                  },
88                ))
89          ],
90        ),
91      ));
92    }
93  }
94  
95  class SavePage extends StatefulWidget {
96    @override
97    _SavePageState createState() => _SavePageState();
98  }
99
100 class _SavePageState extends State<SavePage> {
101   PickedFile? pickedFile;
102   bool isLoading = false;
103 
104   @override
105   Widget build(BuildContext context) {
106     return Scaffold(
107       appBar: AppBar(
108         title: Text('Upload Fie'),
109       ),
110       body: Padding(
111         padding: const EdgeInsets.all(12.0),
112         child: Column(
113           crossAxisAlignment: CrossAxisAlignment.stretch,
114           children: [
115             SizedBox(height: 16),
116             GestureDetector(
117               child: pickedFile != null
118                   ? Container(
119                       width: 250,
120                       height: 250,
121                       decoration:
122                           BoxDecoration(border: Border.all(color: Colors.blue)),
123                       child: kIsWeb
124                           ? Image.network(pickedFile!.path)
125                           : Image.file(File(pickedFile!.path)))
126                   : Container(
127                       width: 250,
128                       height: 250,
129                       decoration:
130                           BoxDecoration(border: Border.all(color: Colors.blue)),
131                       child: Center(
132                         child: Text('Click here to pick image from Gallery'),
133                       ),
134                     ),
135               onTap: () async {
136                 PickedFile? image =
137                     await ImagePicker().getImage(source: ImageSource.gallery);
138 
139                 if (image != null) {
140                   setState(() {
141                     pickedFile = image;
142                   });
143                 }
144               },
145             ),
146             SizedBox(height: 16),
147             Container(
148                 height: 50,
149                 child: ElevatedButton(
150                   child: Text('Upload file'),
151                   style: ElevatedButton.styleFrom(primary: Colors.blue),
152                   onPressed: isLoading || pickedFile == null
153                       ? null
154                       : () async {
155                           setState(() {
156                             isLoading = true;
157                           });
158                           ParseFileBase? parseFile;
159 
160                           if (kIsWeb) {
161                             //Flutter Web
162                             parseFile = ParseWebFile(
163                                 await pickedFile!.readAsBytes(),
164                                 name: 'image.jpg'); //Name for file is required
165                           } else {
166                             //Flutter Mobile/Desktop
167                             parseFile = ParseFile(File(pickedFile!.path));
168                           }
169                           await parseFile.save();
170 
171                           final gallery = ParseObject('Gallery')
172                             ..set('file', parseFile);
173                           await gallery.save();
174
175                           setState(() {
176                             isLoading = false;
177                             pickedFile = null;
178                           });
179 
180                           ScaffoldMessenger.of(context)
181                             ..removeCurrentSnackBar()
182                             ..showSnackBar(SnackBar(
183                               content: Text(
184                                 'Save file with success on Back4app',
185                                 style: TextStyle(
186                                   color: Colors.white,
187                                 ),
188                               ),
189                               duration: Duration(seconds: 3),
190                               backgroundColor: Colors.blue,
191                             ));
192                         },
193                 ))
194           ],
195         ),
196       ),
197     );
198   }
199 }
200
201 class DisplayPage extends StatefulWidget {
202   @override
203   _DisplayPageState createState() => _DisplayPageState();
204 }
205
206 class _DisplayPageState extends State<DisplayPage> {
207   @override
208   Widget build(BuildContext context) {
209     return Scaffold(
210       appBar: AppBar(
211         title: Text("Display Gallery"),
212       ),
213       body: FutureBuilder<List<ParseObject>>(
214           future: getGalleryList(),
215           builder: (context, snapshot) {
216             switch (snapshot.connectionState) {
217               case ConnectionState.none:
218               case ConnectionState.waiting:
219                 return Center(
220                   child: Container(
221                       width: 100,
222                       height: 100,
223                       child: CircularProgressIndicator()),
224                 );
225               default:
226                 if (snapshot.hasError) {
227                   return Center(
228                     child: Text("Error..."),
229                   );
230                 } else {
231                   return ListView.builder(
232                       padding: const EdgeInsets.only(top: 8),
233                       itemCount: snapshot.data!.length,
234                       itemBuilder: (context, index) {
235                         //Web/Mobile/Desktop
236                        ParseFileBase? varFile =
237                             snapshot.data![index].get<ParseFileBase>('file');
238 
239                         //Only iOS/Android/Desktop
240                         /*
241                         ParseFile? varFile =
242                             snapshot.data![index].get<ParseFile>('file');
243                         */
244                         return Image.network(
245                           varFile!.url!,
246                           width: 200,
247                           height: 200,
248                           fit: BoxFit.fitHeight,
249                         );
250                       });
251                 }
252             }
253           }),
254     );
255   }
256 
257   Future<List<ParseObject>> getGalleryList() async {
258     QueryBuilder<ParseObject> queryPublisher =
259         QueryBuilder<ParseObject>(ParseObject('Gallery'))
260           ..orderByAscending('createdAt');
261     final ParseResponse apiResponse = await queryPublisher.query();
262 
263     if (apiResponse.success && apiResponse.results != null) {
264       return apiResponse.results as List<ParseObject>;
265     } else {
266       return [];
267     }
268   }
269 }
```

Find your ApplicationId and Client Key credentials navigating to your app Dashboard->Settings->Security and Keys at [**Back4App Website**](https://www.back4app.com/).

Update your code in main.dart with BOTH values of your project’s ApplicationId and ClientKey in Back4app.

- keyApplicationId = AppId
- keyClientKey = Client Key

Run the project, and the app will load as shown in the image.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/SeiDfLamRqJFys0hfz8xh_image.png" signedSrc size="50" width="320" height="638" position="center" caption}

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/vkn0AimenNqVuC0LWgWVP_image.png" signedSrc size="50" width="320" height="638" position="center" caption}

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/gVi8ZXJg-N0luCP83yayN_image.png" signedSrc size="50" width="320" height="638" position="center" caption}

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/SJhjGyiemfZxKoOMICKBE_image.png" signedSrc size="50" width="320" height="638" position="center" caption}

## Conclusion

At this point, you have uploaded image on Back4App and displayed it in a Flutter application.
