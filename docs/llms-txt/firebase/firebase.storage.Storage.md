# Source: https://firebase.google.com/docs/reference/node/firebase.storage.Storage.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.storage.Storage.md.txt

# Storage | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [storage](https://firebase.google.com/docs/reference/js/v8/firebase.storage).
- Storage

The Firebase Storage service interface.

Do not call this constructor directly. Instead, use
[`firebase.storage()`](https://firebase.google.com/docs/reference/js/v8/firebase.storage).

See
[Get Started on Web](https://firebase.google.com/docs/storage/web/start/)
for a full guide on how to use the Firebase Storage service.

## Index

### Properties

- [app](https://firebase.google.com/docs/reference/js/v8/firebase.storage.Storage#app)
- [maxOperationRetryTime](https://firebase.google.com/docs/reference/js/v8/firebase.storage.Storage#maxoperationretrytime)
- [maxUploadRetryTime](https://firebase.google.com/docs/reference/js/v8/firebase.storage.Storage#maxuploadretrytime)

### Methods

- [ref](https://firebase.google.com/docs/reference/js/v8/firebase.storage.Storage#ref)
- [refFromURL](https://firebase.google.com/docs/reference/js/v8/firebase.storage.Storage#reffromurl)
- [setMaxOperationRetryTime](https://firebase.google.com/docs/reference/js/v8/firebase.storage.Storage#setmaxoperationretrytime)
- [setMaxUploadRetryTime](https://firebase.google.com/docs/reference/js/v8/firebase.storage.Storage#setmaxuploadretrytime)
- [useEmulator](https://firebase.google.com/docs/reference/js/v8/firebase.storage.Storage#useemulator)

## Properties

### app

app: [App](https://firebase.google.com/docs/reference/js/v8/firebase.app.App)  
The [app](https://firebase.google.com/docs/reference/js/v8/firebase.app.App) associated with the `Storage` service
instance.

example
:

        var app = storage.app;


### maxOperationRetryTime

maxOperationRetryTime: number  
The maximum time to retry operations other than uploads or downloads in
milliseconds.

### maxUploadRetryTime

maxUploadRetryTime: number  
The maximum time to retry uploads in milliseconds.

## Methods

### ref

- ref ( path ? : string ) : [Reference](https://firebase.google.com/docs/reference/js/v8/firebase.storage.Reference)
- Returns a reference for the given path in the default bucket.

  #### Parameters

  -

    ##### Optional path: string

    A relative path to initialize the reference with,
    for example `path/to/image.jpg`. If not passed, the returned reference
    points to the bucket root.

  #### Returns [Reference](https://firebase.google.com/docs/reference/js/v8/firebase.storage.Reference)

  A reference for the given path.

### refFromURL

- refFromURL ( url : string ) : [Reference](https://firebase.google.com/docs/reference/js/v8/firebase.storage.Reference)
- Returns a reference for the given absolute URL.

  #### Parameters

  -

    ##### url: string

    A URL in the form:   

    1) a gs:// URL, for example `gs://bucket/files/image.png`   

    2) a download URL taken from object metadata.   

  #### Returns [Reference](https://firebase.google.com/docs/reference/js/v8/firebase.storage.Reference)

  A reference for the given URL.

### setMaxOperationRetryTime

- setMaxOperationRetryTime ( time : number ) : any
-

  see

  :   [firebase.storage.Storage.maxOperationRetryTime](https://firebase.google.com/docs/reference/js/v8/firebase.storage.Storage#maxoperationretrytime)

  #### Parameters

  -

    ##### time: number

    The new maximum operation retry time in milliseconds.

  #### Returns any

### setMaxUploadRetryTime

- setMaxUploadRetryTime ( time : number ) : any
-

  see

  :   [firebase.storage.Storage.maxUploadRetryTime](https://firebase.google.com/docs/reference/js/v8/firebase.storage.Storage#maxuploadretrytime)

  #### Parameters

  -

    ##### time: number

    The new maximum upload retry time in milliseconds.

  #### Returns any

### useEmulator

- useEmulator ( host : string , port : number , options ? : { mockUserToken ?: [EmulatorMockTokenOptions](https://firebase.google.com/docs/reference/js/v8/firebase#emulatormocktokenoptions) \| string } ) : void
- Modify this `Storage` instance to communicate with the Cloud Storage emulator.

  #### Parameters

  -

    ##### host: string

    The emulator host (ex: localhost)
  -

    ##### port: number

    The emulator port (ex: 5001)
  -

    ##### Optional options: { mockUserToken?: [EmulatorMockTokenOptions](https://firebase.google.com/docs/reference/js/v8/firebase#emulatormocktokenoptions) \| string }

    -

      ##### Optional mockUserToken?: [EmulatorMockTokenOptions](https://firebase.google.com/docs/reference/js/v8/firebase#emulatormocktokenoptions) \| string

      the mock auth token to use for unit testing Security Rules

  #### Returns void