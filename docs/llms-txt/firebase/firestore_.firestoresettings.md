# Source: https://firebase.google.com/docs/reference/js/firestore_.firestoresettings.md.txt

# FirestoreSettings interface

Specifies custom configurations for your Cloud Firestore instance. You must set these before invoking any other methods.

**Signature:**  

    export declare interface FirestoreSettings 

## Properties

|                                                                               Property                                                                                |                                                                                 Type                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                            Description                                                                                                                                                                                                                                                                                                                                                                                            |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [cacheSizeBytes](https://firebase.google.com/docs/reference/js/firestore_.firestoresettings.md#firestoresettingscachesizebytes)                                       | number                                                                                                                                                                | NOTE: This field will be deprecated in a future major release. Use `cache` field instead to specify cache size, and other cache configurations.An approximate cache size threshold for the on-disk data. If the cache grows beyond this size, Firestore will start removing data that hasn't been recently used. The size is not a guarantee that the cache will stay below that size, only that if the cache exceeds the given size, cleanup will be attempted.The default value is 40 MB. The threshold must be set to at least 1 MB, and can be set to `CACHE_SIZE_UNLIMITED` to disable garbage collection.                                                                                                                                                                                   |
| [experimentalAutoDetectLongPolling](https://firebase.google.com/docs/reference/js/firestore_.firestoresettings.md#firestoresettingsexperimentalautodetectlongpolling) | boolean                                                                                                                                                               | Configures the SDK's underlying transport (WebChannel) to automatically detect if long-polling should be used. This is very similar to `experimentalForceLongPolling`, but only uses long-polling if required.After having had a default value of `false` since its inception in 2019, the default value of this setting was changed in May 2023 to `true` in v9.22.0 of the Firebase JavaScript SDK. That is, auto-detection of long polling is now enabled by default. To disable it, set this setting to `false`, and please open a GitHub issue to share the problems that motivated you disabling long-polling auto-detection.This setting cannot be used in a Node.js environment.                                                                                                          |
| [experimentalForceLongPolling](https://firebase.google.com/docs/reference/js/firestore_.firestoresettings.md#firestoresettingsexperimentalforcelongpolling)           | boolean                                                                                                                                                               | Forces the SDK's underlying network transport (WebChannel) to use long-polling. Each response from the backend will be closed immediately after the backend sends data (by default responses are kept open in case the backend has more data to send). This avoids incompatibility issues with certain proxies, antivirus software, etc. that incorrectly buffer traffic indefinitely. Use of this option will cause some performance degradation though.This setting cannot be used with `experimentalAutoDetectLongPolling` and may be removed in a future release. If you find yourself using it to work around a specific network reliability issue, please tell us about it in https://github.com/firebase/firebase-js-sdk/issues/1674.This setting cannot be used in a Node.js environment. |
| [experimentalLongPollingOptions](https://firebase.google.com/docs/reference/js/firestore_.firestoresettings.md#firestoresettingsexperimentallongpollingoptions)       | [ExperimentalLongPollingOptions](https://firebase.google.com/docs/reference/js/firestore_.experimentallongpollingoptions.md#experimentallongpollingoptions_interface) | Options that configure the SDK's underlying network transport (WebChannel) when long-polling is used.These options are only used if `experimentalForceLongPolling` is true or if `experimentalAutoDetectLongPolling` is true and the auto-detection determined that long-polling was needed. Otherwise, these options have no effect.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [host](https://firebase.google.com/docs/reference/js/firestore_.firestoresettings.md#firestoresettingshost)                                                           | string                                                                                                                                                                | The hostname to connect to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [ignoreUndefinedProperties](https://firebase.google.com/docs/reference/js/firestore_.firestoresettings.md#firestoresettingsignoreundefinedproperties)                 | boolean                                                                                                                                                               | Whether to skip nested properties that are set to `undefined` during object serialization. If set to `true`, these properties are skipped and not written to Firestore. If set to `false` or omitted, the SDK throws an exception when it encounters properties of type `undefined`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [localCache](https://firebase.google.com/docs/reference/js/firestore_.firestoresettings.md#firestoresettingslocalcache)                                               | [FirestoreLocalCache](https://firebase.google.com/docs/reference/js/firestore_.md#firestorelocalcache)                                                                | Specifies the cache used by the SDK. Available options are `MemoryLocalCache` and `PersistentLocalCache`, each with different configuration options.When unspecified, `MemoryLocalCache` will be used by default.NOTE: setting this field and `cacheSizeBytes` at the same time will throw exception during SDK initialization. Instead, using the configuration in the `FirestoreLocalCache` object to specify the cache size.                                                                                                                                                                                                                                                                                                                                                                   |
| [ssl](https://firebase.google.com/docs/reference/js/firestore_.firestoresettings.md#firestoresettingsssl)                                                             | boolean                                                                                                                                                               | Whether to use SSL when connecting.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

## FirestoreSettings.cacheSizeBytes

NOTE: This field will be deprecated in a future major release. Use `cache` field instead to specify cache size, and other cache configurations.

An approximate cache size threshold for the on-disk data. If the cache grows beyond this size, Firestore will start removing data that hasn't been recently used. The size is not a guarantee that the cache will stay below that size, only that if the cache exceeds the given size, cleanup will be attempted.

The default value is 40 MB. The threshold must be set to at least 1 MB, and can be set to `CACHE_SIZE_UNLIMITED` to disable garbage collection.

**Signature:**  

    cacheSizeBytes?: number;

## FirestoreSettings.experimentalAutoDetectLongPolling

Configures the SDK's underlying transport (WebChannel) to automatically detect if long-polling should be used. This is very similar to `experimentalForceLongPolling`, but only uses long-polling if required.

After having had a default value of `false` since its inception in 2019, the default value of this setting was changed in May 2023 to `true` in v9.22.0 of the Firebase JavaScript SDK. That is, auto-detection of long polling is now enabled by default. To disable it, set this setting to `false`, and please open a GitHub issue to share the problems that motivated you disabling long-polling auto-detection.

This setting cannot be used in a Node.js environment.

**Signature:**  

    experimentalAutoDetectLongPolling?: boolean;

## FirestoreSettings.experimentalForceLongPolling

Forces the SDK's underlying network transport (WebChannel) to use long-polling. Each response from the backend will be closed immediately after the backend sends data (by default responses are kept open in case the backend has more data to send). This avoids incompatibility issues with certain proxies, antivirus software, etc. that incorrectly buffer traffic indefinitely. Use of this option will cause some performance degradation though.

This setting cannot be used with `experimentalAutoDetectLongPolling` and may be removed in a future release. If you find yourself using it to work around a specific network reliability issue, please tell us about it in https://github.com/firebase/firebase-js-sdk/issues/1674.

This setting cannot be used in a Node.js environment.

**Signature:**  

    experimentalForceLongPolling?: boolean;

## FirestoreSettings.experimentalLongPollingOptions

Options that configure the SDK's underlying network transport (WebChannel) when long-polling is used.

These options are only used if `experimentalForceLongPolling` is true or if `experimentalAutoDetectLongPolling` is true and the auto-detection determined that long-polling was needed. Otherwise, these options have no effect.

**Signature:**  

    experimentalLongPollingOptions?: ExperimentalLongPollingOptions;

## FirestoreSettings.host

The hostname to connect to.

**Signature:**  

    host?: string;

## FirestoreSettings.ignoreUndefinedProperties

Whether to skip nested properties that are set to `undefined` during object serialization. If set to `true`, these properties are skipped and not written to Firestore. If set to `false` or omitted, the SDK throws an exception when it encounters properties of type `undefined`.

**Signature:**  

    ignoreUndefinedProperties?: boolean;

## FirestoreSettings.localCache

Specifies the cache used by the SDK. Available options are `MemoryLocalCache` and `PersistentLocalCache`, each with different configuration options.

When unspecified, `MemoryLocalCache` will be used by default.

NOTE: setting this field and `cacheSizeBytes` at the same time will throw exception during SDK initialization. Instead, using the configuration in the `FirestoreLocalCache` object to specify the cache size.

**Signature:**  

    localCache?: FirestoreLocalCache;

## FirestoreSettings.ssl

Whether to use SSL when connecting.

**Signature:**  

    ssl?: boolean;