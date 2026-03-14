# Source: https://mikro-orm.io/api/mongodb/class/ObjectId.md

# publicObjectId<!-- -->

A class representation of the BSON ObjectId type.

### Hierarchy

* BSONValue
  * *ObjectId*

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**cacheHexString](#cacheHexString)

### Accessors

* [**\_bsontype](#_bsontype)
* [**\[bsonType\]](#\[bsonType])
* [**id](#id)

### Methods

* [**equals](#equals)
* [**getTimestamp](#gettimestamp)
* [**inspect](#inspect)
* [**toHexString](#tohexstring)
* [**toJSON](#tojson)
* [**toString](#tostring)
* [**createFromBase64](#createFromBase64)
* [**createFromHexString](#createFromHexString)
* [**createFromTime](#createFromTime)
* [**generate](#generate)
* [**isValid](#isValid)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)constructor

* ****new ObjectId**(): [ObjectId](https://mikro-orm.io/api/mongodb/class/ObjectId.md)
* ****new ObjectId**(inputId): [ObjectId](https://mikro-orm.io/api/mongodb/class/ObjectId.md)
* ****new ObjectId**(inputId): [ObjectId](https://mikro-orm.io/api/mongodb/class/ObjectId.md)
* ****new ObjectId**(inputId): [ObjectId](https://mikro-orm.io/api/mongodb/class/ObjectId.md)
* ****new ObjectId**(inputId): [ObjectId](https://mikro-orm.io/api/mongodb/class/ObjectId.md)
* ****new ObjectId**(inputId): [ObjectId](https://mikro-orm.io/api/mongodb/class/ObjectId.md)

* Overrides BSONValue.constructor

  To generate a new ObjectId, use ObjectId() with no argument.

  ***

  #### Returns [ObjectId](https://mikro-orm.io/api/mongodb/class/ObjectId.md)

## Properties<!-- -->[**](#properties)

### [**](#cacheHexString)staticcacheHexString

**cacheHexString: boolean

## Accessors<!-- -->[**](#accessors)

### [**](#_bsontype)\_bsontype

* **get \_bsontype(): ObjectId

* Overrides BSONValue.\_bsontype

  #### Returns ObjectId

### [**](#\[bsonType])inherited\[bsonType]

* **get \[bsonType]\(): this\[\_bsontype]

* Inherited from BSONValue.\[bsonType]

  #### Returns this\[\_bsontype]

### [**](#id)id

* **get id(): Uint8Array\<ArrayBufferLike>

* The ObjectId bytes

  ***

  #### Returns Uint8Array\<ArrayBufferLike>

## Methods<!-- -->[**](#methods)

### [**](#equals)equals

* ****equals**(otherId): boolean

* Compares the equality of this ObjectId with `otherID`.

  ***

  #### Parameters

  * ##### otherId: undefined | null | string | [ObjectId](https://mikro-orm.io/api/mongodb/class/ObjectId.md) | ObjectIdLike

    ObjectId instance to compare against.

  #### Returns boolean

### [**](#gettimestamp)getTimestamp

* ****getTimestamp**(): Date

* Returns the generation date (accurate up to the second) that this ID was generated.

  ***

  #### Returns Date

### [**](#inspect)inspect

* ****inspect**(depth, options, inspect): string

* Overrides BSONValue.inspect

  Converts to a string representation of this Id.

  ***

  #### Parameters

  * ##### optionaldepth: number

  * ##### optionaloptions: unknown

  * ##### optionalinspect: InspectFn

  #### Returns string

  return the 24 character hex string representation.

### [**](#tohexstring)toHexString

* ****toHexString**(): string

* Returns the ObjectId id as a 24 lowercase character hex string representation

  ***

  #### Returns string

### [**](#tojson)toJSON

* ****toJSON**(): string

* Converts to its JSON the 24 character hex string representation.

  ***

  #### Returns string

### [**](#tostring)toString

* ****toString**(encoding): string

* Converts the id into a 24 character hex string for printing, unless encoding is provided.

  ***

  #### Parameters

  * ##### optionalencoding: hex | base64

    hex or base64

  #### Returns string

### [**](#createFromBase64)staticcreateFromBase64

* ****createFromBase64**(base64): [ObjectId](https://mikro-orm.io/api/mongodb/class/ObjectId.md)

* Creates an ObjectId instance from a base64 string

  ***

  #### Parameters

  * ##### base64: string

  #### Returns [ObjectId](https://mikro-orm.io/api/mongodb/class/ObjectId.md)

### [**](#createFromHexString)staticcreateFromHexString

* ****createFromHexString**(hexString): [ObjectId](https://mikro-orm.io/api/mongodb/class/ObjectId.md)

* Creates an ObjectId from a hex string representation of an ObjectId.

  ***

  #### Parameters

  * ##### hexString: string

    create a ObjectId from a passed in 24 character hexstring.

  #### Returns [ObjectId](https://mikro-orm.io/api/mongodb/class/ObjectId.md)

### [**](#createFromTime)staticcreateFromTime

* ****createFromTime**(time): [ObjectId](https://mikro-orm.io/api/mongodb/class/ObjectId.md)

* Creates an ObjectId from a second based number, with the rest of the ObjectId zeroed out. Used for comparisons or sorting the ObjectId.

  ***

  #### Parameters

  * ##### time: number

    an integer number representing a number of seconds.

  #### Returns [ObjectId](https://mikro-orm.io/api/mongodb/class/ObjectId.md)

### [**](#generate)staticgenerate

* ****generate**(time): Uint8Array\<ArrayBufferLike>

* Generate a 12 byte id buffer used in ObjectId's

  ***

  #### Parameters

  * ##### optionaltime: number

    pass in a second based timestamp.

  #### Returns Uint8Array\<ArrayBufferLike>

### [**](#isValid)staticisValid

* ****isValid**(id): boolean

* Checks if a value can be used to create a valid bson ObjectId

  ***

  #### Parameters

  * ##### id: string | Uint8Array\<ArrayBufferLike> | [ObjectId](https://mikro-orm.io/api/mongodb/class/ObjectId.md) | ObjectIdLike

    any JS value

  #### Returns boolean
