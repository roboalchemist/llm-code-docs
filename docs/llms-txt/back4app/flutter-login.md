# Source: https://docs-containers.back4app.com/docs/flutter/parse-sdk/users/flutter-login.md

---
title: User Login
slug: docs/flutter/parse-sdk/users/flutter-login
description: In this guide you learn how login/logout users in Parse using Flutter plugin for Parse Server
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-18T13:24:43.792Z
updatedAt: 2025-01-16T20:37:10.208Z
---

# User Login and Logout for Flutter using Parse Server

## Introduction

After implementing the User Registration for Flutter on Parse in the last guide, you will learn how to login and logout users using the same ParseUser class. After a Signup, the login operation is performed automatically, and a new user session is created. The Logout operation deletes the active Session object for the logged user.

In this guide, you will learn how to use the **Flutter plugin for Parse Server** to perform login/logout using ParseUser class for your Flutter App.

## Goal

To build a User Login/Logout feature using Parse for a Flutter App.

## Prerequisites

**To complete this tutorial, you will need:**

:::hint{type="info"}
- [**Flutter version 2.2.x or later**](https://flutter.dev/docs/get-started/install)
- [**Android Studio&#x20;**](https://developer.android.com/studio)or [**VS Code installed**](https://code.visualstudio.com/) (with [**Plugins**](https://docs.flutter.dev/get-started/editor) Dart and Flutter)
- An app [**created**](https://www.back4app.com/docs/get-started/new-parse-app) on Back4App:
  - **Note:&#x20;**&#x46;ollow the [**New Parse App Tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse App on Back4App.
- An Flutter app connected to Back4app.
  - **Note:&#x20;**&#x46;ollow the [**Install Parse SDK on Flutter project**](https://www.back4app.com/docs/flutter/parse-sdk/parse-flutter-sdk) to create an Flutter Project connected to Back4App.
- Complete the previous guide so you can have a better understanding of the ParseUser class.
- A device (or virtual device) running Android or iOS.
:::

## Understanding the Login/Logout App

To better understand the Login/SingOut process, we will create an app to login e logout user on your account.

We won’t explain the Flutter application code once this guide’s primary focus is using the Flutter with Parse. Following the next steps, you will build a Login e Logout App at Back4App Database.

## Let’s get started!

In the following steps, you will be able to build a Login/Logout App.

## 1 - Create the Login/Logout App Template

Open your Flutter project from the previous guide **Flutter plugin for Parse Server**. Go to the main.dart file, clean up all the code, and replace it with:

```dart
1   import 'package:flutter/material.dart';
2   import 'package:parse_server_sdk_flutter/parse_server_sdk.dart';
3
4   void main() async {
5     WidgetsFlutterBinding.ensureInitialized();
6 
7     final keyApplicationId = 'YOUR_APP_ID_HERE';
8     final keyClientKey = 'YOUR_CLIENT_KEY_HERE';
9     final keyParseServerUrl = 'https://parseapi.back4app.com';
10
11    await Parse().initialize(keyApplicationId, keyParseServerUrl,
12        clientKey: keyClientKey, debug: true);
13
14    runApp(MyApp());
15  }
16
17  class MyApp extends StatelessWidget {
18    @override
19    Widget build(BuildContext context) {
20      return MaterialApp(
21        title: 'Flutter Login/Logout',
22        theme: ThemeData(
23          primarySwatch: Colors.blue,
24          visualDensity: VisualDensity.adaptivePlatformDensity,
25        ),
26        home: HomePage(),
27      );
28    }
29  }
30  
31  class HomePage extends StatefulWidget {
32    @override
33    _HomePageState createState() => _HomePageState();
34  }
35  
36  class _HomePageState extends State<HomePage> {
37    final controllerUsername = TextEditingController();
38    final controllerPassword = TextEditingController();
39    bool isLoggedIn = false;
40  
41    @override
42    Widget build(BuildContext context) {
43      return Scaffold(
44          appBar: AppBar(
45            title: const Text('Flutter Login/Logout'),
46          ),
47          body: Center(
48            child: SingleChildScrollView(
49              padding: const EdgeInsets.all(8),
50              child: Column(
51                crossAxisAlignment: CrossAxisAlignment.stretch,
52                children: [
53                  Container(
54                    height: 200,
55                    child: Image.network(
56                        'http://blog.back4app.com/wp-content/uploads/2017/11/logo-b4a-1-768x175-1.png'),
57                  ),
58                  Center(
59                    child: const Text('Flutter on Back4App',
60                        style:
61                            TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
62                  ),
63                  SizedBox(
64                    height: 16,
65                  ),
66                  Center(
67                    child: const Text('User Login/Logout',
68                        style: TextStyle(fontSize: 16)),
69                  ),
70                  SizedBox(
71                    height: 16,
72                  ),
73                  TextField(
74                    controller: controllerUsername,
75                    enabled: !isLoggedIn,
76                    keyboardType: TextInputType.text,
77                    textCapitalization: TextCapitalization.none,
78                    autocorrect: false,
79                    decoration: InputDecoration(
80                        border: OutlineInputBorder(
81                            borderSide: BorderSide(color: Colors.black)),
82                        labelText: 'Username'),
83                  ),
84                  SizedBox(
85                    height: 8,
86                  ),
87                  TextField(
88                    controller: controllerPassword,
89                    enabled: !isLoggedIn,
90                    obscureText: true,
91                    keyboardType: TextInputType.text,
92                    textCapitalization: TextCapitalization.none,
93                    autocorrect: false,
94                    decoration: InputDecoration(
95                        border: OutlineInputBorder(
96                            borderSide: BorderSide(color: Colors.black)),
97                        labelText: 'Password'),
98                  ),
99                  SizedBox(
100                   height: 16,
101                 ),
102                 Container(
103                   height: 50,
104                   child: TextButton(
105                     child: const Text('Login'),
106                     onPressed: isLoggedIn ? null : () => doUserLogin(),
107                   ),
108                 ),
109                 SizedBox(
110                   height: 16,
111                 ),
112                 Container(
113                  height: 50,
114                   child: TextButton(
115                     child: const Text('Logout'),
116                     onPressed: !isLoggedIn ? null : () => doUserLogout(),
117                   ),
118                 )
119               ],
120             ),
121           ),
122         ));
123   }
124 
125   void showSuccess(String message) {
126     showDialog(
127       context: context,
128       builder: (BuildContext context) {
129         return AlertDialog(
130           title: const Text("Success!"),
131           content: Text(message),
132           actions: <Widget>[
133             new TextButton(
134               child: const Text("OK"),
135               onPressed: () {
136                 Navigator.of(context).pop();
137               },
138             ),
139           ],
140         );
141       },
142     );
143   }
144 
145   void showError(String errorMessage) {
146     showDialog(
147       context: context,
148       builder: (BuildContext context) {
149         return AlertDialog(
150           title: const Text("Error!"),
151           content: Text(errorMessage),
152           actions: <Widget>[
153             new TextButton(
154               child: const Text("OK"),
155               onPressed: () {
156                 Navigator.of(context).pop();
157               },
158             ),
159           ],
160         );
161       },
162     );
163   }
164 
165   void doUserLogin() async {
166    
167   }
168 
169   void doUserLogout() async {
170    
171   }
172 }
173
```

:::hint{type="info"}
When debug parameter in function Parse().initialize is true, allows displaying Parse API calls on the console. This configuration can assist in debugging the code. It is advisable to disable debug in the release version.
:::

## 2 - Connect Template to Back4app Project

Find your Application Id and Client Key credentials navigating to your app Dashboard at [**Back4App Website**](https://www.back4app.com/).

Update your code in main.dart with the values of your project’s ApplicationId and ClientKey in Back4app.

- **keyApplicationId = App Id**
- **keyClientKey = Client Key**

Run the project, and the app will load as shown in the image.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/VE1p8XtbVl9YvxJ4oH470_image.png" signedSrc size="50" width="321" height="635" position="center" caption}

## 3 - Code for Login User

The User Login function creates a Session object, which points to the User logged in and stores in your local storage a valid user session.

Future calls to methods like currentUser will successfully retrieve your User data and sessionToken for Session object which created in the Dashboard.

Search for the function doUserLogin in the file main.dart. Replace the code inside doUserLogin with:

```dart
1   final username = controllerUsername.text.trim();
2       final password = controllerPassword.text.trim();
3
4       final user = ParseUser(username, password, null);
5 
6       var response = await user.login();
7
8       if (response.success) {
9         showSuccess("User was successfully login!");
10        setState(() {
11          isLoggedIn = true;
12        });
13      } else {
14        showError(response.error!.message);
15      }
```

To build this function, follow these steps:

1. Create a newParseUser class instance with the command ParseUser(username, password, null); using the data entered in the app. The e-mail field is not necessary and must be informed with null.
2. Call thelogin function, which will create a Session in your database in the Parse Dashboard and save the token to local storage
3. Check if the user login was successful. If it wasn’t successful, show the error description message.

The complete function should look like this:

```dart
1     void doUserLogin() async {
2       final username = controllerUsername.text.trim();
3       final password = controllerPassword.text.trim();
4
5       final user = ParseUser(username, password, null);
6
7       var response = await user.login();
8
9       if (response.success) {
10        showSuccess("User was successfully login!");
11        setState(() {
12          isLoggedIn = true;
13        });
14      } else {
15        showError(response.error!.message);
16      }
17    }
```

:::hint{type="info"}
To test it, click on the Run button in Android Studio/VSCode.
:::

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Z8Z2CgsB7YUKk4tJ91_4F_image.png" signedSrc size="50" width="321" height="635" position="center" caption}

After providing the desired user credentials, you will see this message after pressing on Login if everything was successful:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Bw7YyqHurBgLJCvBg9EYq_image.png" signedSrc size="50" width="321" height="635" position="center" caption}

Error handling can be tested if you try to login a user with invalid credentials:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/SaBJxLYqWUo9ua2rIN1O6_image.png" signedSrc size="50" width="321" height="635" position="center" caption}

You will get another error if you try to login with no password:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/odoAAZAaQk60dIyGy_g6m_image.png" signedSrc size="50" width="321" height="635" position="center" caption}

## 4 - Code for Logout User

The User Logout function deletes the Session object, which was created in the login function. It will clear this session on the device and log out of any linked services in your Parse server.

Search for the function doUserLogout in the file main.dart. Replace the code inside doUserLogout with:

```dart
1       final user = await ParseUser.currentUser() as ParseUser;
2       var response = await user.logout();
3
4       if (response.success) {
5         showSuccess("User was successfully logout!");
6         setState(() {
7           isLoggedIn = false;
8         });
9       } else {
10        showError(response.error!.message);
11      }
```

To build this function, follow these steps:

1. Get the current logged user using functionParseUser.currentUser().
2. Call thelogout function for ParseUser object, which will delete Session in your database and clean the token in the local storage.
3. Check if the user logout was successfull. If it wasn’t successful, show the error description message.

The complete code should look like this:

```dart
1     void doUserLogout() async {
2       final user = await ParseUser.currentUser() as ParseUser;
3       var response = await user.logout();
4   
5       if (response.success) {
6         showSuccess("User was successfully logout!");
7         setState(() {
8           isLoggedIn = false;
9         });
10      } else {
11        showError(response.error!.message);
12      }
13    }
```

:::hint{type="info"}
To test it, click on the Run button in Android Studio/VSCode.
:::

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/6T1LA_tKJ9CZ15grhE7Vj_image.png" signedSrc size="50" width="321" height="635" position="center" caption}

After providing the desired user credentials, you will see this message after pressing on Login if everything was successful:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/GBTX41Q1jYmHMHrKfTGU2_image.png" signedSrc size="50" width="321" height="635" position="center" caption}

Click the “Logout” button:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Yq2P3Vt15tCf75963iJZv_image.png" signedSrc size="50" width="321" height="635" position="center" caption}

## It’s done!

At the end of this guide, you can login and logout Parse Users of your app using Parse Server core features through Back4App!
