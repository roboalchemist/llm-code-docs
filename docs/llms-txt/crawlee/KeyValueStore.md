# Source: https://crawlee.dev/js/api/core/class/KeyValueStore.md

# KeyValueStore<!-- -->

The `KeyValueStore` class represents a key-value store, a simple data storage that is used for saving and reading data records or files. Each data record is represented by a unique key and associated with a MIME content type. Key-value stores are ideal for saving screenshots, crawler inputs and outputs, web pages, PDFs or to persist the state of crawlers.

Do not instantiate this class directly, use the [KeyValueStore.open](https://crawlee.dev/js/api/core/class/KeyValueStore.md#open) function instead.

Each crawler run is associated with a default key-value store, which is created exclusively for the run. By convention, the crawler input and output are stored into the default key-value store under the `INPUT` and `OUTPUT` key, respectively. Typically, input and output are JSON files, although it can be any other format. To access the default key-value store directly, you can use the [KeyValueStore.getValue](https://crawlee.dev/js/api/core/class/KeyValueStore.md#getValue) and [KeyValueStore.setValue](https://crawlee.dev/js/api/core/class/KeyValueStore.md#setValue) convenience functions.

To access the input, you can also use the KeyValueStore.getInput convenience function.

`KeyValueStore` stores its data on a local disk.

If the `CRAWLEE_STORAGE_DIR` environment variable is set, the data is stored in the local directory in the following files:

```
{CRAWLEE_STORAGE_DIR}/key_value_stores/{STORE_ID}/{INDEX}.{EXT}
```

Note that `{STORE_ID}` is the name or ID of the key-value store. The default key-value store has ID: `default`, unless you override it by setting the `CRAWLEE_DEFAULT_KEY_VALUE_STORE_ID` environment variable. The `{KEY}` is the key of the record and `{EXT}` corresponds to the MIME content type of the data value.

**Example usage:**

```
// Get crawler input from the default key-value store.
const input = await KeyValueStore.getInput();
// Get some value from the default key-value store.
const otherValue = await KeyValueStore.getValue('my-key');

// Write crawler output to the default key-value store.
await KeyValueStore.setValue('OUTPUT', { myResult: 123 });

// Open a named key-value store
const store = await KeyValueStore.open('some-name');

// Write a record. JavaScript object is automatically converted to JSON,
// strings and binary buffers are stored as they are
await store.setValue('some-key', { foo: 'bar' });

// Read a record. Note that JSON is automatically parsed to a JavaScript object,
// text data returned as a string and other data is returned as binary buffer
const value = await store.getValue('some-key');

 // Drop (delete) the store
await store.drop();
```

## Index[**](#Index)

### Properties

* [**config](#config)
* [**id](#id)
* [**name](#name)
* [**storageObject](#storageObject)

### Methods

* [**\[asyncIterator\]](#\[asyncIterator])
* [**drop](#drop)
* [**entries](#entries)
* [**forEachKey](#forEachKey)
* [**getAutoSavedValue](#getAutoSavedValue)
* [**getPublicUrl](#getPublicUrl)
* [**getValue](#getValue)
* [**keys](#keys)
* [**recordExists](#recordExists)
* [**setValue](#setValue)
* [**values](#values)
* [**getAutoSavedValue](#getAutoSavedValue)
* [**open](#open)
* [**recordExists](#recordExists)

## Properties<!-- -->[**](#Properties)

### [**](#config)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/key_value_store.ts#L123)readonlyconfig

**config: [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md) =

<!-- -->

...

### [**](#id)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/key_value_store.ts#L109)readonlyid

**id: string

### [**](#name)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/key_value_store.ts#L110)optionalreadonlyname

**name?

<!-- -->

: string

### [**](#storageObject)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/key_value_store.ts#L111)optionalreadonlystorageObject

**storageObject?

<!-- -->

: Record\<string, unknown>

## Methods<!-- -->[**](#Methods)

### [**](#\[asyncIterator])[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/key_value_store.ts#L570)\[asyncIterator]

* ****\[asyncIterator]**\<T>(): AsyncGenerator<\[string, T], void, undefined>

- Default async iterator for the key-value store, iterating over entries (key-value pairs). Allows using the store directly in a `for await...of` loop.

  **Example usage:**

  ```
  const keyValueStore = await KeyValueStore.open();
  for await (const [key, value] of keyValueStore) {
    console.log(`${key}: ${value}`);
  }
  ```

  ***

  #### Returns AsyncGenerator<\[string, T], void, undefined>

### [**](#drop)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/key_value_store.ts#L416)drop

* ****drop**(): Promise\<void>

- Removes the key-value store either from the Apify cloud storage or from the local directory, depending on the mode of operation.

  ***

  #### Returns Promise\<void>

### [**](#entries)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/key_value_store.ts#L546)entries

* ****entries**\<T>(options): AsyncIterable<\[string, T], any, any> & Promise<\[string, T]\[]>

- Iterates over key-value store entries (key-value pairs) using an async generator, allowing the use of `for await...of` syntax.

  **Example usage:**

  ```
  const keyValueStore = await KeyValueStore.open();
  for await (const [key, value] of keyValueStore.entries()) {
    console.log(`${key}: ${value}`);
  }
  ```

  ***

  #### Parameters

  * ##### options: [KeyValueStoreIteratorOptions](https://crawlee.dev/js/api/core/interface/KeyValueStoreIteratorOptions.md) = <!-- -->{}

    Options for the iteration.

  #### Returns AsyncIterable<\[string, T], any, any> & Promise<\[string, T]\[]>

### [**](#forEachKey)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/key_value_store.ts#L452)forEachKey

* ****forEachKey**(iteratee, options): Promise\<void>

- Iterates over key-value store keys, yielding each in turn to an `iteratee` function. Each invocation of `iteratee` is called with three arguments: `(key, index, info)`, where `key` is the record key, `index` is a zero-based index of the key in the current iteration (regardless of `options.exclusiveStartKey`) and `info` is an object that contains a single property `size` indicating size of the record in bytes.

  If the `iteratee` function returns a Promise then it is awaited before the next call. If it throws an error, the iteration is aborted and the `forEachKey` function throws the error.

  **Example usage**

  ```
  const keyValueStore = await KeyValueStore.open();
  await keyValueStore.forEachKey(async (key, index, info) => {
    console.log(`Key at ${index}: ${key} has size ${info.size}`);
  });
  ```

  ***

  #### Parameters

  * ##### iteratee: [KeyConsumer](https://crawlee.dev/js/api/core/interface/KeyConsumer.md)

    A function that is called for every key in the key-value store.

  * ##### optionaloptions: [KeyValueStoreIteratorOptions](https://crawlee.dev/js/api/core/interface/KeyValueStoreIteratorOptions.md) = <!-- -->{}

    All `forEachKey()` parameters.

  #### Returns Promise\<void>

### [**](#getAutoSavedValue)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/key_value_store.ts#L249)getAutoSavedValue

* ****getAutoSavedValue**\<T>(key, defaultValue): Promise\<T>

- #### Parameters

  * ##### key: string
  * ##### defaultValue: T = <!-- -->...

  #### Returns Promise\<T>

### [**](#getPublicUrl)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/key_value_store.ts#L577)getPublicUrl

* ****getPublicUrl**(key): string

- Returns a file URL for the given key.

  ***

  #### Parameters

  * ##### key: string

  #### Returns string

### [**](#getValue)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/key_value_store.ts#L161)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/key_value_store.ts#L194)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/key_value_store.ts#L227)getValue

* ****getValue**\<T>(key): Promise\<null | T>
* ****getValue**\<T>(key, defaultValue): Promise\<T>

- Gets a value from the key-value store.

  The function returns a `Promise` that resolves to the record value, whose JavaScript type depends on the MIME content type of the record. Records with the `application/json` content type are automatically parsed and returned as a JavaScript object. Similarly, records with `text/plain` content types are returned as a string. For all other content types, the value is returned as a raw [`Buffer`](https://nodejs.org/api/buffer.html) instance.

  If the record does not exist, the function resolves to `null`.

  To save or delete a value in the key-value store, use the [KeyValueStore.setValue](https://crawlee.dev/js/api/core/class/KeyValueStore.md#setValue) function.

  **Example usage:**

  ```
  const store = await KeyValueStore.open();
  const buffer = await store.getValue('screenshot1.png');
  ```

  ***

  #### Parameters

  * ##### key: string

    Unique key of the record. It can be at most 256 characters long and only consist of the following characters: `a`-`z`, `A`-`Z`, `0`-`9` and `!-_.'()`

  #### Returns Promise\<null | T>

  Returns a promise that resolves to an object, string or [`Buffer`](https://nodejs.org/api/buffer.html), depending on the MIME content type of the record.

### [**](#keys)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/key_value_store.ts#L498)keys

* ****keys**(options): AsyncGenerator\<string, void, undefined>

- Iterates over key-value store keys using an async generator, allowing the use of `for await...of` syntax.

  **Example usage:**

  ```
  const keyValueStore = await KeyValueStore.open();
  for await (const key of keyValueStore.keys()) {
    console.log(key);
  }
  ```

  ***

  #### Parameters

  * ##### options: [KeyValueStoreIteratorOptions](https://crawlee.dev/js/api/core/interface/KeyValueStoreIteratorOptions.md) = <!-- -->{}

    Options for the iteration.

  #### Returns AsyncGenerator\<string, void, undefined>

### [**](#recordExists)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/key_value_store.ts#L242)recordExists

* ****recordExists**(key): Promise\<boolean>

- Tests whether a record with the given key exists in the key-value store without retrieving its value.

  ***

  #### Parameters

  * ##### key: string

    The queried record key.

  #### Returns Promise\<boolean>

  `true` if the record exists, `false` if it does not.

### [**](#setValue)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/key_value_store.ts#L342)setValue

* ****setValue**\<T>(key, value, options): Promise\<void>

- Saves or deletes a record in the key-value store. The function returns a promise that resolves once the record has been saved or deleted.

  **Example usage:**

  ```
  const store = await KeyValueStore.open();
  await store.setValue('OUTPUT', { foo: 'bar' });
  ```

  Beware that the key can be at most 256 characters long and only contain the following characters: `a-zA-Z0-9!-_.'()`

  By default, `value` is converted to JSON and stored with the `application/json; charset=utf-8` MIME content type. To store the value with another content type, pass it in the options as follows:

  ```
  const store = await KeyValueStore.open('my-text-store');
  await store.setValue('RESULTS', 'my text data', { contentType: 'text/plain' });
  ```

  If you set custom content type, `value` must be either a string or [`Buffer`](https://nodejs.org/api/buffer.html), otherwise an error will be thrown.

  If `value` is `null`, the record is deleted instead. Note that the `setValue()` function succeeds regardless whether the record existed or not.

  To retrieve a value from the key-value store, use the [KeyValueStore.getValue](https://crawlee.dev/js/api/core/class/KeyValueStore.md#getValue) function.

  **IMPORTANT:** Always make sure to use the `await` keyword when calling `setValue()`, otherwise the crawler process might finish before the value is stored!

  ***

  #### Parameters

  * ##### key: string

    Unique key of the record. It can be at most 256 characters long and only consist of the following characters: `a`-`z`, `A`-`Z`, `0`-`9` and `!-_.'()`

  * ##### value: null | T

    Record data, which can be one of the following values:

    * If `null`, the record in the key-value store is deleted.
    * If no `options.contentType` is specified, `value` can be any JavaScript object and it will be stringified to JSON.
    * If `options.contentType` is set, `value` is taken as is and it must be a `String` or [`Buffer`](https://nodejs.org/api/buffer.html). For any other value an error will be thrown.

  * ##### optionaloptions: [RecordOptions](https://crawlee.dev/js/api/core/interface/RecordOptions.md) = <!-- -->{}

    Record options.

  #### Returns Promise\<void>

### [**](#values)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/key_value_store.ts#L522)values

* ****values**\<T>(options): AsyncIterable\<T, any, any> & Promise\<T\[]>

- Iterates over key-value store values using an async generator, allowing the use of `for await...of` syntax.

  **Example usage:**

  ```
  const keyValueStore = await KeyValueStore.open();
  for await (const value of keyValueStore.values()) {
    console.log(value);
  }
  ```

  ***

  #### Parameters

  * ##### options: [KeyValueStoreIteratorOptions](https://crawlee.dev/js/api/core/interface/KeyValueStoreIteratorOptions.md) = <!-- -->{}

    Options for the iteration.

  #### Returns AsyncIterable\<T, any, any> & Promise\<T\[]>

### [**](#getAutoSavedValue)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/key_value_store.ts#L720)staticgetAutoSavedValue

* ****getAutoSavedValue**\<T>(key, defaultValue): Promise\<T>

- #### Parameters

  * ##### key: string
  * ##### defaultValue: T = <!-- -->...

  #### Returns Promise\<T>

### [**](#open)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/key_value_store.ts#L596)staticopen

* ****open**(storeIdOrName, options): Promise<[KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md)>

- Opens a key-value store and returns a promise resolving to an instance of the [KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md) class.

  Key-value stores are used to store records or files, along with their MIME content type. The records are stored and retrieved using a unique key. The actual data is stored either on a local filesystem or in the Apify cloud.

  For more details and code examples, see the [KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md) class.

  ***

  #### Parameters

  * ##### optionalstoreIdOrName: null | string

    ID or name of the key-value store to be opened. If `null` or `undefined`, the function returns the default key-value store associated with the crawler run.

  * ##### optionaloptions: [StorageManagerOptions](https://crawlee.dev/js/api/core/interface/StorageManagerOptions.md) = <!-- -->{}

    Storage manager options.

  #### Returns Promise<[KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md)>

### [**](#recordExists)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/key_value_store.ts#L715)staticrecordExists

* ****recordExists**(key): Promise\<boolean>

- Tests whether a record with the given key exists in the default [KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md) associated with the current crawler run.

  ***

  #### Parameters

  * ##### key: string

    The queried record key.

  #### Returns Promise\<boolean>

  `true` if the record exists, `false` if it does not.
