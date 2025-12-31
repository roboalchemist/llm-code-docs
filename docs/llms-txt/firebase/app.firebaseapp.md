# Source: https://firebase.google.com/docs/reference/js/app.firebaseapp.md.txt

# FirebaseApp interface

A [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) holds the initialization information for a collection of services.

Do not call this constructor directly. Instead, use [initializeApp()](https://firebase.google.com/docs/reference/js/app.md#initializeapp_cb2f5e1) to create an app.

**Signature:**  

    export interface FirebaseApp 

## Properties

|                                                                   Property                                                                   |                                                       Type                                                        |                                                                                          Description                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [automaticDataCollectionEnabled](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseappautomaticdatacollectionenabled) | boolean                                                                                                           | The settable config flag for GDPR opt-in/opt-out                                                                                                                                              |
| [name](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseappname)                                                     | string                                                                                                            | The (read-only) name for this app.The default app's name is `"[DEFAULT]"`.                                                                                                                    |
| [options](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseappoptions)                                               | [FirebaseOptions](https://firebase.google.com/docs/reference/js/app.firebaseoptions.md#firebaseoptions_interface) | The (read-only) configuration options for this app. These are the original parameters given in [initializeApp()](https://firebase.google.com/docs/reference/js/app.md#initializeapp_cb2f5e1). |

## FirebaseApp.automaticDataCollectionEnabled

The settable config flag for GDPR opt-in/opt-out

**Signature:**  

    automaticDataCollectionEnabled: boolean;

## FirebaseApp.name

The (read-only) name for this app.

The default app's name is `"[DEFAULT]"`.

**Signature:**  

    readonly name: string;

### Example 1

    // The default app's name is "[DEFAULT]"
    const app = initializeApp(defaultAppConfig);
    console.log(app.name);  // "[DEFAULT]"

### Example 2

    // A named app's name is what you provide to initializeApp()
    const otherApp = initializeApp(otherAppConfig, "other");
    console.log(otherApp.name);  // "other"

## FirebaseApp.options

The (read-only) configuration options for this app. These are the original parameters given in [initializeApp()](https://firebase.google.com/docs/reference/js/app.md#initializeapp_cb2f5e1).

**Signature:**  

    readonly options: FirebaseOptions;

### Example

    const app = initializeApp(config);
    console.log(app.options.databaseURL === config.databaseURL);  // true