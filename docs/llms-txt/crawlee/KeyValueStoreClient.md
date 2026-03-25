# Source: https://crawlee.dev/js/api/types/interface/KeyValueStoreClient.md

# KeyValueStoreClient<!-- -->

Key-value Store client.

## Index[**](#Index)

### Methods

* [**delete](#delete)
* [**deleteRecord](#deleteRecord)
* [**entries](#entries)
* [**get](#get)
* [**getRecord](#getRecord)
* [**keys](#keys)
* [**listKeys](#listKeys)
* [**recordExists](#recordExists)
* [**setRecord](#setRecord)
* [**update](#update)
* [**values](#values)

## Methods<!-- -->[**](#Methods)

### [**](#delete)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L171)delete

* ****delete**(): Promise\<void>

- #### Returns Promise\<void>

### [**](#deleteRecord)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L181)deleteRecord

* ****deleteRecord**(key): Promise\<void>

- #### Parameters

  * ##### key: string

  #### Returns Promise\<void>

### [**](#entries)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L177)optionalentries

* ****entries**(options): AsyncIterable<\[string, unknown], any, any> & Promise<\[string, unknown]\[]>

- #### Parameters

  * ##### optionaloptions: [KeyValueStoreClientListOptions](https://crawlee.dev/js/api/types/interface/KeyValueStoreClientListOptions.md)

  #### Returns AsyncIterable<\[string, unknown], any, any> & Promise<\[string, unknown]\[]>

### [**](#get)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L169)get

* ****get**(): Promise\<undefined | [KeyValueStoreInfo](https://crawlee.dev/js/api/types/interface/KeyValueStoreInfo.md)>

- #### Returns Promise\<undefined | [KeyValueStoreInfo](https://crawlee.dev/js/api/types/interface/KeyValueStoreInfo.md)>

### [**](#getRecord)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L179)getRecord

* ****getRecord**(key, options): Promise\<undefined | [KeyValueStoreRecord](https://crawlee.dev/js/api/types/interface/KeyValueStoreRecord.md)>

- #### Parameters

  * ##### key: string
  * ##### optionaloptions: [KeyValueStoreClientGetRecordOptions](https://crawlee.dev/js/api/types/interface/KeyValueStoreClientGetRecordOptions.md)

  #### Returns Promise\<undefined | [KeyValueStoreRecord](https://crawlee.dev/js/api/types/interface/KeyValueStoreRecord.md)>

### [**](#keys)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L175)optionalkeys

* ****keys**(options): AsyncIterable\<string, any, any> & Promise<[KeyValueStoreClientListData](https://crawlee.dev/js/api/types/interface/KeyValueStoreClientListData.md)>

- #### Parameters

  * ##### optionaloptions: [KeyValueStoreClientListOptions](https://crawlee.dev/js/api/types/interface/KeyValueStoreClientListOptions.md)

  #### Returns AsyncIterable\<string, any, any> & Promise<[KeyValueStoreClientListData](https://crawlee.dev/js/api/types/interface/KeyValueStoreClientListData.md)>

### [**](#listKeys)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L172)listKeys

* ****listKeys**(options): Partial\<AsyncIterable<[KeyValueStoreItemData](https://crawlee.dev/js/api/types/interface/KeyValueStoreItemData.md), any, any>> & Promise<[KeyValueStoreClientListData](https://crawlee.dev/js/api/types/interface/KeyValueStoreClientListData.md)>

- #### Parameters

  * ##### optionaloptions: [KeyValueStoreClientListOptions](https://crawlee.dev/js/api/types/interface/KeyValueStoreClientListOptions.md)

  #### Returns Partial\<AsyncIterable<[KeyValueStoreItemData](https://crawlee.dev/js/api/types/interface/KeyValueStoreItemData.md), any, any>> & Promise<[KeyValueStoreClientListData](https://crawlee.dev/js/api/types/interface/KeyValueStoreClientListData.md)>

### [**](#recordExists)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L178)recordExists

* ****recordExists**(key): Promise\<boolean>

- #### Parameters

  * ##### key: string

  #### Returns Promise\<boolean>

### [**](#setRecord)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L180)setRecord

* ****setRecord**(record, options): Promise\<void>

- #### Parameters

  * ##### record: [KeyValueStoreRecord](https://crawlee.dev/js/api/types/interface/KeyValueStoreRecord.md)
  * ##### optionaloptions: [KeyValueStoreRecordOptions](https://crawlee.dev/js/api/types/interface/KeyValueStoreRecordOptions.md)

  #### Returns Promise\<void>

### [**](#update)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L170)update

* ****update**(newFields): Promise\<Partial<[KeyValueStoreInfo](https://crawlee.dev/js/api/types/interface/KeyValueStoreInfo.md)>>

- #### Parameters

  * ##### newFields: [KeyValueStoreClientUpdateOptions](https://crawlee.dev/js/api/types/interface/KeyValueStoreClientUpdateOptions.md)

  #### Returns Promise\<Partial<[KeyValueStoreInfo](https://crawlee.dev/js/api/types/interface/KeyValueStoreInfo.md)>>

### [**](#values)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L176)optionalvalues

* ****values**(options): AsyncIterable\<unknown, any, any> & Promise\<unknown\[]>

- #### Parameters

  * ##### optionaloptions: [KeyValueStoreClientListOptions](https://crawlee.dev/js/api/types/interface/KeyValueStoreClientListOptions.md)

  #### Returns AsyncIterable\<unknown, any, any> & Promise\<unknown\[]>
