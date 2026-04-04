# Source: https://mikro-orm.io/api/postgresql/class/FullTextType.md

# FullTextType<!-- -->

### Hierarchy

* [Type](https://mikro-orm.io/api/core/class/Type.md)\<string | [WeightedFullTextValue](https://mikro-orm.io/api/postgresql.md#WeightedFullTextValue), string | null | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)>
  * *FullTextType*

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**meta](#meta)
* [**platform](#platform)
* [**prop](#prop)
* [**regconfig](#regconfig)

### Accessors

* [**name](#name)
* [**runtimeType](#runtimeType)

### Methods

* [**compareAsType](#compareAsType)
* [**compareValues](#compareValues)
* [**convertToDatabaseValue](#convertToDatabaseValue)
* [**convertToDatabaseValueSQL](#convertToDatabaseValueSQL)
* [**convertToJSValue](#convertToJSValue)
* [**convertToJSValueSQL](#convertToJSValueSQL)
* [**ensureComparable](#ensureComparable)
* [**getColumnType](#getColumnType)
* [**getDefaultLength](#getDefaultLength)
* [**toJSON](#toJSON)
* [**getType](#getType)
* [**isMappedType](#isMappedType)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/types/FullTextType.ts#L15)constructor

* ****new FullTextType**(regconfig): [FullTextType](https://mikro-orm.io/api/postgresql/class/FullTextType.md)

- Overrides Type.constructor

  #### Parameters

  * ##### regconfig: string = <!-- -->'simple'

  #### Returns [FullTextType](https://mikro-orm.io/api/postgresql/class/FullTextType.md)

## Properties<!-- -->[**](#Properties)

### [**](#meta)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L23)optionalinheritedmeta

**meta?

<!-- -->

: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>

Inherited from Type.meta

### [**](#platform)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L22)optionalinheritedplatform

**platform?

<!-- -->

: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

Inherited from Type.platform

### [**](#prop)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L24)optionalinheritedprop

**prop?

<!-- -->

: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

Inherited from Type.prop

### [**](#regconfig)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/types/FullTextType.ts#L15)publicregconfig

**regconfig: string =

<!-- -->

'simple'

## Accessors<!-- -->[**](#Accessors)

### [**](#name)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L68)inheritedname

* **get name(): string

- Inherited from Type.name

  #### Returns string

### [**](#runtimeType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L63)inheritedruntimeType

* **get runtimeType(): string

- Inherited from Type.runtimeType

  #### Returns string

## Methods<!-- -->[**](#Methods)

### [**](#compareAsType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/types/FullTextType.ts#L19)compareAsType

* ****compareAsType**(): string

- Overrides Type.compareAsType

  How should the raw database values be compared? Used in `EntityComparator`. Possible values: string | number | bigint | boolean | date | any | buffer | array

  ***

  #### Returns string

### [**](#compareValues)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L61)optionalinheritedcompareValues

* ****compareValues**(a, b): boolean

- Inherited from Type.compareValues

  Allows to override the internal comparison logic.

  ***

  #### Parameters

  * ##### a: null | string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)
  * ##### b: null | string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)

  #### Returns boolean

### [**](#convertToDatabaseValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/types/FullTextType.ts#L30)convertToDatabaseValue

* ****convertToDatabaseValue**(value, platform, context): null | string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)

- Overrides Type.convertToDatabaseValue

  Converts a value from its JS representation to its database representation of this type.

  ***

  #### Parameters

  * ##### value: string | [WeightedFullTextValue](https://mikro-orm.io/api/postgresql.md#WeightedFullTextValue)
  * ##### platform: [PostgreSqlPlatform](https://mikro-orm.io/api/postgresql/class/PostgreSqlPlatform.md)
  * ##### optionalcontext: boolean | [TransformContext](https://mikro-orm.io/api/core/interface/TransformContext.md)

  #### Returns null | string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)

### [**](#convertToDatabaseValueSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L43)optionalinheritedconvertToDatabaseValueSQL

* ****convertToDatabaseValueSQL**(key, platform): string

- Inherited from Type.convertToDatabaseValueSQL

  Converts a value from its JS representation to its database representation of this type.

  ***

  #### Parameters

  * ##### key: string
  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  #### Returns string

### [**](#convertToJSValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L36)inheritedconvertToJSValue

* ****convertToJSValue**(value, platform, context): string | [WeightedFullTextValue](https://mikro-orm.io/api/postgresql.md#WeightedFullTextValue)

- Inherited from Type.convertToJSValue

  Converts a value from its database representation to its JS representation of this type.

  ***

  #### Parameters

  * ##### value: null | string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)
  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)
  * ##### optionalcontext: [TransformContext](https://mikro-orm.io/api/core/interface/TransformContext.md)

  #### Returns string | [WeightedFullTextValue](https://mikro-orm.io/api/postgresql.md#WeightedFullTextValue)

### [**](#convertToJSValueSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L48)optionalinheritedconvertToJSValueSQL

* ****convertToJSValueSQL**(key, platform): string

- Inherited from Type.convertToJSValueSQL

  Modifies the SQL expression (identifier, parameter) to convert to a JS value.

  ***

  #### Parameters

  * ##### key: string
  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  #### Returns string

### [**](#ensureComparable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L77)inheritedensureComparable

* ****ensureComparable**\<T>(meta, prop): boolean

- Inherited from Type.ensureComparable

  When a value is hydrated, we convert it back to the database value to ensure comparability, as often the raw database response is not the same as the `convertToDatabaseValue` result. This allows to disable the additional conversion in case you know it is not needed.

  ***

  #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>
  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any>

  #### Returns boolean

### [**](#getColumnType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/types/FullTextType.ts#L23)getColumnType

* ****getColumnType**(): string

- Overrides Type.getColumnType

  Gets the SQL declaration snippet for a field of this type.

  ***

  #### Returns string

### [**](#getDefaultLength)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L110)optionalinheritedgetDefaultLength

* ****getDefaultLength**(platform): number

- Inherited from Type.getDefaultLength

  Get the default length for values of this type

  When doing schema generation, if neither "length" nor "columnType" option is provided, the length will be defaulted to this value.

  When doing entity generation, if the type is recognized to this type, and the inferred length is this value, the length option will be omitted in the output. If this method is not defined, length is always outputted based on what is in the database metadata.

  ***

  #### Parameters

  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

    The platform the default will be used for.

  #### Returns number

  The default value for the given platform.

### [**](#toJSON)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L85)inheritedtoJSON

* ****toJSON**(value, platform): null | string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md) | [WeightedFullTextValue](https://mikro-orm.io/api/postgresql.md#WeightedFullTextValue)

- Inherited from Type.toJSON

  Converts a value from its JS representation to its serialized JSON form of this type. By default uses the runtime value.

  ***

  #### Parameters

  * ##### value: string | [WeightedFullTextValue](https://mikro-orm.io/api/postgresql.md#WeightedFullTextValue)
  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  #### Returns null | string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md) | [WeightedFullTextValue](https://mikro-orm.io/api/postgresql.md#WeightedFullTextValue)

### [**](#getType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L112)staticinheritedgetType

* ****getType**\<JSType, DBType, TypeClass>(cls): InstanceType\<TypeClass>

- Inherited from Type.getType

  #### Parameters

  * ##### cls: TypeClass

  #### Returns InstanceType\<TypeClass>

### [**](#isMappedType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L125)staticinheritedisMappedType

* ****isMappedType**(data): data is [Type](https://mikro-orm.io/api/core/class/Type.md)\<any, any>

- Inherited from Type.isMappedType

  Checks whether the argument is instance of `Type`.

  ***

  #### Parameters

  * ##### data: any

  #### Returns data is [Type](https://mikro-orm.io/api/core/class/Type.md)\<any, any>
