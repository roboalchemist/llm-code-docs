# Source: https://mikro-orm.io/api/core/class/MetadataDiscovery.md

# MetadataDiscovery<!-- -->

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**discover](#discover)
* [**discoverReferences](#discoverReferences)
* [**discoverSync](#discoverSync)
* [**processDiscoveredEntities](#processDiscoveredEntities)
* [**reset](#reset)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataDiscovery.ts#L53)constructor

* ****new MetadataDiscovery**(metadata, platform, config): [MetadataDiscovery](https://mikro-orm.io/api/core/class/MetadataDiscovery.md)

- #### Parameters

  * ##### metadata: [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)
  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)
  * ##### config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  #### Returns [MetadataDiscovery](https://mikro-orm.io/api/core/class/MetadataDiscovery.md)

## Methods<!-- -->[**](#Methods)

### [**](#discover)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataDiscovery.ts#L63)discover

* ****discover**(preferTsNode): Promise<[MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)>

- #### Parameters

  * ##### preferTsNode: boolean = <!-- -->true

  #### Returns Promise<[MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)>

### [**](#discoverReferences)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataDiscovery.ts#L327)discoverReferences

* ****discoverReferences**\<T>(refs): [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>\[]

- #### Parameters

  * ##### refs: ([Constructor](https://mikro-orm.io/api/core.md#Constructor)\<T> | [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<T, never>)\[]

  #### Returns [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>\[]

### [**](#discoverSync)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataDiscovery.ts#L83)discoverSync

* ****discoverSync**(preferTsNode): [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

- #### Parameters

  * ##### preferTsNode: boolean = <!-- -->true

  #### Returns [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

### [**](#processDiscoveredEntities)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataDiscovery.ts#L150)processDiscoveredEntities

* ****processDiscoveredEntities**(discovered): [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>\[]

- #### Parameters

  * ##### discovered: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>\[]

  #### Returns [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>\[]

### [**](#reset)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataDiscovery.ts#L367)reset

* ****reset**(className): void

- #### Parameters

  * ##### className: string

  #### Returns void
