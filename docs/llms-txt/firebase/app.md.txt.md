# Source: https://firebase.google.com/docs/reference/js/app.md.txt

# app package

Firebase App

This package coordinates the communication between the different Firebase components

## Functions

| Function | Description |
|---|---|
| **function(app, ...)** |   |
| [deleteApp(app)](https://firebase.google.com/docs/reference/js/app.md#deleteapp_cf608e1) | Renders this app unusable and frees the resources of all associated services. |
| **function()** |   |
| [getApps()](https://firebase.google.com/docs/reference/js/app.md#getapps) | A (read-only) array of all initialized apps. |
| [initializeApp()](https://firebase.google.com/docs/reference/js/app.md#initializeapp) | Creates and initializes a FirebaseApp instance. |
| **function(config, ...)** |   |
| [initializeServerApp(config)](https://firebase.google.com/docs/reference/js/app.md#initializeserverapp_e7d0728) | Creates and initializes a [FirebaseServerApp](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverapp_interface) instance. |
| **function(libraryKeyOrName, ...)** |   |
| [registerVersion(libraryKeyOrName, version, variant)](https://firebase.google.com/docs/reference/js/app.md#registerversion_f673248) | Registers a library's name and version for platform logging purposes. |
| **function(logCallback, ...)** |   |
| [onLog(logCallback, options)](https://firebase.google.com/docs/reference/js/app.md#onlog_fd46eae) | Sets log handler for all Firebase SDKs. |
| **function(logLevel, ...)** |   |
| [setLogLevel(logLevel)](https://firebase.google.com/docs/reference/js/app.md#setloglevel_697d53a) | Sets log level for all Firebase SDKs.All of the log types above the current log level are captured (i.e. if you set the log level to `info`, errors are logged, but `debug` and `verbose` logs are not). |
| **function(name, ...)** |   |
| [getApp(name)](https://firebase.google.com/docs/reference/js/app.md#getapp_1eaaff4) | Retrieves a [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) instance.When called with no arguments, the default app is returned. When an app name is provided, the app corresponding to that name is returned.An exception is thrown if the app being retrieved has not yet been initialized. |
| **function(options, ...)** |   |
| [initializeApp(options, name)](https://firebase.google.com/docs/reference/js/app.md#initializeapp_cb2f5e1) | Creates and initializes a [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) instance.See [Add Firebase to your app](https://firebase.google.com/docs/web/setup#add_firebase_to_your_app) and [Initialize multiple projects](https://firebase.google.com/docs/web/setup#multiple-projects) for detailed documentation. |
| [initializeApp(options, config)](https://firebase.google.com/docs/reference/js/app.md#initializeapp_079e917) | Creates and initializes a FirebaseApp instance. |
| [initializeServerApp(options, config)](https://firebase.google.com/docs/reference/js/app.md#initializeserverapp_30ab697) | Creates and initializes a [FirebaseServerApp](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverapp_interface) instance.The `FirebaseServerApp` is similar to `FirebaseApp`, but is intended for execution in server side rendering environments only. Initialization will fail if invoked from a browser environment.See [Add Firebase to your app](https://firebase.google.com/docs/web/setup#add_firebase_to_your_app) and [Initialize multiple projects](https://firebase.google.com/docs/web/setup#multiple-projects) for detailed documentation. |

## Interfaces

| Interface | Description |
|---|---|
| [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) | A [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) holds the initialization information for a collection of services.Do not call this constructor directly. Instead, use [initializeApp()](https://firebase.google.com/docs/reference/js/app.md#initializeapp_cb2f5e1) to create an app. |
| [FirebaseAppSettings](https://firebase.google.com/docs/reference/js/app.firebaseappsettings.md#firebaseappsettings_interface) | Configuration options given to [initializeApp()](https://firebase.google.com/docs/reference/js/app.md#initializeapp_cb2f5e1) |
| [FirebaseOptions](https://firebase.google.com/docs/reference/js/app.firebaseoptions.md#firebaseoptions_interface) | Firebase configuration object. Contains a set of parameters required by services in order to successfully communicate with Firebase server APIs and to associate client data with your Firebase project and Firebase application. Typically this object is populated by the Firebase console at project setup. See also: [Learn about the Firebase config object](https://firebase.google.com/docs/web/setup#config-object). |
| [FirebaseServerApp](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverapp_interface) | A [FirebaseServerApp](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverapp_interface) holds the initialization information for a collection of services running in server environments.Do not call this constructor directly. Instead, use [initializeServerApp()](https://firebase.google.com/docs/reference/js/app.md#initializeserverapp_30ab697) to create an app. |
| [FirebaseServerAppSettings](https://firebase.google.com/docs/reference/js/app.firebaseserverappsettings.md#firebaseserverappsettings_interface) | Configuration options given to [initializeServerApp()](https://firebase.google.com/docs/reference/js/app.md#initializeserverapp_30ab697) |

## Variables

| Variable | Description |
|---|---|
| [SDK_VERSION](https://firebase.google.com/docs/reference/js/app.md#sdk_version) | The current SDK version. |

## function(app, ...)

### deleteApp(app)

Renders this app unusable and frees the resources of all associated services.

**Signature:**

    export declare function deleteApp(app: FirebaseApp): Promise<void>;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| app | [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) |   |

**Returns:**

Promise\<void\>

### Example

    deleteApp(app)
      .then(function() {
        console.log("App deleted successfully");
      })
      .catch(function(error) {
        console.log("Error deleting app:", error);
      });

## function()

### getApps()

A (read-only) array of all initialized apps.

**Signature:**

    export declare function getApps(): FirebaseApp[];

**Returns:**

[FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface)\[\]

### initializeApp()

Creates and initializes a FirebaseApp instance.

**Signature:**

    export declare function initializeApp(): FirebaseApp;

**Returns:**

[FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface)

## function(config, ...)

### initializeServerApp(config)

Creates and initializes a [FirebaseServerApp](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverapp_interface) instance.

**Signature:**

    export declare function initializeServerApp(config?: FirebaseServerAppSettings): FirebaseServerApp;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| config | [FirebaseServerAppSettings](https://firebase.google.com/docs/reference/js/app.firebaseserverappsettings.md#firebaseserverappsettings_interface) | Optional `FirebaseServerApp` settings. |

**Returns:**

[FirebaseServerApp](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverapp_interface)

The initialized `FirebaseServerApp`.

#### Exceptions

If invoked in an unsupported non-server environment such as a browser.

If [FirebaseServerAppSettings.releaseOnDeref](https://firebase.google.com/docs/reference/js/app.firebaseserverappsettings.md#firebaseserverappsettingsreleaseonderef) is defined but the runtime doesn't provide Finalization Registry support.

If the `FIREBASE_OPTIONS` environment variable does not contain a valid project configuration required for auto-initialization.

## function(libraryKeyOrName, ...)

### registerVersion(libraryKeyOrName, version, variant)

Registers a library's name and version for platform logging purposes.

**Signature:**

    export declare function registerVersion(libraryKeyOrName: string, version: string, variant?: string): void;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| libraryKeyOrName | string |   |
| version | string | Current version of that library. |
| variant | string | Bundle variant, e.g., node, rn, etc. |

**Returns:**

void

## function(logCallback, ...)

### onLog(logCallback, options)

Sets log handler for all Firebase SDKs.

**Signature:**

    export declare function onLog(logCallback: LogCallback | null, options?: LogOptions): void;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| logCallback | LogCallback \| null | An optional custom log handler that executes user code whenever the Firebase SDK makes a logging call. |
| options | LogOptions |   |

**Returns:**

void

## function(logLevel, ...)

### setLogLevel(logLevel)

Sets log level for all Firebase SDKs.

All of the log types above the current log level are captured (i.e. if you set the log level to `info`, errors are logged, but `debug` and `verbose` logs are not).

**Signature:**

    export declare function setLogLevel(logLevel: LogLevelString): void;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| logLevel | LogLevelString |   |

**Returns:**

void

## function(name, ...)

### getApp(name)

Retrieves a [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) instance.

When called with no arguments, the default app is returned. When an app name is provided, the app corresponding to that name is returned.

An exception is thrown if the app being retrieved has not yet been initialized.

**Signature:**

    export declare function getApp(name?: string): FirebaseApp;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| name | string | Optional name of the app to return. If no name is provided, the default is `"[DEFAULT]"`. |

**Returns:**

[FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface)

The app corresponding to the provided app name. If no app name is provided, the default app is returned.

### Example 1

    // Return the default app
    const app = getApp();

### Example 2

    // Return a named app
    const otherApp = getApp("otherApp");

## function(options, ...)

### initializeApp(options, name)

Creates and initializes a [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) instance.

See [Add Firebase to your app](https://firebase.google.com/docs/web/setup#add_firebase_to_your_app) and [Initialize multiple projects](https://firebase.google.com/docs/web/setup#multiple-projects) for detailed documentation.

**Signature:**

    export declare function initializeApp(options: FirebaseOptions, name?: string): FirebaseApp;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [FirebaseOptions](https://firebase.google.com/docs/reference/js/app.firebaseoptions.md#firebaseoptions_interface) | Options to configure the app's services. |
| name | string | Optional name of the app to initialize. If no name is provided, the default is `"[DEFAULT]"`. |

**Returns:**

[FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface)

The initialized app.

#### Exceptions

If the optional `name` parameter is malformed or empty.

If a `FirebaseApp` already exists with the same name but with a different configuration.

### Example 1


    // Initialize default app
    // Retrieve your own options values by adding a web app on
    // https://console.firebase.google.com
    initializeApp({
      apiKey: "AIza....",                             // Auth / General Use
      authDomain: "YOUR_APP.firebaseapp.com",         // Auth with popup/redirect
      databaseURL: "https://YOUR_APP.firebaseio.com", // Realtime Database
      storageBucket: "YOUR_APP.appspot.com",          // Storage
      messagingSenderId: "123456789"                  // Cloud Messaging
    });

### Example 2


    // Initialize another app
    const otherApp = initializeApp({
      databaseURL: "https://<OTHER_DATABASE_NAME>.firebaseio.com",
      storageBucket: "<OTHER_STORAGE_BUCKET>.appspot.com"
    }, "otherApp");

### initializeApp(options, config)

Creates and initializes a FirebaseApp instance.

**Signature:**

    export declare function initializeApp(options: FirebaseOptions, config?: FirebaseAppSettings): FirebaseApp;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [FirebaseOptions](https://firebase.google.com/docs/reference/js/app.firebaseoptions.md#firebaseoptions_interface) | Options to configure the app's services. |
| config | [FirebaseAppSettings](https://firebase.google.com/docs/reference/js/app.firebaseappsettings.md#firebaseappsettings_interface) | FirebaseApp Configuration |

**Returns:**

[FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface)

#### Exceptions

If [FirebaseAppSettings.name](https://firebase.google.com/docs/reference/js/app.firebaseappsettings.md#firebaseappsettingsname) is defined but the value is malformed or empty.

If a `FirebaseApp` already exists with the same name but with a different configuration.

### initializeServerApp(options, config)

Creates and initializes a [FirebaseServerApp](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverapp_interface) instance.

The `FirebaseServerApp` is similar to `FirebaseApp`, but is intended for execution in server side rendering environments only. Initialization will fail if invoked from a browser environment.

See [Add Firebase to your app](https://firebase.google.com/docs/web/setup#add_firebase_to_your_app) and [Initialize multiple projects](https://firebase.google.com/docs/web/setup#multiple-projects) for detailed documentation.

**Signature:**

    export declare function initializeServerApp(options: FirebaseOptions | FirebaseApp, config?: FirebaseServerAppSettings): FirebaseServerApp;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [FirebaseOptions](https://firebase.google.com/docs/reference/js/app.firebaseoptions.md#firebaseoptions_interface) \| [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) | `Firebase.AppOptions` to configure the app's services, or a a `FirebaseApp` instance which contains the `AppOptions` within. |
| config | [FirebaseServerAppSettings](https://firebase.google.com/docs/reference/js/app.firebaseserverappsettings.md#firebaseserverappsettings_interface) | Optional `FirebaseServerApp` settings. |

**Returns:**

[FirebaseServerApp](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverapp_interface)

The initialized `FirebaseServerApp`.

#### Exceptions

If invoked in an unsupported non-server environment such as a browser.

If [FirebaseServerAppSettings.releaseOnDeref](https://firebase.google.com/docs/reference/js/app.firebaseserverappsettings.md#firebaseserverappsettingsreleaseonderef) is defined but the runtime doesn't provide Finalization Registry support.

### Example


    // Initialize an instance of `FirebaseServerApp`.
    // Retrieve your own options values by adding a web app on
    // https://console.firebase.google.com
    initializeServerApp({
        apiKey: "AIza....",                             // Auth / General Use
        authDomain: "YOUR_APP.firebaseapp.com",         // Auth with popup/redirect
        databaseURL: "https://YOUR_APP.firebaseio.com", // Realtime Database
        storageBucket: "YOUR_APP.appspot.com",          // Storage
        messagingSenderId: "123456789"                  // Cloud Messaging
      },
      {
       authIdToken: "Your Auth ID Token"
      });

## SDK_VERSION

The current SDK version.

**Signature:**

    SDK_VERSION: string