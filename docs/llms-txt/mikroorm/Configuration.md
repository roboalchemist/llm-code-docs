# Source: https://mikro-orm.io/api/core/class/Configuration.md

# Configuration<!-- --> \<D, EM>

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**get](#get)
* [**getAll](#getall)
* [**getCachedService](#getcachedservice)
* [**getComparator](#getcomparator)
* [**getDataloaderType](#getdataloadertype)
* [**getDriver](#getdriver)
* [**getExtension](#getextension)
* [**getHydrator](#gethydrator)
* [**getLogger](#getlogger)
* [**getMetadataCacheAdapter](#getmetadatacacheadapter)
* [**getMetadataProvider](#getmetadataprovider)
* [**getNamingStrategy](#getnamingstrategy)
* [**getPlatform](#getplatform)
* [**getRepositoryClass](#getrepositoryclass)
* [**getResultCacheAdapter](#getresultcacheadapter)
* [**getSchema](#getschema)
* [**getSlowQueryLogger](#getslowquerylogger)
* [**registerExtension](#registerextension)
* [**reset](#reset)
* [**resetServiceCache](#resetservicecache)
* [**set](#set)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L180)constructor

* ****new Configuration**\<D, EM>(options, validate): [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)\<D, EM>

* #### Parameters

  * ##### options: Partial<[Options](https://mikro-orm.io/api/core/interface/Options.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>, (string | [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<any, never, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>> | [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<Partial\<any>>)\[]>>

  * ##### validate: boolean = <!-- -->true

  #### Returns [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)\<D, EM>

## Methods<!-- -->[**](#methods)

### [**](#get)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L224)get

* ****get**\<T, U>(key, defaultValue): U

* Gets specific configuration option. Falls back to specified `defaultValue` if provided.

  ***

  #### Parameters

  * ##### key: T

  * ##### optionaldefaultValue: U

  #### Returns U

### [**](#getall)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L232)getAll

* ****getAll**(): [Options](https://mikro-orm.io/api/core/interface/Options.md)\<D, EM, (string | [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<any, never, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>> | [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<Partial\<any>>)\[]>

* #### Returns [Options](https://mikro-orm.io/api/core/interface/Options.md)\<D, EM, (string | [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<any, never, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>> | [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<Partial\<any>>)\[]>

### [**](#getcachedservice)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L385)getCachedService

* ****getCachedService**\<T>(cls, ...args): InstanceType\<T>

* Creates instance of given service and caches it.

  ***

  #### Parameters

  * ##### cls: T

  * ##### rest...args: ConstructorParameters\<T>

  #### Returns InstanceType\<T>

### [**](#getcomparator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L334)getComparator

* ****getComparator**(metadata): [EntityComparator](https://mikro-orm.io/api/core/class/EntityComparator.md)

* Gets instance of Comparator. (cached)

  ***

  #### Parameters

  * ##### metadata: [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

  #### Returns [EntityComparator](https://mikro-orm.io/api/core/class/EntityComparator.md)

### [**](#getdataloadertype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L274)getDataloaderType

* ****getDataloaderType**(): [DataloaderType](https://mikro-orm.io/api/core/enum/DataloaderType.md)

* #### Returns [DataloaderType](https://mikro-orm.io/api/core/enum/DataloaderType.md)

### [**](#getdriver)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L293)getDriver

* ****getDriver**(): D

* Gets current database driver instance.

  ***

  #### Returns D

### [**](#getextension)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L301)getExtension

* ****getExtension**\<T>(name): undefined | T

* #### Parameters

  * ##### name: string

  #### Returns undefined | T

### [**](#gethydrator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L327)getHydrator

* ****getHydrator**(metadata): IHydrator

* Gets instance of Hydrator. (cached)

  ***

  #### Parameters

  * ##### metadata: [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

  #### Returns IHydrator

### [**](#getlogger)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L254)getLogger

* ****getLogger**(): [Logger](https://mikro-orm.io/api/core/interface/Logger.md)

* Gets Logger instance.

  ***

  #### Returns [Logger](https://mikro-orm.io/api/core/interface/Logger.md)

### [**](#getmetadatacacheadapter)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L348)getMetadataCacheAdapter

* ****getMetadataCacheAdapter**(): [SyncCacheAdapter](https://mikro-orm.io/api/core/interface/SyncCacheAdapter.md)

* Gets instance of metadata CacheAdapter. (cached)

  ***

  #### Returns [SyncCacheAdapter](https://mikro-orm.io/api/core/interface/SyncCacheAdapter.md)

### [**](#getmetadataprovider)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L341)getMetadataProvider

* ****getMetadataProvider**(): [MetadataProvider](https://mikro-orm.io/api/core/class/MetadataProvider.md)

* Gets instance of MetadataProvider. (cached)

  ***

  #### Returns [MetadataProvider](https://mikro-orm.io/api/core/class/MetadataProvider.md)

### [**](#getnamingstrategy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L320)getNamingStrategy

* ****getNamingStrategy**(): [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

* Gets instance of NamingStrategy. (cached)

  ***

  #### Returns [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

### [**](#getplatform)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L217)getPlatform

* ****getPlatform**(): ReturnType\<D\[getPlatform]>

* #### Returns ReturnType\<D\[getPlatform]>

### [**](#getrepositoryclass)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L370)getRepositoryClass

* ****getRepositoryClass**(repository): undefined | [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)<[EntityRepository](https://mikro-orm.io/api/core/class/EntityRepository.md)\<any>>

* Gets EntityRepository class to be instantiated.

  ***

  #### Parameters

  * ##### repository: () => [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)<[EntityRepository](https://mikro-orm.io/api/core/class/EntityRepository.md)\<Partial\<any>>>

  #### Returns undefined | [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)<[EntityRepository](https://mikro-orm.io/api/core/class/EntityRepository.md)\<any>>

### [**](#getresultcacheadapter)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L360)getResultCacheAdapter

* ****getResultCacheAdapter**(): [CacheAdapter](https://mikro-orm.io/api/core/interface/CacheAdapter.md)

* Gets instance of CacheAdapter for result cache. (cached)

  ***

  #### Returns [CacheAdapter](https://mikro-orm.io/api/core/interface/CacheAdapter.md)

### [**](#getschema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L282)getSchema

* ****getSchema**(skipDefaultSchema): undefined | string

* #### Parameters

  * ##### skipDefaultSchema: boolean = <!-- -->false

  #### Returns undefined | string

### [**](#getslowquerylogger)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L262)getSlowQueryLogger

* ****getSlowQueryLogger**(): [Logger](https://mikro-orm.io/api/core/interface/Logger.md)

* Gets the logger instance for slow queries. Falls back to the main logger if no custom slow query logger factory is configured.

  ***

  #### Returns [Logger](https://mikro-orm.io/api/core/interface/Logger.md)

### [**](#registerextension)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L297)registerExtension

* ****registerExtension**(name, cb): void

* #### Parameters

  * ##### name: string

  * ##### cb: () => unknown

  #### Returns void

### [**](#reset)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L247)reset

* ****reset**\<T>(key): void

* Resets the configuration to its default value

  ***

  #### Parameters

  * ##### key: T

  #### Returns void

### [**](#resetservicecache)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L396)resetServiceCache

* ****resetServiceCache**(): void

* #### Returns void

### [**](#set)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L239)set

* ****set**\<T, U>(key, value): void

* Overrides specified configuration value.

  ***

  #### Parameters

  * ##### key: T

  * ##### value: U

  #### Returns void
