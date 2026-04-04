# Source: https://mikro-orm.io/api/core/class/MetadataDiscovery.md

# MetadataDiscovery<!-- -->

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**discover](#discover)
* [**discoverReferences](#discoverreferences)
* [**discoverSync](#discoversync)
* [**processDiscoveredEntities](#processdiscoveredentities)
* [**reset](#reset)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataDiscovery.ts#L41)constructor

* ****new MetadataDiscovery**(metadata, platform, config): [MetadataDiscovery](https://mikro-orm.io/api/core/class/MetadataDiscovery.md)

* #### Parameters

  * ##### metadata: [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  * ##### config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  #### Returns [MetadataDiscovery](https://mikro-orm.io/api/core/class/MetadataDiscovery.md)

## Methods<!-- -->[**](#methods)

### [**](#discover)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataDiscovery.ts#L51)discover

* ****discover**(preferTs): Promise<[MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)>

* #### Parameters

  * ##### preferTs: boolean = <!-- -->true

  #### Returns Promise<[MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)>

### [**](#discoverreferences)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataDiscovery.ts#L322)discoverReferences

* ****discoverReferences**\<T>(refs, validate): [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>\[]

* #### Parameters

  * ##### refs: Iterable<[EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<T> | [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<T, never, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>, any, any>

  * ##### validate: boolean = <!-- -->true

  #### Returns [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>\[]

### [**](#discoversync)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataDiscovery.ts#L81)discoverSync

* ****discoverSync**(): [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

* #### Returns [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

### [**](#processdiscoveredentities)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataDiscovery.ts#L172)processDiscoveredEntities

* ****processDiscoveredEntities**(discovered): [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>\[]

* #### Parameters

  * ##### discovered: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>\[]

  #### Returns [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>\[]

### [**](#reset)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataDiscovery.ts#L379)reset

* ****reset**\<T>(entityName): void

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  #### Returns void
