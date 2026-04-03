# Source: https://firebase.google.com/docs/reference/node/firebase.app.App.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.app.App.md.txt

# App | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [app](https://firebase.google.com/docs/reference/js/v8/firebase.app).
- App

A Firebase App holds the initialization information for a collection of
services.

Do not call this constructor directly. Instead, use
[`firebase.initializeApp()`](https://firebase.google.com/docs/reference/js/v8/firebase#initializeapp) to create an app.

## Index

### Properties

- [automaticDataCollectionEnabled](https://firebase.google.com/docs/reference/js/v8/firebase.app.App#automaticdatacollectionenabled)
- [name](https://firebase.google.com/docs/reference/js/v8/firebase.app.App#name)
- [options](https://firebase.google.com/docs/reference/js/v8/firebase.app.App#options)

### Methods

- [analytics](https://firebase.google.com/docs/reference/js/v8/firebase.app.App#analytics)
- [appCheck](https://firebase.google.com/docs/reference/js/v8/firebase.app.App#appcheck)
- [auth](https://firebase.google.com/docs/reference/js/v8/firebase.app.App#auth)
- [database](https://firebase.google.com/docs/reference/js/v8/firebase.app.App#database)
- [delete](https://firebase.google.com/docs/reference/js/v8/firebase.app.App#delete)
- [firestore](https://firebase.google.com/docs/reference/js/v8/firebase.app.App#firestore)
- [functions](https://firebase.google.com/docs/reference/js/v8/firebase.app.App#functions)
- [installations](https://firebase.google.com/docs/reference/js/v8/firebase.app.App#installations)
- [messaging](https://firebase.google.com/docs/reference/js/v8/firebase.app.App#messaging)
- [performance](https://firebase.google.com/docs/reference/js/v8/firebase.app.App#performance)
- [remoteConfig](https://firebase.google.com/docs/reference/js/v8/firebase.app.App#remoteconfig)
- [storage](https://firebase.google.com/docs/reference/js/v8/firebase.app.App#storage)

## Properties

### automaticDataCollectionEnabled

automaticDataCollectionEnabled: boolean  
The settable config flag for GDPR opt-in/opt-out

### name

name: string  
The (read-only) name for this app.

The default app's name is `"[DEFAULT]"`.

example
:

        // The default app's name is "[DEFAULT]"
        firebase.initializeApp(defaultAppConfig);
        console.log(firebase.app().name);  // "[DEFAULT]"


example
:

        // A named app's name is what you provide to initializeApp()
        var otherApp = firebase.initializeApp(otherAppConfig, "other");
        console.log(otherApp.name);  // "other"


### options

options: Object  
The (read-only) configuration options for this app. These are the original
parameters given in
[`firebase.initializeApp()`](https://firebase.google.com/docs/reference/js/v8/firebase#initializeapp).

example
:

        var app = firebase.initializeApp(config);
        console.log(app.options.databaseURL === config.databaseURL);  // true


## Methods

### analytics

- analytics ( ) : [Analytics](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.Analytics)
- Gets the [`Analytics`](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.Analytics) service for the
  current app. If the current app is not the default one, throws an error.

  The Analytics SDK does not work in a Node.js environment.

  example
  :

          const analytics = app.analytics();
          // The above is shorthand for:
          // const analytics = firebase.analytics(app);


  #### Returns [Analytics](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.Analytics)

### appCheck

- appCheck ( ) : [AppCheck](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.AppCheck)
-

  #### Returns [AppCheck](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.AppCheck)

### auth

- auth ( ) : [Auth](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth)
- Gets the [`Auth`](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth) service for the current app.

  example
  :

          var auth = app.auth();
          // The above is shorthand for:
          // var auth = firebase.auth(app);


  #### Returns [Auth](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth)

### database

- database ( url ? : string ) : [Database](https://firebase.google.com/docs/reference/js/v8/firebase.database.Database)
- Gets the [`Database`](https://firebase.google.com/docs/reference/js/v8/firebase.database.Database) service for the
  current app.

  example
  :

          var database = app.database();
          // The above is shorthand for:
          // var database = firebase.database(app);


  #### Parameters

  -

    ##### Optional url: string

  #### Returns [Database](https://firebase.google.com/docs/reference/js/v8/firebase.database.Database)

### delete

- delete ( ) : Promise \< any \>
- Renders this app unusable and frees the resources of all associated
  services.

  example
  :

          app.delete()
            .then(function() {
              console.log("App deleted successfully");
            })
            .catch(function(error) {
              console.log("Error deleting app:", error);
            });


  #### Returns Promise\<any\>

### firestore

- firestore ( ) : [Firestore](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Firestore)
-

  #### Returns [Firestore](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Firestore)

### functions

- functions ( regionOrCustomDomain ? : string ) : [Functions](https://firebase.google.com/docs/reference/js/v8/firebase.functions.Functions)
-

  #### Parameters

  -

    ##### Optional regionOrCustomDomain: string

  #### Returns [Functions](https://firebase.google.com/docs/reference/js/v8/firebase.functions.Functions)

### installations

- installations ( ) : [Installations](https://firebase.google.com/docs/reference/js/v8/firebase.installations.Installations)
- Gets the [`Installations`](https://firebase.google.com/docs/reference/js/v8/firebase.installations.Installations) service for the
  current app.

  The Installations SDK does not work in a Node.js environment.

  example
  :

          const installations = app.installations();
          // The above is shorthand for:
          // const installations = firebase.installations(app);


  #### Returns [Installations](https://firebase.google.com/docs/reference/js/v8/firebase.installations.Installations)

### messaging

- messaging ( ) : [Messaging](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.Messaging)
- Gets the [`Messaging`](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.Messaging) service for the
  current app.

  The Messaging SDK does not work in a Node.js environment.

  example
  :

          var messaging = app.messaging();
          // The above is shorthand for:
          // var messaging = firebase.messaging(app);


  #### Returns [Messaging](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.Messaging)

### performance

- performance ( ) : [Performance](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Performance)
- Gets the [`Performance`](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Performance) service for the
  current app. If the current app is not the default one, throws an error.

  The Performance SDK does not work in a Node.js environment.

  example
  :

          const perf = app.performance();
          // The above is shorthand for:
          // const perf = firebase.performance(app);


  #### Returns [Performance](https://firebase.google.com/docs/reference/js/v8/firebase.performance.Performance)

### remoteConfig

- remoteConfig ( ) : [RemoteConfig](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.RemoteConfig)
- Gets the [`RemoteConfig`](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.RemoteConfig) instance.

  The Remote Config SDK does not work in a Node.js environment.

  example
  :

          const rc = app.remoteConfig();
          // The above is shorthand for:
          // const rc = firebase.remoteConfig(app);


  #### Returns [RemoteConfig](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.RemoteConfig)

### storage

- storage ( url ? : string ) : [Storage](https://firebase.google.com/docs/reference/js/v8/firebase.storage.Storage)
- Gets the [`Storage`](https://firebase.google.com/docs/reference/js/v8/firebase.storage.Storage) service for the current
  app, optionally initialized with a custom storage bucket.

  example
  :

          var storage = app.storage();
          // The above is shorthand for:
          // var storage = firebase.storage(app);


  example
  :

          var storage = app.storage("gs://your-app.appspot.com");


  #### Parameters

  -

    ##### Optional url: string

    The gs:// url to your Firebase Storage Bucket.
    If not passed, uses the app's default Storage Bucket.

  #### Returns [Storage](https://firebase.google.com/docs/reference/js/v8/firebase.storage.Storage)