# Source: https://crawlee.dev/js/api/types/interface/DatasetCollectionClient.md

# DatasetCollectionClient<!-- -->

Dataset collection client.

## Index[**](#Index)

### Methods

* [**getOrCreate](#getOrCreate)
* [**list](#list)

## Methods<!-- -->[**](#Methods)

### [**](#getOrCreate)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L54)getOrCreate

* ****getOrCreate**(name): Promise<[DatasetCollectionData](https://crawlee.dev/js/api/types/interface/DatasetCollectionData.md)>

- #### Parameters

  * ##### optionalname: string

  #### Returns Promise<[DatasetCollectionData](https://crawlee.dev/js/api/types/interface/DatasetCollectionData.md)>

### [**](#list)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L53)list

* ****list**(): Promise<[PaginatedList](https://crawlee.dev/js/api/types/interface/PaginatedList.md)<[Dataset](https://crawlee.dev/js/api/types/interface/Dataset.md)>>

- #### Returns Promise<[PaginatedList](https://crawlee.dev/js/api/types/interface/PaginatedList.md)<[Dataset](https://crawlee.dev/js/api/types/interface/Dataset.md)>>
