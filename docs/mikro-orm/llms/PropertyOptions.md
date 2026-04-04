# Source: https://mikro-orm.io/api/core/interface/PropertyOptions.md

# PropertyOptions<!-- --> \<Owner>

### Hierarchy

* *PropertyOptions*

  * [PrimaryKeyOptions](https://mikro-orm.io/api/core/interface/PrimaryKeyOptions.md)
  * [SerializedPrimaryKeyOptions](https://mikro-orm.io/api/core/interface/SerializedPrimaryKeyOptions.md)
  * [ReferenceOptions](https://mikro-orm.io/api/core/interface/ReferenceOptions.md)
  * [EnumOptions](https://mikro-orm.io/api/core/interface/EnumOptions.md)
  * [FormulaOptions](https://mikro-orm.io/api/core/interface/FormulaOptions.md)
  * [EmbeddedOptions](https://mikro-orm.io/api/core/interface/EmbeddedOptions.md)

## Index[**](#Index)

### Properties

* [**accessor](#accessor)
* [**autoincrement](#autoincrement)
* [**check](#check)
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
* [**trackChanges](#trackChanges)
* [**type](#type)
* [**unique](#unique)
* [**unsigned](#unsigned)
* [**version](#version)

## Properties<!-- -->[**](#Properties)

### [**](#accessor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L290)optionalaccessor

**accessor?

<!-- -->

: boolean | keyof

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

### [**](#autoincrement)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L107)optionalautoincrement

**autoincrement?

<!-- -->

: boolean

Explicitly specify the auto increment of the primary key.

### [**](#check)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L193)optionalcheck

**check?

<!-- -->

: string | [CheckCallback](https://mikro-orm.io/api/core.md#CheckCallback)\<Owner>

Specify column with check constraints. (Postgres driver only)

* **@see**

  <https://mikro-orm.io/docs/defining-entities#check-constraints>

### [**](#columnType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L75)optionalcolumnType

**columnType?

<!-- -->

: [AnyString](https://mikro-orm.io/api/core.md#AnyString) | ColumnType

Specify an exact database column type for Generator. This option is only for simple properties represented by a single column. (SQL only)

### [**](#columnTypes)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L79)optionalcolumnTypes

**columnTypes?

<!-- -->

: ([AnyString](https://mikro-orm.io/api/core.md#AnyString) | ColumnType)\[]

Specify an exact database column type for Generator. This option is suitable for composite keys, where one property is represented by multiple columns. (SQL only)

### [**](#comment)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L320)optionalcomment

**comment?

<!-- -->

: string

Specify comment of column for Generator. (SQL only)

### [**](#concurrencyCheck)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L179)optionalconcurrencyCheck

**concurrencyCheck?

<!-- -->

: boolean

Set to true to enable Locking via concurrency fields.

### [**](#customOrder)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L316)optionalcustomOrder

**customOrder?

<!-- -->

: string\[] | number\[] | boolean\[]

Specify a custom order based on the values. (SQL only)

### [**](#default)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L126)optionaldefault

**default?

<!-- -->

: null | string | number | boolean | string\[] | number\[]

Specify default column value for Generator. This is a runtime value, assignable to the entity property. (SQL only)

### [**](#defaultRaw)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L131)optionaldefaultRaw

**defaultRaw?

<!-- -->

: string

Specify SQL functions for Generator. (SQL only) Since v4 you should use defaultRaw for SQL functions. e.g. now()

### [**](#extra)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L322)optionalextra

**extra?

<!-- -->

: string

mysql only

### [**](#fieldName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L64)optionalfieldName

**fieldName?

<!-- -->

: string

Specify database column name for this property.

* **@see**

  <https://mikro-orm.io/docs/naming-strategy>

### [**](#fieldNames)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L71)optionalfieldNames

**fieldNames?

<!-- -->

: string\[]

Specify database column names for this property. Same as `fieldName` but for composite FKs.

* **@see**

  <https://mikro-orm.io/docs/naming-strategy>

### [**](#formula)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L137)optionalformula

**formula?

<!-- -->

: string | (alias) => string

Set to map some SQL snippet for the entity.

* **@see**

  <https://mikro-orm.io/docs/defining-entities#formulas> Formulas

### [**](#generated)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L141)optionalgenerated

**generated?

<!-- -->

: string | GeneratedColumnCallback\<Owner>

For generated columns. This will be appended to the column type after the `generated always` clause.

### [**](#getter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L230)optionalgetter

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

### [**](#getterName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L243)optionalgetterName

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

### [**](#groups)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L312)optionalgroups

**groups?

<!-- -->

: string\[]

Specify serialization groups for `serialize()` calls. If a property does not specify any group, it will be included, otherwise only properties with a matching group are included.

### [**](#hidden)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L171)optionalhidden

**hidden?

<!-- -->

: boolean

Set to true to omit the property when Serializing.

### [**](#hydrate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L157)optionalhydrate

**hydrate?

<!-- -->

: boolean

Set false to disable hydration of this property. Useful for persisted getters.

### [**](#ignoreSchemaChanges)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L328)optionalignoreSchemaChanges

**ignoreSchemaChanges?

<!-- -->

: (type | extra | default)\[]

Set to avoid a perpetual diff from the Generator when columns are generated.

* **@see**

  <https://mikro-orm.io/docs/defining-entities#sql-generated-columns>

### [**](#index)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L183)optionalindex

**index?

<!-- -->

: string | boolean

Explicitly specify index on a property.

### [**](#lazy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L199)optionallazy

**lazy?

<!-- -->

: boolean

Set to omit the property from the select clause for lazy loading.

* **@see**

  <https://mikro-orm.io/docs/defining-entities#lazy-scalar-properties>

### [**](#length)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L95)optionallength

**length?

<!-- -->

: number

Set length of database column, used for datetime/timestamp/varchar column types for Generator. (SQL only)

### [**](#name)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L58)optionalname

**name?

<!-- -->

: string

Alias for `fieldName`.

### [**](#nullable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L145)optionalnullable

**nullable?

<!-- -->

: boolean

Set column as nullable for Generator.

### [**](#onCreate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L116)optionalonCreate

**onCreate?

<!-- -->

: (entity, em) => any

Automatically set the property value when entity gets created, executed during flush operation.

***

#### Type declaration

* * **(entity, em): any

  - #### Parameters

    * ##### entity: Owner
    * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

    #### Returns any

### [**](#onUpdate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L121)optionalonUpdate

**onUpdate?

<!-- -->

: (entity, em) => any

Automatically update the property value every time entity gets updated, executed during flush operation.

***

#### Type declaration

* * **(entity, em): any

  - #### Parameters

    * ##### entity: Owner
    * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

    #### Returns any

### [**](#persist)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L153)optionalpersist

**persist?

<!-- -->

: boolean

Set false to define Property.

### [**](#precision)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L99)optionalprecision

**precision?

<!-- -->

: number

Set precision of database column to represent the number of significant digits. (SQL only)

### [**](#primary)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L206)optionalprimary

**primary?

<!-- -->

: boolean

Set true to define entity's unique primary key identifier. Alias for `@PrimaryKey()` decorator

* **@see**

  <https://mikro-orm.io/docs/decorators#primarykey>

### [**](#ref)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L161)optionalref

**ref?

<!-- -->

: boolean

Enable `ScalarReference` wrapper for lazy values. Use this in combination with `lazy: true` to have a type-safe accessor object in place of the value.

### [**](#returning)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L111)optionalreturning

**returning?

<!-- -->

: boolean

Add the property to the `returning` statement.

### [**](#runtimeType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L91)optionalruntimeType

**runtimeType?

<!-- -->

: string

Runtime type of the property. This is the JS type that your property is mapped to, e.g. `string` or `number`, and is normally inferred automatically via `reflect-metadata`. In some cases, the inference won't work, and you might need to specify the `runtimeType` explicitly - the most common one is when you use a union type with null like `foo: number | null`.

### [**](#scale)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L103)optionalscale

**scale?

<!-- -->

: number

Set scale of database column to represents the number of digits after the decimal point. (SQL only)

### [**](#serializedName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L307)optionalserializedName

**serializedName?

<!-- -->

: string

Specify name of key for the serialized value.

### [**](#serializedPrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L297)optionalserializedPrimaryKey

**serializedPrimaryKey?

<!-- -->

: boolean

Set to define serialized primary key for MongoDB. (virtual) Alias for `@SerializedPrimaryKey()` decorator.

* **@see**

  <https://mikro-orm.io/docs/decorators#serializedprimarykey>

### [**](#serializer)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L303)optionalserializer

**serializer?

<!-- -->

: (value, options) => any

Set to use serialize property. Allow to specify a callback that will be used when serializing a property.

* **@see**

  <https://mikro-orm.io/docs/serializing#property-serializers>

***

#### Type declaration

* * **(value, options): any

  - #### Parameters

    * ##### value: any
    * ##### optionaloptions: [SerializeOptions](https://mikro-orm.io/api/core/interface/SerializeOptions.md)\<any, never, never>

    #### Returns any

### [**](#setter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L218)optionalsetter

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

### [**](#trackChanges)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L167)optionaltrackChanges

**trackChanges?

<!-- -->

: boolean

Set false to disable change tracking on a property level.

* **@see**

  <https://mikro-orm.io/docs/unit-of-work#change-tracking-and-performance-considerations>

### [**](#type)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L86)optionaltype

**type?

<!-- -->

: string | Date | uint8array | array | enumArray | unknown | [AnyString](https://mikro-orm.io/api/core.md#AnyString) | [Type](https://mikro-orm.io/api/core/class/Type.md)\<any, any> | [Constructor](https://mikro-orm.io/api/core.md#Constructor)\<Partial\<any>> | ObjectId | [Constructor](https://mikro-orm.io/api/core.md#Constructor)<[Type](https://mikro-orm.io/api/core/class/Type.md)\<any, any>> | () => unknown | ColumnType

Explicitly specify the runtime type.

* **@see**

  * <https://mikro-orm.io/docs/metadata-providers>
  * <https://mikro-orm.io/docs/custom-types>

### [**](#unique)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L187)optionalunique

**unique?

<!-- -->

: string | boolean

Set column as unique for Generator. (SQL only)

### [**](#unsigned)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L149)optionalunsigned

**unsigned?

<!-- -->

: boolean

Set column as unsigned for Generator. (SQL only)

### [**](#version)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L175)optionalversion

**version?

<!-- -->

: boolean

Set to true to enable Locking via version field. (SQL only)
