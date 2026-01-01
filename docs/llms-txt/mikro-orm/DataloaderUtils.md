# Source: https://mikro-orm.io/api/core/class/DataloaderUtils.md

# DataloaderUtils<!-- -->

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**entitiesAndOptsMapToQueries](#entitiesAndOptsMapToQueries)
* [**getColBatchLoadFn](#getColBatchLoadFn)
* [**getColFilter](#getColFilter)
* [**getDataloaderType](#getDataloaderType)
* [**getManyToManyColBatchLoadFn](#getManyToManyColBatchLoadFn)
* [**getRefBatchLoadFn](#getRefBatchLoadFn)
* [**groupInversedOrMappedKeysByEntityAndOpts](#groupInversedOrMappedKeysByEntityAndOpts)
* [**groupPrimaryKeysByEntityAndOpts](#groupPrimaryKeysByEntityAndOpts)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)constructor

* ****new DataloaderUtils**(): [DataloaderUtils](https://mikro-orm.io/api/core/class/DataloaderUtils.md)

- #### Returns [DataloaderUtils](https://mikro-orm.io/api/core/class/DataloaderUtils.md)

## Methods<!-- -->[**](#Methods)

### [**](#entitiesAndOptsMapToQueries)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/DataloaderUtils.ts#L112)staticentitiesAndOptsMapToQueries

* ****entitiesAndOptsMapToQueries**(entitiesAndOptsMap, em): Promise<\[string, any\[]]>\[]

- Turn the entity+options map into actual queries. The keys are the entity names + a stringified version of the options and the values are filter Maps which will be used as the values of an $or operator so we end up with a query per entity+opts. We must populate the inverse side of the relationship in order to be able to later retrieve the PK(s) from its item(s). Together with the query the promises will also return the key which can be used to narrow down the results pertaining to a certain set of options.

  ***

  #### Parameters

  * ##### entitiesAndOptsMap: Map\<string, Map\<string, Set\<any>>>
  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns Promise<\[string, any\[]]>\[]

### [**](#getColBatchLoadFn)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/DataloaderUtils.ts#L183)staticgetColBatchLoadFn

* ****getColBatchLoadFn**(em): BatchLoadFn<\[[Collection](https://mikro-orm.io/api/core/class/Collection.md)\<any, object>, Omit<[InitCollectionOptions](https://mikro-orm.io/api/core/interface/InitCollectionOptions.md)\<any, any, \*, never>, dataloader>?], any>

- Returns the 1:M collection dataloader batchLoadFn, which aggregates collections by entity, makes one query per entity and maps each input collection to the corresponding result.

  ***

  #### Parameters

  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns BatchLoadFn<\[[Collection](https://mikro-orm.io/api/core/class/Collection.md)\<any, object>, Omit<[InitCollectionOptions](https://mikro-orm.io/api/core/interface/InitCollectionOptions.md)\<any, any, \*, never>, dataloader>?], any>

### [**](#getColFilter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/DataloaderUtils.ts#L157)staticgetColFilter

* ****getColFilter**\<T, S>(collection): (result) => result is S

- Creates a filter which returns the results pertaining to a certain collection. First checks if the Entity type matches, then retrieves the inverse side of the relationship where the filtering will be done in order to match the target collection.

  ***

  #### Parameters

  * ##### collection: [Collection](https://mikro-orm.io/api/core/class/Collection.md)\<any, object>

  #### Returns (result) => result is S

  * * **(result): result is S

    - #### Parameters

      * ##### result: T

      #### Returns result is S

### [**](#getDataloaderType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/DataloaderUtils.ts#L248)staticgetDataloaderType

* ****getDataloaderType**(dataloaderCfg): [DataloaderType](https://mikro-orm.io/api/core/enum/DataloaderType.md)

- #### Parameters

  * ##### dataloaderCfg: boolean | [DataloaderType](https://mikro-orm.io/api/core/enum/DataloaderType.md)

  #### Returns [DataloaderType](https://mikro-orm.io/api/core/enum/DataloaderType.md)

### [**](#getManyToManyColBatchLoadFn)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/DataloaderUtils.ts#L207)staticgetManyToManyColBatchLoadFn

* ****getManyToManyColBatchLoadFn**(em): BatchLoadFn<\[[Collection](https://mikro-orm.io/api/core/class/Collection.md)\<any, object>, Omit<[InitCollectionOptions](https://mikro-orm.io/api/core/interface/InitCollectionOptions.md)\<any, any, \*, never>, dataloader>?], any>

- Returns the M:N collection dataloader batchLoadFn, which aggregates collections by entity, makes one query per entity and maps each input collection to the corresponding result.

  ***

  #### Parameters

  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns BatchLoadFn<\[[Collection](https://mikro-orm.io/api/core/class/Collection.md)\<any, object>, Omit<[InitCollectionOptions](https://mikro-orm.io/api/core/interface/InitCollectionOptions.md)\<any, any, \*, never>, dataloader>?], any>

### [**](#getRefBatchLoadFn)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/DataloaderUtils.ts#L49)staticgetRefBatchLoadFn

* ****getRefBatchLoadFn**(em): BatchLoadFn<\[[Reference](https://mikro-orm.io/api/core/class/Reference.md)\<any>, Omit<[LoadReferenceOptions](https://mikro-orm.io/api/core/interface/LoadReferenceOptions.md)\<any, any, \*, never>, dataloader>?], any>

- Returns the reference dataloader batchLoadFn, which aggregates references by entity, makes one query per entity and maps each input reference to the corresponding result.

  ***

  #### Parameters

  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns BatchLoadFn<\[[Reference](https://mikro-orm.io/api/core/class/Reference.md)\<any>, Omit<[LoadReferenceOptions](https://mikro-orm.io/api/core/interface/LoadReferenceOptions.md)\<any, any, \*, never>, dataloader>?], any>

### [**](#groupInversedOrMappedKeysByEntityAndOpts)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/DataloaderUtils.ts#L74)staticgroupInversedOrMappedKeysByEntityAndOpts

* ****groupInversedOrMappedKeysByEntityAndOpts**(collsWithOpts): Map\<string, Map\<string, Set\<any>>>

- Groups collections by entity and returns a Map whose keys are the entity names and whose values are filter Maps which we can use to narrow down the find query to return just the items of the collections that have been dataloaded. The entries of the filter Map will be used as the values of an $or operator so we end up with a query per entity.

  ***

  #### Parameters

  * ##### collsWithOpts: readonly<!-- --> \[[Collection](https://mikro-orm.io/api/core/class/Collection.md)\<any, object>, Omit<[InitCollectionOptions](https://mikro-orm.io/api/core/interface/InitCollectionOptions.md)\<any, any, \*, never>, dataloader>?]\[]

  #### Returns Map\<string, Map\<string, Set\<any>>>

### [**](#groupPrimaryKeysByEntityAndOpts)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/DataloaderUtils.ts#L16)staticgroupPrimaryKeysByEntityAndOpts

* ****groupPrimaryKeysByEntityAndOpts**(refsWithOpts): Map\<string, Set\<any>>

- Groups identified references by entity and returns a Map with the class name as the index and the corresponding primary keys as the value.

  ***

  #### Parameters

  * ##### refsWithOpts: readonly<!-- --> \[[Reference](https://mikro-orm.io/api/core/class/Reference.md)\<any>, Omit<[LoadReferenceOptions](https://mikro-orm.io/api/core/interface/LoadReferenceOptions.md)\<any, any, \*, never>, dataloader>?]\[]

  #### Returns Map\<string, Set\<any>>
