# Source: https://firebase.google.com/docs/functions/1st-gen/callable-1st.md.txt

<br />

| **Note:** The 1st-gen functionality described in this page is also supported inCloud Functions(2nd gen) with improved features and performance. For more information about 2nd gen, see the[version comparison](https://firebase.google.com/docs/functions/version-comparison). To go directly to the 2nd gen guide for this feature, see[Call functions from your app](https://firebase.google.com/docs/functions/callable).

TheCloud Functions for Firebaseclient SDKs let you call functions directly from a Firebase app. To call a function from your app in this way, write and deploy an HTTP Callable function inCloud Functions, and then add client logic to call the function from your app.

It's important to keep in mind that HTTP callable functions are similar but**not identical to**HTTP functions. To use HTTP callable functions you must use the client SDK for your platform together with the backend API (or implement the protocol). Callables have these key difference from HTTP functions:

- With callables,Firebase Authenticationtokens,FCMtokens, andApp Checktokens, when available, are automatically included in requests.
- The trigger automatically deserializes the request body and validates auth tokens.

TheFirebaseSDK forCloud Functions2nd gen and higher interoperates with these Firebase client SDK minimum versions to support HTTPS Callable functions:

- FirebaseSDK forAppleplatforms 12.7.0
- FirebaseSDK forAndroid22.1.0
- Firebase Modular Web SDK v. 9.7.0

If you want to add similar functionality to an app built on an unsupported platform, see the[Protocol Specification for`https.onCall`](https://firebase.google.com/docs/functions/callable-reference). The rest of this guide provides instructions on how to write, deploy, and call an HTTP callable function for Apple platforms, Android, web, C++, and Unity.

## Write and deploy the callable function

Use[`functions.https.onCall`](https://firebase.google.com/docs/reference/functions/firebase-functions.https#httpsoncall)to create an HTTPS callable function. This method takes two parameters:`data`, and optional`context`:

<br />

```javascript
  // Saves a message to the Firebase Realtime Database but sanitizes the
  // text by removing swearwords.
  exports.addMessage = functions.https.onCall((data, context) => {
    // ...
  });
  
```

<br />

For a callable function that saves a text message to theRealtime Database, for example,`data`could contain the message text, while`context`parameters represent user auth information:  

    // Message text passed from the client.
    const text = request.data.text;
    // Authentication / user information is automatically added to the request.
    const uid = request.auth.uid;
    const name = request.auth.token.name || null;
    const picture = request.auth.token.picture || null;
    const email = request.auth.token.email || null;  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/callable-functions/functions/index.js#L85-L89

Distance between the location of the callable function and the location of the calling client can create network latency. To optimize performance, consider specifying the[function location](https://firebase.google.com/docs/functions/locations)where applicable, and make sure to align the callable's location with the location set when you[initialize the SDK](https://firebase.google.com/docs/functions/callable#initialize_the_client_sdk)on the client side.

Optionally, you can attach anApp Checkattestation to help protect your backend resources from abuse, such as billing fraud or phishing. See[EnableApp Checkenforcement forCloud Functions](https://firebase.google.com/docs/app-check/cloud-functions).
| **Note:** Use only the[`functions.https`](https://firebase.google.com/docs/reference/functions/firebase-functions.https)backend API to write callable functions. The**[HTTP trigger API](https://firebase.google.com/docs/reference/functions/firebase-functions.httpsfunction#httpsfunction_interface)is entirely separate and not interoperable with callable functions.**

### Sending back the result

To send data back to the client, return data that can be JSON encoded. For example, to return the result of an addition operation:  

    // returning result.
    return {
      firstNumber: firstNumber,
      secondNumber: secondNumber,
      operator: "+",
      operationResult: firstNumber + secondNumber,
    };  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/callable-functions/functions/index.js#L49-L55

To return data after an asynchronous operation, return a promise. The data returned by the promise is sent back to the client. For example, you could return sanitized text that the callable function wrote to theRealtime Database:  

    // Saving the new message to the Realtime Database.
    const sanitizedMessage = sanitizer.sanitizeText(text); // Sanitize message.

    return getDatabase().ref("/messages").push({
      text: sanitizedMessage,
      author: {uid, name, picture, email},
    }).then(() => {
      logger.info("New Message written");
      // Returning the sanitized message to the client.
      return {text: sanitizedMessage};
    })  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/callable-functions/functions/index.js#L93-L103

### Handle errors

To ensure the client gets useful error details, return errors from a callable by throwing (or returning a Promise rejected with) an instance of`functions.https.HttpsError`. The error has a`code`attribute that can be one of the values listed at[`functions.https.HttpsError`](https://firebase.google.com/docs/reference/functions/firebase-functions.https.httpserror). The errors also have a string`message`, which defaults to an empty string. They can also have an optional`details`field with an arbitrary value. If an error other than`HttpsError`is thrown from your functions, your client instead receives an error with the message`INTERNAL`and the code`internal`.

For example, a function could throw data validation and authentication errors with error messages to return to the calling client:  

    // Checking attribute.
    if (!(typeof text === "string") || text.length === 0) {
      // Throwing an HttpsError so that the client gets the error details.
      throw new HttpsError("invalid-argument", "The function must be called " +
              "with one arguments \"text\" containing the message text to add.");
    }
    // Checking that the user is authenticated.
    if (!request.auth) {
      // Throwing an HttpsError so that the client gets the error details.
      throw new HttpsError("failed-precondition", "The function must be " +
              "called while authenticated.");
    }  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/callable-functions/functions/index.js#L70-L81

### Deploy the callable function

After you save a completed callable function within`index.js`, it is deployed along with all other functions when you run`firebase deploy`. To deploy only the callable, use the`--only`argument as shown to perform[partial deploys](https://firebase.google.com/docs/cli#partial_deploys):  

```
firebase deploy --only functions:addMessage
```

If you encounter permissions errors when deploying functions, make sure that the appropriate[IAM roles](https://firebase.google.com/docs/projects/iam/permissions#functions)are assigned to the user running the deployment commands.

## Set up your client development environment

Make sure you meet any prerequisites, then add the required dependencies and client libraries to your app.  

### iOS+

Follow the instructions to[add Firebase to your Apple app](https://firebase.google.com/docs/ios/setup).

Use Swift Package Manager to install and manage Firebase dependencies.
| Visit[our installation guide](https://firebase.google.com/docs/ios/installation-methods)to learn about the different ways you can add Firebase SDKs to your Apple project, including importing frameworks directly and using CocoaPods.

1. In Xcode, with your app project open, navigate to**File \> Add Packages**.
2. When prompted, add the Firebase Apple platforms SDK repository:  

```text
  https://github.com/firebase/firebase-ios-sdk.git
```
| **Note:**New projects should use the default (latest) SDK version, but you can choose an older version if needed.
3. Choose theCloud Functionslibrary.
4. Add the`-ObjC`flag to the*Other Linker Flags*section of your target's build settings.
5. When finished, Xcode will automatically begin resolving and downloading your dependencies in the background.

### Web

1. Follow the instructions to[add Firebase to your Web app](https://firebase.google.com/docs/web/setup). Make sure to run the following command from your terminal:  

   ```objective-c
   npm install firebase@12.7.0 --save
   ```
2. Manually require both Firebase core andCloud Functions:

   ```python
    import { initializeApp } from 'firebase/app';
    import { getFunctions } from 'firebase/functions';

    const app = initializeApp({
        projectId: '### CLOUD FUNCTIONS PROJECT ID ###',
        apiKey: '### FIREBASE API KEY ###',
        authDomain: '### FIREBASE AUTH DOMAIN ###',
      });
    const functions = getFunctions(app);
   ```

### Web

1. Follow the instructions to[add Firebase to your Web app](https://firebase.google.com/docs/web/setup).
2. Add the Firebase core andCloud Functionsclient libraries to your app:  

   ```text
   <script src="https://www.gstatic.com/firebasejs/8.10.1/firebase.js"></script>
   <script src="https://www.gstatic.com/firebasejs/8.10.1/firebase-functions.js"></script>
   ```

TheCloud FunctionsSDK is also available as an npm package.

1. Run the following command from your terminal:  

   ```objective-c
   npm install firebase@8.10.1 --save
   ```
2. Manually require both Firebase core andCloud Functions:  

   ```gdscript
   const firebase = require("firebase");
   // Required for side-effects
   require("firebase/functions");
   ```

### Kotlin

1. Follow the instructions to[add Firebase to your Android app](https://firebase.google.com/docs/android/setup).

2. In your**module (app-level) Gradle file** (usually`<project>/<app-module>/build.gradle.kts`or`<project>/<app-module>/build.gradle`), add the dependency for theCloud Functionslibrary for Android. We recommend using the[Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom)to control library versioning.

   <br />

   ```kotlin
   dependencies {
       // Import the BoM for the Firebase platform
       implementation(platform("com.google.firebase:firebase-bom:34.7.0"))

       // Add the dependency for the Cloud Functions library
       // When using the BoM, you don't specify versions in Firebase library dependencies
       implementation("com.google.firebase:firebase-functions")
   }
   ```

   By using the[Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom), your app will always use compatible versions of Firebase Android libraries.
   *(Alternative)* Add Firebase library dependencies*without* using theBoM

   If you choose not to use theFirebase BoM, you must specify each Firebase library version in its dependency line.

   **Note that if you use*multiple* Firebase libraries in your app, we strongly recommend using theBoMto manage library versions, which ensures that all versions are compatible.**  

   ```groovy
   dependencies {
       // Add the dependency for the Cloud Functions library
       // When NOT using the BoM, you must specify versions in Firebase library dependencies
       implementation("com.google.firebase:firebase-functions:22.1.0")
   }
   ```

   <br />

### Java

1. Follow the instructions to[add Firebase to your Android app](https://firebase.google.com/docs/android/setup).

2. In your**module (app-level) Gradle file** (usually`<project>/<app-module>/build.gradle.kts`or`<project>/<app-module>/build.gradle`), add the dependency for theCloud Functionslibrary for Android. We recommend using the[Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom)to control library versioning.

   <br />

   ```java
   dependencies {
       // Import the BoM for the Firebase platform
       implementation(platform("com.google.firebase:firebase-bom:34.7.0"))

       // Add the dependency for the Cloud Functions library
       // When using the BoM, you don't specify versions in Firebase library dependencies
       implementation("com.google.firebase:firebase-functions")
   }
   ```

   By using the[Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom), your app will always use compatible versions of Firebase Android libraries.
   *(Alternative)* Add Firebase library dependencies*without* using theBoM

   If you choose not to use theFirebase BoM, you must specify each Firebase library version in its dependency line.

   **Note that if you use*multiple* Firebase libraries in your app, we strongly recommend using theBoMto manage library versions, which ensures that all versions are compatible.**  

   ```groovy
   dependencies {
       // Add the dependency for the Cloud Functions library
       // When NOT using the BoM, you must specify versions in Firebase library dependencies
       implementation("com.google.firebase:firebase-functions:22.1.0")
   }
   ```

   <br />

### Dart

1. Follow the instructions to[add Firebase to your Flutter app](https://firebase.google.com/docs/flutter/setup).

2. From the root of your Flutter project, run the following command to install the plugin:

       flutter pub add cloud_functions

3. Once complete, rebuild your Flutter application:

       flutter run

4. Once installed, you can access the`cloud_functions`plugin by importing it in your Dart code:

       import 'package:cloud_functions/cloud_functions.dart';

### C++

For**C++ with Android**:

1. Follow the instructions to[add Firebase to your C++ project](https://firebase.google.com/docs/cpp/setup?platform=android).
2. Add the**`firebase_functions`** library to your`CMakeLists.txt`file.

For**C++ with Apple platforms**:

1. Follow the instructions to[add Firebase to your C++ project](https://firebase.google.com/docs/cpp/setup?platform=ios).
2. Add theCloud Functionspod to your`Podfile`:  

   ```c++
   pod 'Firebase/Functions'
   ```
3. Save the file, then run:  

   ```c++
   pod install
   ```
4. Add the Firebase core andCloud Functionsframeworks from the[FirebaseC++SDK](https://firebase.google.com/download/cpp)to your Xcode project.
   - `firebase.framework`
   - `firebase_functions.framework`

### Unity

1. Follow the instructions to[add Firebase to your Unity project](https://firebase.google.com/docs/unity/setup).
2. Add the`FirebaseFunctions.unitypackage`from the[FirebaseUnitySDK](https://firebase.google.com/download/unity)to your Unity project.

## Initialize the client SDK

Initialize an instance ofCloud Functions:  

### Swift

    lazy var functions = Functions.functions()  
    https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/qs-snippets/LegacyFunctionsQuickstart/FunctionsExampleSwift/CloudAddCell.swift#L27-L27

### Objective-C

    @property(strong, nonatomic) FIRFunctions *functions;
    // ...
    self.functions = [FIRFunctions functions];  
    https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/qs-snippets/LegacyFunctionsQuickstart/FunctionsExample/CloudAddCell.m#L35-L35

### Web

    firebase.initializeApp({
      apiKey: '### FIREBASE API KEY ###',
      authDomain: '### FIREBASE AUTH DOMAIN ###',
      projectId: '### CLOUD FUNCTIONS PROJECT ID ###'
      databaseURL: 'https://### YOUR DATABASE NAME ###.firebaseio.com',
    });

    // Initialize Cloud Functions through Firebase
    var functions = firebase.functions();

### Web

    const app = initializeApp({
      projectId: '### CLOUD FUNCTIONS PROJECT ID ###',
      apiKey: '### FIREBASE API KEY ###',
      authDomain: '### FIREBASE AUTH DOMAIN ###',
    });
    const functions = getFunctions(app);

### Kotlin

```kotlin
private lateinit var functions: FirebaseFunctions
// ...
functions = Firebase.functions  
https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/functions/app/src/main/java/devrel/firebase/google/com/functions/kotlin/MainActivity.kt#L22-L22
```

### Java

```java
private FirebaseFunctions mFunctions;
// ...
mFunctions = FirebaseFunctions.getInstance();https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/functions/app/src/main/java/devrel/firebase/google/com/functions/MainActivity.java#L52-L52
```

### Dart

    final functions = FirebaseFunctions.instance;

### C++

    firebase::functions::Functions* functions;
    // ...
    functions = firebase::functions::Functions::GetInstance(app);

### Unity

    functions = Firebase.Functions.DefaultInstance;

| **Note:** To call a function running in any[location](https://firebase.google.com/docs/functions/locations)other than the default`us-central1`, you must set the appropriate value at initialization. For example, on Android you would initialize with`getInstance(FirebaseApp app, String region)`.

## Call the function

### Swift

    functions.httpsCallable("addMessage").call(["text": inputField.text]) { result, error in
      if let error = error as NSError? {
        if error.domain == FunctionsErrorDomain {
          let code = FunctionsErrorCode(rawValue: error.code)
          let message = error.localizedDescription
          let details = error.userInfo[FunctionsErrorDetailsKey]
        }
        // ...
      }
      if let data = result?.data as? [String: Any], let text = data["text"] as? String {
        self.resultField.text = text
      }
    }  
    https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/qs-snippets/LegacyFunctionsQuickstart/FunctionsExampleSwift/CommentCell.swift#L31-L48

### Objective-C

    [[_functions HTTPSCallableWithName:@"addMessage"] callWithObject:@{@"text": _inputField.text}
                                                          completion:^(FIRHTTPSCallableResult * _Nullable result, NSError * _Nullable error) {
      if (error) {
        if ([error.domain isEqual:@"com.firebase.functions"]) {
          FIRFunctionsErrorCode code = error.code;
          NSString *message = error.localizedDescription;
          NSObject *details = error.userInfo[@"details"];
        }
        // ...
      }
      self->_resultField.text = result.data[@"text"];
    }];

### Web

    var addMessage = firebase.functions().httpsCallable('addMessage');
    addMessage({ text: messageText })
      .then((result) => {
        // Read result of the Cloud Function.
        var sanitizedMessage = result.data.text;
      });  
    https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/functions/callable.js#L24-L29

### Web

    import { getFunctions, httpsCallable } from "firebase/functions";

    const functions = getFunctions();
    const addMessage = httpsCallable(functions, 'addMessage');
    addMessage({ text: messageText })
      .then((result) => {
        // Read result of the Cloud Function.
        /** @type {any} */
        const data = result.data;
        const sanitizedMessage = data.text;
      });  
    https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/functions-next/callable/fb_functions_call_add_message.js#L8-L18

### Kotlin

```kotlin
private fun addMessage(text: String): Task<String> {
    // Create the arguments to the callable function.
    val data = hashMapOf(
        "text" to text,
        "push" to true,
    )

    return functions
        .getHttpsCallable("addMessage")
        .call(data)
        .continueWith { task ->
            // This continuation runs on either success or failure, but if the task
            // has failed then result will throw an Exception which will be
            // propagated down.
            val result = task.result?.data as String
            result
        }
}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/functions/app/src/main/java/devrel/firebase/google/com/functions/kotlin/MainActivity.kt#L58-L75
```

### Java

```java
private Task<String> addMessage(String text) {
    // Create the arguments to the callable function.
    Map<String, Object> data = new HashMap<>();
    data.put("text", text);
    data.put("push", true);

    return mFunctions
            .getHttpsCallable("addMessage")
            .call(data)
            .continueWith(new Continuation<HttpsCallableResult, String>() {
                @Override
                public String then(@NonNull Task<HttpsCallableResult> task) throws Exception {
                    // This continuation runs on either success or failure, but if the task
                    // has failed then getResult() will throw an Exception which will be
                    // propagated down.
                    String result = (String) task.getResult().getData();
                    return result;
                }
            });
}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/functions/app/src/main/java/devrel/firebase/google/com/functions/MainActivity.java#L90-L109
```

### Dart

        final result = await FirebaseFunctions.instance.httpsCallable('addMessage').call(
          {
            "text": text,
            "push": true,
          },
        );
        _response = result.data as String;

### C++

    firebase::Future<firebase::functions::HttpsCallableResult> AddMessage(
        const std::string& text) {
      // Create the arguments to the callable function.
      firebase::Variant data = firebase::Variant::EmptyMap();
      data.map()["text"] = firebase::Variant(text);
      data.map()["push"] = true;

      // Call the function and add a callback for the result.
      firebase::functions::HttpsCallableReference doSomething =
          functions->GetHttpsCallable("addMessage");
      return doSomething.Call(data);
    }

### Unity

    private Task<string> addMessage(string text) {
      // Create the arguments to the callable function.
      var data = new Dictionary<string, object>();
      data["text"] = text;
      data["push"] = true;

      // Call the function and extract the operation from the result.
      var function = functions.GetHttpsCallable("addMessage");
      return function.CallAsync(data).ContinueWith((task) => {
        return (string) task.Result.Data;
      });
    }

### Handle errors on the client

The client receives an error if the server threw an error or if the resulting promise was rejected.

If the error returned by the function is of type`function.https.HttpsError`, then the client receives the error`code`,`message`, and`details`from the server error. Otherwise, the error contains the message`INTERNAL`and the code`INTERNAL`. See guidance for how to[handle errors](https://firebase.google.com/docs/functions/callable#handle_errors)in your callable function.  

### Swift

    if let error = error as NSError? {
      if error.domain == FunctionsErrorDomain {
        let code = FunctionsErrorCode(rawValue: error.code)
        let message = error.localizedDescription
        let details = error.userInfo[FunctionsErrorDetailsKey]
      }
      // ...
    }  
    https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/qs-snippets/LegacyFunctionsQuickstart/FunctionsExampleSwift/CloudAddCell.swift#L36-L46

### Objective-C

    if (error) {
      if ([error.domain isEqual:@"com.firebase.functions"]) {
        FIRFunctionsErrorCode code = error.code;
        NSString *message = error.localizedDescription;
        NSObject *details = error.userInfo[@"details"];
      }
      // ...
    }  
    https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/qs-snippets/LegacyFunctionsQuickstart/FunctionsExample/CloudAddCell.m#L49-L59

### Web

    var addMessage = firebase.functions().httpsCallable('addMessage');
    addMessage({ text: messageText })
      .then((result) => {
        // Read result of the Cloud Function.
        var sanitizedMessage = result.data.text;
      })
      .catch((error) => {
        // Getting the Error details.
        var code = error.code;
        var message = error.message;
        var details = error.details;
        // ...
      });  
    https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/functions/callable.js#L37-L49

### Web

    import { getFunctions, httpsCallable } from "firebase/functions";

    const functions = getFunctions();
    const addMessage = httpsCallable(functions, 'addMessage');
    addMessage({ text: messageText })
      .then((result) => {
        // Read result of the Cloud Function.
        /** @type {any} */
        const data = result.data;
        const sanitizedMessage = data.text;
      })
      .catch((error) => {
        // Getting the Error details.
        const code = error.code;
        const message = error.message;
        const details = error.details;
        // ...
      });  
    https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/functions-next/callable/fb_functions_call_add_message_error.js#L8-L25

### Kotlin

```kotlin
addMessage(inputMessage)
    .addOnCompleteListener { task ->
        if (!task.isSuccessful) {
            val e = task.exception
            if (e is FirebaseFunctionsException) {
                val code = e.code
                val details = e.details
            }
        }
    }https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/functions/app/src/main/java/devrel/firebase/google/com/functions/kotlin/MainActivity.kt#L100-L109
```

### Java

```java
addMessage(inputMessage)
  .addOnCompleteListener(new OnCompleteListener<String>() {
    @Override
    public void onComplete(@NonNull Task<String> task) {
      if (!task.isSuccessful()) {
        Exception e = task.getException();
        if (e instanceof FirebaseFunctionsException) {
          FirebaseFunctionsException ffe = (FirebaseFunctionsException) e;
          FirebaseFunctionsException.Code code = ffe.getCode();
          Object details = ffe.getDetails();
        }
      }
    }
  });https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/functions/app/src/main/java/devrel/firebase/google/com/functions/MainActivity.java#L139-L152
```

### Dart

    try {
      final result =
          await FirebaseFunctions.instance.httpsCallable('addMessage').call();
    } on FirebaseFunctionsException catch (error) {
      print(error.code);
      print(error.details);
      print(error.message);
    }

### C++

    void OnAddMessageCallback(
        const firebase::Future<firebase::functions::HttpsCallableResult>& future) {
      if (future.error() != firebase::functions::kErrorNone) {
        // Function error code, will be kErrorInternal if the failure was not
        // handled properly in the function call.
        auto code = static_cast<firebase::functions::Error>(future.error());

        // Display the error in the UI.
        DisplayError(code, future.error_message());
        return;
      }

      const firebase::functions::HttpsCallableResult* result = future.result();
      firebase::Variant data = result->data();
      // This will assert if the result returned from the function wasn't a string.
      std::string message = data.string_value();
      // Display the result in the UI.
      DisplayResult(message);
    }

    // ...

    // ...
      auto future = AddMessage(message);
      future.OnCompletion(OnAddMessageCallback);
      // ...

### Unity

     addMessage(text).ContinueWith((task) => {
      if (task.IsFaulted) {
        foreach (var inner in task.Exception.InnerExceptions) {
          if (inner is FunctionsException) {
            var e = (FunctionsException) inner;
            // Function error code, will be INTERNAL if the failure
            // was not handled properly in the function call.
            var code = e.ErrorCode;
            var message = e.ErrorMessage;
          }
        }
      } else {
        string result = task.Result;
      }
    });

## Recommended: Prevent abuse withApp Check

Before you launch your app, you should enable[App Check](https://firebase.google.com/docs/app-check/cloud-functions)to help ensure that only your apps can access your callable function endpoints.