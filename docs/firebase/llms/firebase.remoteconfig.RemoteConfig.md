# Source: https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.RemoteConfig.md.txt

# RemoteConfig | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [remoteConfig](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig).
- RemoteConfig

The Firebase Remote Config service interface.

Do not call this constructor directly. Instead, use
[`firebase.remoteConfig()`](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig).

## Index

### Properties

- [app](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.RemoteConfig#app)
- [defaultConfig](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.RemoteConfig#defaultconfig)
- [fetchTimeMillis](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.RemoteConfig#fetchtimemillis)
- [lastFetchStatus](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.RemoteConfig#lastfetchstatus)
- [settings](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.RemoteConfig#settings)

### Methods

- [activate](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.RemoteConfig#activate)
- [ensureInitialized](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.RemoteConfig#ensureinitialized)
- [fetch](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.RemoteConfig#fetch)
- [fetchAndActivate](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.RemoteConfig#fetchandactivate)
- [getAll](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.RemoteConfig#getall)
- [getBoolean](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.RemoteConfig#getboolean)
- [getNumber](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.RemoteConfig#getnumber)
- [getString](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.RemoteConfig#getstring)
- [getValue](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.RemoteConfig#getvalue)
- [setLogLevel](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.RemoteConfig#setloglevel)

## Properties

### app

app: [App](https://firebase.google.com/docs/reference/js/v8/firebase.app.App)  
The [app](https://firebase.google.com/docs/reference/js/v8/firebase.app.App) associated with the `Performance` service
instance.

example
:

        var app = analytics.app;


### defaultConfig

defaultConfig: {}  
Object containing default values for configs.  

#### Type declaration

-

  ##### \[key: string\]: string \| number \| boolean

### fetchTimeMillis

fetchTimeMillis: number  
The Unix timestamp in milliseconds of the last *successful* fetch, or negative one if
the [RemoteConfig](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.RemoteConfig) instance either hasn't fetched or initialization
is incomplete.

### lastFetchStatus

lastFetchStatus: [FetchStatus](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig#fetchstatus)  
The status of the last fetch *attempt*.

### settings

settings: [Settings](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.Settings)  
Defines configuration for the Remote Config SDK.

## Methods

### activate

- activate ( ) : Promise \< boolean \>
- Makes the last fetched config available to the getters.
  Returns a promise which resolves to true if the current call activated the fetched configs.
  If the fetched configs were already activated, the promise will resolve to false.

  #### Returns Promise\<boolean\>

### ensureInitialized

- ensureInitialized ( ) : Promise \< void \>
- Ensures the last activated config are available to the getters.

  #### Returns Promise\<void\>

### fetch

- fetch ( ) : Promise \< void \>
- Fetches and caches configuration from the Remote Config service.

  #### Returns Promise\<void\>

### fetchAndActivate

- fetchAndActivate ( ) : Promise \< boolean \>
- Performs fetch and activate operations, as a convenience.
  Returns a promise which resolves to true if the current call activated the fetched configs.
  If the fetched configs were already activated, the promise will resolve to false.

  #### Returns Promise\<boolean\>

### getAll

- getAll ( ) : {}
- Gets all config.

  #### Returns {}

  -

    ##### \[key: string\]: [Value](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.Value)

### getBoolean

- getBoolean ( key : string ) : boolean
- Gets the value for the given key as a boolean.

  Convenience method for calling `remoteConfig.getValue(key).asBoolean()`.

  #### Parameters

  -

    ##### key: string

  #### Returns boolean

### getNumber

- getNumber ( key : string ) : number
- Gets the value for the given key as a number.

  Convenience method for calling `remoteConfig.getValue(key).asNumber()`.

  #### Parameters

  -

    ##### key: string

  #### Returns number

### getString

- getString ( key : string ) : string
- Gets the value for the given key as a String.

  Convenience method for calling `remoteConfig.getValue(key).asString()`.

  #### Parameters

  -

    ##### key: string

  #### Returns string

### getValue

- getValue ( key : string ) : [Value](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.Value)
- Gets the [Value](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.Value) for the given key.

  #### Parameters

  -

    ##### key: string

  #### Returns [Value](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.Value)

### setLogLevel

- setLogLevel ( logLevel : [LogLevel](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig#loglevel) ) : void
- Defines the log level to use.

  #### Parameters

  -

    ##### logLevel: [LogLevel](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig#loglevel)

  #### Returns void