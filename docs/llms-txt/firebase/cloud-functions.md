# Source: https://firebase.google.com/docs/app-check/cloud-functions.md.txt

When you[understand howApp Checkwill affect your users](https://firebase.google.com/docs/app-check/monitor-functions-metrics)and you're ready to proceed, you can enableApp Checkenforcement for[callable functions](https://firebase.google.com/docs/functions/callable).

## Enable enforcement

To begin enforcingApp Checktoken requirements in your callable functions, modify your functions to check for validApp Checktokens, as shown below. Once you enable enforcement, all unverified requests will be rejected.

1. Install theCloud FunctionsSDK.

   ### Node.js (2nd gen)

   Update your project's`firebase-functions`dependency to version 4.0.0 or newer:  

       npm install firebase-functions@">=4.0.0"

   ### Node.js (1st gen)

   Update your project's`firebase-functions`dependency to version 4.0.0 or newer:  

       npm install firebase-functions@">=4.0.0"

   ### Python (preview)

   Add`firebase-functions`to`functions/requirements.txt`:  

       firebase-functions >= 0.1.0

   Then, update the dependencies in your project's virtual environment:  

       ./venv/bin/pip install -r requirements.txt

2. Enable the App Check enforcement runtime option for your function:

   ### Node.js (2nd gen)

       const { onCall } = require("firebase-functions/v2/https");

       exports.yourV2CallableFunction = onCall(
         {
       enforceAppCheck: true, // Reject requests with missing or invalid App Check tokens.
       },
         (request) => {
           // request.app contains data from App Check, including the app ID.
           // Your function logic follows.
           ...
         }
       );

   ### Node.js (1st gen)

       const functions = require("firebase-functions/v1");

       exports.yourV1CallableFunction = functions
         .runWith({
       enforceAppCheck: true, // Reject requests with missing or invalid App Check tokens.
       })
         .https.onCall((data, context) => {
               // context.app contains data from App Check, including the app ID.
               // Your function logic follows.
               ...
         });

   ### Python (preview)

       from firebase_functions import https_fn

       @https_fn.on_call(
           enforce_app_check=True # Reject requests with missing or invalid App Check tokens.
       )
       def your_callable_function(req: https_fn.CallableRequest) -> https_fn.Response:
           # req.app contains data from App Check, including the app ID.
           # Your function logic follows.
           ...

3. Redeploy your functions:

   ```
   firebase deploy --only functions
   ```

Once these changes are deployed, your callable functions will require validApp Checktokens. TheCloud Functionsclient SDKs automatically attach anApp Checktoken when you invoke a callable function.

## Replay protection (beta)

To protect a callable function from replay attacks, you can consume the App Check token after verifying it. Once the token is consumed, it cannot be used again.
| **Note:** The replay protection beta supports only the Cloud Functions SDK for Node.js.

Note that using replay protection adds a network round trip to token verification, and therefore adds latency to the function call. For this reason, most apps typically enable replay protection only on particularly sensitive endpoints.

To consume tokens:

1. In the[Google Cloudconsole](https://console.cloud.google.com/iam-admin/iam?project=_), grant the "Firebase App Check Token Verifier" role to the service account used by the function.

   - If you're explicitly initializing the Admin SDK and you specified your project's Admin SDK service account credentials, the required role is already granted.
   - If you're using 1st generation Cloud Functions with the default Admin SDK configuration, grant the role to the**App Engine default service account** . See[Changing service account permissions](https://cloud.google.com/appengine/docs/legacy/standard/python/service-account#modifying_the_default_service_account).
   - If you're using 2nd generation Cloud Functions with the default Admin SDK configuration, grant the role to the**Default compute service account**.
2. Set`consumeAppCheckToken`to`true`in your function definition:

   ### Node.js (2nd gen)

       const { onCall } = require("firebase-functions/v2/https");

       exports.yourV2CallableFunction = onCall(
         {
           enforceAppCheck: true, // Reject requests with missing or invalid App Check tokens.
           consumeAppCheckToken: true // Consume the token after verification.
         },
         (request) => {
           // request.app contains data from App Check, including the app ID.
           // Your function logic follows.
           ...
         }
       );

   ### Node.js (1st gen)

       const functions = require("firebase-functions/v1");

       exports.yourV1CallableFunction = functions
         .runWith({
             enforceAppCheck: true, // Reject requests with missing or invalid App Check tokens.
             consumeAppCheckToken: true // Consume the token after verification.
         })
         .https.onCall((data, context) => {
             // context.app contains data from App Check, including the app ID.
             // Your function logic follows.
             ...
         });

3. Update your app client code to acquire consumable limited-use tokens when you call the function:

   ### Swift

       let options = HTTPSCallableOptions(requireLimitedUseAppCheckTokens: true)
       let yourCallableFunction =
           Functions.functions().httpsCallable("yourCallableFunction", options: options)
       do {
           let result = try await yourCallableFunction.call()
       } catch {
           // ...
       }

   ### Kotlin

       val yourCallableFunction = Firebase.functions.getHttpsCallable("yourCallableFunction") {
           limitedUseAppCheckTokens = true
       }
       val result = yourCallableFunction.call().await()

   ### Java

       HttpsCallableReference yourCallableFunction = FirebaseFunctions.getInstance().getHttpsCallable(
               "yourCallableFunction",
               new HttpsCallableOptions.Builder()
                       .setLimitedUseAppCheckTokens(true)
                       .build()
       );
       Task<HttpsCallableResult> result = yourCallableFunction.call();

   ### Web

       import { getFunctions, httpsCallable } from "firebase/functions";

       const yourCallableFunction = httpsCallable(
         getFunctions(),
         "yourCallableFunction",
         { limitedUseAppCheckTokens: true },
       );
       await yourCallableFunction();