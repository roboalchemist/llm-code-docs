# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.md.txt

# firebase-admin.app package

Firebase App and SDK initialization.

## Functions

|                                                                Function                                                                 |                                                                                                                                                                                                                                                                                                                              Description                                                                                                                                                                                                                                                                                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [applicationDefault(httpAgent)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.md#applicationdefault_2121df4) | Returns a credential created from the [Google Application Default Credentials](https://developers.google.com/identity/protocols/application-default-credentials) that grants admin access to Firebase services. This credential can be used in the call to [initializeApp()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.md#initializeapp_2848fbd).Google Application Default Credentials are available on any Google infrastructure, such as Google App Engine and Google Compute Engine.See [Initialize the SDK](https://firebase.google.com/docs/admin/setup#initialize_the_sdk) for more details.                                    |
| [cert(serviceAccountPathOrObject, httpAgent)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.md#cert_13d5f11) | Returns a credential created from the provided service account that grants admin access to Firebase services. This credential can be used in the call to [initializeApp()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.md#initializeapp_2848fbd).See [Initialize the SDK](https://firebase.google.com/docs/admin/setup#initialize_the_sdk) for more details.                                                                                                                                                                                                                                                                             |
| [deleteApp(app)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.md#deleteapp_8a40afc)                         | Renders this given `App` unusable and frees the resources of all associated services (though it does \*not\* clean up any backend resources). When running the SDK locally, this method must be called to ensure graceful termination of the process.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [getApp(appName)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.md#getapp_e087377)                           | Returns an existing [App](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.app.md#app_interface) instance for the provided name. If no name is provided the the default app name is used.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [getApps()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.md#getapps)                                        | A (read-only) array of all initialized apps.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [initializeApp(options, appName)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.md#initializeapp_2848fbd)    | Initializes the `App` instance.Creates a new instance of [App](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.app.md#app_interface) if one doesn't exist, or returns an existing `App` instance if one exists with the same `appName` and `options`.Note, due to the inablity to compare `http.Agent` objects and `Credential` objects, this function cannot support idempotency if either of `options.httpAgent` or `options.credential` are defined. When either is defined, subsequent invocations will throw a `FirebaseAppError` instead of returning an `App` object.For example, to safely initialize an app that may already exist: |

    let app;
    try {
      app = getApp("myApp");
    } catch (error) {
      app = initializeApp({ credential: myCredential }, "myApp");
    }

\|
\| [refreshToken(refreshTokenPathOrObject, httpAgent)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.md#refreshtoken_3d7f083) \| Returns a credential created from the provided refresh token that grants admin access to Firebase services. This credential can be used in the call to [initializeApp()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.md#initializeapp_2848fbd).See [Initialize the SDK](https://firebase.google.com/docs/admin/setup#initialize_the_sdk) for more details. \|

## Classes

|                                                                  Class                                                                  |                              Description                               |
|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| [AppErrorCodes](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.apperrorcodes.md#apperrorcodes_class)          | App client error codes and their default messages.                     |
| [FirebaseAppError](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.firebaseapperror.md#firebaseapperror_class) | Firebase App error code structure. This extends PrefixedFirebaseError. |

## Interfaces

|                                                                            Interface                                                                             |                                                                                                                       Description                                                                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [App](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.app.md#app_interface)                                                             | A Firebase app holds the initialization information for a collection of services.                                                                                                                                                                        |
| [AppOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.appoptions.md#appoptions_interface)                                        | Available options to pass to [initializeApp()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.md#initializeapp_2848fbd).                                                                                                       |
| [Credential](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.credential.md#credential_interface)                                        | Interface that provides Google OAuth2 access tokens used to authenticate with Firebase services.In most cases, you will not need to implement this yourself and can instead use the default implementations provided by the `firebase-admin/app` module. |
| [FirebaseArrayIndexError](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.firebasearrayindexerror.md#firebasearrayindexerror_interface) | Composite type which includes both a `FirebaseError` object and an index which can be used to get the errored item.                                                                                                                                      |
| [FirebaseError](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.firebaseerror.md#firebaseerror_interface)                               | `FirebaseError` is a subclass of the standard JavaScript `Error` object. In addition to a message string and stack trace, it contains a string code.                                                                                                     |
| [GoogleOAuthAccessToken](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.googleoauthaccesstoken.md#googleoauthaccesstoken_interface)    | Interface for Google OAuth 2.0 access tokens.                                                                                                                                                                                                            |
| [ServiceAccount](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.serviceaccount.md#serviceaccount_interface)                            |                                                                                                                                                                                                                                                          |

## Variables

|                                                Variable                                                | Description |
|--------------------------------------------------------------------------------------------------------|-------------|
| [SDK_VERSION](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.md#sdk_version) |             |

## applicationDefault(httpAgent)

Returns a credential created from the [Google Application Default Credentials](https://developers.google.com/identity/protocols/application-default-credentials) that grants admin access to Firebase services. This credential can be used in the call to [initializeApp()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.md#initializeapp_2848fbd).

Google Application Default Credentials are available on any Google infrastructure, such as Google App Engine and Google Compute Engine.

See [Initialize the SDK](https://firebase.google.com/docs/admin/setup#initialize_the_sdk) for more details.

**Signature:**  

    export declare function applicationDefault(httpAgent?: Agent): Credential;

### Parameters

| Parameter | Type  |                                                                    Description                                                                    |
|-----------|-------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| httpAgent | Agent | Optional [HTTP Agent](https://nodejs.org/api/http.html#http_class_http_agent) to be used when retrieving access tokens from Google token servers. |

**Returns:**

[Credential](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.credential.md#credential_interface)

A credential authenticated via Google Application Default Credentials that can be used to initialize an app.

### Example

    initializeApp({
      credential: applicationDefault(),
      databaseURL: "https://<DATABASE_NAME>.firebaseio.com"
    });

## cert(serviceAccountPathOrObject, httpAgent)

Returns a credential created from the provided service account that grants admin access to Firebase services. This credential can be used in the call to [initializeApp()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.md#initializeapp_2848fbd).

See [Initialize the SDK](https://firebase.google.com/docs/admin/setup#initialize_the_sdk) for more details.

**Signature:**  

    export declare function cert(serviceAccountPathOrObject: string | ServiceAccount, httpAgent?: Agent): Credential;

### Parameters

|         Parameter          |                                                                      Type                                                                       |                                                                    Description                                                                    |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| serviceAccountPathOrObject | string \| [ServiceAccount](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.serviceaccount.md#serviceaccount_interface) | The path to a service account key JSON file or an object representing a service account key.                                                      |
| httpAgent                  | Agent                                                                                                                                           | Optional [HTTP Agent](https://nodejs.org/api/http.html#http_class_http_agent) to be used when retrieving access tokens from Google token servers. |

**Returns:**

[Credential](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.credential.md#credential_interface)

A credential authenticated via the provided service account that can be used to initialize an app.

### Example 1

    // Providing a path to a service account key JSON file
    const serviceAccount = require("path/to/serviceAccountKey.json");
    initializeApp({
      credential: cert(serviceAccount),
      databaseURL: "https://<DATABASE_NAME>.firebaseio.com"
    });

### Example 2

    // Providing a service account object inline
    initializeApp({
      credential: cert({
        projectId: "<PROJECT_ID>",
        clientEmail: "foo@<PROJECT_ID>.iam.gserviceaccount.com",
        privateKey: "-----BEGIN PRIVATE KEY-----<KEY>-----END PRIVATE KEY-----\n"
      }),
      databaseURL: "https://<DATABASE_NAME>.firebaseio.com"
    });

## deleteApp(app)

Renders this given `App` unusable and frees the resources of all associated services (though it does \*not\* clean up any backend resources). When running the SDK locally, this method must be called to ensure graceful termination of the process.

**Signature:**  

    export declare function deleteApp(app: App): Promise<void>;

### Parameters

| Parameter |                                                 Type                                                 | Description |
|-----------|------------------------------------------------------------------------------------------------------|-------------|
| app       | [App](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.app.md#app_interface) |             |

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

## getApp(appName)

Returns an existing [App](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.app.md#app_interface) instance for the provided name. If no name is provided the the default app name is used.

**Signature:**  

    export declare function getApp(appName?: string): App;

### Parameters

| Parameter |  Type  |             Description              |
|-----------|--------|--------------------------------------|
| appName   | string | Optional name of the `App` instance. |

**Returns:**

[App](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.app.md#app_interface)

An existing `App` instance that matches the name provided.

### Exceptions

FirebaseAppError if no `App` exists for the given name.

FirebaseAppError if the `appName` is malformed.

## getApps()

A (read-only) array of all initialized apps.

**Signature:**  

    export declare function getApps(): App[];

**Returns:**

[App](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.app.md#app_interface)\[\]

An array containing all initialized apps.

## initializeApp(options, appName)

Initializes the `App` instance.

Creates a new instance of [App](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.app.md#app_interface) if one doesn't exist, or returns an existing `App` instance if one exists with the same `appName` and `options`.

Note, due to the inablity to compare `http.Agent` objects and `Credential` objects, this function cannot support idempotency if either of `options.httpAgent` or `options.credential` are defined. When either is defined, subsequent invocations will throw a `FirebaseAppError` instead of returning an `App` object.

For example, to safely initialize an app that may already exist:  

    let app;
    try {
      app = getApp("myApp");
    } catch (error) {
      app = initializeApp({ credential: myCredential }, "myApp");
    }

**Signature:**  

    export declare function initializeApp(options?: AppOptions, appName?: string): App;

### Parameters

| Parameter |                                                           Type                                                            |                                                                                                                                                                                                                    Description                                                                                                                                                                                                                    |
|-----------|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| options   | [AppOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.appoptions.md#appoptions_interface) | Optional A set of [AppOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.appoptions.md#appoptions_interface) for the `App` instance. If not present, `initializeApp` will try to initialize with the options from the `FIREBASE_CONFIG` environment variable. If the environment variable contains a string that starts with `{` it will be parsed as JSON, otherwise it will be assumed to be pointing to a file. |
| appName   | string                                                                                                                    | Optional name of the `App` instance.                                                                                                                                                                                                                                                                                                                                                                                                              |

**Returns:**

[App](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.app.md#app_interface)

A new App instance, or the existing App if the instance already exists with the provided configuration.

### Exceptions

FirebaseAppError if an `App` with the same name has already been initialized with a different set of `AppOptions`.

FirebaseAppError if an existing `App` exists and `options.httpAgent` or `options.credential` are defined. This is due to the function's inability to determine if the existing `App`'s `options` equate to the `options` parameter of this function. It's recommended to use [getApp()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.md#getapp_e087377) or [getApps()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.md#getapps) if your implementation uses either of these two fields in `AppOptions`.

## refreshToken(refreshTokenPathOrObject, httpAgent)

Returns a credential created from the provided refresh token that grants admin access to Firebase services. This credential can be used in the call to [initializeApp()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.md#initializeapp_2848fbd).

See [Initialize the SDK](https://firebase.google.com/docs/admin/setup#initialize_the_sdk) for more details.

**Signature:**  

    export declare function refreshToken(refreshTokenPathOrObject: string | object, httpAgent?: Agent): Credential;

### Parameters

|        Parameter         |       Type       |                                                                    Description                                                                    |
|--------------------------|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| refreshTokenPathOrObject | string \| object | The path to a Google OAuth2 refresh token JSON file or an object representing a Google OAuth2 refresh token.                                      |
| httpAgent                | Agent            | Optional [HTTP Agent](https://nodejs.org/api/http.html#http_class_http_agent) to be used when retrieving access tokens from Google token servers. |

**Returns:**

[Credential](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.credential.md#credential_interface)

A credential authenticated via the provided service account that can be used to initialize an app.

### Example

    // Providing a path to a refresh token JSON file
    const refreshToken = require("path/to/refreshToken.json");
    initializeApp({
      credential: refreshToken(refreshToken),
      databaseURL: "https://<DATABASE_NAME>.firebaseio.com"
    });

## SDK_VERSION

**Signature:**  

    SDK_VERSION: string