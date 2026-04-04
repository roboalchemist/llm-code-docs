# Source: https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.Settings.md.txt

# Settings | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [remoteConfig](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig).
- Settings

Defines configuration options for the Remote Config SDK.

## Index

### Properties

- [fetchTimeoutMillis](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.Settings#fetchtimeoutmillis)
- [minimumFetchIntervalMillis](https://firebase.google.com/docs/reference/js/v8/firebase.remoteconfig.Settings#minimumfetchintervalmillis)

## Properties

### fetchTimeoutMillis

fetchTimeoutMillis: number  
Defines the maximum amount of milliseconds to wait for a response when fetching
configuration from the Remote Config server. Defaults to 60000 (One minute).

### minimumFetchIntervalMillis

minimumFetchIntervalMillis: number  
Defines the maximum age in milliseconds of an entry in the config cache before
it is considered stale. Defaults to 43200000 (Twelve hours).