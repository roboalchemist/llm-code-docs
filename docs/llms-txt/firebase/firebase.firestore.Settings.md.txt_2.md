# Source: https://firebase.google.com/docs/reference/node/firebase.firestore.Settings.md.txt

# Settings | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/node/firebase).
- [firestore](https://firebase.google.com/docs/reference/node/firebase.firestore).
- Settings

Specifies custom configurations for your Cloud Firestore instance.
You must set these before invoking any other methods.

## Index

### Properties

- [cacheSizeBytes](https://firebase.google.com/docs/reference/node/firebase.firestore.Settings#cachesizebytes)
- [host](https://firebase.google.com/docs/reference/node/firebase.firestore.Settings#host)
- [ignoreUndefinedProperties](https://firebase.google.com/docs/reference/node/firebase.firestore.Settings#ignoreundefinedproperties)
- [merge](https://firebase.google.com/docs/reference/node/firebase.firestore.Settings#merge)
- [ssl](https://firebase.google.com/docs/reference/node/firebase.firestore.Settings#ssl)

## Properties

### Optional cacheSizeBytes

cacheSizeBytes: number An approximate cache size threshold for the on-disk data. If the cache grows beyond this
size, Firestore will start removing data that hasn't been recently used. The size is not a
guarantee that the cache will stay below that size, only that if the cache exceeds the given
size, cleanup will be attempted.

The default value is 40 MB. The threshold must be set to at least 1 MB, and can be set to
CACHE_SIZE_UNLIMITED to disable garbage collection.

### Optional host

host: string The hostname to connect to.

### Optional ignoreUndefinedProperties

ignoreUndefinedProperties: boolean Whether to skip nested properties that are set to `undefined` during
object serialization. If set to `true`, these properties are skipped
and not written to Firestore. If set to `false` or omitted, the SDK
throws an exception when it encounters properties of type `undefined`.

### Optional merge

merge: boolean Whether to merge the provided settings with the existing settings. If
set to `true`, the settings are merged with existing settings. If
set to `false` or left unset, the settings replace the existing
settings.

### Optional ssl

ssl: boolean Whether to use SSL when connecting.