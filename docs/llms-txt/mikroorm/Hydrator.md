# Source: https://mikro-orm.io/api/core/class/Hydrator.md

# abstractHydrator<!-- -->

### Hierarchy

* *Hydrator*
  * [ObjectHydrator](https://mikro-orm.io/api/core/class/ObjectHydrator.md)

### Implements

* IHydrator

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**hydrate](#hydrate)
* [**hydrateReference](#hydratereference)
* [**isRunning](#isrunning)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/hydration/Hydrator.ts#L11)constructor

* ****new Hydrator**(metadata, platform, config): [Hydrator](https://mikro-orm.io/api/core/class/Hydrator.md)

* #### Parameters

  * ##### metadata: [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  * ##### config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  #### Returns [Hydrator](https://mikro-orm.io/api/core/class/Hydrator.md)

## Methods<!-- -->[**](#methods)

### [**](#hydrate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/hydration/Hydrator.ts#L20)hydrate

* ****hydrate**\<T>(entity, meta, data, factory, type, newEntity, convertCustomTypes, schema, parentSchema): void

* Implementation of IHydrator.hydrate

  * **@inheritDoc**

  ***

  #### Parameters

  * ##### entity: T

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

  * ##### data: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

  * ##### factory: [EntityFactory](https://mikro-orm.io/api/core/class/EntityFactory.md)

  * ##### type: full | reference

  * ##### newEntity: boolean = <!-- -->false

  * ##### convertCustomTypes: boolean = <!-- -->false

  * ##### optionalschema: string

  * ##### optionalparentSchema: string

  #### Returns void

### [**](#hydratereference)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/hydration/Hydrator.ts#L45)hydrateReference

* ****hydrateReference**\<T>(entity, meta, data, factory, convertCustomTypes, schema, parentSchema): void

* Implementation of IHydrator.hydrateReference

  * **@inheritDoc**

  ***

  #### Parameters

  * ##### entity: T

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

  * ##### data: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

  * ##### factory: [EntityFactory](https://mikro-orm.io/api/core/class/EntityFactory.md)

  * ##### optionalconvertCustomTypes: boolean

  * ##### optionalschema: string

  * ##### optionalparentSchema: string

  #### Returns void

### [**](#isrunning)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/hydration/Hydrator.ts#L61)isRunning

* ****isRunning**(): boolean

* Implementation of IHydrator.isRunning

  #### Returns boolean
