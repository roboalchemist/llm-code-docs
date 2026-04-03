# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.app.md.txt

# App interface

A Firebase app holds the initialization information for a collection of services.

**Signature:**  

    export interface App 

## Properties

|                                               Property                                                |                                                           Type                                                            |                                                                                                     Description                                                                                                      |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [name](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.app.md#appname)       | string                                                                                                                    | The (read-only) name for this app.The default app's name is `"[DEFAULT]"`.                                                                                                                                           |
| [options](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.app.md#appoptions) | [AppOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.appoptions.md#appoptions_interface) | The (read-only) configuration options for this app. These are the original parameters given in [initializeApp()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.md#initializeapp_2848fbd). |

## App.name

The (read-only) name for this app.

The default app's name is `"[DEFAULT]"`.

**Signature:**  

    name: string;

### Example 1

    // The default app's name is "[DEFAULT]"
    initializeApp(defaultAppConfig);
    console.log(admin.app().name);  // "[DEFAULT]"

### Example 2

    // A named app's name is what you provide to initializeApp()
    const otherApp = initializeApp(otherAppConfig, "other");
    console.log(otherApp.name);  // "other"

## App.options

The (read-only) configuration options for this app. These are the original parameters given in [initializeApp()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.md#initializeapp_2848fbd).

**Signature:**  

    options: AppOptions;

### Example

    const app = initializeApp(config);
    console.log(app.options.credential === config.credential);  // true
    console.log(app.options.databaseURL === config.databaseURL);  // true