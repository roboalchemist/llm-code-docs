# Source: https://mikro-orm.io/api/core/class/MediumIntType.md

# MediumIntType<!-- -->

### Hierarchy

* [IntegerType](https://mikro-orm.io/api/core/class/IntegerType.md)
  * *MediumIntType*

## Index[**](#index)

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
* [**getColumnType](#getcolumntype)
* [**getDefaultLength](#getDefaultLength)
* [**toJSON](#toJSON)
* [**getType](#getType)
* [**isMappedType](#isMappedType)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)constructor

* ****new MediumIntType**(): [MediumIntType](https://mikro-orm.io/api/core/class/MediumIntType.md)

* Inherited from IntegerType.constructor

  #### Returns [MediumIntType](https://mikro-orm.io/api/core/class/MediumIntType.md)

## Properties<!-- -->[**](#properties)

### [**](#meta)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/Type.ts#L22)optionalinheritedmeta

**meta?

<!-- -->

: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>

Inherited from IntegerType.meta

### [**](#platform)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/Type.ts#L21)optionalinheritedplatform

**platform?

<!-- -->

: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

Inherited from IntegerType.platform

### [**](#prop)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/Type.ts#L23)optionalinheritedprop

**prop?

<!-- -->

: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

Inherited from IntegerType.prop

## Accessors<!-- -->[**](#accessors)

### [**](#name)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/Type.ts#L67)inheritedname

* **get name(): string

* Inherited from IntegerType.name

  #### Returns string

### [**](#runtimeType)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/Type.ts#L62)inheritedruntimeType

* **get runtimeType(): string

* Inherited from IntegerType.runtimeType

  #### Returns string

## Methods<!-- -->[**](#methods)

### [**](#compareAsType)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/IntegerType.ts#L10)inheritedcompareAsType

* ****compareAsType**(): string

* Inherited from IntegerType.compareAsType

  How should the raw database values be compared? Used in `EntityComparator`. Possible values: string | number | bigint | boolean | date | any | buffer | array

  ***

  #### Returns string

### [**](#compareValues)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/Type.ts#L60)optionalinheritedcompareValues

* ****compareValues**(a, b): boolean

* Inherited from IntegerType.compareValues

  Allows to override the internal comparison logic.

  ***

  #### Parameters

  * ##### a: undefined | null | number

  * ##### b: undefined | null | number

  #### Returns boolean

### [**](#convertToDatabaseValue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/Type.ts#L28)inheritedconvertToDatabaseValue

* ****convertToDatabaseValue**(value, platform, context): undefined | null | number

* Inherited from IntegerType.convertToDatabaseValue

  Converts a value from its JS representation to its database representation of this type.

  ***

  #### Parameters

  * ##### value: undefined | null | number

  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  * ##### optionalcontext: [TransformContext](https://mikro-orm.io/api/core/interface/TransformContext.md)

  #### Returns undefined | null | number

### [**](#convertToDatabaseValueSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/Type.ts#L42)optionalinheritedconvertToDatabaseValueSQL

* ****convertToDatabaseValueSQL**(key, platform): string

* Inherited from IntegerType.convertToDatabaseValueSQL

  Converts a value from its JS representation to its database representation of this type.

  ***

  #### Parameters

  * ##### key: string

  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  #### Returns string

### [**](#convertToJSValue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/Type.ts#L35)inheritedconvertToJSValue

* ****convertToJSValue**(value, platform, context): undefined | null | number

* Inherited from IntegerType.convertToJSValue

  Converts a value from its database representation to its JS representation of this type.

  ***

  #### Parameters

  * ##### value: undefined | null | number

  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  * ##### optionalcontext: [TransformContext](https://mikro-orm.io/api/core/interface/TransformContext.md)

  #### Returns undefined | null | number

### [**](#convertToJSValueSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/Type.ts#L47)optionalinheritedconvertToJSValueSQL

* ****convertToJSValueSQL**(key, platform): string

* Inherited from IntegerType.convertToJSValueSQL

  Modifies the SQL expression (identifier, parameter) to convert to a JS value.

  ***

  #### Parameters

  * ##### key: string

  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  #### Returns string

### [**](#ensureComparable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/IntegerType.ts#L14)inheritedensureComparable

* ****ensureComparable**(): boolean

* Inherited from IntegerType.ensureComparable

  When a value is hydrated, we convert it back to the database value to ensure comparability, as often the raw database response is not the same as the `convertToDatabaseValue` result. This allows to disable the additional conversion in case you know it is not needed.

  ***

  #### Returns boolean

### [**](#getcolumntype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/MediumIntType.ts#L6)getColumnType

* ****getColumnType**(prop, platform): string

* Overrides IntegerType.getColumnType

  Gets the SQL declaration snippet for a field of this type.

  ***

  #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  #### Returns string

### [**](#getDefaultLength)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/Type.ts#L109)optionalinheritedgetDefaultLength

* ****getDefaultLength**(platform): number

* Inherited from IntegerType.getDefaultLength

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

* ****toJSON**(value, platform): undefined | null | number

* Inherited from IntegerType.toJSON

  Converts a value from its JS representation to its serialized JSON form of this type. By default uses the runtime value.

  ***

  #### Parameters

  * ##### value: undefined | null | number

  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  #### Returns undefined | null | number

### [**](#getType)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/Type.ts#L111)staticinheritedgetType

* ****getType**\<JSType, DBType, TypeClass>(cls): InstanceType\<TypeClass>

* Inherited from IntegerType.getType

  #### Parameters

  * ##### cls: TypeClass

  #### Returns InstanceType\<TypeClass>

### [**](#isMappedType)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/Type.ts#L128)staticinheritedisMappedType

* ****isMappedType**(data): data is [Type](https://mikro-orm.io/api/core/class/Type.md)\<any, any>

* Inherited from IntegerType.isMappedType

  Checks whether the argument is instance of `Type`.

  ***

  #### Parameters

  * ##### data: any

  #### Returns data is [Type](https://mikro-orm.io/api/core/class/Type.md)\<any, any>
