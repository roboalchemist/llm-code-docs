# Source: https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md.txt

# FirebaseServerApp interface

A [FirebaseServerApp](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverapp_interface) holds the initialization information for a collection of services running in server environments.

Do not call this constructor directly. Instead, use [initializeServerApp()](https://firebase.google.com/docs/reference/js/app.md#initializeserverapp_30ab697) to create an app.

**Signature:**  

    export interface FirebaseServerApp extends FirebaseApp 

**Extends:** [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface)

## Properties

|                                                   Property                                                   |                                                                      Type                                                                       |                                                                                                              Description                                                                                                              |
|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [name](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverappname)         | string                                                                                                                                          | There is no `getApp()` operation for `FirebaseServerApp`, so the name is not relevant for applications. However, it may be used internally, and is declared here so that `FirebaseServerApp` conforms to the `FirebaseApp` interface. |
| [settings](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverappsettings) | [FirebaseServerAppSettings](https://firebase.google.com/docs/reference/js/app.firebaseserverappsettings.md#firebaseserverappsettings_interface) | The (read-only) configuration settings for this server app. These are the original parameters given in [initializeServerApp()](https://firebase.google.com/docs/reference/js/app.md#initializeserverapp_30ab697).                     |

## FirebaseServerApp.name

There is no `getApp()` operation for `FirebaseServerApp`, so the name is not relevant for applications. However, it may be used internally, and is declared here so that `FirebaseServerApp` conforms to the `FirebaseApp` interface.

**Signature:**  

    name: string;

## FirebaseServerApp.settings

The (read-only) configuration settings for this server app. These are the original parameters given in [initializeServerApp()](https://firebase.google.com/docs/reference/js/app.md#initializeserverapp_30ab697).

**Signature:**  

    readonly settings: FirebaseServerAppSettings;

### Example

    const app = initializeServerApp(settings);
    console.log(app.settings.authIdToken === options.authIdToken);  // true