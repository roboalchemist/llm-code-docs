# Source: https://firebase.google.com/docs/web/alt-setup.md.txt

<br />

For most Firebase web apps we strongly recommend using[the SDK via npm](https://firebase.google.com/docs/web/setup). However, for users with special requirements, Firebase provides alternative[ways to add the SDK](https://firebase.google.com/docs/web/learn-more#ways-to-add-web-sdks). This page provides detailed setup instructions for these alternative methods:

- CDN (content delivery network)
- npm for Node.js apps

Using these methods, you can add any of the[available libraries](https://firebase.google.com/docs/web/learn-more#available-libraries)to your app.  

### From the CDN

You can configure partial import of theFirebaseJavaScriptSDK and only load the Firebase products that you need. Firebase stores each library of theFirebaseJavaScriptSDK on our global CDN (content delivery network).

1. To include only[specific Firebase products](https://firebase.google.com/docs/web/learn-more#libraries-cdn)(for example,AuthenticationandCloud Firestore), add the following script to the bottom of your`<body>`tag, but before you use any Firebase services:

   ```javascript
   <body>
     <!-- Insert this script at the bottom of the HTML, but before you use any Firebase services -->
     <script type="module">
       import { initializeApp } from 'https://www.gstatic.com/firebasejs/12.7.0/firebase-app.js'

       // If you enabled Analytics in your project, add the Firebase SDK for Google Analytics
       import { getAnalytics } from 'https://www.gstatic.com/firebasejs/12.7.0/firebase-analytics.js'

       // Add Firebase products that you want to use
       import { getAuth } from 'https://www.gstatic.com/firebasejs/12.7.0/firebase-auth.js'
       import { getFirestore } from 'https://www.gstatic.com/firebasejs/12.7.0/firebase-firestore.js'
     </script>
   </body>
   ```
   | You can optionally[delay loading of Firebase SDKs](https://firebase.google.com/docs/web/learn-more#delay-sdks-cdn)until the entire page has loaded.
2. Add your Firebase configuration object, and then initialize Firebase in your app:

   ```javascript
   <body>
     <script type="module">
       // ...

       // TODO: Replace the following with your app's https://firebase.google.com/docs/web/learn-more#config-object
       const firebaseConfig = {
         // ...
       };

       // Initialize Firebase
       const app = initializeApp(firebaseConfig);
     </script>
   </body>
   ```

### Node.js apps

| **Caution:** The following instructions are for using theFirebaseJavaScriptSDK as a client for end-user access (for example, in a Node.js desktop or IoT application). To set up administrative access from privileged environments (such as servers),[set up theFirebaseAdmin SDK](https://firebase.google.com/docs/admin/setup)instead.

1. Install theFirebaseJavaScriptSDK:

   1. If you don't already have a`package.json`file, create one by running the following command from the root of your JavaScript project:

      ```
      npm init
      ```
   2. Install the`firebase`npm package and save it to your`package.json`file by running:

      ```
      npm install --save firebase@12.7.0
      ```
2. Use one of the following options to use the Firebase module in your app:

   - **You can`require`modules from any JavaScript file**

     To include only[specific Firebase products](https://firebase.google.com/docs/web/learn-more#libraries-nodejs)(likeAuthenticationandCloud Firestore):  

         // Firebase App (the core Firebase SDK) is always required and
         // must be listed before other Firebase SDKs
         var firebase = require("firebase/app");

         // Add the Firebase products that you want to use
         require("firebase/auth");
         require("firebase/firestore");

     Include the entireFirebaseJavaScriptSDK, rather than individual SDKs*(not recommended for production apps)*
     | Loading the entire SDK is not efficient for production web apps.  
     Use this option for development purposes only.  

     ```javascript
     var firebase = require("firebase");
     ```

     <br />

   - **You can use ESM syntax to`import`modules**

     To include only[specific Firebase products](https://firebase.google.com/docs/web/learn-more#libraries-nodejs)(likeAuthenticationandCloud Firestore):  

         // Firebase App (the core Firebase SDK) is always required and
         // must be listed before other Firebase SDKs
         import firebase from "firebase/app";

         // Add the Firebase services that you want to use
         import "firebase/auth";
         import "firebase/firestore";

     Include the entireFirebaseJavaScriptSDK, rather than individual SDKs*(not recommended for production apps)*
     | Loading the entire SDK is not efficient for production web apps.  
     Use this option for development purposes only.  

     ```python
     import firebase from "firebase";
     ```
3. Add your Firebase configuration object, and then initialize Firebase in your app:

   ```javascript
   import { initializeApp } from 'firebase/app';

   // TODO: Replace the following with your app's https://firebase.google.com/docs/web/learn-more#config-object
   const firebaseConfig = {
     //...
   };

   // Initialize Firebase
   const app = initializeApp(firebaseConfig);
   ```