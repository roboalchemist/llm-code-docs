# Source: https://mikro-orm.io/api/core/class/ObjectHydrator.md

# ObjectHydrator<!-- -->

### Hierarchy

* [Hydrator](https://mikro-orm.io/api/core/class/Hydrator.md)
  * *ObjectHydrator*

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**hydrate](#hydrate)
* [**hydrateReference](#hydrateReference)
* [**isRunning](#isRunning)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/hydration/Hydrator.ts#L12)constructor

* ****new ObjectHydrator**(metadata, platform, config): [ObjectHydrator](https://mikro-orm.io/api/core/class/ObjectHydrator.md)

- Inherited from Hydrator.constructor

  #### Parameters

  * ##### metadata: [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)
  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)
  * ##### config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  #### Returns [ObjectHydrator](https://mikro-orm.io/api/core/class/ObjectHydrator.md)

## Methods<!-- -->[**](#Methods)

### [**](#hydrate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/hydration/ObjectHydrator.ts#L26)hydrate

* ****hydrate**\<T>(entity, meta, data, factory, type, newEntity, convertCustomTypes, schema, parentSchema, normalizeAccessors): void

- Overrides Hydrator.hydrate

  * **@inheritDoc**

  ***

  #### Parameters

  * ##### entity: T
  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>
  * ##### data: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>
  * ##### factory: [EntityFactory](https://mikro-orm.io/api/core/class/EntityFactory.md)
  * ##### type: full | reference
  * ##### newEntity: boolean = <!-- -->false
  * ##### convertCustomTypes: boolean = <!-- -->false
  * ##### optionalschema: string
  * ##### optionalparentSchema: string
  * ##### optionalnormalizeAccessors: boolean

  #### Returns void

### [**](#hydrateReference)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/hydration/ObjectHydrator.ts#L39)hydrateReference

* ****hydrateReference**\<T>(entity, meta, data, factory, convertCustomTypes, schema, parentSchema, normalizeAccessors): void

- Overrides Hydrator.hydrateReference

  * **@inheritDoc**

  ***

  #### Parameters

  * ##### entity: T
  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>
  * ##### data: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>
  * ##### factory: [EntityFactory](https://mikro-orm.io/api/core/class/EntityFactory.md)
  * ##### convertCustomTypes: boolean = <!-- -->false
  * ##### optionalschema: string
  * ##### optionalparentSchema: string
  * ##### optionalnormalizeAccessors: boolean

  #### Returns void

### [**](#isRunning)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/hydration/Hydrator.ts#L42)inheritedisRunning

* ****isRunning**(): boolean

- Inherited from Hydrator.isRunning

  #### Returns boolean
