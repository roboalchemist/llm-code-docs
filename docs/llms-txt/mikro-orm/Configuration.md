# Source: https://mikro-orm.io/api/core/class/Configuration.md

# Configuration<!-- --> \<D, EM>

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**DEFAULTS](#DEFAULTS)

### Methods

* [**get](#get)
* [**getAll](#getAll)
* [**getCachedService](#getCachedService)
* [**getClientUrl](#getClientUrl)
* [**getComparator](#getComparator)
* [**getDriver](#getDriver)
* [**getExtension](#getExtension)
* [**getHydrator](#getHydrator)
* [**getLogger](#getLogger)
* [**getMetadataCacheAdapter](#getMetadataCacheAdapter)
* [**getMetadataProvider](#getMetadataProvider)
* [**getNamingStrategy](#getNamingStrategy)
* [**getPlatform](#getPlatform)
* [**getRepositoryClass](#getRepositoryClass)
* [**getResultCacheAdapter](#getResultCacheAdapter)
* [**getSchema](#getSchema)
* [**registerExtension](#registerExtension)
* [**reset](#reset)
* [**resetServiceCache](#resetServiceCache)
* [**set](#set)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L183)constructor

* ****new Configuration**\<D, EM>(options, validate): [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)\<D, EM>

- #### Parameters

  * ##### options: [Options](https://mikro-orm.io/api/core.md#Options)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>
  * ##### validate: boolean = <!-- -->true

  #### Returns [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)\<D, EM>

## Properties<!-- -->[**](#Properties)

### [**](#DEFAULTS)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L48)staticreadonlyDEFAULTS

**DEFAULTS: { allowGlobalContext: false; assign: { ignoreUndefined: false; mergeEmbeddedProperties: true; mergeObjectProperties: false; updateByPrimaryKey: true; updateNestedEntities: true }; autoJoinOneToOneOwner: true; autoJoinRefsForFilters: true; baseDir: string; batchSize: number; colors: true; connect: true; context: (name) => undefined | [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>; contextName: string; dataloader: NONE; debug: false; discovery: { alwaysAnalyseProperties: true; checkDuplicateEntities: true; checkDuplicateFieldNames: true; checkDuplicateTableNames: true; checkNonPersistentCompositeProps: true; disableDynamicFileAccess: false; inferDefaultValues: true; requireEntitiesArray: false; warnWhenNoEntities: true }; driverOptions: {}; dynamicImportProvider: (id) => Promise\<any>; embeddables: { prefixMode: absolute }; ensureDatabase: true; ensureIndexes: false; entities: never\[]; entitiesTs: never\[]; entityGenerator: { bidirectionalRelations: false; entityDefinition: decorators; enumMode: ts-enum; fileName: (className) => string; forceUndefined: true; identifiedReferences: false; onlyPurePivotTables: false; outputPurePivotTables: false; readOnlyPivotTables: false; scalarPropertiesForRelations: never; scalarTypeInDecorator: false; undefinedDefaults: false; useCoreBaseEntity: false }; extensions: never\[]; filters: {}; filtersOnRelations: true; findExactlyOneOrFailHandler: (entityName, where) => [NotFoundError](https://mikro-orm.io/api/core/class/NotFoundError.md)\<Partial\<any>>; findOneOrFailHandler: (entityName, where) => [NotFoundError](https://mikro-orm.io/api/core/class/NotFoundError.md)\<Partial\<any>>; flushMode: AUTO; forceEntityConstructor: false; forceUndefined: false; hashAlgorithm: md5; highlighter: [NullHighlighter](https://mikro-orm.io/api/core/class/NullHighlighter.md); hydrator: typeof [ObjectHydrator](https://mikro-orm.io/api/core/class/ObjectHydrator.md); ignoreDeprecations: false; ignoreUndefinedInQuery: false; loadStrategy: JOINED; logger: (message, ...optionalParams) => void; metadataCache: { adapter: typeof [FileCacheAdapter](https://mikro-orm.io/api/core/class/FileCacheAdapter.md); options: { cacheDir: string }; pretty: false }; metadataProvider: typeof [ReflectMetadataProvider](https://mikro-orm.io/api/core/class/ReflectMetadataProvider.md); migrations: { allOrNothing: true; disableForeignKeys: false; dropTables: true; emit: ts; fileName: (timestamp, name) => string; glob: string; path: string; safe: false; silent: false; snapshot: true; tableName: string; transactional: true }; onQuery: (sql) => string; persistOnCreate: true; pool: {}; populateAfterFlush: true; populateWhere: ALL; preferReadReplicas: true; processOnCreateHooksEarly: false; propagationOnPrototype: true; resultCache: { adapter: typeof [MemoryCacheAdapter](https://mikro-orm.io/api/core/class/MemoryCacheAdapter.md); expiration: number; options: {} }; schemaGenerator: { createForeignKeyConstraints: true; disableForeignKeys: false; ignoreSchema: never\[]; skipColumns: {}; skipTables: never\[] }; seeder: { defaultSeeder: string; emit: ts; fileName: (className) => string; glob: string; path: string }; serialization: { includePrimaryKeys: true }; strict: false; subscribers: never\[]; upsertManaged: true; validate: false; validateRequired: true; verbose: false } =

<!-- -->

...

#### Type declaration

* ##### allowGlobalContext: false

* ##### assign: { ignoreUndefined: false; mergeEmbeddedProperties: true; mergeObjectProperties: false; updateByPrimaryKey: true; updateNestedEntities: true }

  * ##### ignoreUndefined: false
  * ##### mergeEmbeddedProperties: true
  * ##### mergeObjectProperties: false
  * ##### updateByPrimaryKey: true
  * ##### updateNestedEntities: true

* ##### autoJoinOneToOneOwner: true

* ##### autoJoinRefsForFilters: true

* ##### baseDir: string

* ##### batchSize: number

* ##### colors: true

* ##### connect: true

* ##### context: (name) => undefined | [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  * * **(name): undefined | [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

    - #### Parameters

      * ##### name: string

      #### Returns undefined | [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

* ##### contextName: string

* ##### dataloader: NONE

* ##### debug: false

* ##### discovery: { alwaysAnalyseProperties: true; checkDuplicateEntities: true; checkDuplicateFieldNames: true; checkDuplicateTableNames: true; checkNonPersistentCompositeProps: true; disableDynamicFileAccess: false; inferDefaultValues: true; requireEntitiesArray: false; warnWhenNoEntities: true }

  * ##### alwaysAnalyseProperties: true
  * ##### checkDuplicateEntities: true
  * ##### checkDuplicateFieldNames: true
  * ##### checkDuplicateTableNames: true
  * ##### checkNonPersistentCompositeProps: true
  * ##### disableDynamicFileAccess: false
  * ##### inferDefaultValues: true
  * ##### requireEntitiesArray: false
  * ##### warnWhenNoEntities: true

* ##### driverOptions: {}



* ##### dynamicImportProvider: (id) => Promise\<any>

  * * **(id): Promise\<any>

    - #### Parameters

      * ##### id: string

      #### Returns Promise\<any>

* ##### embeddables: { prefixMode: absolute }

  * ##### prefixMode: absolute

* ##### ensureDatabase: true

* ##### ensureIndexes: false

* ##### entities: never\[]

* ##### entitiesTs: never\[]

* ##### entityGenerator: { bidirectionalRelations: false; entityDefinition: decorators; enumMode: ts-enum; fileName: (className) => string; forceUndefined: true; identifiedReferences: false; onlyPurePivotTables: false; outputPurePivotTables: false; readOnlyPivotTables: false; scalarPropertiesForRelations: never; scalarTypeInDecorator: false; undefinedDefaults: false; useCoreBaseEntity: false }

  * ##### bidirectionalRelations: false

  * ##### entityDefinition: decorators

  * ##### enumMode: ts-enum

  * ##### fileName: (className) => string

    * * **(className): string

      - #### Parameters

        * ##### className: string

        #### Returns string

  * ##### forceUndefined: true

  * ##### identifiedReferences: false

  * ##### onlyPurePivotTables: false

  * ##### outputPurePivotTables: false

  * ##### readOnlyPivotTables: false

  * ##### scalarPropertiesForRelations: never

  * ##### scalarTypeInDecorator: false

  * ##### undefinedDefaults: false

  * ##### useCoreBaseEntity: false

* ##### extensions: never\[]

* ##### filters: {}



* ##### filtersOnRelations: true

* ##### findExactlyOneOrFailHandler: (entityName, where) => [NotFoundError](https://mikro-orm.io/api/core/class/NotFoundError.md)\<Partial\<any>>

  * * **(entityName, where): [NotFoundError](https://mikro-orm.io/api/core/class/NotFoundError.md)\<Partial\<any>>

    - #### Parameters

      * ##### entityName: string
      * ##### where: IPrimaryKeyValue | [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

      #### Returns [NotFoundError](https://mikro-orm.io/api/core/class/NotFoundError.md)\<Partial\<any>>

* ##### findOneOrFailHandler: (entityName, where) => [NotFoundError](https://mikro-orm.io/api/core/class/NotFoundError.md)\<Partial\<any>>

  * * **(entityName, where): [NotFoundError](https://mikro-orm.io/api/core/class/NotFoundError.md)\<Partial\<any>>

    - #### Parameters

      * ##### entityName: string
      * ##### where: IPrimaryKeyValue | [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

      #### Returns [NotFoundError](https://mikro-orm.io/api/core/class/NotFoundError.md)\<Partial\<any>>

* ##### flushMode: AUTO

* ##### forceEntityConstructor: false

* ##### forceUndefined: false

* ##### hashAlgorithm: md5

* ##### highlighter: [NullHighlighter](https://mikro-orm.io/api/core/class/NullHighlighter.md)

* ##### hydrator: typeof [ObjectHydrator](https://mikro-orm.io/api/core/class/ObjectHydrator.md)

* ##### ignoreDeprecations: false

* ##### ignoreUndefinedInQuery: false

* ##### loadStrategy: JOINED

* ##### logger: (message, ...optionalParams) => void

  * * **(message, ...optionalParams): void

    - Prints to `stdout` with newline. Multiple arguments can be passed, with the first used as the primary message and all additional used as substitution values similar to [`printf(3)`](http://man7.org/linux/man-pages/man3/printf.3.html) (the arguments are all passed to [`util.format()`](https://nodejs.org/docs/latest-v24.x/api/util.html#utilformatformat-args)).

      ```
      const count = 5;
      console.log('count: %d', count);
      // Prints: count: 5, to stdout
      console.log('count:', count);
      // Prints: count: 5, to stdout
      ```

      See [`util.format()`](https://nodejs.org/docs/latest-v24.x/api/util.html#utilformatformat-args) for more information.

      * **@since**

        v0.1.100

      ***

      #### Parameters

      * ##### optionalmessage: any
      * ##### rest...optionalParams: any\[]

      #### Returns void

* ##### metadataCache: { adapter: typeof [FileCacheAdapter](https://mikro-orm.io/api/core/class/FileCacheAdapter.md); options: { cacheDir: string }; pretty: false }

  * ##### adapter: typeof [FileCacheAdapter](https://mikro-orm.io/api/core/class/FileCacheAdapter.md)

  * ##### options: { cacheDir: string }

    * ##### cacheDir: string

  * ##### pretty: false

* ##### metadataProvider: typeof [ReflectMetadataProvider](https://mikro-orm.io/api/core/class/ReflectMetadataProvider.md)

* ##### migrations: { allOrNothing: true; disableForeignKeys: false; dropTables: true; emit: ts; fileName: (timestamp, name) => string; glob: string; path: string; safe: false; silent: false; snapshot: true; tableName: string; transactional: true }

  * ##### allOrNothing: true

  * ##### disableForeignKeys: false

  * ##### dropTables: true

  * ##### emit: ts

  * ##### fileName: (timestamp, name) => string

    * * **(timestamp, name): string

      - #### Parameters

        * ##### timestamp: string
        * ##### optionalname: string

        #### Returns string

  * ##### glob: string

  * ##### path: string

  * ##### safe: false

  * ##### silent: false

  * ##### snapshot: true

  * ##### tableName: string

  * ##### transactional: true

* ##### onQuery: (sql) => string

  * * **(sql): string

    - #### Parameters

      * ##### sql: string

      #### Returns string

* ##### persistOnCreate: true

* ##### pool: {}



* ##### populateAfterFlush: true

* ##### populateWhere: ALL

* ##### preferReadReplicas: true

* ##### processOnCreateHooksEarly: false

* ##### propagationOnPrototype: true

* ##### resultCache: { adapter: typeof [MemoryCacheAdapter](https://mikro-orm.io/api/core/class/MemoryCacheAdapter.md); expiration: number; options: {} }

  * ##### adapter: typeof [MemoryCacheAdapter](https://mikro-orm.io/api/core/class/MemoryCacheAdapter.md)

  * ##### expiration: number

  * ##### options: {}



* ##### schemaGenerator: { createForeignKeyConstraints: true; disableForeignKeys: false; ignoreSchema: never\[]; skipColumns: {}; skipTables: never\[] }

  * ##### createForeignKeyConstraints: true

  * ##### disableForeignKeys: false

  * ##### ignoreSchema: never\[]

  * ##### skipColumns: {}



  * ##### skipTables: never\[]

* ##### seeder: { defaultSeeder: string; emit: ts; fileName: (className) => string; glob: string; path: string }

  * ##### defaultSeeder: string

  * ##### emit: ts

  * ##### fileName: (className) => string

    * * **(className): string

      - #### Parameters

        * ##### className: string

        #### Returns string

  * ##### glob: string

  * ##### path: string

* ##### serialization: { includePrimaryKeys: true }

  * ##### includePrimaryKeys: true

* ##### strict: false

* ##### subscribers: never\[]

* ##### upsertManaged: true

* ##### validate: false

* ##### validateRequired: true

* ##### verbose: false

## Methods<!-- -->[**](#Methods)

### [**](#get)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L217)get

* ****get**\<T, U>(key, defaultValue): U

- Gets specific configuration option. Falls back to specified `defaultValue` if provided.

  ***

  #### Parameters

  * ##### key: T
  * ##### optionaldefaultValue: U

  #### Returns U

### [**](#getAll)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L225)getAll

* ****getAll**(): [MikroORMOptions](https://mikro-orm.io/api/core/interface/MikroORMOptions.md)\<D, EM>

- #### Returns [MikroORMOptions](https://mikro-orm.io/api/core/interface/MikroORMOptions.md)\<D, EM>

### [**](#getCachedService)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L361)getCachedService

* ****getCachedService**\<T>(cls, ...args): InstanceType\<T>

- Creates instance of given service and caches it.

  ***

  #### Parameters

  * ##### cls: T
  * ##### rest...args: ConstructorParameters\<T>

  #### Returns InstanceType\<T>

### [**](#getClientUrl)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L258)getClientUrl

* ****getClientUrl**(hidePassword): string

- Gets current client URL (connection string).

  ***

  #### Parameters

  * ##### hidePassword: boolean = <!-- -->false

  #### Returns string

### [**](#getComparator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L318)getComparator

* ****getComparator**(metadata): [EntityComparator](https://mikro-orm.io/api/core/class/EntityComparator.md)

- Gets instance of Comparator. (cached)

  ***

  #### Parameters

  * ##### metadata: [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

  #### Returns [EntityComparator](https://mikro-orm.io/api/core/class/EntityComparator.md)

### [**](#getDriver)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L277)getDriver

* ****getDriver**(): D

- Gets current database driver instance.

  ***

  #### Returns D

### [**](#getExtension)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L285)getExtension

* ****getExtension**\<T>(name): undefined | T

- #### Parameters

  * ##### name: string

  #### Returns undefined | T

### [**](#getHydrator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L311)getHydrator

* ****getHydrator**(metadata): IHydrator

- Gets instance of Hydrator. (cached)

  ***

  #### Parameters

  * ##### metadata: [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

  #### Returns IHydrator

### [**](#getLogger)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L247)getLogger

* ****getLogger**(): [Logger](https://mikro-orm.io/api/core/interface/Logger.md)

- Gets Logger instance.

  ***

  #### Returns [Logger](https://mikro-orm.io/api/core/interface/Logger.md)

### [**](#getMetadataCacheAdapter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L332)getMetadataCacheAdapter

* ****getMetadataCacheAdapter**(): [SyncCacheAdapter](https://mikro-orm.io/api/core/interface/SyncCacheAdapter.md)

- Gets instance of metadata CacheAdapter. (cached)

  ***

  #### Returns [SyncCacheAdapter](https://mikro-orm.io/api/core/interface/SyncCacheAdapter.md)

### [**](#getMetadataProvider)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L325)getMetadataProvider

* ****getMetadataProvider**(): [MetadataProvider](https://mikro-orm.io/api/core/class/MetadataProvider.md)

- Gets instance of MetadataProvider. (cached)

  ***

  #### Returns [MetadataProvider](https://mikro-orm.io/api/core/class/MetadataProvider.md)

### [**](#getNamingStrategy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L304)getNamingStrategy

* ****getNamingStrategy**(): [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

- Gets instance of NamingStrategy. (cached)

  ***

  #### Returns [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

### [**](#getPlatform)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L251)getPlatform

* ****getPlatform**(): [Platform](https://mikro-orm.io/api/core/class/Platform.md)

- #### Returns [Platform](https://mikro-orm.io/api/core/class/Platform.md)

### [**](#getRepositoryClass)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L346)getRepositoryClass

* ****getRepositoryClass**(repository): undefined | [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)<[EntityRepository](https://mikro-orm.io/api/core/class/EntityRepository.md)\<any>>

- Gets EntityRepository class to be instantiated.

  ***

  #### Parameters

  * ##### repository: () => [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)<[EntityRepository](https://mikro-orm.io/api/core/class/EntityRepository.md)\<Partial\<any>>>


  #### Returns undefined | [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)<[EntityRepository](https://mikro-orm.io/api/core/class/EntityRepository.md)\<any>>

### [**](#getResultCacheAdapter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L339)getResultCacheAdapter

* ****getResultCacheAdapter**(): [CacheAdapter](https://mikro-orm.io/api/core/interface/CacheAdapter.md)

- Gets instance of CacheAdapter for result cache. (cached)

  ***

  #### Returns [CacheAdapter](https://mikro-orm.io/api/core/interface/CacheAdapter.md)

### [**](#getSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L266)getSchema

* ****getSchema**(skipDefaultSchema): undefined | string

- #### Parameters

  * ##### skipDefaultSchema: boolean = <!-- -->false

  #### Returns undefined | string

### [**](#registerExtension)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L281)registerExtension

* ****registerExtension**(name, cb): void

- #### Parameters

  * ##### name: string
  * ##### cb: () => unknown


  #### Returns void

### [**](#reset)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L240)reset

* ****reset**\<T>(key): void

- Resets the configuration to its default value

  ***

  #### Parameters

  * ##### key: T

  #### Returns void

### [**](#resetServiceCache)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L370)resetServiceCache

* ****resetServiceCache**(): void

- #### Returns void

### [**](#set)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L232)set

* ****set**\<T, U>(key, value): void

- Overrides specified configuration value.

  ***

  #### Parameters

  * ##### key: T
  * ##### value: U

  #### Returns void
