# Source: https://firebase.google.com/docs/reference/js/app.firebaseserverappsettings.md.txt

# FirebaseServerAppSettings interface

Configuration options given to [initializeServerApp()](https://firebase.google.com/docs/reference/js/app.md#initializeserverapp_30ab697)

**Signature:**  

    export interface FirebaseServerAppSettings extends Omit<FirebaseAppSettings, 'name'> 

**Extends:** Omit\<[FirebaseAppSettings](https://firebase.google.com/docs/reference/js/app.firebaseappsettings.md#firebaseappsettings_interface), 'name'\>

## Properties

|                                                                 Property                                                                 |  Type  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [appCheckToken](https://firebase.google.com/docs/reference/js/app.firebaseserverappsettings.md#firebaseserverappsettingsappchecktoken)   | string | An optional App Check token. If provided, the Firebase SDKs that use App Check will utilize this App Check token in place of requiring an instance of App Check to be initialized.If the token fails local verification due to expiration or parsing errors, then a console error is logged at the time of initialization of the `FirebaseServerApp` instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [authIdToken](https://firebase.google.com/docs/reference/js/app.firebaseserverappsettings.md#firebaseserverappsettingsauthidtoken)       | string | An optional Auth ID token used to resume a signed in user session from a client runtime environment.Invoking `getAuth` with a `FirebaseServerApp` configured with a validated `authIdToken` causes an automatic attempt to sign in the user that the `authIdToken` represents. The token needs to have been recently minted for this operation to succeed.If the token fails local verification due to expiration or parsing errors, then a console error is logged at the time of initialization of the `FirebaseServerApp` instance.If the Auth service has failed to validate the token when the Auth SDK is initialized, then an warning is logged to the console and the Auth SDK will not sign in a user on initialization.If a user is successfully signed in, then the Auth instance's `onAuthStateChanged` callback is invoked with the `User` object as per standard Auth flows. However, `User` objects created via an `authIdToken` do not have a refresh token. Attempted `refreshToken` operations fail. |
| [releaseOnDeref](https://firebase.google.com/docs/reference/js/app.firebaseserverappsettings.md#firebaseserverappsettingsreleaseonderef) | object | An optional object. If provided, the Firebase SDK uses a `FinalizationRegistry` object to monitor the garbage collection status of the provided object. The Firebase SDK releases its reference on the `FirebaseServerApp` instance when the provided `releaseOnDeref` object is garbage collected.You can use this field to reduce memory management overhead for your application. If provided, an app running in a SSR pass does not need to perform `FirebaseServerApp` cleanup, so long as the reference object is deleted (by falling out of SSR scope, for instance.)If an object is not provided then the application must clean up the `FirebaseServerApp` instance by invoking `deleteApp`.If the application provides an object in this parameter, but the application is executed in a JavaScript engine that predates the support of `FinalizationRegistry` (introduced in node v14.6.0, for instance), then an error is thrown at `FirebaseServerApp` initialization.                                    |

## FirebaseServerAppSettings.appCheckToken

An optional App Check token. If provided, the Firebase SDKs that use App Check will utilize this App Check token in place of requiring an instance of App Check to be initialized.

If the token fails local verification due to expiration or parsing errors, then a console error is logged at the time of initialization of the `FirebaseServerApp` instance.

**Signature:**  

    appCheckToken?: string;

## FirebaseServerAppSettings.authIdToken

An optional Auth ID token used to resume a signed in user session from a client runtime environment.

Invoking `getAuth` with a `FirebaseServerApp` configured with a validated `authIdToken` causes an automatic attempt to sign in the user that the `authIdToken` represents. The token needs to have been recently minted for this operation to succeed.

If the token fails local verification due to expiration or parsing errors, then a console error is logged at the time of initialization of the `FirebaseServerApp` instance.

If the Auth service has failed to validate the token when the Auth SDK is initialized, then an warning is logged to the console and the Auth SDK will not sign in a user on initialization.

If a user is successfully signed in, then the Auth instance's `onAuthStateChanged` callback is invoked with the `User` object as per standard Auth flows. However, `User` objects created via an `authIdToken` do not have a refresh token. Attempted `refreshToken` operations fail.

**Signature:**  

    authIdToken?: string;

## FirebaseServerAppSettings.releaseOnDeref

An optional object. If provided, the Firebase SDK uses a `FinalizationRegistry` object to monitor the garbage collection status of the provided object. The Firebase SDK releases its reference on the `FirebaseServerApp` instance when the provided `releaseOnDeref` object is garbage collected.

You can use this field to reduce memory management overhead for your application. If provided, an app running in a SSR pass does not need to perform `FirebaseServerApp` cleanup, so long as the reference object is deleted (by falling out of SSR scope, for instance.)

If an object is not provided then the application must clean up the `FirebaseServerApp` instance by invoking `deleteApp`.

If the application provides an object in this parameter, but the application is executed in a JavaScript engine that predates the support of `FinalizationRegistry` (introduced in node v14.6.0, for instance), then an error is thrown at `FirebaseServerApp` initialization.

**Signature:**  

    releaseOnDeref?: object;