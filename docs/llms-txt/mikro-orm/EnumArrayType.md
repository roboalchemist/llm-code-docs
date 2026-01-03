# Source: https://mikro-orm.io/api/core/class/EnumArrayType.md

# EnumArrayType<!-- --> \<T>

### Hierarchy

* [ArrayType](https://mikro-orm.io/api/core/class/ArrayType.md)\<T>
  * *EnumArrayType*

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**meta](#meta)
* [**platform](#platform)
* [**prop](#prop)

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

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/EnumArrayType.ts#L18)constructor

* ****new EnumArrayType**\<T>(owner, items, hydrate): [EnumArrayType](https://mikro-orm.io/api/core/class/EnumArrayType.md)\<T>

- Overrides ArrayType.constructor

  #### Parameters

  * ##### owner: string
  * ##### optionalitems: T\[]
  * ##### hydrate: (i) => T = <!-- -->...


  #### Returns [EnumArrayType](https://mikro-orm.io/api/core/class/EnumArrayType.md)\<T>

## Properties<!-- -->[**](#Properties)

### [**](#meta)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L23)optionalinheritedmeta

**meta?

<!-- -->

: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>

Inherited from ArrayType.meta

### [**](#platform)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L22)optionalinheritedplatform

**platform?

<!-- -->

: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

Inherited from ArrayType.platform

### [**](#prop)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L24)optionalinheritedprop

**prop?

<!-- -->

: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

Inherited from ArrayType.prop

## Accessors<!-- -->[**](#Accessors)

### [**](#name)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L68)inheritedname

* **get name(): string

- Inherited from ArrayType.name

  #### Returns string

### [**](#runtimeType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L63)inheritedruntimeType

* **get runtimeType(): string

- Inherited from ArrayType.runtimeType

  #### Returns string

## Methods<!-- -->[**](#Methods)

### [**](#compareAsType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/ArrayType.ts#L45)inheritedcompareAsType

* ****compareAsType**(): string

- Inherited from ArrayType.compareAsType

  How should the raw database values be compared? Used in `EntityComparator`. Possible values: string | number | bigint | boolean | date | any | buffer | array

  ***

  #### Returns string

### [**](#compareValues)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L61)optionalinheritedcompareValues

* ****compareValues**(a, b): boolean

- Inherited from ArrayType.compareValues

  Allows to override the internal comparison logic.

  ***

  #### Parameters

  * ##### a: null | string
  * ##### b: null | string

  #### Returns boolean

### [**](#convertToDatabaseValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/EnumArrayType.ts#L24)convertToDatabaseValue

* ****convertToDatabaseValue**(value, platform, context): null | string

- Overrides ArrayType.convertToDatabaseValue

  Converts a value from its JS representation to its database representation of this type.

  ***

  #### Parameters

  * ##### value: null | T\[]
  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)
  * ##### optionalcontext: [TransformContext](https://mikro-orm.io/api/core/interface/TransformContext.md)

  #### Returns null | string

### [**](#convertToDatabaseValueSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L43)optionalinheritedconvertToDatabaseValueSQL

* ****convertToDatabaseValueSQL**(key, platform): string

- Inherited from ArrayType.convertToDatabaseValueSQL

  Converts a value from its JS representation to its database representation of this type.

  ***

  #### Parameters

  * ##### key: string
  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  #### Returns string

### [**](#convertToJSValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/ArrayType.ts#L33)inheritedconvertToJSValue

* ****convertToJSValue**(value, platform): null | T\[]

- Inherited from ArrayType.convertToJSValue

  Converts a value from its database representation to its JS representation of this type.

  ***

  #### Parameters

  * ##### value: null | string | T\[]
  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  #### Returns null | T\[]

### [**](#convertToJSValueSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L48)optionalinheritedconvertToJSValueSQL

* ****convertToJSValueSQL**(key, platform): string

- Inherited from ArrayType.convertToJSValueSQL

  Modifies the SQL expression (identifier, parameter) to convert to a JS value.

  ***

  #### Parameters

  * ##### key: string
  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  #### Returns string

### [**](#ensureComparable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L77)inheritedensureComparable

* ****ensureComparable**\<T>(meta, prop): boolean

- Inherited from ArrayType.ensureComparable

  When a value is hydrated, we convert it back to the database value to ensure comparability, as often the raw database response is not the same as the `convertToDatabaseValue` result. This allows to disable the additional conversion in case you know it is not needed.

  ***

  #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>
  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any>

  #### Returns boolean

### [**](#getColumnType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/EnumArrayType.ts#L37)getColumnType

* ****getColumnType**(prop, platform): string

- Overrides ArrayType.getColumnType

  Gets the SQL declaration snippet for a field of this type.

  ***

  #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>
  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  #### Returns string

### [**](#getDefaultLength)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L110)optionalinheritedgetDefaultLength

* ****getDefaultLength**(platform): number

- Inherited from ArrayType.getDefaultLength

  Get the default length for values of this type

  When doing schema generation, if neither "length" nor "columnType" option is provided, the length will be defaulted to this value.

  When doing entity generation, if the type is recognized to this type, and the inferred length is this value, the length option will be omitted in the output. If this method is not defined, length is always outputted based on what is in the database metadata.

  ***

  #### Parameters

  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

    The platform the default will be used for.

  #### Returns number

  The default value for the given platform.

### [**](#toJSON)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/ArrayType.ts#L49)inheritedtoJSON

* ****toJSON**(value): T\[]

- Inherited from ArrayType.toJSON

  Converts a value from its JS representation to its serialized JSON form of this type. By default uses the runtime value.

  ***

  #### Parameters

  * ##### value: T\[]

  #### Returns T\[]

### [**](#getType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L112)staticinheritedgetType

* ****getType**\<JSType, DBType, TypeClass>(cls): InstanceType\<TypeClass>

- Inherited from ArrayType.getType

  #### Parameters

  * ##### cls: TypeClass

  #### Returns InstanceType\<TypeClass>

### [**](#isMappedType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L125)staticinheritedisMappedType

* ****isMappedType**(data): data is [Type](https://mikro-orm.io/api/core/class/Type.md)\<any, any>

- Inherited from ArrayType.isMappedType

  Checks whether the argument is instance of `Type`.

  ***

  #### Parameters

  * ##### data: any

  #### Returns data is [Type](https://mikro-orm.io/api/core/class/Type.md)\<any, any>
