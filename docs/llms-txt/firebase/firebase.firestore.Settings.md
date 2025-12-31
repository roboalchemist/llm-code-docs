# Source: https://firebase.google.com/docs/reference/node/firebase.firestore.Settings.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Settings.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.firestore.Settings.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Settings.md.txt

# Settings | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [firestore](https://firebase.google.com/docs/reference/js/v8/firebase.firestore).
- Settings

Specifies custom configurations for your Cloud Firestore instance.
You must set these before invoking any other methods.

## Index

### Properties

- [cacheSizeBytes](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Settings#cachesizebytes)
- [experimentalAutoDetectLongPolling](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Settings#experimentalautodetectlongpolling)
- [experimentalForceLongPolling](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Settings#experimentalforcelongpolling)
- [host](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Settings#host)
- [ignoreUndefinedProperties](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Settings#ignoreundefinedproperties)
- [merge](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Settings#merge)
- [ssl](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Settings#ssl)

## Properties

### Optional cacheSizeBytes

cacheSizeBytes: number  
An approximate cache size threshold for the on-disk data. If the cache grows beyond this
size, Firestore will start removing data that hasn't been recently used. The size is not a
guarantee that the cache will stay below that size, only that if the cache exceeds the given
size, cleanup will be attempted.

The default value is 40 MB. The threshold must be set to at least 1 MB, and can be set to
CACHE_SIZE_UNLIMITED to disable garbage collection.

### Optional experimentalAutoDetectLongPolling

experimentalAutoDetectLongPolling: boolean  
Configures the SDK's underlying transport (WebChannel) to automatically detect if
long-polling should be used. This is very similar to `experimentalForceLongPolling`,
but only uses long-polling if required.

This setting will likely be enabled by default in future releases and cannot be
combined with `experimentalForceLongPolling`.

This setting does not work in a Node.js environment.

### Optional experimentalForceLongPolling

experimentalForceLongPolling: boolean  
Forces the SDK's underlying network transport (WebChannel) to use
long-polling. Each response from the backend will be closed immediately
after the backend sends data (by default responses are kept open in
case the backend has more data to send). This avoids incompatibility
issues with certain proxies, antivirus software, etc. that incorrectly
buffer traffic indefinitely. Use of this option will cause some
performance degradation though.

This setting cannot be used with `experimentalAutoDetectLongPolling` and
may be removed in a future release. If you find yourself using it to
work around a specific network reliability issue, please tell us about
it in <https://github.com/firebase/firebase-js-sdk/issues/1674>.

This setting does not work in a Node.js environment.

### Optional host

host: string  
The hostname to connect to.

### Optional ignoreUndefinedProperties

ignoreUndefinedProperties: boolean  
Whether to skip nested properties that are set to `undefined` during
object serialization. If set to `true`, these properties are skipped
and not written to Firestore. If set to `false` or omitted, the SDK
throws an exception when it encounters properties of type `undefined`.

### Optional merge

merge: boolean  
Whether to merge the provided settings with the existing settings. If
set to `true`, the settings are merged with existing settings. If
set to `false` or left unset, the settings replace the existing
settings.

### Optional ssl

ssl: boolean  
Whether to use SSL when connecting.