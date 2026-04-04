# Source: https://mikro-orm.io/api/core/class/Type.md

# abstractType<!-- --> \<JSType, DBType>

### Hierarchy

* *Type*

  * [DateType](https://mikro-orm.io/api/core/class/DateType.md)
  * [TimeType](https://mikro-orm.io/api/core/class/TimeType.md)
  * [DateTimeType](https://mikro-orm.io/api/core/class/DateTimeType.md)
  * [BigIntType](https://mikro-orm.io/api/core/class/BigIntType.md)
  * [Uint8ArrayType](https://mikro-orm.io/api/core/class/Uint8ArrayType.md)
  * [ArrayType](https://mikro-orm.io/api/core/class/ArrayType.md)
  * [EnumType](https://mikro-orm.io/api/core/class/EnumType.md)
  * [JsonType](https://mikro-orm.io/api/core/class/JsonType.md)
  * [IntegerType](https://mikro-orm.io/api/core/class/IntegerType.md)
  * [SmallIntType](https://mikro-orm.io/api/core/class/SmallIntType.md)
  * [TinyIntType](https://mikro-orm.io/api/core/class/TinyIntType.md)
  * [FloatType](https://mikro-orm.io/api/core/class/FloatType.md)
  * [DoubleType](https://mikro-orm.io/api/core/class/DoubleType.md)
  * [BooleanType](https://mikro-orm.io/api/core/class/BooleanType.md)
  * [DecimalType](https://mikro-orm.io/api/core/class/DecimalType.md)
  * [StringType](https://mikro-orm.io/api/core/class/StringType.md)
  * [UuidType](https://mikro-orm.io/api/core/class/UuidType.md)
  * [TextType](https://mikro-orm.io/api/core/class/TextType.md)
  * [UnknownType](https://mikro-orm.io/api/core/class/UnknownType.md)
  * [IntervalType](https://mikro-orm.io/api/core/class/IntervalType.md)
  * [FullTextType](https://mikro-orm.io/api/postgresql/class/FullTextType.md)
  * [UnicodeStringType](https://mikro-orm.io/api/mssql/class/UnicodeStringType.md)

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

* ****new Type**\<JSType, DBType>(): [Type](https://mikro-orm.io/api/core/class/Type.md)\<JSType, DBType>

- #### Returns [Type](https://mikro-orm.io/api/core/class/Type.md)\<JSType, DBType>

## Properties<!-- -->[**](#Properties)

### [**](#meta)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L23)optionalmeta

**meta?

<!-- -->

: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>

### [**](#platform)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L22)optionalplatform

**platform?

<!-- -->

: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

### [**](#prop)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L24)optionalprop

**prop?

<!-- -->

: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

## Accessors<!-- -->[**](#Accessors)

### [**](#name)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L68)name

* **get name(): string

- #### Returns string

### [**](#runtimeType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L63)runtimeType

* **get runtimeType(): string

- #### Returns string

## Methods<!-- -->[**](#Methods)

### [**](#compareAsType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L54)compareAsType

* ****compareAsType**(): string

- How should the raw database values be compared? Used in `EntityComparator`. Possible values: string | number | bigint | boolean | date | any | buffer | array

  ***

  #### Returns string

### [**](#compareValues)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L61)optionalcompareValues

* ****compareValues**(a, b): boolean

- Allows to override the internal comparison logic.

  ***

  #### Parameters

  * ##### a: DBType
  * ##### b: DBType

  #### Returns boolean

### [**](#convertToDatabaseValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L29)convertToDatabaseValue

* ****convertToDatabaseValue**(value, platform, context): DBType

- Converts a value from its JS representation to its database representation of this type.

  ***

  #### Parameters

  * ##### value: JSType
  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)
  * ##### optionalcontext: [TransformContext](https://mikro-orm.io/api/core/interface/TransformContext.md)

  #### Returns DBType

### [**](#convertToDatabaseValueSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L43)optionalconvertToDatabaseValueSQL

* ****convertToDatabaseValueSQL**(key, platform): string

- Converts a value from its JS representation to its database representation of this type.

  ***

  #### Parameters

  * ##### key: string
  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  #### Returns string

### [**](#convertToJSValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L36)convertToJSValue

* ****convertToJSValue**(value, platform, context): JSType

- Converts a value from its database representation to its JS representation of this type.

  ***

  #### Parameters

  * ##### value: DBType
  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)
  * ##### optionalcontext: [TransformContext](https://mikro-orm.io/api/core/interface/TransformContext.md)

  #### Returns JSType

### [**](#convertToJSValueSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L48)optionalconvertToJSValueSQL

* ****convertToJSValueSQL**(key, platform): string

- Modifies the SQL expression (identifier, parameter) to convert to a JS value.

  ***

  #### Parameters

  * ##### key: string
  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  #### Returns string

### [**](#ensureComparable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L77)ensureComparable

* ****ensureComparable**\<T>(meta, prop): boolean

- When a value is hydrated, we convert it back to the database value to ensure comparability, as often the raw database response is not the same as the `convertToDatabaseValue` result. This allows to disable the additional conversion in case you know it is not needed.

  ***

  #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>
  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any>

  #### Returns boolean

### [**](#getColumnType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L92)getColumnType

* ****getColumnType**(prop, platform): string

- Gets the SQL declaration snippet for a field of this type.

  ***

  #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>
  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  #### Returns string

### [**](#getDefaultLength)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L110)optionalgetDefaultLength

* ****getDefaultLength**(platform): number

- Get the default length for values of this type

  When doing schema generation, if neither "length" nor "columnType" option is provided, the length will be defaulted to this value.

  When doing entity generation, if the type is recognized to this type, and the inferred length is this value, the length option will be omitted in the output. If this method is not defined, length is always outputted based on what is in the database metadata.

  ***

  #### Parameters

  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

    The platform the default will be used for.

  #### Returns number

  The default value for the given platform.

### [**](#toJSON)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L85)toJSON

* ****toJSON**(value, platform): JSType | DBType

- Converts a value from its JS representation to its serialized JSON form of this type. By default uses the runtime value.

  ***

  #### Parameters

  * ##### value: JSType
  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  #### Returns JSType | DBType

### [**](#getType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L112)staticgetType

* ****getType**\<JSType, DBType, TypeClass>(cls): InstanceType\<TypeClass>

- #### Parameters

  * ##### cls: TypeClass

  #### Returns InstanceType\<TypeClass>

### [**](#isMappedType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/Type.ts#L125)staticisMappedType

* ****isMappedType**(data): data is [Type](https://mikro-orm.io/api/core/class/Type.md)\<any, any>

- Checks whether the argument is instance of `Type`.

  ***

  #### Parameters

  * ##### data: any

  #### Returns data is [Type](https://mikro-orm.io/api/core/class/Type.md)\<any, any>
