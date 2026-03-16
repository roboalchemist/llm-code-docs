# Source: https://crawlee.dev/js/api/types/interface/Dataset.md

# Source: https://crawlee.dev/js/api/core/class/Dataset.md

# Dataset<!-- --> \<Data>

The `Dataset` class represents a store for structured data where each object stored has the same attributes, such as online store products or real estate offers. You can imagine it as a table, where each object is a row and its attributes are columns. Dataset is an append-only storage - you can only add new records to it but you cannot modify or remove existing records. Typically it is used to store crawling results.

Do not instantiate this class directly, use the [Dataset.open](https://crawlee.dev/js/api/core/class/Dataset.md#open) function instead.

`Dataset` stores its data either on local disk or in the Apify cloud, depending on whether the `APIFY_LOCAL_STORAGE_DIR` or `APIFY_TOKEN` environment variables are set.

If the `APIFY_LOCAL_STORAGE_DIR` environment variable is set, the data is stored in the local directory in the following files:

```
{APIFY_LOCAL_STORAGE_DIR}/datasets/{DATASET_ID}/{INDEX}.json
```

Note that `{DATASET_ID}` is the name or ID of the dataset. The default dataset has ID: `default`, unless you override it by setting the `APIFY_DEFAULT_DATASET_ID` environment variable. Each dataset item is stored as a separate JSON file, where `{INDEX}` is a zero-based index of the item in the dataset.

If the `APIFY_TOKEN` environment variable is set but `APIFY_LOCAL_STORAGE_DIR` not, the data is stored in the [Apify Dataset](https://docs.apify.com/storage/dataset) cloud storage. Note that you can force usage of the cloud storage also by passing the `forceCloud` option to [Dataset.open](https://crawlee.dev/js/api/core/class/Dataset.md#open) function, even if the `APIFY_LOCAL_STORAGE_DIR` variable is set.

**Example usage:**

```
// Write a single row to the default dataset
await Dataset.pushData({ col1: 123, col2: 'val2' });

// Open a named dataset
const dataset = await Dataset.open('some-name');

// Write a single row
await dataset.pushData({ foo: 'bar' });

// Write multiple rows
await dataset.pushData([
  { foo: 'bar2', col2: 'val2' },
  { col3: 123 },
]);

// Export the entirety of the dataset to one file in the key-value store
await dataset.exportToCSV('MY-DATA');
```

## Index[**](#Index)

### Properties

* [**client](#client)
* [**config](#config)
* [**id](#id)
* [**log](#log)
* [**name](#name)
* [**storageObject](#storageObject)

### Methods

* [**\[asyncIterator\]](#\[asyncIterator])
* [**drop](#drop)
* [**entries](#entries)
* [**export](#export)
* [**exportTo](#exportTo)
* [**exportToCSV](#exportToCSV)
* [**exportToJSON](#exportToJSON)
* [**forEach](#forEach)
* [**getData](#getData)
* [**getInfo](#getInfo)
* [**map](#map)
* [**pushData](#pushData)
* [**reduce](#reduce)
* [**values](#values)
* [**exportToCSV](#exportToCSV)
* [**exportToJSON](#exportToJSON)
* [**getData](#getData)
* [**open](#open)

## Properties<!-- -->[**](#Properties)

### [**](#client)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L235)client

**client: [DatasetClient](https://crawlee.dev/js/api/types/interface/DatasetClient.md)\<Data>

### [**](#config)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L244)readonlyconfig

**config: [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md) =

<!-- -->

...

### [**](#id)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L233)id

**id: string

### [**](#log)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L237)log

**log: [Log](https://crawlee.dev/js/api/core/class/Log.md) =

<!-- -->

...

### [**](#name)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L234)optionalname

**name?

<!-- -->

: string

### [**](#storageObject)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L236)optionalreadonlystorageObject

**storageObject?

<!-- -->

: Record\<string, unknown>

## Methods<!-- -->[**](#Methods)

### [**](#\[asyncIterator])[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L677)\[asyncIterator]

* ****\[asyncIterator]**(): AsyncGenerator\<Data, void, undefined>

- Default async iterator for the dataset, iterating over items. Allows using the dataset directly in a `for await...of` loop.

  **Example usage:**

  ```
  const dataset = await Dataset.open('my-results');
  for await (const item of dataset) {
    console.log(item);
  }
  ```

  ***

  #### Returns AsyncGenerator\<Data, void, undefined>

### [**](#drop)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L685)drop

* ****drop**(): Promise\<void>

- Removes the dataset either from the Apify cloud storage or from the local directory, depending on the mode of operation.

  ***

  #### Returns Promise\<void>

### [**](#entries)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L653)entries

* ****entries**(options): AsyncIterable<\[number, Data], any, any> & Promise<[PaginatedList](https://crawlee.dev/js/api/types/interface/PaginatedList.md)<\[number, Data]>>

- Iterates over dataset entries (index-value pairs) using an async generator, allowing the use of `for await...of` syntax.

  **Example usage:**

  ```
  const dataset = await Dataset.open('my-results');
  for await (const [index, item] of dataset.entries()) {
    console.log(`Item at ${index}: ${JSON.stringify(item)}`);
  }
  ```

  ***

  #### Parameters

  * ##### options: [DatasetIteratorOptions](https://crawlee.dev/js/api/core/interface/DatasetIteratorOptions.md) = <!-- -->{}

    Options for the iteration.

  #### Returns AsyncIterable<\[number, Data], any, any> & Promise<[PaginatedList](https://crawlee.dev/js/api/types/interface/PaginatedList.md)<\[number, Data]>>

### [**](#export)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L323)export

* ****export**(options): Promise\<Data\[]>

- Returns all the data from the dataset. This will iterate through the whole dataset via the `listItems()` client method, which gives you only paginated results.

  ***

  #### Parameters

  * ##### options: [DatasetExportOptions](https://crawlee.dev/js/api/core/interface/DatasetExportOptions.md) = <!-- -->{}

  #### Returns Promise\<Data\[]>

### [**](#exportTo)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L355)exportTo

* ****exportTo**(key, options, contentType): Promise\<Data\[]>

- Save the entirety of the dataset's contents into one file within a key-value store.

  ***

  #### Parameters

  * ##### key: string

    The name of the value to save the data in.

  * ##### optionaloptions: [DatasetExportToOptions](https://crawlee.dev/js/api/core/interface/DatasetExportToOptions.md)

    An optional options object where you can provide the dataset and target KVS name.

  * ##### optionalcontentType: string

    Only JSON and CSV are supported currently, defaults to JSON.

  #### Returns Promise\<Data\[]>

### [**](#exportToCSV)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L406)exportToCSV

* ****exportToCSV**(key, options): Promise\<void>

- Save entire default dataset's contents into one CSV file within a key-value store.

  ***

  #### Parameters

  * ##### key: string

    The name of the value to save the data in.

  * ##### optionaloptions: Omit<[DatasetExportToOptions](https://crawlee.dev/js/api/core/interface/DatasetExportToOptions.md), fromDataset>

    An optional options object where you can provide the target KVS name.

  #### Returns Promise\<void>

### [**](#exportToJSON)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L396)exportToJSON

* ****exportToJSON**(key, options): Promise\<void>

- Save entire default dataset's contents into one JSON file within a key-value store.

  ***

  #### Parameters

  * ##### key: string

    The name of the value to save the data in.

  * ##### optionaloptions: Omit<[DatasetExportToOptions](https://crawlee.dev/js/api/core/interface/DatasetExportToOptions.md), fromDataset>

    An optional options object where you can provide the target KVS name.

  #### Returns Promise\<void>

### [**](#forEach)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L484)forEach

* ****forEach**(iteratee, options, index): Promise\<void>

- Iterates over dataset items, yielding each in turn to an `iteratee` function. Each invocation of `iteratee` is called with two arguments: `(item, index)`.

  If the `iteratee` function returns a Promise then it is awaited before the next call. If it throws an error, the iteration is aborted and the `forEach` function throws the error.

  **Example usage**

  ```
  const dataset = await Dataset.open('my-results');
  await dataset.forEach(async (item, index) => {
    console.log(`Item at ${index}: ${JSON.stringify(item)}`);
  });
  ```

  ***

  #### Parameters

  * ##### iteratee: [DatasetConsumer](https://crawlee.dev/js/api/core/interface/DatasetConsumer.md)\<Data>

    A function that is called for every item in the dataset.

  * ##### optionaloptions: [DatasetIteratorOptions](https://crawlee.dev/js/api/core/interface/DatasetIteratorOptions.md) = <!-- -->{}

    All `forEach()` parameters.

  * ##### optionalindex: number = <!-- -->0

    Specifies the initial index number passed to the `iteratee` function.

  #### Returns Promise\<void>

### [**](#getData)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L303)getData

* ****getData**(options): Promise<[DatasetContent](https://crawlee.dev/js/api/core/interface/DatasetContent.md)\<Data>>

- Returns [DatasetContent](https://crawlee.dev/js/api/core/interface/DatasetContent.md) object holding the items in the dataset based on the provided parameters.

  ***

  #### Parameters

  * ##### options: [DatasetDataOptions](https://crawlee.dev/js/api/core/interface/DatasetDataOptions.md) = <!-- -->{}

  #### Returns Promise<[DatasetContent](https://crawlee.dev/js/api/core/interface/DatasetContent.md)\<Data>>

### [**](#getInfo)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L458)getInfo

* ****getInfo**(): Promise\<undefined | [DatasetInfo](https://crawlee.dev/js/api/types/interface/DatasetInfo.md)>

- Returns an object containing general information about the dataset.

  The function returns the same object as the Apify API Client's [getDataset](https://docs.apify.com/api/apify-client-js/latest#ApifyClient-datasets-getDataset) function, which in turn calls the [Get dataset](https://apify.com/docs/api/v2#/reference/datasets/dataset/get-dataset) API endpoint.

  **Example:**

  ```
  {
    id: "WkzbQMuFYuamGv3YF",
    name: "my-dataset",
    userId: "wRsJZtadYvn4mBZmm",
    createdAt: new Date("2015-12-12T07:34:14.202Z"),
    modifiedAt: new Date("2015-12-13T08:36:13.202Z"),
    accessedAt: new Date("2015-12-14T08:36:13.202Z"),
    itemCount: 14,
  }
  ```

  ***

  #### Returns Promise\<undefined | [DatasetInfo](https://crawlee.dev/js/api/types/interface/DatasetInfo.md)>

### [**](#map)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L514)map

* ****map**\<R>(iteratee, options): Promise\<R\[]>

- Produces a new array of values by mapping each value in list through a transformation function `iteratee()`. Each invocation of `iteratee()` is called with two arguments: `(element, index)`.

  If `iteratee` returns a `Promise` then it's awaited before a next call.

  ***

  #### Parameters

  * ##### iteratee: [DatasetMapper](https://crawlee.dev/js/api/core/interface/DatasetMapper.md)\<Data, R>

  * ##### optionaloptions: [DatasetIteratorOptions](https://crawlee.dev/js/api/core/interface/DatasetIteratorOptions.md) = <!-- -->{}

    All `map()` parameters.

  #### Returns Promise\<R\[]>

### [**](#pushData)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L276)pushData

* ****pushData**(data): Promise\<void>

- Stores an object or an array of objects to the dataset. The function returns a promise that resolves when the operation finishes. It has no result, but throws on invalid args or other errors.

  **IMPORTANT**: Make sure to use the `await` keyword when calling `pushData()`, otherwise the crawler process might finish before the data is stored!

  The size of the data is limited by the receiving API and therefore `pushData()` will only allow objects whose JSON representation is smaller than 9MB. When an array is passed, none of the included objects may be larger than 9MB, but the array itself may be of any size.

  The function internally chunks the array into separate items and pushes them sequentially. The chunking process is stable (keeps order of data), but it does not provide a transaction safety mechanism. Therefore, in the event of an uploading error (after several automatic retries), the function's Promise will reject and the dataset will be left in a state where some of the items have already been saved to the dataset while other items from the source array were not. To overcome this limitation, the developer may, for example, read the last item saved in the dataset and re-attempt the save of the data from this item onwards to prevent duplicates.

  ***

  #### Parameters

  * ##### data: Data | Data\[]

    Object or array of objects containing data to be stored in the default dataset. The objects must be serializable to JSON and the JSON representation of each object must be smaller than 9MB.

  #### Returns Promise\<void>

### [**](#reduce)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L544)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L565)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L584)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L586)reduce

* ****reduce**(iteratee): Promise\<undefined | Data>
* ****reduce**(iteratee, memo, options): Promise\<undefined | Data>
* ****reduce**\<T>(iteratee, memo, options): Promise\<T>

- Reduces a list of values down to a single value.

  The first element of the dataset is the initial value, with each successive reductions should be returned by `iteratee()`. The `iteratee()` is passed three arguments: the `memo`, `value` and `index` of the current element being folded into the reduction.

  The `iteratee` is first invoked on the second element of the list (`index = 1`), with the first element given as the memo parameter. After that, the rest of the elements in the dataset is passed to `iteratee`, with the result of the previous invocation as the memo.

  If `iteratee()` returns a `Promise` it's awaited before a next call.

  If the dataset is empty, reduce will return undefined.

  ***

  #### Parameters

  * ##### iteratee: [DatasetReducer](https://crawlee.dev/js/api/core/interface/DatasetReducer.md)\<Data, Data>

  #### Returns Promise\<undefined | Data>

### [**](#values)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L623)values

* ****values**(options): AsyncIterable\<Data, any, any> & Promise<[PaginatedList](https://crawlee.dev/js/api/types/interface/PaginatedList.md)\<Data>>

- Iterates over dataset items using an async generator, allowing the use of `for await...of` syntax.

  **Example usage:**

  ```
  const dataset = await Dataset.open('my-results');
  for await (const item of dataset.values()) {
    console.log(item);
  }
  ```

  ***

  #### Parameters

  * ##### options: [DatasetIteratorOptions](https://crawlee.dev/js/api/core/interface/DatasetIteratorOptions.md) = <!-- -->{}

    Options for the iteration.

  #### Returns AsyncIterable\<Data, any, any> & Promise<[PaginatedList](https://crawlee.dev/js/api/types/interface/PaginatedList.md)\<Data>>

### [**](#exportToCSV)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L429)staticexportToCSV

* ****exportToCSV**(key, options): Promise\<void>

- Save entire default dataset's contents into one CSV file within a key-value store.

  ***

  #### Parameters

  * ##### key: string

    The name of the value to save the data in.

  * ##### optionaloptions: [DatasetExportToOptions](https://crawlee.dev/js/api/core/interface/DatasetExportToOptions.md)

    An optional options object where you can provide the dataset and target KVS name.

  #### Returns Promise\<void>

### [**](#exportToJSON)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L416)staticexportToJSON

* ****exportToJSON**(key, options): Promise\<void>

- Save entire default dataset's contents into one JSON file within a key-value store.

  ***

  #### Parameters

  * ##### key: string

    The name of the value to save the data in.

  * ##### optionaloptions: [DatasetExportToOptions](https://crawlee.dev/js/api/core/interface/DatasetExportToOptions.md)

    An optional options object where you can provide the dataset and target KVS name.

  #### Returns Promise\<void>

### [**](#getData)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L764)staticgetData

* ****getData**\<Data>(options): Promise<[DatasetContent](https://crawlee.dev/js/api/core/interface/DatasetContent.md)\<Data>>

- Returns [DatasetContent](https://crawlee.dev/js/api/core/interface/DatasetContent.md) object holding the items in the dataset based on the provided parameters.

  ***

  #### Parameters

  * ##### options: [DatasetDataOptions](https://crawlee.dev/js/api/core/interface/DatasetDataOptions.md) = <!-- -->{}

  #### Returns Promise<[DatasetContent](https://crawlee.dev/js/api/core/interface/DatasetContent.md)\<Data>>

### [**](#open)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L707)staticopen

* ****open**\<Data>(datasetIdOrName, options): Promise<[Dataset](https://crawlee.dev/js/api/core/class/Dataset.md)\<Data>>

- Opens a dataset and returns a promise resolving to an instance of the [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md) class.

  Datasets are used to store structured data where each object stored has the same attributes, such as online store products or real estate offers. The actual data is stored either on the local filesystem or in the cloud.

  For more details and code examples, see the [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md) class.

  ***

  #### Parameters

  * ##### optionaldatasetIdOrName: null | string

    ID or name of the dataset to be opened. If `null` or `undefined`, the function returns the default dataset associated with the crawler run.

  * ##### optionaloptions: [StorageManagerOptions](https://crawlee.dev/js/api/core/interface/StorageManagerOptions.md) = <!-- -->{}

    Storage manager options.

  #### Returns Promise<[Dataset](https://crawlee.dev/js/api/core/class/Dataset.md)\<Data>>
