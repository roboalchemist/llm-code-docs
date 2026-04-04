# Source: https://mikro-orm.io/api/core/class/EntityComparator.md

# EntityComparator<!-- -->

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**diffEntities](#diffentities)
* [**mapResult](#mapresult)
* [**matching](#matching)
* [**prepareEntity](#prepareentity)
* [**isComparable](#isComparable)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/EntityComparator.ts#L49)constructor

* ****new EntityComparator**(metadata, platform, config): [EntityComparator](https://mikro-orm.io/api/core/class/EntityComparator.md)

* #### Parameters

  * ##### metadata: IMetadataStorage

  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  * ##### optionalconfig: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  #### Returns [EntityComparator](https://mikro-orm.io/api/core/class/EntityComparator.md)

## Methods<!-- -->[**](#methods)

### [**](#diffentities)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/EntityComparator.ts#L58)diffEntities

* ****diffEntities**\<T>(entityName, a, b, options): [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

* Computes difference between two entities.

  ***

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### a: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

  * ##### b: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

  * ##### optionaloptions: { includeInverseSides?<!-- -->: boolean }

    * ##### optionalincludeInverseSides: boolean

  #### Returns [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

### [**](#mapresult)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/EntityComparator.ts#L85)mapResult

* ****mapResult**\<T>(meta, result): [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

* Maps database columns to properties.

  ***

  #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

  * ##### result: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>

  #### Returns [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

### [**](#matching)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/EntityComparator.ts#L68)matching

* ****matching**\<T>(entityName, a, b): boolean

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### a: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

  * ##### b: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

  #### Returns boolean

### [**](#prepareentity)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/EntityComparator.ts#L77)prepareEntity

* ****prepareEntity**\<T>(entity): [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

* Removes ORM specific code from entities and prepares it for serializing. Used before change set computation. References will be mapped to primary keys, collections to arrays of primary keys.

  ***

  #### Parameters

  * ##### entity: T

  #### Returns [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

### [**](#isComparable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/EntityComparator.ts#L1039)staticisComparable

* ****isComparable**\<T>(prop, root): boolean

* perf: used to generate list of comparable properties during discovery, so we speed up the runtime comparison

  ***

  #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any>

  * ##### root: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>

  #### Returns boolean
