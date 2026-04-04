# Source: https://mikro-orm.io/api/mongodb/class/ObjectId.md

# publicObjectId<!-- -->

A class representation of the BSON ObjectId type.

### Hierarchy

* BSONValue
  * *ObjectId*

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**cacheHexString](#cacheHexString)

### Accessors

* [**\_bsontype](#_bsontype)
* [**id](#id)

### Methods

* [**equals](#equals)
* [**getTimestamp](#getTimestamp)
* [**inspect](#inspect)
* [**toHexString](#toHexString)
* [**toJSON](#toJSON)
* [**toString](#toString)
* [**createFromBase64](#createFromBase64)
* [**createFromHexString](#createFromHexString)
* [**createFromTime](#createFromTime)
* [**generate](#generate)
* [**isValid](#isValid)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/bson/bson.d.ts#L1354)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/bson/bson.d.ts#L1360)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/bson/bson.d.ts#L1366)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/bson/bson.d.ts#L1372)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/bson/bson.d.ts#L1378)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/bson/bson.d.ts#L1380)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/bson/bson.d.ts#L1386)constructor

* ****new ObjectId**(inputId): [ObjectId](https://mikro-orm.io/api/mongodb/class/ObjectId.md)
* ****new ObjectId**(inputId): [ObjectId](https://mikro-orm.io/api/mongodb/class/ObjectId.md)
* ****new ObjectId**(inputId): [ObjectId](https://mikro-orm.io/api/mongodb/class/ObjectId.md)
* ****new ObjectId**(inputId): [ObjectId](https://mikro-orm.io/api/mongodb/class/ObjectId.md)
* ****new ObjectId**(inputId): [ObjectId](https://mikro-orm.io/api/mongodb/class/ObjectId.md)
* ****new ObjectId**(): [ObjectId](https://mikro-orm.io/api/mongodb/class/ObjectId.md)
* ****new ObjectId**(inputId): [ObjectId](https://mikro-orm.io/api/mongodb/class/ObjectId.md)

- Overrides BSONValue.constructor

  Create ObjectId from a number.

  * **@deprecated**

    Instead, use `static createFromTime()` to set a numeric value for the new ObjectId.

  ***

  #### Parameters

  * ##### inputId: number

    A number.

  #### Returns [ObjectId](https://mikro-orm.io/api/mongodb/class/ObjectId.md)

## Properties<!-- -->[**](#Properties)

### [**](#cacheHexString)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/bson/bson.d.ts#L1346)staticcacheHexString

**cacheHexString: boolean

## Accessors<!-- -->[**](#Accessors)

### [**](#_bsontype)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/bson/bson.d.ts#L1344)\_bsontype

* **get \_bsontype(): ObjectId

- Overrides BSONValue.\_bsontype

  #### Returns ObjectId

### [**](#id)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/bson/bson.d.ts#L1391)id

* **get id(): Uint8Array\<ArrayBufferLike>

- The ObjectId bytes

  ***

  #### Returns Uint8Array\<ArrayBufferLike>

## Methods<!-- -->[**](#Methods)

### [**](#equals)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/bson/bson.d.ts#L1416)equals

* ****equals**(otherId): boolean

- Compares the equality of this ObjectId with `otherID`.

  ***

  #### Parameters

  * ##### otherId: undefined | null | string | [ObjectId](https://mikro-orm.io/api/mongodb/class/ObjectId.md) | ObjectIdLike

    ObjectId instance to compare against.

  #### Returns boolean

### [**](#getTimestamp)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/bson/bson.d.ts#L1418)getTimestamp

* ****getTimestamp**(): Date

- Returns the generation date (accurate up to the second) that this ID was generated.

  ***

  #### Returns Date

### [**](#inspect)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/bson/bson.d.ts#L1448)inspect

* ****inspect**(depth, options, inspect): string

- Overrides BSONValue.inspect

  Converts to a string representation of this Id.

  ***

  #### Parameters

  * ##### optionaldepth: number
  * ##### optionaloptions: unknown
  * ##### optionalinspect: InspectFn

  #### Returns string

  return the 24 character hex string representation.

### [**](#toHexString)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/bson/bson.d.ts#L1395)toHexString

* ****toHexString**(): string

- Returns the ObjectId id as a 24 lowercase character hex string representation

  ***

  #### Returns string

### [**](#toJSON)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/bson/bson.d.ts#L1409)toJSON

* ****toJSON**(): string

- Converts to its JSON the 24 character hex string representation.

  ***

  #### Returns string

### [**](#toString)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/bson/bson.d.ts#L1407)toString

* ****toString**(encoding): string

- Converts the id into a 24 character hex string for printing, unless encoding is provided.

  ***

  #### Parameters

  * ##### optionalencoding: base64 | hex

    hex or base64

  #### Returns string

### [**](#createFromBase64)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/bson/bson.d.ts#L1434)staticcreateFromBase64

* ****createFromBase64**(base64): [ObjectId](https://mikro-orm.io/api/mongodb/class/ObjectId.md)

- Creates an ObjectId instance from a base64 string

  ***

  #### Parameters

  * ##### base64: string

  #### Returns [ObjectId](https://mikro-orm.io/api/mongodb/class/ObjectId.md)

### [**](#createFromHexString)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/bson/bson.d.ts#L1432)staticcreateFromHexString

* ****createFromHexString**(hexString): [ObjectId](https://mikro-orm.io/api/mongodb/class/ObjectId.md)

- Creates an ObjectId from a hex string representation of an ObjectId.

  ***

  #### Parameters

  * ##### hexString: string

    create a ObjectId from a passed in 24 character hexstring.

  #### Returns [ObjectId](https://mikro-orm.io/api/mongodb/class/ObjectId.md)

### [**](#createFromTime)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/bson/bson.d.ts#L1426)staticcreateFromTime

* ****createFromTime**(time): [ObjectId](https://mikro-orm.io/api/mongodb/class/ObjectId.md)

- Creates an ObjectId from a second based number, with the rest of the ObjectId zeroed out. Used for comparisons or sorting the ObjectId.

  ***

  #### Parameters

  * ##### time: number

    an integer number representing a number of seconds.

  #### Returns [ObjectId](https://mikro-orm.io/api/mongodb/class/ObjectId.md)

### [**](#generate)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/bson/bson.d.ts#L1402)staticgenerate

* ****generate**(time): Uint8Array\<ArrayBufferLike>

- Generate a 12 byte id buffer used in ObjectId's

  ***

  #### Parameters

  * ##### optionaltime: number

    pass in a second based timestamp.

  #### Returns Uint8Array\<ArrayBufferLike>

### [**](#isValid)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/bson/bson.d.ts#L1439)staticisValid

* ****isValid**(id): boolean

- Checks if a value can be used to create a valid bson ObjectId

  ***

  #### Parameters

  * ##### id: string | number | Uint8Array\<ArrayBufferLike> | [ObjectId](https://mikro-orm.io/api/mongodb/class/ObjectId.md) | ObjectIdLike

    any JS value

  #### Returns boolean
