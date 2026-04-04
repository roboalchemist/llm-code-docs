# Source: https://mikro-orm.io/api/core/class/EntityComparator.md

# EntityComparator<!-- -->

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**diffEntities](#diffEntities)
* [**mapResult](#mapResult)
* [**matching](#matching)
* [**prepareEntity](#prepareEntity)
* [**isComparable](#isComparable)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/EntityComparator.ts#L35)constructor

* ****new EntityComparator**(metadata, platform): [EntityComparator](https://mikro-orm.io/api/core/class/EntityComparator.md)

- #### Parameters

  * ##### metadata: IMetadataStorage
  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  #### Returns [EntityComparator](https://mikro-orm.io/api/core/class/EntityComparator.md)

## Methods<!-- -->[**](#Methods)

### [**](#diffEntities)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/EntityComparator.ts#L41)diffEntities

* ****diffEntities**\<T>(entityName, a, b, options): [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

- Computes difference between two entities.

  ***

  #### Parameters

  * ##### entityName: string
  * ##### a: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>
  * ##### b: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>
  * ##### optionaloptions: { includeInverseSides?<!-- -->: boolean }
    * ##### optionalincludeInverseSides: boolean

  #### Returns [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

### [**](#mapResult)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/EntityComparator.ts#L63)mapResult

* ****mapResult**\<T>(entityName, result): [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

- Maps database columns to properties.

  ***

  #### Parameters

  * ##### entityName: string
  * ##### result: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>

  #### Returns [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

### [**](#matching)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/EntityComparator.ts#L46)matching

* ****matching**\<T>(entityName, a, b): boolean

- #### Parameters

  * ##### entityName: string
  * ##### a: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>
  * ##### b: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

  #### Returns boolean

### [**](#prepareEntity)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/EntityComparator.ts#L55)prepareEntity

* ****prepareEntity**\<T>(entity): [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

- Removes ORM specific code from entities and prepares it for serializing. Used before change set computation. References will be mapped to primary keys, collections to arrays of primary keys.

  ***

  #### Parameters

  * ##### entity: T

  #### Returns [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

### [**](#isComparable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/EntityComparator.ts#L783)staticisComparable

* ****isComparable**\<T>(prop, root): boolean

- perf: used to generate list of comparable properties during discovery, so we speed up the runtime comparison

  ***

  #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any>
  * ##### root: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>

  #### Returns boolean
