# Source: https://mikro-orm.io/api/core/interface/MikroORMOptions.md

# MikroORMOptions<!-- --> \<D, EM>

### Hierarchy

* [ConnectionOptions](https://mikro-orm.io/api/core/interface/ConnectionOptions.md)
  * *MikroORMOptions*

## Index[**](#Index)

### Properties

* [**allowGlobalContext](#allowGlobalContext)
* [**assign](#assign)
* [**autoJoinOneToOneOwner](#autoJoinOneToOneOwner)
* [**autoJoinRefsForFilters](#autoJoinRefsForFilters)
* [**baseDir](#baseDir)
* [**batchSize](#batchSize)
* [**charset](#charset)
* [**clientUrl](#clientUrl)
* [**collate](#collate)
* [**colors](#colors)
* [**connect](#connect)
* [**context](#context)
* [**contextName](#contextName)
* [**dataloader](#dataloader)
* [**dbName](#dbName)
* [**debug](#debug)
* [**disableIdentityMap](#disableIdentityMap)
* [**disableTransactions](#disableTransactions)
* [**discovery](#discovery)
* [**driver](#driver)
* [**driverOptions](#driverOptions)
* [**dynamicImportProvider](#dynamicImportProvider)
* [**embeddables](#embeddables)
* [**ensureDatabase](#ensureDatabase)
* [**ensureIndexes](#ensureIndexes)
* [**entities](#entities)
* [**entitiesTs](#entitiesTs)
* [**entityGenerator](#entityGenerator)
* [**entityManager](#entityManager)
* [**entityRepository](#entityRepository)
* [**extensions](#extensions)
* [**filters](#filters)
* [**filtersOnRelations](#filtersOnRelations)
* [**findExactlyOneOrFailHandler](#findExactlyOneOrFailHandler)
* [**findOneOrFailHandler](#findOneOrFailHandler)
* [**flushMode](#flushMode)
* [**forceEntityConstructor](#forceEntityConstructor)
* [**forceUndefined](#forceUndefined)
* [**forceUtcTimezone](#forceUtcTimezone)
* [**hashAlgorithm](#hashAlgorithm)
* [**highlighter](#highlighter)
* [**host](#host)
* [**hydrator](#hydrator)
* [**ignoreDeprecations](#ignoreDeprecations)
* [**ignoreUndefinedInQuery](#ignoreUndefinedInQuery)
* [**implicitTransactions](#implicitTransactions)
* [**loadStrategy](#loadStrategy)
* [**logger](#logger)
* [**loggerFactory](#loggerFactory)
* [**metadataCache](#metadataCache)
* [**metadataProvider](#metadataProvider)
* [**migrations](#migrations)
* [**multipleStatements](#multipleStatements)
* [**name](#name)
* [**namingStrategy](#namingStrategy)
* [**onQuery](#onQuery)
* [**password](#password)
* [**persistOnCreate](#persistOnCreate)
* [**pool](#pool)
* [**populateAfterFlush](#populateAfterFlush)
* [**populateWhere](#populateWhere)
* [**port](#port)
* [**preferReadReplicas](#preferReadReplicas)
* [**preferTs](#preferTs)
* [**processOnCreateHooksEarly](#processOnCreateHooksEarly)
* [**propagationOnPrototype](#propagationOnPrototype)
* [**replicas](#replicas)
* [**resultCache](#resultCache)
* [**schema](#schema)
* [**schemaGenerator](#schemaGenerator)
* [**seeder](#seeder)
* [**serialization](#serialization)
* [**strict](#strict)
* [**subscribers](#subscribers)
* [**timezone](#timezone)
* [**tsNode](#tsNode)
* [**upsertManaged](#upsertManaged)
* [**useBatchInserts](#useBatchInserts)
* [**useBatchUpdates](#useBatchUpdates)
* [**user](#user)
* [**validate](#validate)
* [**validateRequired](#validateRequired)
* [**verbose](#verbose)

## Properties<!-- -->[**](#Properties)

### [**](#allowGlobalContext)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L648)allowGlobalContext

**allowGlobalContext: boolean

### [**](#assign)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L618)assign

**assign: [AssignOptions](https://mikro-orm.io/api/core/interface/AssignOptions.md)\<boolean>

### [**](#autoJoinOneToOneOwner)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L608)autoJoinOneToOneOwner

**autoJoinOneToOneOwner: boolean

### [**](#autoJoinRefsForFilters)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L609)autoJoinRefsForFilters

**autoJoinRefsForFilters: boolean

### [**](#baseDir)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L666)baseDir

**baseDir: string

### [**](#batchSize)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L634)batchSize

**batchSize: number

### [**](#charset)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L522)optionalinheritedcharset

**charset?

<!-- -->

: string

Inherited from ConnectionOptions.charset

### [**](#clientUrl)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L517)optionalinheritedclientUrl

**clientUrl?

<!-- -->

: string

Inherited from ConnectionOptions.clientUrl

### [**](#collate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L523)optionalinheritedcollate

**collate?

<!-- -->

: string

Inherited from ConnectionOptions.collate

### [**](#colors)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L651)optionalcolors

**colors?

<!-- -->

: boolean

### [**](#connect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L604)connect

**connect: boolean

### [**](#context)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L646)context

**context: (name) => undefined | [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

#### Type declaration

* * **(name): undefined | [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  - #### Parameters

    * ##### name: string

    #### Returns undefined | [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

### [**](#contextName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L647)contextName

**contextName: string

### [**](#dataloader)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L637)dataloader

**dataloader: boolean | [DataloaderType](https://mikro-orm.io/api/core/enum/DataloaderType.md)

### [**](#dbName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L514)optionalinheriteddbName

**dbName?

<!-- -->

: string

Inherited from ConnectionOptions.dbName

### [**](#debug)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L655)debug

**debug: boolean | [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)\[]

### [**](#disableIdentityMap)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L649)optionaldisableIdentityMap

**disableIdentityMap?

<!-- -->

: boolean

### [**](#disableTransactions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L603)optionaldisableTransactions

**disableTransactions?

<!-- -->

: boolean

### [**](#discovery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L599)discovery

**discovery: [MetadataDiscoveryOptions](https://mikro-orm.io/api/core/interface/MetadataDiscoveryOptions.md)

### [**](#driver)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L600)optionaldriver

**driver?

<!-- -->

: new (config) => D

#### Type declaration

* * **new (config): D

  - #### Parameters

    * ##### config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

    #### Returns D

### [**](#driverOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L526)optionalinheriteddriverOptions

**driverOptions?

<!-- -->

: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

Inherited from ConnectionOptions.driverOptions

### [**](#dynamicImportProvider)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L697)dynamicImportProvider

**dynamicImportProvider: (id) => Promise\<unknown>

#### Type declaration

* * **(id): Promise\<unknown>

  - #### Parameters

    * ##### id: string

    #### Returns Promise\<unknown>

### [**](#embeddables)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L676)embeddables

**embeddables: { prefixMode: [EmbeddedPrefixMode](https://mikro-orm.io/api/core.md#EmbeddedPrefixMode) }

#### Type declaration

* ##### prefixMode: [EmbeddedPrefixMode](https://mikro-orm.io/api/core.md#EmbeddedPrefixMode)

### [**](#ensureDatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L630)ensureDatabase

**ensureDatabase: boolean | [EnsureDatabaseOptions](https://mikro-orm.io/api/core/interface/EnsureDatabaseOptions.md)

### [**](#ensureIndexes)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L631)ensureIndexes

**ensureIndexes: boolean

### [**](#entities)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L594)entities

**entities: (string | [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<Partial\<any>> | [EntityClassGroup](https://mikro-orm.io/api/core.md#EntityClassGroup)\<Partial\<any>> | [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<any, never>)\[]

### [**](#entitiesTs)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L595)entitiesTs

**entitiesTs: (string | [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<Partial\<any>> | [EntityClassGroup](https://mikro-orm.io/api/core.md#EntityClassGroup)\<Partial\<any>> | [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<any, never>)\[]

### [**](#entityGenerator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L679)entityGenerator

**entityGenerator: [GenerateOptions](https://mikro-orm.io/api/core/interface/GenerateOptions.md)

### [**](#entityManager)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L641)optionalentityManager

**entityManager?

<!-- -->

: [Constructor](https://mikro-orm.io/api/core.md#Constructor)\<EM>

### [**](#entityRepository)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L640)optionalentityRepository

**entityRepository?

<!-- -->

: [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)<[EntityRepository](https://mikro-orm.io/api/core/class/EntityRepository.md)\<any>>

### [**](#extensions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L596)extensions

**extensions: { register: (orm) => void }\[]

### [**](#filters)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L598)filters

**filters: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<{ name?

<!-- -->

: string } & Omit\<FilterDef, name>>

### [**](#filtersOnRelations)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L610)filtersOnRelations

**filtersOnRelations: boolean

### [**](#findExactlyOneOrFailHandler)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L654)findExactlyOneOrFailHandler

**findExactlyOneOrFailHandler: (entityName, where) => Error

#### Type declaration

* * **(entityName, where): Error

  - #### Parameters

    * ##### entityName: string
    * ##### where: IPrimaryKeyValue | [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

    #### Returns Error

### [**](#findOneOrFailHandler)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L653)findOneOrFailHandler

**findOneOrFailHandler: (entityName, where) => Error

#### Type declaration

* * **(entityName, where): Error

  - #### Parameters

    * ##### entityName: string
    * ##### where: IPrimaryKeyValue | [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

    #### Returns Error

### [**](#flushMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L639)flushMode

**flushMode: always | [FlushMode](https://mikro-orm.io/api/core/enum/FlushMode.md) | commit | auto

### [**](#forceEntityConstructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L621)forceEntityConstructor

**forceEntityConstructor: boolean | (string | [Constructor](https://mikro-orm.io/api/core.md#Constructor)\<Partial\<any>>)\[]

### [**](#forceUndefined)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L622)forceUndefined

**forceUndefined: boolean

### [**](#forceUtcTimezone)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L628)optionalforceUtcTimezone

**forceUtcTimezone?

<!-- -->

: boolean

### [**](#hashAlgorithm)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L696)hashAlgorithm

**hashAlgorithm: md5 | sha256

### [**](#highlighter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L657)highlighter

**highlighter: [Highlighter](https://mikro-orm.io/api/core/interface/Highlighter.md)

### [**](#host)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L518)optionalinheritedhost

**host?

<!-- -->

: string

Inherited from ConnectionOptions.host

### [**](#hydrator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L635)hydrator

**hydrator: HydratorConstructor

### [**](#ignoreDeprecations)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L656)ignoreDeprecations

**ignoreDeprecations: boolean | string\[]

### [**](#ignoreUndefinedInQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L606)optionalignoreUndefinedInQuery

**ignoreUndefinedInQuery?

<!-- -->

: boolean

### [**](#implicitTransactions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L602)optionalimplicitTransactions

**implicitTransactions?

<!-- -->

: boolean

### [**](#loadStrategy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L636)loadStrategy

**loadStrategy: [LoadStrategy](https://mikro-orm.io/api/core/enum/LoadStrategy.md) | select-in | joined | balanced

### [**](#logger)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L650)logger

**logger: (message) => void

#### Type declaration

* * **(message): void

  - #### Parameters

    * ##### message: string

    #### Returns void

### [**](#loggerFactory)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L652)optionalloggerFactory

**loggerFactory?

<!-- -->

: (options) => [Logger](https://mikro-orm.io/api/core/interface/Logger.md)

#### Type declaration

* * **(options): [Logger](https://mikro-orm.io/api/core/interface/Logger.md)

  - #### Parameters

    * ##### options: [LoggerOptions](https://mikro-orm.io/api/core/interface/LoggerOptions.md)

    #### Returns [Logger](https://mikro-orm.io/api/core/interface/Logger.md)

### [**](#metadataCache)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L680)metadataCache

**metadataCache: { adapter?

<!-- -->

: new (...params) => [SyncCacheAdapter](https://mikro-orm.io/api/core/interface/SyncCacheAdapter.md); combined?

<!-- -->

: string | boolean; enabled?

<!-- -->

: boolean; options?

<!-- -->

: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary); pretty?

<!-- -->

: boolean }

#### Type declaration

* ##### optionaladapter?<!-- -->: new (...params) => [SyncCacheAdapter](https://mikro-orm.io/api/core/interface/SyncCacheAdapter.md)

  * * **new (...params): [SyncCacheAdapter](https://mikro-orm.io/api/core/interface/SyncCacheAdapter.md)

    - #### Parameters

      * ##### rest...params: any\[]

      #### Returns [SyncCacheAdapter](https://mikro-orm.io/api/core/interface/SyncCacheAdapter.md)

* ##### optionalcombined?<!-- -->: string | boolean

* ##### optionalenabled?<!-- -->: boolean

* ##### optionaloptions?<!-- -->: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

* ##### optionalpretty?<!-- -->: boolean

### [**](#metadataProvider)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L693)metadataProvider

**metadataProvider: new (config) => [MetadataProvider](https://mikro-orm.io/api/core/class/MetadataProvider.md)

#### Type declaration

* * **new (config): [MetadataProvider](https://mikro-orm.io/api/core/class/MetadataProvider.md)

  - #### Parameters

    * ##### config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

    #### Returns [MetadataProvider](https://mikro-orm.io/api/core/class/MetadataProvider.md)

### [**](#migrations)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L667)migrations

**migrations: [MigrationsOptions](https://mikro-orm.io/api/core.md#MigrationsOptions)

### [**](#multipleStatements)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L524)optionalinheritedmultipleStatements

**multipleStatements?

<!-- -->

: boolean

Inherited from ConnectionOptions.multipleStatements

### [**](#name)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L516)optionalinheritedname

**name?

<!-- -->

: string

Inherited from ConnectionOptions.name

### [**](#namingStrategy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L601)optionalnamingStrategy

**namingStrategy?

<!-- -->

: new () => [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

#### Type declaration

* * **new (): [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

  - #### Returns [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

### [**](#onQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L607)onQuery

**onQuery: (sql, params) => string

#### Type declaration

* * **(sql, params): string

  - #### Parameters

    * ##### sql: string
    * ##### params: unknown\[]

    #### Returns string

### [**](#password)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L521)optionalinheritedpassword

**password?

<!-- -->

: string | () => [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<string> | [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)<[DynamicPassword](https://mikro-orm.io/api/core/interface/DynamicPassword.md)>

Inherited from ConnectionOptions.password

### [**](#persistOnCreate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L619)persistOnCreate

**persistOnCreate: boolean

### [**](#pool)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L525)optionalinheritedpool

**pool?

<!-- -->

: [PoolConfig](https://mikro-orm.io/api/core/interface/PoolConfig.md)

Inherited from ConnectionOptions.pool

### [**](#populateAfterFlush)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L612)populateAfterFlush

**populateAfterFlush: boolean

### [**](#populateWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L638)optionalpopulateWhere

**populateWhere?

<!-- -->

: [PopulateHint](https://mikro-orm.io/api/core/enum/PopulateHint.md) | infer | all

### [**](#port)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L519)optionalinheritedport

**port?

<!-- -->

: number

Inherited from ConnectionOptions.port

### [**](#preferReadReplicas)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L695)preferReadReplicas

**preferReadReplicas: boolean

### [**](#preferTs)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L663)optionalpreferTs

**preferTs?

<!-- -->

: boolean

Using this option, you can force the ORM to use the TS options regardless of whether the TypeScript support is detected or not. This effectively means using `entitiesTs` for discovery and `pathTs` for migrations and seeders. Should be used only for tests and stay disabled for production builds.

### [**](#processOnCreateHooksEarly)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L627)processOnCreateHooksEarly

**processOnCreateHooksEarly: boolean

Property `onCreate` hooks are normally executed during `flush` operation. With this option, they will be processed early inside `em.create()` method.

### [**](#propagationOnPrototype)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L611)propagationOnPrototype

**propagationOnPrototype: boolean

### [**](#replicas)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L642)optionalreplicas

**replicas?

<!-- -->

: [ConnectionOptions](https://mikro-orm.io/api/core/interface/ConnectionOptions.md)\[]

### [**](#resultCache)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L687)resultCache

**resultCache: { adapter?

<!-- -->

: new (...params) => [CacheAdapter](https://mikro-orm.io/api/core/interface/CacheAdapter.md); expiration?

<!-- -->

: number; global?

<!-- -->

: number | boolean | \[string, number]; options?

<!-- -->

: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary) }

#### Type declaration

* ##### optionaladapter?<!-- -->: new (...params) => [CacheAdapter](https://mikro-orm.io/api/core/interface/CacheAdapter.md)

  * * **new (...params): [CacheAdapter](https://mikro-orm.io/api/core/interface/CacheAdapter.md)

    - #### Parameters

      * ##### rest...params: any\[]

      #### Returns [CacheAdapter](https://mikro-orm.io/api/core/interface/CacheAdapter.md)

* ##### optionalexpiration?<!-- -->: number

* ##### optionalglobal?<!-- -->: number | boolean | \[string, number]

* ##### optionaloptions?<!-- -->: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L515)optionalinheritedschema

**schema?

<!-- -->

: string

Inherited from ConnectionOptions.schema

### [**](#schemaGenerator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L668)schemaGenerator

**schemaGenerator: { createForeignKeyConstraints?

<!-- -->

: boolean; disableForeignKeys?

<!-- -->

: boolean; ignoreSchema?

<!-- -->

: string\[]; managementDbName?

<!-- -->

: string; skipColumns?

<!-- -->

: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<(string | RegExp)\[]>; skipTables?

<!-- -->

: (string | RegExp)\[] }

#### Type declaration

* ##### optionalcreateForeignKeyConstraints?<!-- -->: boolean
* ##### optionaldisableForeignKeys?<!-- -->: boolean
* ##### optionalignoreSchema?<!-- -->: string\[]
* ##### optionalmanagementDbName?<!-- -->: string
* ##### optionalskipColumns?<!-- -->: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<(string | RegExp)\[]>
* ##### optionalskipTables?<!-- -->: (string | RegExp)\[]

### [**](#seeder)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L694)seeder

**seeder: [SeederOptions](https://mikro-orm.io/api/core/interface/SeederOptions.md)

### [**](#serialization)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L613)serialization

**serialization: { forceObject?

<!-- -->

: boolean; includePrimaryKeys?

<!-- -->

: boolean }

#### Type declaration

* ##### optionalforceObject?<!-- -->: boolean

  Enforce unpopulated references to be returned as objects, e.g. `{ author: { id: 1 } }` instead of `{ author: 1 }`.

* ##### optionalincludePrimaryKeys?<!-- -->: boolean

### [**](#strict)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L643)strict

**strict: boolean

### [**](#subscribers)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L597)subscribers

**subscribers: ([EventSubscriber](https://mikro-orm.io/api/core/interface/EventSubscriber.md)\<any> | [Constructor](https://mikro-orm.io/api/core.md#Constructor)<[EventSubscriber](https://mikro-orm.io/api/core/interface/EventSubscriber.md)\<any>>)\[]

### [**](#timezone)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L629)optionaltimezone

**timezone?

<!-- -->

: string

### [**](#tsNode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L665)optionaltsNode

**tsNode?

<!-- -->

: boolean

* **@deprecated**

  use `preferTs` instead

### [**](#upsertManaged)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L620)upsertManaged

**upsertManaged: boolean

### [**](#useBatchInserts)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L632)optionaluseBatchInserts

**useBatchInserts?

<!-- -->

: boolean

### [**](#useBatchUpdates)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L633)optionaluseBatchUpdates

**useBatchUpdates?

<!-- -->

: boolean

### [**](#user)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L520)optionalinheriteduser

**user?

<!-- -->

: string

Inherited from ConnectionOptions.user

### [**](#validate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L644)validate

**validate: boolean

### [**](#validateRequired)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L645)validateRequired

**validateRequired: boolean

### [**](#verbose)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L605)verbose

**verbose: boolean
