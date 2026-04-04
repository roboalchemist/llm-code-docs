# Source: https://mikro-orm.io/api/core/interface/ManyToOneOptions.md

# ManyToOneOptions<!-- --> \<Owner, Target>

### Hierarchy

* [ReferenceOptions](https://mikro-orm.io/api/core/interface/ReferenceOptions.md)\<Owner, Target>
  * *ManyToOneOptions*

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
* [**createForeignKeyConstraint](#createForeignKeyConstraint)
* [**customOrder](#customOrder)
* [**default](#default)
* [**defaultRaw](#defaultRaw)
* [**deferMode](#deferMode)
* [**deleteRule](#deleteRule)
* [**eager](#eager)
* [**entity](#entity)
* [**extra](#extra)
* [**fieldName](#fieldName)
* [**fieldNames](#fieldNames)
* [**filters](#filters)
* [**foreignKeyName](#foreignKeyName)
* [**formula](#formula)
* [**generated](#generated)
* [**getter](#getter)
* [**getterName](#getterName)
* [**groups](#groups)
* [**hidden](#hidden)
* [**hydrate](#hydrate)
* [**ignoreSchemaChanges](#ignoreSchemaChanges)
* [**index](#index)
* [**inversedBy](#inversedBy)
* [**joinColumn](#joinColumn)
* [**joinColumns](#joinColumns)
* [**lazy](#lazy)
* [**length](#length)
* [**mapToPk](#mapToPk)
* [**name](#name)
* [**nullable](#nullable)
* [**onCreate](#onCreate)
* [**onUpdate](#onUpdate)
* [**ownColumns](#ownColumns)
* [**persist](#persist)
* [**precision](#precision)
* [**primary](#primary)
* [**ref](#ref)
* [**referenceColumnName](#referenceColumnName)
* [**referencedColumnNames](#referencedColumnNames)
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
* [**updateRule](#updateRule)
* [**version](#version)

## Properties<!-- -->[**](#Properties)

### [**](#accessor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L290)optionalinheritedaccessor

**accessor?

<!-- -->

: boolean | keyof

<!-- -->

Owner

Inherited from ReferenceOptions.accessor

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

Inherited from ReferenceOptions.autoincrement

Explicitly specify the auto increment of the primary key.

### [**](#cascade)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L336)optionalinheritedcascade

**cascade?

<!-- -->

: [Cascade](https://mikro-orm.io/api/core/enum/Cascade.md)\[]

Inherited from ReferenceOptions.cascade

Set what actions on owning entity should be cascaded to the relationship. Defaults to \[Cascade.PERSIST, Cascade.MERGE] (see [cascading](https://mikro-orm.io/docs/cascading.md)).

### [**](#check)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L193)optionalinheritedcheck

**check?

<!-- -->

: string | [CheckCallback](https://mikro-orm.io/api/core.md#CheckCallback)\<Owner>

Inherited from ReferenceOptions.check

Specify column with check constraints. (Postgres driver only)

* **@see**

  <https://mikro-orm.io/docs/defining-entities#check-constraints>

### [**](#columnType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L75)optionalinheritedcolumnType

**columnType?

<!-- -->

: [AnyString](https://mikro-orm.io/api/core.md#AnyString) | ColumnType

Inherited from ReferenceOptions.columnType

Specify an exact database column type for Generator. This option is only for simple properties represented by a single column. (SQL only)

### [**](#columnTypes)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L79)optionalinheritedcolumnTypes

**columnTypes?

<!-- -->

: ([AnyString](https://mikro-orm.io/api/core.md#AnyString) | ColumnType)\[]

Inherited from ReferenceOptions.columnTypes

Specify an exact database column type for Generator. This option is suitable for composite keys, where one property is represented by multiple columns. (SQL only)

### [**](#comment)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L320)optionalinheritedcomment

**comment?

<!-- -->

: string

Inherited from ReferenceOptions.comment

Specify comment of column for Generator. (SQL only)

### [**](#concurrencyCheck)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L179)optionalinheritedconcurrencyCheck

**concurrencyCheck?

<!-- -->

: boolean

Inherited from ReferenceOptions.concurrencyCheck

Set to true to enable Locking via concurrency fields.

### [**](#createForeignKeyConstraint)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/ManyToOne.ts#L60)optionalcreateForeignKeyConstraint

**createForeignKeyConstraint?

<!-- -->

: boolean

Enable/disable foreign key constraint creation on this relation

### [**](#customOrder)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L316)optionalinheritedcustomOrder

**customOrder?

<!-- -->

: string\[] | number\[] | boolean\[]

Inherited from ReferenceOptions.customOrder

Specify a custom order based on the values. (SQL only)

### [**](#default)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L126)optionalinheriteddefault

**default?

<!-- -->

: null | string | number | boolean | string\[] | number\[]

Inherited from ReferenceOptions.default

Specify default column value for Generator. This is a runtime value, assignable to the entity property. (SQL only)

### [**](#defaultRaw)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L131)optionalinheriteddefaultRaw

**defaultRaw?

<!-- -->

: string

Inherited from ReferenceOptions.defaultRaw

Specify SQL functions for Generator. (SQL only) Since v4 you should use defaultRaw for SQL functions. e.g. now()

### [**](#deferMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/ManyToOne.ts#L57)optionaldeferMode

**deferMode?

<!-- -->

: [DeferMode](https://mikro-orm.io/api/core/enum/DeferMode.md) | immediate | deferred

Set the constraint type. Immediate constraints are checked for each statement, while deferred ones are only checked at the end of the transaction. Only for postgres unique constraints.

### [**](#deleteRule)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/ManyToOne.ts#L51)optionaldeleteRule

**deleteRule?

<!-- -->

: [AnyString](https://mikro-orm.io/api/core.md#AnyString) | cascade | no action | set null | set default

What to do when the target entity gets deleted.

### [**](#eager)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L339)optionalinheritedeager

**eager?

<!-- -->

: boolean

Inherited from ReferenceOptions.eager

Always load the relationship. Discouraged for use with to-many relations for performance reasons.

### [**](#entity)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L333)optionalinheritedentity

**entity?

<!-- -->

: string | () => [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<Target>

Inherited from ReferenceOptions.entity

Set target entity type.

### [**](#extra)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L322)optionalinheritedextra

**extra?

<!-- -->

: string

Inherited from ReferenceOptions.extra

mysql only

### [**](#fieldName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L64)optionalinheritedfieldName

**fieldName?

<!-- -->

: string

Inherited from ReferenceOptions.fieldName

Specify database column name for this property.

* **@see**

  <https://mikro-orm.io/docs/naming-strategy>

### [**](#fieldNames)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L71)optionalinheritedfieldNames

**fieldNames?

<!-- -->

: string\[]

Inherited from ReferenceOptions.fieldNames

Specify database column names for this property. Same as `fieldName` but for composite FKs.

* **@see**

  <https://mikro-orm.io/docs/naming-strategy>

### [**](#filters)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L345)optionalinheritedfilters

**filters?

<!-- -->

: [FilterOptions](https://mikro-orm.io/api/core.md#FilterOptions)

Inherited from ReferenceOptions.filters

Control filter parameters for the relation. This will serve as a default value when processing filters on this relation. It's value can be overridden via `em.fork()` or `FindOptions`.

### [**](#foreignKeyName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/ManyToOne.ts#L63)optionalforeignKeyName

**foreignKeyName?

<!-- -->

: string

Set a custom foreign key constraint name, overriding NamingStrategy.indexName().

### [**](#formula)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L137)optionalinheritedformula

**formula?

<!-- -->

: string | (alias) => string

Inherited from ReferenceOptions.formula

Set to map some SQL snippet for the entity.

* **@see**

  <https://mikro-orm.io/docs/defining-entities#formulas> Formulas

### [**](#generated)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L141)optionalinheritedgenerated

**generated?

<!-- -->

: string | GeneratedColumnCallback\<Owner>

Inherited from ReferenceOptions.generated

For generated columns. This will be appended to the column type after the `generated always` clause.

### [**](#getter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L230)optionalinheritedgetter

**getter?

<!-- -->

: boolean

Inherited from ReferenceOptions.getter

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

Inherited from ReferenceOptions.getterName

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

Inherited from ReferenceOptions.groups

Specify serialization groups for `serialize()` calls. If a property does not specify any group, it will be included, otherwise only properties with a matching group are included.

### [**](#hidden)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L171)optionalinheritedhidden

**hidden?

<!-- -->

: boolean

Inherited from ReferenceOptions.hidden

Set to true to omit the property when Serializing.

### [**](#hydrate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L157)optionalinheritedhydrate

**hydrate?

<!-- -->

: boolean

Inherited from ReferenceOptions.hydrate

Set false to disable hydration of this property. Useful for persisted getters.

### [**](#ignoreSchemaChanges)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L328)optionalinheritedignoreSchemaChanges

**ignoreSchemaChanges?

<!-- -->

: (type | extra | default)\[]

Inherited from ReferenceOptions.ignoreSchemaChanges

Set to avoid a perpetual diff from the Generator when columns are generated.

* **@see**

  <https://mikro-orm.io/docs/defining-entities#sql-generated-columns>

### [**](#index)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L183)optionalinheritedindex

**index?

<!-- -->

: string | boolean

Inherited from ReferenceOptions.index

Explicitly specify index on a property.

### [**](#inversedBy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/ManyToOne.ts#L24)optionalinversedBy

**inversedBy?

<!-- -->

: (string & keyof

<!-- -->

Target) | (e) => any

Point to the inverse side property name.

### [**](#joinColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/ManyToOne.ts#L36)optionaljoinColumn

**joinColumn?

<!-- -->

: string

Override the default database column name on the owning side (see [Naming Strategy](https://mikro-orm.io/docs/naming-strategy.md)). This option is only for simple properties represented by a single column.

### [**](#joinColumns)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/ManyToOne.ts#L39)optionaljoinColumns

**joinColumns?

<!-- -->

: string\[]

Override the default database column name on the owning side (see [Naming Strategy](https://mikro-orm.io/docs/naming-strategy.md)). This option is suitable for composite keys, where one property is represented by multiple columns.

### [**](#lazy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L199)optionalinheritedlazy

**lazy?

<!-- -->

: boolean

Inherited from ReferenceOptions.lazy

Set to omit the property from the select clause for lazy loading.

* **@see**

  <https://mikro-orm.io/docs/defining-entities#lazy-scalar-properties>

### [**](#length)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L95)optionalinheritedlength

**length?

<!-- -->

: number

Inherited from ReferenceOptions.length

Set length of database column, used for datetime/timestamp/varchar column types for Generator. (SQL only)

### [**](#mapToPk)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/ManyToOne.ts#L33)optionalmapToPk

**mapToPk?

<!-- -->

: boolean

Map this relation to the primary key value instead of an entity.

### [**](#name)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L58)optionalinheritedname

**name?

<!-- -->

: string

Inherited from ReferenceOptions.name

Alias for `fieldName`.

### [**](#nullable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L145)optionalinheritednullable

**nullable?

<!-- -->

: boolean

Inherited from ReferenceOptions.nullable

Set column as nullable for Generator.

### [**](#onCreate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L116)optionalinheritedonCreate

**onCreate?

<!-- -->

: (entity, em) => any

Inherited from ReferenceOptions.onCreate

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

Inherited from ReferenceOptions.onUpdate

Automatically update the property value every time entity gets updated, executed during flush operation.

***

#### Type declaration

* * **(entity, em): any

  - #### Parameters

    * ##### entity: Owner
    * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

    #### Returns any

### [**](#ownColumns)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/ManyToOne.ts#L42)optionalownColumns

**ownColumns?

<!-- -->

: string\[]

When a part of a composite column is shared in other properties, use this option to specify what columns are considered as owned by this property. This is useful when your composite property is nullable, but parts of it are not.

### [**](#persist)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L153)optionalinheritedpersist

**persist?

<!-- -->

: boolean

Inherited from ReferenceOptions.persist

Set false to define Property.

### [**](#precision)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L99)optionalinheritedprecision

**precision?

<!-- -->

: number

Inherited from ReferenceOptions.precision

Set precision of database column to represent the number of significant digits. (SQL only)

### [**](#primary)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/ManyToOne.ts#L30)optionalprimary

**primary?

<!-- -->

: boolean

Overrides ReferenceOptions.primary

Use this relation as a primary key.

### [**](#ref)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/ManyToOne.ts#L27)optionalref

**ref?

<!-- -->

: boolean

Overrides ReferenceOptions.ref

Wrap the entity in [Reference](https://mikro-orm.io/api/core/class/Reference.md) wrapper.

### [**](#referenceColumnName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/ManyToOne.ts#L45)optionalreferenceColumnName

**referenceColumnName?

<!-- -->

: string

Override the default database column name on the target entity (see [Naming Strategy](https://mikro-orm.io/docs/naming-strategy.md)). This option is only for simple properties represented by a single column.

### [**](#referencedColumnNames)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/ManyToOne.ts#L48)optionalreferencedColumnNames

**referencedColumnNames?

<!-- -->

: string\[]

Override the default database column name on the target entity (see [Naming Strategy](https://mikro-orm.io/docs/naming-strategy.md)). This option is suitable for composite keys, where one property is represented by multiple columns.

### [**](#returning)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L111)optionalinheritedreturning

**returning?

<!-- -->

: boolean

Inherited from ReferenceOptions.returning

Add the property to the `returning` statement.

### [**](#runtimeType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L91)optionalinheritedruntimeType

**runtimeType?

<!-- -->

: string

Inherited from ReferenceOptions.runtimeType

Runtime type of the property. This is the JS type that your property is mapped to, e.g. `string` or `number`, and is normally inferred automatically via `reflect-metadata`. In some cases, the inference won't work, and you might need to specify the `runtimeType` explicitly - the most common one is when you use a union type with null like `foo: number | null`.

### [**](#scale)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L103)optionalinheritedscale

**scale?

<!-- -->

: number

Inherited from ReferenceOptions.scale

Set scale of database column to represents the number of digits after the decimal point. (SQL only)

### [**](#serializedName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L307)optionalinheritedserializedName

**serializedName?

<!-- -->

: string

Inherited from ReferenceOptions.serializedName

Specify name of key for the serialized value.

### [**](#serializedPrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L297)optionalinheritedserializedPrimaryKey

**serializedPrimaryKey?

<!-- -->

: boolean

Inherited from ReferenceOptions.serializedPrimaryKey

Set to define serialized primary key for MongoDB. (virtual) Alias for `@SerializedPrimaryKey()` decorator.

* **@see**

  <https://mikro-orm.io/docs/decorators#serializedprimarykey>

### [**](#serializer)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L303)optionalinheritedserializer

**serializer?

<!-- -->

: (value, options) => any

Inherited from ReferenceOptions.serializer

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

Inherited from ReferenceOptions.setter

Set true to define the properties as setter. (virtual)

* **@example**

  ```
  @Property({ setter: true })
  set address(value: string) {
      this._address = value.toLocaleLowerCase();
  }
  ```

### [**](#strategy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L342)optionalinheritedstrategy

**strategy?

<!-- -->

: [LoadStrategy](https://mikro-orm.io/api/core/enum/LoadStrategy.md) | select-in | joined | balanced

Inherited from ReferenceOptions.strategy

Override the default loading strategy for this property. This option has precedence over the global `loadStrategy`, but can be overridden by `FindOptions.strategy`.

### [**](#trackChanges)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L167)optionalinheritedtrackChanges

**trackChanges?

<!-- -->

: boolean

Inherited from ReferenceOptions.trackChanges

Set false to disable change tracking on a property level.

* **@see**

  <https://mikro-orm.io/docs/unit-of-work#change-tracking-and-performance-considerations>

### [**](#type)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L86)optionalinheritedtype

**type?

<!-- -->

: string | Date | uint8array | array | enumArray | unknown | [AnyString](https://mikro-orm.io/api/core.md#AnyString) | [Type](https://mikro-orm.io/api/core/class/Type.md)\<any, any> | [Constructor](https://mikro-orm.io/api/core.md#Constructor)\<Partial\<any>> | ObjectId | [Constructor](https://mikro-orm.io/api/core.md#Constructor)<[Type](https://mikro-orm.io/api/core/class/Type.md)\<any, any>> | () => unknown | ColumnType

Inherited from ReferenceOptions.type

Explicitly specify the runtime type.

* **@see**

  * <https://mikro-orm.io/docs/metadata-providers>
  * <https://mikro-orm.io/docs/custom-types>

### [**](#unique)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L187)optionalinheritedunique

**unique?

<!-- -->

: string | boolean

Inherited from ReferenceOptions.unique

Set column as unique for Generator. (SQL only)

### [**](#unsigned)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L149)optionalinheritedunsigned

**unsigned?

<!-- -->

: boolean

Inherited from ReferenceOptions.unsigned

Set column as unsigned for Generator. (SQL only)

### [**](#updateRule)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/ManyToOne.ts#L54)optionalupdateRule

**updateRule?

<!-- -->

: [AnyString](https://mikro-orm.io/api/core.md#AnyString) | cascade | no action | set null | set default

What to do when the reference to the target entity gets updated.

### [**](#version)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L175)optionalinheritedversion

**version?

<!-- -->

: boolean

Inherited from ReferenceOptions.version

Set to true to enable Locking via version field. (SQL only)
