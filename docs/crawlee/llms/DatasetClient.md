# Source: https://crawlee.dev/js/api/types/interface/DatasetClient.md

# DatasetClient<!-- --> \<Data>

## Index[**](#Index)

### Methods

* [**delete](#delete)
* [**downloadItems](#downloadItems)
* [**get](#get)
* [**listEntries](#listEntries)
* [**listItems](#listItems)
* [**pushItems](#pushItems)
* [**update](#update)

## Methods<!-- -->[**](#Methods)

### [**](#delete)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L87)delete

* ****delete**(): Promise\<void>

- #### Returns Promise\<void>

### [**](#downloadItems)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L88)downloadItems

* ****downloadItems**(...args): Promise\<Buffer\<ArrayBufferLike>>

- #### Parameters

  * ##### rest...args: unknown\[]

  #### Returns Promise\<Buffer\<ArrayBufferLike>>

### [**](#get)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L85)get

* ****get**(): Promise\<undefined | [DatasetInfo](https://crawlee.dev/js/api/types/interface/DatasetInfo.md)>

- #### Returns Promise\<undefined | [DatasetInfo](https://crawlee.dev/js/api/types/interface/DatasetInfo.md)>

### [**](#listEntries)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L90)optionallistEntries

* ****listEntries**(options): AsyncIterable<\[number, Data], any, any> & Promise<[PaginatedList](https://crawlee.dev/js/api/types/interface/PaginatedList.md)<\[number, Data]>>

- #### Parameters

  * ##### optionaloptions: [DatasetClientListOptions](https://crawlee.dev/js/api/types/interface/DatasetClientListOptions.md)

  #### Returns AsyncIterable<\[number, Data], any, any> & Promise<[PaginatedList](https://crawlee.dev/js/api/types/interface/PaginatedList.md)<\[number, Data]>>

### [**](#listItems)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L89)listItems

* ****listItems**(options): AsyncIterable\<Data, any, any> & Promise<[PaginatedList](https://crawlee.dev/js/api/types/interface/PaginatedList.md)\<Data>>

- #### Parameters

  * ##### optionaloptions: [DatasetClientListOptions](https://crawlee.dev/js/api/types/interface/DatasetClientListOptions.md)

  #### Returns AsyncIterable\<Data, any, any> & Promise<[PaginatedList](https://crawlee.dev/js/api/types/interface/PaginatedList.md)\<Data>>

### [**](#pushItems)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L93)pushItems

* ****pushItems**(items): Promise\<void>

- #### Parameters

  * ##### items: string | string\[] | Data | Data\[]

  #### Returns Promise\<void>

### [**](#update)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L86)update

* ****update**(newFields): Promise\<Partial<[DatasetInfo](https://crawlee.dev/js/api/types/interface/DatasetInfo.md)>>

- #### Parameters

  * ##### newFields: [DatasetClientUpdateOptions](https://crawlee.dev/js/api/types/interface/DatasetClientUpdateOptions.md)

  #### Returns Promise\<Partial<[DatasetInfo](https://crawlee.dev/js/api/types/interface/DatasetInfo.md)>>
