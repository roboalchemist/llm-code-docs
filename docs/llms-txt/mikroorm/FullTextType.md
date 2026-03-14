# Source: https://mikro-orm.io/api/sql/class/FullTextType.md

# FullTextType<!-- -->

### Hierarchy

* [Type](https://mikro-orm.io/api/core/class/Type.md)\<string | [WeightedFullTextValue](https://mikro-orm.io/api/sql.md#WeightedFullTextValue), string | null | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)>
  * *FullTextType*

## Index[**](#index)

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

* [**compareAsType](#compareastype)
* [**compareValues](#compareValues)
* [**convertToDatabaseValue](#converttodatabasevalue)
* [**convertToDatabaseValueSQL](#convertToDatabaseValueSQL)
* [**convertToJSValue](#convertToJSValue)
* [**convertToJSValueSQL](#convertToJSValueSQL)
* [**ensureComparable](#ensureComparable)
* [**getColumnType](#getcolumntype)
* [**getDefaultLength](#getDefaultLength)
* [**toJSON](#toJSON)
* [**getType](#getType)
* [**isMappedType](#isMappedType)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/FullTextType.ts#L14)constructor

* ****new FullTextType**(regconfig): [FullTextType](https://mikro-orm.io/api/sql/class/FullTextType.md)

* Overrides Type.constructor

  #### Parameters

  * ##### regconfig: string = <!-- -->'simple'

  #### Returns [FullTextType](https://mikro-orm.io/api/sql/class/FullTextType.md)

## Properties<!-- -->[**](#properties)

### [**](#meta)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/Type.ts#L22)optionalinheritedmeta

**meta?

<!-- -->

: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>

Inherited from Type.meta

### [**](#platform)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/Type.ts#L21)optionalinheritedplatform

**platform?

<!-- -->

: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

Inherited from Type.platform

### [**](#prop)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/Type.ts#L23)optionalinheritedprop

**prop?

<!-- -->

: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

Inherited from Type.prop

### [**](#regconfig)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/FullTextType.ts#L14)publicregconfig

**regconfig: string =

<!-- -->

'simple'

## Accessors<!-- -->[**](#accessors)

### [**](#name)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/Type.ts#L67)inheritedname

* **get name(): string

* Inherited from Type.name

  #### Returns string

### [**](#runtimeType)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/Type.ts#L62)inheritedruntimeType

* **get runtimeType(): string

* Inherited from Type.runtimeType

  #### Returns string

## Methods<!-- -->[**](#methods)

### [**](#compareastype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/FullTextType.ts#L18)compareAsType

* ****compareAsType**(): string

* Overrides Type.compareAsType

  How should the raw database values be compared? Used in `EntityComparator`. Possible values: string | number | bigint | boolean | date | any | buffer | array

  ***

  #### Returns string

### [**](#compareValues)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/Type.ts#L60)optionalinheritedcompareValues

* ****compareValues**(a, b): boolean

* Inherited from Type.compareValues

  Allows to override the internal comparison logic.

  ***

  #### Parameters

  * ##### a: null | string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

  * ##### b: null | string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

  #### Returns boolean

### [**](#converttodatabasevalue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/FullTextType.ts#L29)convertToDatabaseValue

* ****convertToDatabaseValue**(value, platform, context): null | string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

* Overrides Type.convertToDatabaseValue

  Converts a value from its JS representation to its database representation of this type.

  ***

  #### Parameters

  * ##### value: string | [WeightedFullTextValue](https://mikro-orm.io/api/sql.md#WeightedFullTextValue)

  * ##### platform: [BasePostgreSqlPlatform](https://mikro-orm.io/api/sql/class/BasePostgreSqlPlatform.md)

  * ##### optionalcontext: boolean | [TransformContext](https://mikro-orm.io/api/core/interface/TransformContext.md)

  #### Returns null | string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

### [**](#convertToDatabaseValueSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/Type.ts#L42)optionalinheritedconvertToDatabaseValueSQL

* ****convertToDatabaseValueSQL**(key, platform): string

* Inherited from Type.convertToDatabaseValueSQL

  Converts a value from its JS representation to its database representation of this type.

  ***

  #### Parameters

  * ##### key: string

  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  #### Returns string

### [**](#convertToJSValue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/Type.ts#L35)inheritedconvertToJSValue

* ****convertToJSValue**(value, platform, context): string | [WeightedFullTextValue](https://mikro-orm.io/api/sql.md#WeightedFullTextValue)

* Inherited from Type.convertToJSValue

  Converts a value from its database representation to its JS representation of this type.

  ***

  #### Parameters

  * ##### value: null | string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  * ##### optionalcontext: [TransformContext](https://mikro-orm.io/api/core/interface/TransformContext.md)

  #### Returns string | [WeightedFullTextValue](https://mikro-orm.io/api/sql.md#WeightedFullTextValue)

### [**](#convertToJSValueSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/Type.ts#L47)optionalinheritedconvertToJSValueSQL

* ****convertToJSValueSQL**(key, platform): string

* Inherited from Type.convertToJSValueSQL

  Modifies the SQL expression (identifier, parameter) to convert to a JS value.

  ***

  #### Parameters

  * ##### key: string

  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  #### Returns string

### [**](#ensureComparable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/Type.ts#L76)inheritedensureComparable

* ****ensureComparable**\<T>(meta, prop): boolean

* Inherited from Type.ensureComparable

  When a value is hydrated, we convert it back to the database value to ensure comparability, as often the raw database response is not the same as the `convertToDatabaseValue` result. This allows to disable the additional conversion in case you know it is not needed.

  ***

  #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any>

  #### Returns boolean

### [**](#getcolumntype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/FullTextType.ts#L22)getColumnType

* ****getColumnType**(): string

* Overrides Type.getColumnType

  Gets the SQL declaration snippet for a field of this type.

  ***

  #### Returns string

### [**](#getDefaultLength)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/Type.ts#L109)optionalinheritedgetDefaultLength

* ****getDefaultLength**(platform): number

* Inherited from Type.getDefaultLength

  Get the default length for values of this type

  When doing schema generation, if neither "length" nor "columnType" option is provided, the length will be defaulted to this value.

  When doing entity generation, if the type is recognized to this type, and the inferred length is this value, the length option will be omitted in the output. If this method is not defined, length is always outputted based on what is in the database metadata.

  ***

  #### Parameters

  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

    The platform the default will be used for.

  #### Returns number

  The default value for the given platform.

### [**](#toJSON)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/Type.ts#L84)inheritedtoJSON

* ****toJSON**(value, platform): null | string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | [WeightedFullTextValue](https://mikro-orm.io/api/sql.md#WeightedFullTextValue)

* Inherited from Type.toJSON

  Converts a value from its JS representation to its serialized JSON form of this type. By default uses the runtime value.

  ***

  #### Parameters

  * ##### value: string | [WeightedFullTextValue](https://mikro-orm.io/api/sql.md#WeightedFullTextValue)

  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  #### Returns null | string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | [WeightedFullTextValue](https://mikro-orm.io/api/sql.md#WeightedFullTextValue)

### [**](#getType)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/Type.ts#L111)staticinheritedgetType

* ****getType**\<JSType, DBType, TypeClass>(cls): InstanceType\<TypeClass>

* Inherited from Type.getType

  #### Parameters

  * ##### cls: TypeClass

  #### Returns InstanceType\<TypeClass>

### [**](#isMappedType)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/Type.ts#L128)staticinheritedisMappedType

* ****isMappedType**(data): data is [Type](https://mikro-orm.io/api/core/class/Type.md)\<any, any>

* Inherited from Type.isMappedType

  Checks whether the argument is instance of `Type`.

  ***

  #### Parameters

  * ##### data: any

  #### Returns data is [Type](https://mikro-orm.io/api/core/class/Type.md)\<any, any>
