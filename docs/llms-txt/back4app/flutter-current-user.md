# Source: https://docs-containers.back4app.com/docs/flutter/parse-sdk/users/flutter-current-user.md

---
title: Current User
slug: docs/flutter/parse-sdk/users/flutter-current-user
description: In this guide you will learn how get current user on session using Flutter plugin for Parse Server
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-18T14:31:21.671Z
updatedAt: 2025-01-16T20:37:20.790Z
---

# Get current User on session

## Introduction

It would not be enjoyable if the user had to log in every time they open your app. You can avoid this by using the cached current ParseUser object. Whenever you use any signup or login methods, the user is cached locally. You can manage this cache as a session, and automatically assume the user is logged in.
In this guide, you will learn how to use the **Flutter plugin for Parse Server** to get current User on session using ParseUser class for your Flutter App.

## Goal

Get current User on session using Parse for a Flutter App.

## Prerequisites

**To complete this tutorial, you will need:**

:::hint{type="info"}
- [**Flutter version 2.2.x or later**](https://flutter.dev/docs/get-started/install)
- [**Android Studio&#x20;**](https://developer.android.com/studio)or [**VS Code installed**](https://code.visualstudio.com/) (with [**Plugins**](https://docs.flutter.dev/get-started/editor) Dart and Flutter)
- A Flutter app created and connected to Back4App.
  - **Note:&#x20;**&#x46;ollow the [**Install Parse SDK on Flutter project**](https://www.back4app.com/docs/flutter/parse-sdk/parse-flutter-sdk) to create an Flutter Project connected to Back4App.
- Complete the previous guide so ou can have a better understanding of the ParseUser class.
- A device (not Simulator) running Android or iOS.
:::

## Understanding the Get Current User App

To better understand the get current User on session process, we will create an app to signUp, login e logout a user. The application is similar to the previous guide, where we perform the signup, login, and logout. As we’re going to use the same project in the following guides, you can find some not yet available functions.
We won’t explain the Flutter application code once this guide’s primary focus is using the Flutter with Parse. Following the next steps, you will build a Login e Logout App at Back4App Database.

## Let’s get started!

In the following steps, you will be able to build app a get current user.

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
12        clientKey: keyClientKey,
13        debug: true);
14
15    runApp(MyApp());
16  }
17
18  class MyApp extends StatelessWidget {
19    Future<bool> hasUserLogged() async {
20      return Future.value(false);
21    }
22
23    @override
24    Widget build(BuildContext context) {
25      return MaterialApp(
26        title: 'Flutter - Parse Server',
27        theme: ThemeData(
28          primarySwatch: Colors.blue,
29          visualDensity: VisualDensity.adaptivePlatformDensity,
30        ),
31        home: FutureBuilder<bool>(
32            future: hasUserLogged(),
33            builder: (context, snapshot) {
34              switch (snapshot.connectionState) {
35                case ConnectionState.none:
36                case ConnectionState.waiting:
37                  return Scaffold(
38                    body: Center(
39                      child: Container(
40                          width: 100,
41                          height: 100,
42                          child: CircularProgressIndicator()),
43                    ),
44                  );
45                default:
46                  if (snapshot.hasData && snapshot.data!) {
47                    return UserPage();
48                  } else {
49                    return LoginPage();
50                  }
51              }
52            }),
53      );
54    }
55  }
56
57  class LoginPage extends StatefulWidget {
58    @override
59    _LoginPageState createState() => _LoginPageState();
60  }
61
62  class _LoginPageState extends State<LoginPage> {
63    final controllerUsername = TextEditingController();
64    final controllerPassword = TextEditingController();
65    bool isLoggedIn = false;
66
67    @override
68    Widget build(BuildContext context) {
69      return Scaffold(
70          appBar: AppBar(
71            title: const Text('Flutter - Parse Server'),
72          ),
73          body: Center(
74            child: SingleChildScrollView(
75              padding: const EdgeInsets.all(8),
76              child: Column(
77                crossAxisAlignment: CrossAxisAlignment.stretch,
78                children: [
79                  Container(
80                    height: 200,
81                    child: Image.network(
82                        'https://blog.back4app.com/wp-content/uploads/2017/11/logo-b4a-1-768x175-1.png'),
83                  ),
84                  Center(
85                    child: const Text('Flutter on Back4App',
86                        style:
87                            TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
88                  ),
89                  SizedBox(
90                    height: 16,
91                  ),
92                  TextField(
93                    controller: controllerUsername,
94                    enabled: !isLoggedIn,
95                    keyboardType: TextInputType.text,
96                    textCapitalization: TextCapitalization.none,
97                    autocorrect: false,
98                    decoration: InputDecoration(
99                        border: OutlineInputBorder(
100                           borderSide: BorderSide(color: Colors.black)),
101                       labelText: 'Username'),
102                 ),
103                 SizedBox(
104                   height: 8,
105                 ),
106                 TextField(
107                   controller: controllerPassword,
108                   enabled: !isLoggedIn,
109                   obscureText: true,
110                   keyboardType: TextInputType.text,
111                   textCapitalization: TextCapitalization.none,
112                   autocorrect: false,
113                   decoration: InputDecoration(
114                       border: OutlineInputBorder(
115                           borderSide: BorderSide(color: Colors.black)),
116                       labelText: 'Password'),
117                 ),
118                 SizedBox(
119                   height: 16,
120                 ),
121                 Container(
122                   height: 50,
123                   child: ElevatedButton(
124                     child: const Text('Login'),
125                     onPressed: isLoggedIn ? null : () => doUserLogin(),
126                   ),
127                 ),
128                 SizedBox(
129                   height: 16,
130                 ),
131                 Container(
132                   height: 50,
133                   child: ElevatedButton(
134                     child: const Text('Sign Up'),
135                     onPressed: () => navigateToSignUp(),
136                   ),
137                 ),
138                 SizedBox( 
139                   height: 16,
140                 ),
141                 Container(
142                   height: 50,
143                   child: ElevatedButton(
144                     child: const Text('Reset Password'),
145                     onPressed: () => navigateToResetPassword(),
146                   ),
147                 )
148               ),
149            ),
150          ),
151        ));
152  }
153
154  void doUserLogin() async {
155    final username = controllerUsername.text.trim();
156    final password = controllerPassword.text.trim();
157
158    final user = ParseUser(username, password, null);
159
160    var response = await user.login();
161
162    if (response.success) {
163      navigateToUser();
164    } else {
165      Message.showError(context: context, message: response.error!.message);
166    }
167  }
168
169  void navigateToUser() {
170    Navigator.pushAndRemoveUntil(
171      context,
172      MaterialPageRoute(builder: (context) => UserPage()),
173      (Route<dynamic> route) => false,
174    );
175  }
176
177  void navigateToSignUp() {
178    Navigator.push(
179      context,
180      MaterialPageRoute(builder: (context) => SignUpPage()),
181    );
182  }
183
184  void navigateToResetPassword() {
185    Navigator.push(
186      context,
187      MaterialPageRoute(builder: (context) => ResetPasswordPage()),
188    );
189  }
190 }
191
192 class SignUpPage extends StatefulWidget {
193  @override
194  _SignUpPageState createState() => _SignUpPageState();
195 }
196
197 class _SignUpPageState extends State<SignUpPage> {
198  final controllerUsername = TextEditingController();
199  final controllerPassword = TextEditingController();
200  final controllerEmail = TextEditingController();
201
202  @override
203  Widget build(BuildContext context) {
204    return Scaffold(
205        appBar: AppBar(
206          title: const Text('Flutter Sign Up'),
207        ),
208        body: Center(
209          child: SingleChildScrollView(
210            padding: const EdgeInsets.all(8),
211            child: Column(
212              crossAxisAlignment: CrossAxisAlignment.stretch,
213              children: [
214                Container(
215                  height: 200,
216                  child: Image.network(
217                      'https://blog.back4app.com/wp-content/uploads/2017/11/logo-b4a-1-768x175-1.png'),
218                ),
219                Center(
220                  child: const Text('Flutter on Back4App',
221                      style:
222                          TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
223                ),
224                SizedBox(
225                  height: 16,
226                ),
227                Center(
228                  child: const Text('User registration',
229                      style: TextStyle(fontSize: 16)),
230                ),
231                SizedBox(
232                  height: 16,
233                ),
234                TextField(
235                  controller: controllerUsername,
236                  keyboardType: TextInputType.text,
237                  textCapitalization: TextCapitalization.none,
238                  autocorrect: false,
239                  decoration: InputDecoration(
240                      border: OutlineInputBorder(
241                          borderSide: BorderSide(color: Colors.black)),
242                      labelText: 'Username'),
243                ),
244                SizedBox(
245                  height: 8,
246                ),
247                TextField(
248                  controller: controllerEmail,
249                  keyboardType: TextInputType.emailAddress,
250                  textCapitalization: TextCapitalization.none,
251                  autocorrect: false,
252                  decoration: InputDecoration(
253                      border: OutlineInputBorder(
254                          borderSide: BorderSide(color: Colors.black)),
255                      labelText: 'E-mail'),
256                ),
257                SizedBox(
258                  height: 8,
259                ),
260                TextField(
261                  controller: controllerPassword,
262                  obscureText: true,
263                  keyboardType: TextInputType.text,
264                  textCapitalization: TextCapitalization.none,
265                  autocorrect: false,
266                  decoration: InputDecoration(
267                      border: OutlineInputBorder(
268                          borderSide: BorderSide(color: Colors.black)),
269                      labelText: 'Password'),
270                ),
271                SizedBox(
272                  height: 8,
273                ),
274                Container(
275                  height: 50,
276                  child: ElevatedButton(
277                    child: const Text('Sign Up'),
278                    onPressed: () => doUserRegistration(),
279                  ),
280                )
281              ],
282            ),
283          ),
284        ));
285  }
286
287  void doUserRegistration() async {
288    final username = controllerUsername.text.trim();
289    final email = controllerEmail.text.trim();
290    final password = controllerPassword.text.trim();
291
292    final user = ParseUser.createUser(username, password, email);
293
294    var response = await user.signUp();
295
296    if (response.success) {
297      Message.showSuccess(
298          context: context,
299          message: 'User was successfully created!',
300          onPressed: () async {
301            Navigator.pushAndRemoveUntil(
302              context,
303              MaterialPageRoute(builder: (context) => UserPage()),
304              (Route<dynamic> route) => false,
305            );
306          });
307    } else {
308      Message.showError(context: context, message: response.error!.message);
309    }
310  }
311 }
312
313 class UserPage extends StatelessWidget {
314  ParseUser? currentUser;
315
316  Future<ParseUser?> getUser() async {
317  }
318
319  @override
320  Widget build(BuildContext context) {
321    void doUserLogout() async {
322      var response = await currentUser!.logout();
323      if (response.success) {
324        Message.showSuccess(
325            context: context,
326            message: 'User was successfully logout!',
327            onPressed: () {
328              Navigator.pushAndRemoveUntil(
329                context,
330                MaterialPageRoute(builder: (context) => LoginPage()),
331                (Route<dynamic> route) => false,
332              );
333            });
334      } else {
335        Message.showError(context: context, message: response.error!.message);
336      }
337    }
338
339    return Scaffold(
340        appBar: AppBar(
341          title: Text('User logged in - Current User'),
342        ),
343        body: FutureBuilder<ParseUser?>(
344            future: getUser(),
345            builder: (context, snapshot) {
346              switch (snapshot.connectionState) {
347                case ConnectionState.none:
348                case ConnectionState.waiting:
349                  return Center(
350                    child: Container(
351                        width: 100,
352                        height: 100,
353                        child: CircularProgressIndicator()),
354                  );
355                default:
356                  return Padding(
357                    padding: const EdgeInsets.all(8.0),
358                    child: Column(
359                      crossAxisAlignment: CrossAxisAlignment.stretch,
360                      mainAxisAlignment: MainAxisAlignment.center,
361                      children: [
362                        Center(
363                            child: Text('Hello, ${snapshot.data!.username}')),
364                        SizedBox(
365                          height: 16,
366                        ),
367                        Container(
368                          height: 50,
369                          child: ElevatedButton(
370                            child: const Text('Logout'),
371                            onPressed: () => doUserLogout(),
372                          ),
373                        ),
374                      ],
375                    ),
376                  );
377              }
378            }));
379  }
380 }
381
382 class ResetPasswordPage extends StatefulWidget {
383  @override
384  _ResetPasswordPageState createState() => _ResetPasswordPageState();
385 }
386
387 class _ResetPasswordPageState extends State<ResetPasswordPage> {
388  final controllerEmail = TextEditingController();
389
390  @override
391  Widget build(BuildContext context) {
392    return Scaffold(
393        appBar: AppBar(
394          title: Text('Reset Password'),
395        ),
396        body: SingleChildScrollView(
397          padding: const EdgeInsets.all(8),
398          child: Column(
399            crossAxisAlignment: CrossAxisAlignment.stretch,
400            children: [
401              TextField(
402                controller: controllerEmail,
403                keyboardType: TextInputType.emailAddress,
404                textCapitalization: TextCapitalization.none,
405                autocorrect: false,
406                decoration: InputDecoration(
407                    border: OutlineInputBorder(
408                        borderSide: BorderSide(color: Colors.black)),
409                    labelText: 'E-mail'),
410              ),
411              SizedBox(
412                height: 8,
413              ),
414              Container(
415                height: 50,
416                child: ElevatedButton(
417                  child: const Text('Reset Password'),
418                  onPressed: () => doUserResetPassword(),
419                ),
420              )
421            ],
422          ),
423        ));
424  }
425
426  void doUserResetPassword() async {}
427 }
428
429 class Message {
430  static void showSuccess(
431      {required BuildContext context,
432      required String message,
433      VoidCallback? onPressed}) {
434    showDialog(
435      context: context,
436      builder: (BuildContext context) {
437        return AlertDialog(
438          title: const Text("Success!"),
439          content: Text(message),
440          actions: <Widget>[
441            new ElevatedButton(
442              child: const Text("OK"),
443              onPressed: () {
444                Navigator.of(context).pop();
445                if (onPressed != null) {
446                  onPressed();
447                }
448              },
449            ),
450          ],
451        );
452      },
453    );
454  }
455
456  static void showError(
457      {required BuildContext context,
458      required String message,
459      VoidCallback? onPressed}) {
460    showDialog(
461      context: context,
462      builder: (BuildContext context) {
463        return AlertDialog(
464          title: const Text("Error!"),
465          content: Text(message),
466          actions: <Widget>[
467            new ElevatedButton(
468              child: const Text("OK"),
469              onPressed: () {
470                Navigator.of(context).pop();
471                if (onPressed != null) {
472                  onPressed();
473                }
474              },
475            ),
476          ],
477        );
478      },
479    );
480  }
481 }
482
```

:::hint{type="info"}
When debug parameter in function Parse().initialize is true, allows displaying Parse API calls on the console. This configuration can help you debug the code. It is prudent to disable debug in the release version.
:::

## 2 - Connect Template to Back4app Project

Find your Application Id and Client Key credentials navigating to your app Dashboard at [**Back4App Website**](https://www.back4app.com/).

Update your code in main.dart with the values of your project’s ApplicationId and ClientKey in Back4app.

- **keyApplicationId** **= App Id**
- **keyClientKey** **= Client Key**

Run the project, and the app will load as shown in the image.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/4Theva5wIFKOP4aLYKfCq_image.png" signedSrc size="50" width="325" height="636" position="center" caption}

## 3 - Code for get current user on Session

The User Login or SignUp function creates a Session object, which points to the User logged in and stores in your local storage a valid user session.

Calls to methods currentUser will successfully retrieve your ParseUser data and sessionToken for Session object.

Search for the function hasUserLogged in the file main.dart.

Replace the code inside hasUserLogged with:

```javascript
1       ParseUser? currentUser = await ParseUser.currentUser() as ParseUser?;
2       if (currentUser == null) {
3         return false;
4       }
5       //Checks whether the user's session token is valid
6       final ParseResponse? parseResponse =
7           await ParseUser.getCurrentUserFromServer(currentUser.sessionToken!);
8
9       if (parseResponse?.success == null || !parseResponse!.success) {
10        //Invalid session. Logout
11        await currentUser.logout();
12        return false;
13      } else {
14        return true;
15      }
```

To build this function, follow these steps:

1. Call the ParseUser.currentUser() function, which will return a ParseUser object from local storage.
2. IfParseUser is null, we do not have any users with an active session in the app.
3. IfParseUser is not null, we have a user with an active session in our app.
4. The user’s session needs to be validated on the Parse Server, as it has a lifetime.
5. If the token is not valid, it is necessary to call the logout function to clear the current session and the user needs to log in again.

The complete function should look like this:

```javascript
1     Future<bool> hasUserLogged() async {
2       ParseUser? currentUser = await ParseUser.currentUser() as ParseUser?;
3       if (currentUser == null) {
4         return false;
5       }
6       //Checks whether the user's session token is valid
7       final ParseResponse? parseResponse =
8           await ParseUser.getCurrentUserFromServer(currentUser.sessionToken!);
9   
10      if (parseResponse?.success == null || !parseResponse!.success) {
11        //Invalid session. Logout
12        await currentUser.logout();
13        return false;
14      } else {
15        return true;
16      }
17    }
```

Look for the function getUser in the file main.dart.

Replace the code inside getUser with:

```dart
1    currentUser = await ParseUser.currentUser() as ParseUser?;
2    return currentUser;
```

To build this function, follow these steps:

1. Call the ParseUser.currentUser() function, which will return a ParseUser object from local storage.

The complete function should look like this:

```dart
1     Future<ParseUser> getUser() async {
2       currentUser = await ParseUser.currentUser() as ParseUser?;
3       return currentUser;
4     }
```

:::hint{type="info"}
To test it, click on theRunbutton in Android Studio/VSCode.
:::

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/3_Cl98oXfNlWh9xqseJ7y_image.png" signedSrc size="50" width="325" height="636" position="center" caption}

SignUp or Login and the next screen will display the username of the logged in user.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/gqmLgfctsrs4P6DJpRXbQ_image.png" signedSrc size="50" width="325" height="636" position="center" caption}

Quit the application and run again.

If a valid user session is identified, the screen with the user’s username will be displayed.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/YT5lGyUOJwNjkMqLAeBoT_image.png" signedSrc size="50" width="325" height="636" position="center" caption}

## It’s done!

At the end of this guide, you can get current user on Session of your app using Parse Server core features through Back4App!
