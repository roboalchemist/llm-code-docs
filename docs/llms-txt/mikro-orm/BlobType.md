# Source: https://mikro-orm.io/api/core/class/BlobType.md

# BlobType<!-- -->

### Hierarchy

* [Uint8ArrayType](https://mikro-orm.io/api/core/class/Uint8ArrayType.md)
  * *BlobType*

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

### [**](#constructor)constructor

* ****new BlobType**(): [BlobType](https://mikro-orm.io/api/core/class/BlobType.md)

- Inherited from Uint8ArrayType.constructor

  #### Returns [BlobType](https://mikro-orm.io/api/core/class/BlobType.md)

## Properties<!-- -->[**](#Properties)

### [**](#meta)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L23)optionalinheritedmeta

**meta?

<!-- -->

: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>

Inherited from Uint8ArrayType.meta

### [**](#platform)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L22)optionalinheritedplatform

**platform?

<!-- -->

: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

Inherited from Uint8ArrayType.platform

### [**](#prop)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L24)optionalinheritedprop

**prop?

<!-- -->

: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

Inherited from Uint8ArrayType.prop

## Accessors<!-- -->[**](#Accessors)

### [**](#name)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L68)inheritedname

* **get name(): string

- Inherited from Uint8ArrayType.name

  #### Returns string

### [**](#runtimeType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L63)inheritedruntimeType

* **get runtimeType(): string

- Inherited from Uint8ArrayType.runtimeType

  #### Returns string

## Methods<!-- -->[**](#Methods)

### [**](#compareAsType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/BlobType.ts#L21)compareAsType

* ****compareAsType**(): string

- Overrides Uint8ArrayType.compareAsType

  How should the raw database values be compared? Used in `EntityComparator`. Possible values: string | number | bigint | boolean | date | any | buffer | array

  ***

  #### Returns string

### [**](#compareValues)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L61)optionalinheritedcompareValues

* ****compareValues**(a, b): boolean

- Inherited from Uint8ArrayType.compareValues

  Allows to override the internal comparison logic.

  ***

  #### Parameters

  * ##### a: null | Uint8Array\<ArrayBufferLike>
  * ##### b: null | Uint8Array\<ArrayBufferLike>

  #### Returns boolean

### [**](#convertToDatabaseValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Uint8ArrayType.ts#L7)inheritedconvertToDatabaseValue

* ****convertToDatabaseValue**(value): Buffer\<ArrayBufferLike>

- Inherited from Uint8ArrayType.convertToDatabaseValue

  Converts a value from its JS representation to its database representation of this type.

  ***

  #### Parameters

  * ##### value: Uint8Array\<ArrayBufferLike>

  #### Returns Buffer\<ArrayBufferLike>

### [**](#convertToDatabaseValueSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L43)optionalinheritedconvertToDatabaseValueSQL

* ****convertToDatabaseValueSQL**(key, platform): string

- Inherited from Uint8ArrayType.convertToDatabaseValueSQL

  Converts a value from its JS representation to its database representation of this type.

  ***

  #### Parameters

  * ##### key: string
  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  #### Returns string

### [**](#convertToJSValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/BlobType.ts#L7)convertToJSValue

* ****convertToJSValue**(value): null | Buffer\<ArrayBufferLike>

- Overrides Uint8ArrayType.convertToJSValue

  Converts a value from its database representation to its JS representation of this type.

  ***

  #### Parameters

  * ##### value: Buffer\<ArrayBufferLike>

  #### Returns null | Buffer\<ArrayBufferLike>

### [**](#convertToJSValueSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L48)optionalinheritedconvertToJSValueSQL

* ****convertToJSValueSQL**(key, platform): string

- Inherited from Uint8ArrayType.convertToJSValueSQL

  Modifies the SQL expression (identifier, parameter) to convert to a JS value.

  ***

  #### Parameters

  * ##### key: string
  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  #### Returns string

### [**](#ensureComparable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/BlobType.ts#L25)ensureComparable

* ****ensureComparable**(): boolean

- Overrides Uint8ArrayType.ensureComparable

  When a value is hydrated, we convert it back to the database value to ensure comparability, as often the raw database response is not the same as the `convertToDatabaseValue` result. This allows to disable the additional conversion in case you know it is not needed.

  ***

  #### Returns boolean

### [**](#getColumnType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/BlobType.ts#L29)getColumnType

* ****getColumnType**(prop, platform): string

- Overrides Uint8ArrayType.getColumnType

  Gets the SQL declaration snippet for a field of this type.

  ***

  #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>
  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  #### Returns string

### [**](#getDefaultLength)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L110)optionalinheritedgetDefaultLength

* ****getDefaultLength**(platform): number

- Inherited from Uint8ArrayType.getDefaultLength

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

* ****toJSON**(value, platform): null | Uint8Array\<ArrayBufferLike>

- Inherited from Uint8ArrayType.toJSON

  Converts a value from its JS representation to its serialized JSON form of this type. By default uses the runtime value.

  ***

  #### Parameters

  * ##### value: null | Uint8Array\<ArrayBufferLike>
  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  #### Returns null | Uint8Array\<ArrayBufferLike>

### [**](#getType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L112)staticinheritedgetType

* ****getType**\<JSType, DBType, TypeClass>(cls): InstanceType\<TypeClass>

- Inherited from Uint8ArrayType.getType

  #### Parameters

  * ##### cls: TypeClass

  #### Returns InstanceType\<TypeClass>

### [**](#isMappedType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L125)staticinheritedisMappedType

* ****isMappedType**(data): data is [Type](https://mikro-orm.io/api/core/class/Type.md)\<any, any>

- Inherited from Uint8ArrayType.isMappedType

  Checks whether the argument is instance of `Type`.

  ***

  #### Parameters

  * ##### data: any

  #### Returns data is [Type](https://mikro-orm.io/api/core/class/Type.md)\<any, any>
