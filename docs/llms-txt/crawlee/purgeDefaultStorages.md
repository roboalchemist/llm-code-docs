# Source: https://crawlee.dev/js/api/core/function/purgeDefaultStorages.md

# purgeDefaultStorages<!-- -->

### Callable

* ****purgeDefaultStorages**(options): Promise\<void>
* ****purgeDefaultStorages**(config, client): Promise\<void>

***

* Cleans up the local storage folder (defaults to `./storage`) created when running code locally. Purging will remove all the files in all storages except for INPUT.json in the default KV store.

  Purging of storages is happening automatically when we run our crawler (or when we open some storage explicitly, e.g. via `RequestList.open()`). We can disable that via `purgeOnStart` [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md) option or by setting `CRAWLEE_PURGE_ON_START` environment variable to `0` or `false`.

  This is a shortcut for running (optional) `purge` method on the StorageClient interface, in other words it will call the `purge` method of the underlying storage implementation we are currently using. You can make sure the storage is purged only once for a given execution context if you set `onlyPurgeOnce` to `true` in the `options` object

  ***

  #### Parameters

  * ##### optionaloptions: PurgeDefaultStorageOptions

  #### Returns Promise\<void>
