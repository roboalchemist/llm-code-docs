# Source: https://mikro-orm.io/api/core/interface/ReferenceOptions.md

# ReferenceOptions<!-- --> \<Owner, Target>

### Hierarchy

* [PropertyOptions](https://mikro-orm.io/api/core/interface/PropertyOptions.md)\<Owner>

  * *ReferenceOptions*

    * [OneToManyOptions](https://mikro-orm.io/api/core/interface/OneToManyOptions.md)
    * [ManyToOneOptions](https://mikro-orm.io/api/core/interface/ManyToOneOptions.md)
    * [ManyToManyOptions](https://mikro-orm.io/api/core/interface/ManyToManyOptions.md)

## Index[**](#Index)

### Properties

* [**accessor](#accessor)
* [**autoincrement](#autoincrement)
* [**cascade](#cascade)
* [**check](#check)
* [**columnType](#columnType)
* [**columnTypes](#columnTypes)
* [**comment](#comment)
* [**concurrencyCheck](#concurrencyCheck)
* [**customOrder](#customOrder)
* [**default](#default)
* [**defaultRaw](#defaultRaw)
* [**eager](#eager)
* [**entity](#entity)
* [**extra](#extra)
* [**fieldName](#fieldName)
* [**fieldNames](#fieldNames)
* [**filters](#filters)
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
* [**strategy](#strategy)
* [**trackChanges](#trackChanges)
* [**type](#type)
* [**unique](#unique)
* [**unsigned](#unsigned)
* [**version](#version)

## Properties<!-- -->[**](#Properties)

### [**](#accessor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L290)optionalinheritedaccessor

**accessor?

<!-- -->

: boolean | keyof

<!-- -->

Owner

Inherited from PropertyOptions.accessor

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

### [**](#autoincrement)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L107)optionalinheritedautoincrement

**autoincrement?

<!-- -->

: boolean

Inherited from PropertyOptions.autoincrement

Explicitly specify the auto increment of the primary key.

### [**](#cascade)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L336)optionalcascade

**cascade?

<!-- -->

: [Cascade](https://mikro-orm.io/api/core/enum/Cascade.md)\[]

Set what actions on owning entity should be cascaded to the relationship. Defaults to \[Cascade.PERSIST, Cascade.MERGE] (see [cascading](https://mikro-orm.io/docs/cascading.md)).

### [**](#check)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L193)optionalinheritedcheck

**check?

<!-- -->

: string | [CheckCallback](https://mikro-orm.io/api/core.md#CheckCallback)\<Owner>

Inherited from PropertyOptions.check

Specify column with check constraints. (Postgres driver only)

* **@see**

  <https://mikro-orm.io/docs/defining-entities#check-constraints>

### [**](#columnType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L75)optionalinheritedcolumnType

**columnType?

<!-- -->

: [AnyString](https://mikro-orm.io/api/core.md#AnyString) | ColumnType

Inherited from PropertyOptions.columnType

Specify an exact database column type for Generator. This option is only for simple properties represented by a single column. (SQL only)

### [**](#columnTypes)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L79)optionalinheritedcolumnTypes

**columnTypes?

<!-- -->

: ([AnyString](https://mikro-orm.io/api/core.md#AnyString) | ColumnType)\[]

Inherited from PropertyOptions.columnTypes

Specify an exact database column type for Generator. This option is suitable for composite keys, where one property is represented by multiple columns. (SQL only)

### [**](#comment)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L320)optionalinheritedcomment

**comment?

<!-- -->

: string

Inherited from PropertyOptions.comment

Specify comment of column for Generator. (SQL only)

### [**](#concurrencyCheck)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L179)optionalinheritedconcurrencyCheck

**concurrencyCheck?

<!-- -->

: boolean

Inherited from PropertyOptions.concurrencyCheck

Set to true to enable Locking via concurrency fields.

### [**](#customOrder)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L316)optionalinheritedcustomOrder

**customOrder?

<!-- -->

: string\[] | number\[] | boolean\[]

Inherited from PropertyOptions.customOrder

Specify a custom order based on the values. (SQL only)

### [**](#default)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L126)optionalinheriteddefault

**default?

<!-- -->

: null | string | number | boolean | string\[] | number\[]

Inherited from PropertyOptions.default

Specify default column value for Generator. This is a runtime value, assignable to the entity property. (SQL only)

### [**](#defaultRaw)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L131)optionalinheriteddefaultRaw

**defaultRaw?

<!-- -->

: string

Inherited from PropertyOptions.defaultRaw

Specify SQL functions for Generator. (SQL only) Since v4 you should use defaultRaw for SQL functions. e.g. now()

### [**](#eager)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L339)optionaleager

**eager?

<!-- -->

: boolean

Always load the relationship. Discouraged for use with to-many relations for performance reasons.

### [**](#entity)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L333)optionalentity

**entity?

<!-- -->

: string | () => [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<Target>

Set target entity type.

### [**](#extra)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L322)optionalinheritedextra

**extra?

<!-- -->

: string

Inherited from PropertyOptions.extra

mysql only

### [**](#fieldName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L64)optionalinheritedfieldName

**fieldName?

<!-- -->

: string

Inherited from PropertyOptions.fieldName

Specify database column name for this property.

* **@see**

  <https://mikro-orm.io/docs/naming-strategy>

### [**](#fieldNames)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L71)optionalinheritedfieldNames

**fieldNames?

<!-- -->

: string\[]

Inherited from PropertyOptions.fieldNames

Specify database column names for this property. Same as `fieldName` but for composite FKs.

* **@see**

  <https://mikro-orm.io/docs/naming-strategy>

### [**](#filters)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L345)optionalfilters

**filters?

<!-- -->

: [FilterOptions](https://mikro-orm.io/api/core.md#FilterOptions)

Control filter parameters for the relation. This will serve as a default value when processing filters on this relation. It's value can be overridden via `em.fork()` or `FindOptions`.

### [**](#formula)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L137)optionalinheritedformula

**formula?

<!-- -->

: string | (alias) => string

Inherited from PropertyOptions.formula

Set to map some SQL snippet for the entity.

* **@see**

  <https://mikro-orm.io/docs/defining-entities#formulas> Formulas

### [**](#generated)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L141)optionalinheritedgenerated

**generated?

<!-- -->

: string | GeneratedColumnCallback\<Owner>

Inherited from PropertyOptions.generated

For generated columns. This will be appended to the column type after the `generated always` clause.

### [**](#getter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L230)optionalinheritedgetter

**getter?

<!-- -->

: boolean

Inherited from PropertyOptions.getter

Set true to define the properties as getter. (virtual)

* **@example**

  ```
  @Property({ getter: true })
  get fullName() {
    return this.firstName + this.lastName;
  }
  ```

### [**](#getterName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L243)optionalinheritedgetterName

**getterName?

<!-- -->

: keyof

<!-- -->

Owner

Inherited from PropertyOptions.getterName

When defining a property over a method (not a getter, a regular function), you can use this option to point to the method name.

* **@example**

  ```
  @Property({ getter: true })
  getFullName() {
    return this.firstName + this.lastName;
  }
  ```

### [**](#groups)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L312)optionalinheritedgroups

**groups?

<!-- -->

: string\[]

Inherited from PropertyOptions.groups

Specify serialization groups for `serialize()` calls. If a property does not specify any group, it will be included, otherwise only properties with a matching group are included.

### [**](#hidden)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L171)optionalinheritedhidden

**hidden?

<!-- -->

: boolean

Inherited from PropertyOptions.hidden

Set to true to omit the property when Serializing.

### [**](#hydrate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L157)optionalinheritedhydrate

**hydrate?

<!-- -->

: boolean

Inherited from PropertyOptions.hydrate

Set false to disable hydration of this property. Useful for persisted getters.

### [**](#ignoreSchemaChanges)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L328)optionalinheritedignoreSchemaChanges

**ignoreSchemaChanges?

<!-- -->

: (type | extra | default)\[]

Inherited from PropertyOptions.ignoreSchemaChanges

Set to avoid a perpetual diff from the Generator when columns are generated.

* **@see**

  <https://mikro-orm.io/docs/defining-entities#sql-generated-columns>

### [**](#index)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L183)optionalinheritedindex

**index?

<!-- -->

: string | boolean

Inherited from PropertyOptions.index

Explicitly specify index on a property.

### [**](#lazy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L199)optionalinheritedlazy

**lazy?

<!-- -->

: boolean

Inherited from PropertyOptions.lazy

Set to omit the property from the select clause for lazy loading.

* **@see**

  <https://mikro-orm.io/docs/defining-entities#lazy-scalar-properties>

### [**](#length)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L95)optionalinheritedlength

**length?

<!-- -->

: number

Inherited from PropertyOptions.length

Set length of database column, used for datetime/timestamp/varchar column types for Generator. (SQL only)

### [**](#name)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L58)optionalinheritedname

**name?

<!-- -->

: string

Inherited from PropertyOptions.name

Alias for `fieldName`.

### [**](#nullable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L145)optionalinheritednullable

**nullable?

<!-- -->

: boolean

Inherited from PropertyOptions.nullable

Set column as nullable for Generator.

### [**](#onCreate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L116)optionalinheritedonCreate

**onCreate?

<!-- -->

: (entity, em) => any

Inherited from PropertyOptions.onCreate

Automatically set the property value when entity gets created, executed during flush operation.

***

#### Type declaration

* * **(entity, em): any

  - #### Parameters

    * ##### entity: Owner
    * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

    #### Returns any

### [**](#onUpdate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L121)optionalinheritedonUpdate

**onUpdate?

<!-- -->

: (entity, em) => any

Inherited from PropertyOptions.onUpdate

Automatically update the property value every time entity gets updated, executed during flush operation.

***

#### Type declaration

* * **(entity, em): any

  - #### Parameters

    * ##### entity: Owner
    * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

    #### Returns any

### [**](#persist)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L153)optionalinheritedpersist

**persist?

<!-- -->

: boolean

Inherited from PropertyOptions.persist

Set false to define Property.

### [**](#precision)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L99)optionalinheritedprecision

**precision?

<!-- -->

: number

Inherited from PropertyOptions.precision

Set precision of database column to represent the number of significant digits. (SQL only)

### [**](#primary)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L206)optionalinheritedprimary

**primary?

<!-- -->

: boolean

Inherited from PropertyOptions.primary

Set true to define entity's unique primary key identifier. Alias for `@PrimaryKey()` decorator

* **@see**

  <https://mikro-orm.io/docs/decorators#primarykey>

### [**](#ref)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L161)optionalinheritedref

**ref?

<!-- -->

: boolean

Inherited from PropertyOptions.ref

Enable `ScalarReference` wrapper for lazy values. Use this in combination with `lazy: true` to have a type-safe accessor object in place of the value.

### [**](#returning)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L111)optionalinheritedreturning

**returning?

<!-- -->

: boolean

Inherited from PropertyOptions.returning

Add the property to the `returning` statement.

### [**](#runtimeType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L91)optionalinheritedruntimeType

**runtimeType?

<!-- -->

: string

Inherited from PropertyOptions.runtimeType

Runtime type of the property. This is the JS type that your property is mapped to, e.g. `string` or `number`, and is normally inferred automatically via `reflect-metadata`. In some cases, the inference won't work, and you might need to specify the `runtimeType` explicitly - the most common one is when you use a union type with null like `foo: number | null`.

### [**](#scale)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L103)optionalinheritedscale

**scale?

<!-- -->

: number

Inherited from PropertyOptions.scale

Set scale of database column to represents the number of digits after the decimal point. (SQL only)

### [**](#serializedName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L307)optionalinheritedserializedName

**serializedName?

<!-- -->

: string

Inherited from PropertyOptions.serializedName

Specify name of key for the serialized value.

### [**](#serializedPrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L297)optionalinheritedserializedPrimaryKey

**serializedPrimaryKey?

<!-- -->

: boolean

Inherited from PropertyOptions.serializedPrimaryKey

Set to define serialized primary key for MongoDB. (virtual) Alias for `@SerializedPrimaryKey()` decorator.

* **@see**

  <https://mikro-orm.io/docs/decorators#serializedprimarykey>

### [**](#serializer)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L303)optionalinheritedserializer

**serializer?

<!-- -->

: (value, options) => any

Inherited from PropertyOptions.serializer

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

### [**](#setter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L218)optionalinheritedsetter

**setter?

<!-- -->

: boolean

Inherited from PropertyOptions.setter

Set true to define the properties as setter. (virtual)

* **@example**

  ```
  @Property({ setter: true })
  set address(value: string) {
      this._address = value.toLocaleLowerCase();
  }
  ```

### [**](#strategy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L342)optionalstrategy

**strategy?

<!-- -->

: [LoadStrategy](https://mikro-orm.io/api/core/enum/LoadStrategy.md) | select-in | joined | balanced

Override the default loading strategy for this property. This option has precedence over the global `loadStrategy`, but can be overridden by `FindOptions.strategy`.

### [**](#trackChanges)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L167)optionalinheritedtrackChanges

**trackChanges?

<!-- -->

: boolean

Inherited from PropertyOptions.trackChanges

Set false to disable change tracking on a property level.

* **@see**

  <https://mikro-orm.io/docs/unit-of-work#change-tracking-and-performance-considerations>

### [**](#type)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L86)optionalinheritedtype

**type?

<!-- -->

: string | Date | uint8array | array | enumArray | unknown | [AnyString](https://mikro-orm.io/api/core.md#AnyString) | [Type](https://mikro-orm.io/api/core/class/Type.md)\<any, any> | [Constructor](https://mikro-orm.io/api/core.md#Constructor)\<Partial\<any>> | ObjectId | [Constructor](https://mikro-orm.io/api/core.md#Constructor)<[Type](https://mikro-orm.io/api/core/class/Type.md)\<any, any>> | () => unknown | ColumnType

Inherited from PropertyOptions.type

Explicitly specify the runtime type.

* **@see**

  * <https://mikro-orm.io/docs/metadata-providers>
  * <https://mikro-orm.io/docs/custom-types>

### [**](#unique)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L187)optionalinheritedunique

**unique?

<!-- -->

: string | boolean

Inherited from PropertyOptions.unique

Set column as unique for Generator. (SQL only)

### [**](#unsigned)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L149)optionalinheritedunsigned

**unsigned?

<!-- -->

: boolean

Inherited from PropertyOptions.unsigned

Set column as unsigned for Generator. (SQL only)

### [**](#version)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L175)optionalinheritedversion

**version?

<!-- -->

: boolean

Inherited from PropertyOptions.version

Set to true to enable Locking via version field. (SQL only)
