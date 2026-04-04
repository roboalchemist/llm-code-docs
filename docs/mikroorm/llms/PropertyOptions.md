# Source: https://mikro-orm.io/api/core/interface/PropertyOptions.md

# PropertyOptions<!-- --> \<Owner>

### Hierarchy

* *PropertyOptions*

  * [ReferenceOptions](https://mikro-orm.io/api/core/interface/ReferenceOptions.md)
  * [EmbeddedOptions](https://mikro-orm.io/api/core/interface/EmbeddedOptions.md)
  * [EnumOptions](https://mikro-orm.io/api/core/interface/EnumOptions.md)
  * [PrimaryKeyOptions](https://mikro-orm.io/api/core/interface/PrimaryKeyOptions.md)
  * [SerializedPrimaryKeyOptions](https://mikro-orm.io/api/core/interface/SerializedPrimaryKeyOptions.md)

## Index[**](#index)

### Properties

* [**accessor](#accessor)
* [**autoincrement](#autoincrement)
* [**columnType](#columnType)
* [**columnTypes](#columnTypes)
* [**comment](#comment)
* [**concurrencyCheck](#concurrencyCheck)
* [**customOrder](#customOrder)
* [**default](#default)
* [**defaultRaw](#defaultRaw)
* [**extra](#extra)
* [**fieldName](#fieldName)
* [**fieldNames](#fieldNames)
* [**formula](#formula)
* [**generated](#generated)
* [**getter](#getter)
* [**getterName](#getterName)
* [**groups](#groups)
* [**hidden](#hidden)
* [**hydrate](#hydrate)
* [**check](#check)
* [**ignoreSchemaChanges](#ignoreSchemaChanges)
* [**index](#index)
* [**lazy](#lazy)
* [**length](#length)
* [**name](#name)
* [**nullable](#nullable)
* [**onCreate](#onCreate)
* [**onUpdate](#onUpdate)
* [**persist](#persist)
* [**precision](#precision)
* [**primary](#primary)
* [**ref](#ref)
* [**returning](#returning)
* [**runtimeType](#runtimeType)
* [**scale](#scale)
* [**serializedName](#serializedName)
* [**serializedPrimaryKey](#serializedPrimaryKey)
* [**serializer](#serializer)
* [**setter](#setter)
* [**type](#type)
* [**unique](#unique)
* [**unsigned](#unsigned)
* [**version](#version)

## Properties<!-- -->[**](#properties)

### [**](#accessor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L322)optionalaccessor

**accessor?

<!-- -->

: boolean | [AnyString](https://mikro-orm.io/api/core.md#AnyString) | keyof

<!-- -->

Owner

When using a private property backed by a public get/set pair, use the `accessor` option to point to the other side.

> The `fieldName` will be inferred based on the accessor name unless specified explicitly.

If the `accessor` option points to something, the ORM will use the backing property directly.

* **@example**

  ```
  @Entity()
  export class User {
    // the ORM will use the backing field directly
    @Property({ accessor: 'email' })
    private _email: string;

    get email() {
      return this._email;
    }

    set email() {
      return this._email;
    }
  }
  ```

  If you want to the ORM to use your accessor internally too, use `accessor: true` on the get/set property instead. This is handy if you want to use a native private property for the backing field.

* **@example**

  ```
  @Entity({ forceConstructor: true })
  export class User {
    #email: string;

    // the ORM will use the accessor internally
    @Property({ accessor: true })
    get email() {
      return this.#email;
    }

    set email() {
      return this.#email;
    }
  }
  ```

### [**](#autoincrement)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L145)optionalautoincrement

**autoincrement?

<!-- -->

: boolean

Explicitly specify the auto increment of the primary key.

### [**](#columnType)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L104)optionalcolumnType

**columnType?

<!-- -->

: [AnyString](https://mikro-orm.io/api/core.md#AnyString) | ColumnType

Specify an exact database column type for Generator. This option is only for simple properties represented by a single column. (SQL only)

### [**](#columnTypes)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L108)optionalcolumnTypes

**columnTypes?

<!-- -->

: ([AnyString](https://mikro-orm.io/api/core.md#AnyString) | ColumnType)\[]

Specify an exact database column type for Generator. This option is suitable for composite keys, where one property is represented by multiple columns. (SQL only)

### [**](#comment)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L352)optionalcomment

**comment?

<!-- -->

: string

Specify comment of column for Generator. (SQL only)

### [**](#concurrencyCheck)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L211)optionalconcurrencyCheck

**concurrencyCheck?

<!-- -->

: boolean

Set to true to enable Locking via concurrency fields.

### [**](#customOrder)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L348)optionalcustomOrder

**customOrder?

<!-- -->

: string\[] | number\[] | boolean\[]

Specify a custom order based on the values. (SQL only)

### [**](#default)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L164)optionaldefault

**default?

<!-- -->

: null | string | number | boolean | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | Date | string\[] | number\[]

Specify default column value for Generator. This is a runtime value, assignable to the entity property. (SQL only)

### [**](#defaultRaw)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L169)optionaldefaultRaw

**defaultRaw?

<!-- -->

: string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

Specify SQL functions for Generator. (SQL only) Since v4 you should use defaultRaw for SQL functions. e.g. now()

### [**](#extra)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L354)optionalextra

**extra?

<!-- -->

: string

mysql only

### [**](#fieldName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L93)optionalfieldName

**fieldName?

<!-- -->

: string

Specify database column name for this property.

* **@see**

  <https://mikro-orm.io/docs/naming-strategy>

### [**](#fieldNames)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L100)optionalfieldNames

**fieldNames?

<!-- -->

: string\[]

Specify database column names for this property. Same as `fieldName` but for composite FKs.

* **@see**

  <https://mikro-orm.io/docs/naming-strategy>

### [**](#formula)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L175)optionalformula

**formula?

<!-- -->

: string | [FormulaCallback](https://mikro-orm.io/api/core.md#FormulaCallback)\<Owner>

Set to map some SQL snippet for the entity.

* **@see**

  <https://mikro-orm.io/docs/defining-entities#formulas> Formulas

### [**](#generated)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L179)optionalgenerated

**generated?

<!-- -->

: string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | [GeneratedColumnCallback](https://mikro-orm.io/api/core.md#GeneratedColumnCallback)\<Owner>

For generated columns. This will be appended to the column type after the `generated always` clause.

### [**](#getter)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L262)optionalgetter

**getter?

<!-- -->

: boolean

Set true to define the properties as getter. (virtual)

* **@example**

  ```
  @Property({ getter: true })
  get fullName() {
    return this.firstName + this.lastName;
  }
  ```

### [**](#getterName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L275)optionalgetterName

**getterName?

<!-- -->

: keyof

<!-- -->

Owner

When defining a property over a method (not a getter, a regular function), you can use this option to point to the method name.

* **@example**

  ```
  @Property({ getter: true })
  getFullName() {
    return this.firstName + this.lastName;
  }
  ```

### [**](#groups)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L344)optionalgroups

**groups?

<!-- -->

: string\[]

Specify serialization groups for `serialize()` calls. If a property does not specify any group, it will be included, otherwise only properties with a matching group are included.

### [**](#hidden)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L203)optionalhidden

**hidden?

<!-- -->

: boolean

Set to true to omit the property when Serializing.

### [**](#hydrate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L195)optionalhydrate

**hydrate?

<!-- -->

: boolean

Set false to disable hydration of this property. Useful for persisted getters.

### [**](#check)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L225)optionalcheck

**check?

<!-- -->

: string | [CheckCallback](https://mikro-orm.io/api/core.md#CheckCallback)\<Owner>

Specify column with check constraints. (Postgres driver only)

* **@see**

  <https://mikro-orm.io/docs/defining-entities#check-constraints>

### [**](#ignoreSchemaChanges)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L360)optionalignoreSchemaChanges

**ignoreSchemaChanges?

<!-- -->

: (type | extra | default)\[]

Set to avoid a perpetual diff from the Generator when columns are generated.

* **@see**

  <https://mikro-orm.io/docs/defining-entities#sql-generated-columns>

### [**](#index)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L215)optionalindex

**index?

<!-- -->

: string | boolean

Explicitly specify index on a property.

### [**](#lazy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L231)optionallazy

**lazy?

<!-- -->

: boolean

Set to omit the property from the select clause for lazy loading.

* **@see**

  <https://mikro-orm.io/docs/defining-entities#lazy-scalar-properties>

### [**](#length)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L133)optionallength

**length?

<!-- -->

: number

Set length of database column, used for datetime/timestamp/varchar column types for Generator. (SQL only)

### [**](#name)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L87)optionalname

**name?

<!-- -->

: string

Alias for `fieldName`.

### [**](#nullable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L183)optionalnullable

**nullable?

<!-- -->

: boolean

Set column as nullable for Generator.

### [**](#onCreate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L154)optionalonCreate

**onCreate?

<!-- -->

: (entity, em) => any

Automatically set the property value when entity gets created, executed during flush operation.

***

#### Type declaration

* * **(entity, em): any

  * #### Parameters

    * ##### entity: Owner

    * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

    #### Returns any

### [**](#onUpdate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L159)optionalonUpdate

**onUpdate?

<!-- -->

: (entity, em) => any

Automatically update the property value every time entity gets updated, executed during flush operation.

***

#### Type declaration

* * **(entity, em): any

  * #### Parameters

    * ##### entity: Owner

    * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

    #### Returns any

### [**](#persist)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L191)optionalpersist

**persist?

<!-- -->

: boolean

Set false to define Property.

### [**](#precision)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L137)optionalprecision

**precision?

<!-- -->

: number

Set precision of database column to represent the number of significant digits. (SQL only)

### [**](#primary)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L238)optionalprimary

**primary?

<!-- -->

: boolean

Set true to define entity's unique primary key identifier. Alias for `@PrimaryKey()` decorator

* **@see**

  <https://mikro-orm.io/docs/decorators#primarykey>

### [**](#ref)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L199)optionalref

**ref?

<!-- -->

: boolean

Enable `ScalarReference` wrapper for lazy values. Use this in combination with `lazy: true` to have a type-safe accessor object in place of the value.

### [**](#returning)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L149)optionalreturning

**returning?

<!-- -->

: boolean

Add the property to the `returning` statement.

### [**](#runtimeType)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L129)optionalruntimeType

**runtimeType?

<!-- -->

: string

Runtime type of the property. This is the JS type that your property is mapped to, e.g. `string` or `number`, and is normally inferred automatically via `reflect-metadata`. In some cases, the inference won't work, and you might need to specify the `runtimeType` explicitly - the most common one is when you use a union type with null like `foo: number | null`.

### [**](#scale)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L141)optionalscale

**scale?

<!-- -->

: number

Set scale of database column to represents the number of digits after the decimal point. (SQL only)

### [**](#serializedName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L339)optionalserializedName

**serializedName?

<!-- -->

: string

Specify name of key for the serialized value.

### [**](#serializedPrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L329)optionalserializedPrimaryKey

**serializedPrimaryKey?

<!-- -->

: boolean

Set to define serialized primary key for MongoDB. (virtual) Alias for `@SerializedPrimaryKey()` decorator.

* **@see**

  <https://mikro-orm.io/docs/decorators#serializedprimarykey>

### [**](#serializer)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L335)optionalserializer

**serializer?

<!-- -->

: (value, options) => any

Set to use serialize property. Allow to specify a callback that will be used when serializing a property.

* **@see**

  <https://mikro-orm.io/docs/serializing#property-serializers>

***

#### Type declaration

* * **(value, options): any

  * #### Parameters

    * ##### value: any

    * ##### optionaloptions: [SerializeOptions](https://mikro-orm.io/api/core/interface/SerializeOptions.md)\<any, never, never>

    #### Returns any

### [**](#setter)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L250)optionalsetter

**setter?

<!-- -->

: boolean

Set true to define the properties as setter. (virtual)

* **@example**

  ```
  @Property({ setter: true })
  set address(value: string) {
      this._address = value.toLocaleLowerCase();
  }
  ```

### [**](#type)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L115)optionaltype

**type?

<!-- -->

: string | [AnyString](https://mikro-orm.io/api/core.md#AnyString) | Date | uint8array | array | enumArray | unknown | [Type](https://mikro-orm.io/api/core/class/Type.md)\<any, any> | ObjectId | [Constructor](https://mikro-orm.io/api/core.md#Constructor)\<Partial\<any>> | [Constructor](https://mikro-orm.io/api/core.md#Constructor)<[Type](https://mikro-orm.io/api/core/class/Type.md)\<any, any>> | () => unknown | ColumnType

Explicitly specify the runtime type.

* **@see**

  * <https://mikro-orm.io/docs/metadata-providers>
  * <https://mikro-orm.io/docs/custom-types>

### [**](#unique)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L219)optionalunique

**unique?

<!-- -->

: string | boolean

Set column as unique for Generator. (SQL only)

### [**](#unsigned)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L187)optionalunsigned

**unsigned?

<!-- -->

: boolean

Set column as unsigned for Generator. (SQL only)

### [**](#version)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L207)optionalversion

**version?

<!-- -->

: boolean

Set to true to enable Locking via version field. (SQL only)
