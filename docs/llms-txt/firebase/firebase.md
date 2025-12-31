# Source: https://firebase.google.com/docs/reference/cpp/namespace/firebase.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.md.txt

# firebase | JavaScript SDK

# - firebase

`firebase` is a global namespace from which all Firebase
services are accessed.

## Index

### Modules

- [User](https://firebase.google.com/docs/reference/js/v8/firebase.User)
- [analytics](https://firebase.google.com/docs/reference/js/v8/firebase.analytics)
- [app](https://firebase.google.com/docs/reference/js/v8/firebase.app)
- [appCheck](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck)
- [auth](https://firebase.google.com/docs/reference/js/v8/firebase.auth)
- [database](https://firebase.google.com/docs/reference/js/v8/firebase.database)
- [firestore](https://firebase.google.com/docs/reference/js/v8/firebase.firestore)
- [functions](https://firebase.google.com/docs/reference/js/v8/firebase.functions)
- [installations](https://firebase.google.com/docs/reference/js/v8/firebase.installations)
- [messaging](https://firebase.google.com/docs/reference/js/v8/firebase.messaging)
- [performance](https://firebase.google.com/docs/reference/js/v8/firebase.performance)
- [remoteConfig](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig)
- [storage](https://firebase.google.com/docs/reference/js/v8/firebase.storage)

### Interfaces

- [FirebaseError](https://firebase.google.com/docs/reference/js/v8/firebase.FirebaseError)
- [FirebaseIdToken](https://firebase.google.com/docs/reference/js/v8/firebase.FirebaseIdToken)
- [UserInfo](https://firebase.google.com/docs/reference/js/v8/firebase.UserInfo)

### Type aliases

- [EmulatorMockTokenOptions](https://firebase.google.com/docs/reference/js/v8/firebase#emulatormocktokenoptions)
- [FirebaseSignInProvider](https://firebase.google.com/docs/reference/js/v8/firebase#firebasesigninprovider)
- [LogLevel](https://firebase.google.com/docs/reference/js/v8/firebase#loglevel)

### Variables

- [SDK_VERSION](https://firebase.google.com/docs/reference/js/v8/firebase#sdk_version)
- [apps](https://firebase.google.com/docs/reference/js/v8/firebase#apps)

### Functions

- [initializeApp](https://firebase.google.com/docs/reference/js/v8/firebase#initializeapp)
- [onLog](https://firebase.google.com/docs/reference/js/v8/firebase#onlog)
- [registerVersion](https://firebase.google.com/docs/reference/js/v8/firebase#registerversion)
- [setLogLevel](https://firebase.google.com/docs/reference/js/v8/firebase#setloglevel)

## Type aliases

### EmulatorMockTokenOptions

EmulatorMockTokenOptions: { user_id: string } \| { sub: string } \& Partial\<[FirebaseIdToken](https://firebase.google.com/docs/reference/js/v8/firebase.FirebaseIdToken)\>

### FirebaseSignInProvider

FirebaseSignInProvider: "custom" \| "email" \| "password" \| "phone" \| "anonymous" \| "google.com" \| "facebook.com" \| "github.com" \| "twitter.com" \| "microsoft.com" \| "apple.com"

### LogLevel

LogLevel: "debug" \| "verbose" \| "info" \| "warn" \| "error" \| "silent"  
The JS SDK supports 5 log levels and also allows a user the ability to
silence the logs altogether.

The order is as follows:
silent \< debug \< verbose \< info \< warn \< error

## Variables

### SDK_VERSION

SDK_VERSION: string  
The current SDK version.

### apps

apps: [App](https://firebase.google.com/docs/reference/js/v8/firebase.app.App)\[\]  
A (read-only) array of all initialized apps.

## Functions

### initializeApp

- initializeApp ( options : Object , name ? : string ) : [App](https://firebase.google.com/docs/reference/js/v8/firebase.app.App)
- Creates and initializes a Firebase [app](https://firebase.google.com/docs/reference/js/v8/firebase.app.App) instance.

  See
  [Add Firebase to your app](https://firebase.google.com/docs/web/setup#add_firebase_to_your_app) and
  [Initialize multiple projects](https://firebase.google.com/docs/web/learn-more#multiple-projects) for detailed documentation.

  example
  :


          // Initialize default app
          // Retrieve your own options values by adding a web app on
          // https://console.firebase.google.com
          firebase.initializeApp({
            apiKey: "AIza....",                             // Auth / General Use
            appId: "1:27992087142:web:ce....",              // General Use
            projectId: "my-firebase-project",               // General Use
            authDomain: "YOUR_APP.firebaseapp.com",         // Auth with popup/redirect
            databaseURL: "https://YOUR_APP.firebaseio.com", // Realtime Database
            storageBucket: "YOUR_APP.appspot.com",          // Storage
            messagingSenderId: "123456789",                 // Cloud Messaging
            measurementId: "G-12345"                        // Analytics
          });


  example
  :


          // Initialize another app
          var otherApp = firebase.initializeApp({
            apiKey: "AIza....",
            appId: "1:27992087142:web:ce....",
            projectId: "my-firebase-project",
            databaseURL: "https://<OTHER_DATABASE_NAME>.firebaseio.com",
            storageBucket: "<OTHER_STORAGE_BUCKET>.appspot.com"
          }, "nameOfOtherApp");


  #### Parameters

  -

    ##### options: Object

    Options to configure the app's services.
  -

    ##### Optional name: string

    Optional name of the app to initialize. If no name
    is provided, the default is `"[DEFAULT]"`.

  #### Returns [App](https://firebase.google.com/docs/reference/js/v8/firebase.app.App)

  The initialized app.

### onLog

- onLog ( logCallback : ( callbackParams : { args : any \[\] ; level : [LogLevel](https://firebase.google.com/docs/reference/js/v8/firebase#loglevel) ; message : string ; type : string } ) =\> void , options ? : { level : [LogLevel](https://firebase.google.com/docs/reference/js/v8/firebase#loglevel) } ) : void
- Sets log handler for all Firebase packages.

  #### Parameters

  -

    ##### logCallback: (callbackParams: { args: any\[\]; level: [LogLevel](https://firebase.google.com/docs/reference/js/v8/firebase#loglevel); message: string; type: string }) =\> void

    An optional custom log handler that executes user code whenever
    the Firebase SDK makes a logging call.
    -
      - (callbackParams: { args: any\[\]; level: [LogLevel](https://firebase.google.com/docs/reference/js/v8/firebase#loglevel); message: string; type: string }): void

      <!-- -->

      -

        #### Parameters

        -

          ##### callbackParams: { args: any\[\]; level: [LogLevel](https://firebase.google.com/docs/reference/js/v8/firebase#loglevel); message: string; type: string }

          -

            ##### args: any\[\]

            The raw arguments passed to the log call.
          -

            ##### level: [LogLevel](https://firebase.google.com/docs/reference/js/v8/firebase#loglevel)

            Level of event logged.
          -

            ##### message: string

            Any text from logged arguments joined into one string.
          -

            ##### type: string

            A string indicating the name of the package that made the log call,
            such as `@firebase/firestore`.

        #### Returns void

  -

    ##### Optional options: { level: [LogLevel](https://firebase.google.com/docs/reference/js/v8/firebase#loglevel) }

    -

      ##### level: [LogLevel](https://firebase.google.com/docs/reference/js/v8/firebase#loglevel)

      Threshhold log level. Only logs at or above this level trigger the `logCallback`
      passed to `onLog`.

  #### Returns void

### registerVersion

- registerVersion ( library : string , version : string , variant ? : string ) : void
- Registers a library's name and version for platform logging purposes.

  #### Parameters

  -

    ##### library: string

    Name of 1p or 3p library (e.g. firestore, angularfire)
  -

    ##### version: string

    Current version of that library.
  -

    ##### Optional variant: string

    Bundle variant, e.g., node, rn, etc.

  #### Returns void

### setLogLevel

- setLogLevel ( logLevel : [LogLevel](https://firebase.google.com/docs/reference/js/v8/firebase#loglevel) ) : void
- Sets log level for all Firebase packages.

  All of the log types above the current log level are captured (i.e. if
  you set the log level to `info`, errors are logged, but `debug` and
  `verbose` logs are not).

  #### Parameters

  -

    ##### logLevel: [LogLevel](https://firebase.google.com/docs/reference/js/v8/firebase#loglevel)

  #### Returns void