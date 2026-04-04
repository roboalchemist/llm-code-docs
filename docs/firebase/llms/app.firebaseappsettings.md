# Source: https://firebase.google.com/docs/reference/js/app.firebaseappsettings.md.txt

# FirebaseAppSettings interface

Configuration options given to [initializeApp()](https://firebase.google.com/docs/reference/js/app.md#initializeapp_cb2f5e1)

**Signature:**  

    export interface FirebaseAppSettings 

## Properties

|                                                                           Property                                                                           |  Type   |                              Description                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|-----------------------------------------------------------------------|
| [automaticDataCollectionEnabled](https://firebase.google.com/docs/reference/js/app.firebaseappsettings.md#firebaseappsettingsautomaticdatacollectionenabled) | boolean | The settable config flag for GDPR opt-in/opt-out. Defaults to true.   |
| [name](https://firebase.google.com/docs/reference/js/app.firebaseappsettings.md#firebaseappsettingsname)                                                     | string  | custom name for the Firebase App. The default value is `"[DEFAULT]"`. |

## FirebaseAppSettings.automaticDataCollectionEnabled

The settable config flag for GDPR opt-in/opt-out. Defaults to true.

**Signature:**  

    automaticDataCollectionEnabled?: boolean;

## FirebaseAppSettings.name

custom name for the Firebase App. The default value is `"[DEFAULT]"`.

**Signature:**  

    name?: string;