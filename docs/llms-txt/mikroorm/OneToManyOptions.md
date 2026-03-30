# Source: https://mikro-orm.io/api/core/interface/OneToManyOptions.md

# OneToManyOptions<!-- --> \<Owner, Target>

### Hierarchy

* [ReferenceOptions](https://mikro-orm.io/api/core/interface/ReferenceOptions.md)\<Owner, Target>
  * *OneToManyOptions*

## Index[**](#index)

### Properties

* [**accessor](#accessor)
* [**autoincrement](#autoincrement)
* [**cascade](#cascade)
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
* [**check](#check)
* [**ignoreSchemaChanges](#ignoreSchemaChanges)
* [**index](#index)
* [**inverseJoinColumn](#inverseJoinColumn)
* [**inverseJoinColumns](#inverseJoinColumns)
* [**joinColumn](#joinColumn)
* [**joinColumns](#joinColumns)
* [**lazy](#lazy)
* [**length](#length)
* [**mappedBy](#mappedby)
* [**name](#name)
* [**nullable](#nullable)
* [**onCreate](#onCreate)
* [**onUpdate](#onUpdate)
* [**orderBy](#orderBy)
* [**orphanRemoval](#orphanRemoval)
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
* [**type](#type)
* [**unique](#unique)
* [**unsigned](#unsigned)
* [**version](#version)
* [**where](#where)

## Properties<!-- -->[**](#properties)

### [**](#accessor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L322)optionalinheritedaccessor

**accessor?

<!-- -->

: boolean | [AnyString](https://mikro-orm.io/api/core.md#AnyString) | keyof

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

### [**](#autoincrement)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L145)optionalinheritedautoincrement

**autoincrement?

<!-- -->

: boolean

Inherited from ReferenceOptions.autoincrement

Explicitly specify the auto increment of the primary key.

### [**](#cascade)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L368)optionalinheritedcascade

**cascade?

<!-- -->

: [Cascade](https://mikro-orm.io/api/core/enum/Cascade.md)\[]

Inherited from ReferenceOptions.cascade

Set what actions on owning entity should be cascaded to the relationship. Defaults to \[Cascade.PERSIST, Cascade.MERGE] (see [cascading](https://mikro-orm.io/docs/cascading.md)).

### [**](#columnType)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L104)optionalinheritedcolumnType

**columnType?

<!-- -->

: [AnyString](https://mikro-orm.io/api/core.md#AnyString) | ColumnType

Inherited from ReferenceOptions.columnType

Specify an exact database column type for Generator. This option is only for simple properties represented by a single column. (SQL only)

### [**](#columnTypes)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L108)optionalinheritedcolumnTypes

**columnTypes?

<!-- -->

: ([AnyString](https://mikro-orm.io/api/core.md#AnyString) | ColumnType)\[]

Inherited from ReferenceOptions.columnTypes

Specify an exact database column type for Generator. This option is suitable for composite keys, where one property is represented by multiple columns. (SQL only)

### [**](#comment)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L352)optionalinheritedcomment

**comment?

<!-- -->

: string

Inherited from ReferenceOptions.comment

Specify comment of column for Generator. (SQL only)

### [**](#concurrencyCheck)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L211)optionalinheritedconcurrencyCheck

**concurrencyCheck?

<!-- -->

: boolean

Inherited from ReferenceOptions.concurrencyCheck

Set to true to enable Locking via concurrency fields.

### [**](#customOrder)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L348)optionalinheritedcustomOrder

**customOrder?

<!-- -->

: string\[] | number\[] | boolean\[]

Inherited from ReferenceOptions.customOrder

Specify a custom order based on the values. (SQL only)

### [**](#default)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L164)optionalinheriteddefault

**default?

<!-- -->

: null | string | number | boolean | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | Date | string\[] | number\[]

Inherited from ReferenceOptions.default

Specify default column value for Generator. This is a runtime value, assignable to the entity property. (SQL only)

### [**](#defaultRaw)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L169)optionalinheriteddefaultRaw

**defaultRaw?

<!-- -->

: string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

Inherited from ReferenceOptions.defaultRaw

Specify SQL functions for Generator. (SQL only) Since v4 you should use defaultRaw for SQL functions. e.g. now()

### [**](#eager)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L371)optionalinheritedeager

**eager?

<!-- -->

: boolean

Inherited from ReferenceOptions.eager

Always load the relationship. Discouraged for use with to-many relations for performance reasons.

### [**](#entity)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L365)optionalinheritedentity

**entity?

<!-- -->

: () => [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<Target> | [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<Target>\[]

Inherited from ReferenceOptions.entity

Set target entity type. For polymorphic relations, pass an array of entity types.

***

#### Type declaration

* * **(): [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<Target> | [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<Target>\[]

  * #### Returns [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<Target> | [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<Target>\[]

### [**](#extra)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L354)optionalinheritedextra

**extra?

<!-- -->

: string

Inherited from ReferenceOptions.extra

mysql only

### [**](#fieldName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L93)optionalinheritedfieldName

**fieldName?

<!-- -->

: string

Inherited from ReferenceOptions.fieldName

Specify database column name for this property.

* **@see**

  <https://mikro-orm.io/docs/naming-strategy>

### [**](#fieldNames)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L100)optionalinheritedfieldNames

**fieldNames?

<!-- -->

: string\[]

Inherited from ReferenceOptions.fieldNames

Specify database column names for this property. Same as `fieldName` but for composite FKs.

* **@see**

  <https://mikro-orm.io/docs/naming-strategy>

### [**](#filters)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L377)optionalinheritedfilters

**filters?

<!-- -->

: [FilterOptions](https://mikro-orm.io/api/core.md#FilterOptions)

Inherited from ReferenceOptions.filters

Control filter parameters for the relation. This will serve as a default value when processing filters on this relation. It's value can be overridden via `em.fork()` or `FindOptions`.

### [**](#formula)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L175)optionalinheritedformula

**formula?

<!-- -->

: string | [FormulaCallback](https://mikro-orm.io/api/core.md#FormulaCallback)\<Owner>

Inherited from ReferenceOptions.formula

Set to map some SQL snippet for the entity.

* **@see**

  <https://mikro-orm.io/docs/defining-entities#formulas> Formulas

### [**](#generated)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L179)optionalinheritedgenerated

**generated?

<!-- -->

: string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | [GeneratedColumnCallback](https://mikro-orm.io/api/core.md#GeneratedColumnCallback)\<Owner>

Inherited from ReferenceOptions.generated

For generated columns. This will be appended to the column type after the `generated always` clause.

### [**](#getter)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L262)optionalinheritedgetter

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

### [**](#getterName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L275)optionalinheritedgetterName

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

### [**](#groups)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L344)optionalinheritedgroups

**groups?

<!-- -->

: string\[]

Inherited from ReferenceOptions.groups

Specify serialization groups for `serialize()` calls. If a property does not specify any group, it will be included, otherwise only properties with a matching group are included.

### [**](#hidden)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L203)optionalinheritedhidden

**hidden?

<!-- -->

: boolean

Inherited from ReferenceOptions.hidden

Set to true to omit the property when Serializing.

### [**](#hydrate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L195)optionalinheritedhydrate

**hydrate?

<!-- -->

: boolean

Inherited from ReferenceOptions.hydrate

Set false to disable hydration of this property. Useful for persisted getters.

### [**](#check)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L225)optionalinheritedcheck

**check?

<!-- -->

: string | [CheckCallback](https://mikro-orm.io/api/core.md#CheckCallback)\<Owner>

Inherited from ReferenceOptions.check

Specify column with check constraints. (Postgres driver only)

* **@see**

  <https://mikro-orm.io/docs/defining-entities#check-constraints>

### [**](#ignoreSchemaChanges)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L360)optionalinheritedignoreSchemaChanges

**ignoreSchemaChanges?

<!-- -->

: (type | extra | default)\[]

Inherited from ReferenceOptions.ignoreSchemaChanges

Set to avoid a perpetual diff from the Generator when columns are generated.

* **@see**

  <https://mikro-orm.io/docs/defining-entities#sql-generated-columns>

### [**](#index)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L215)optionalinheritedindex

**index?

<!-- -->

: string | boolean

Inherited from ReferenceOptions.index

Explicitly specify index on a property.

### [**](#inverseJoinColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L521)optionalinverseJoinColumn

**inverseJoinColumn?

<!-- -->

: string

Override the default database column name on the inverse side (see [Naming Strategy](https://mikro-orm.io/docs/naming-strategy.md)). This option is only for simple properties represented by a single column.

### [**](#inverseJoinColumns)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L524)optionalinverseJoinColumns

**inverseJoinColumns?

<!-- -->

: string\[]

Override the default database column name on the inverse side (see [Naming Strategy](https://mikro-orm.io/docs/naming-strategy.md)). This option is suitable for composite keys, where one property is represented by multiple columns.

### [**](#joinColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L515)optionaljoinColumn

**joinColumn?

<!-- -->

: string

Override the default database column name on the owning side (see [Naming Strategy](https://mikro-orm.io/docs/naming-strategy.md)). This option is only for simple properties represented by a single column.

### [**](#joinColumns)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L518)optionaljoinColumns

**joinColumns?

<!-- -->

: string\[]

Override the default database column name on the owning side (see [Naming Strategy](https://mikro-orm.io/docs/naming-strategy.md)). This option is suitable for composite keys, where one property is represented by multiple columns.

### [**](#lazy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L231)optionalinheritedlazy

**lazy?

<!-- -->

: boolean

Inherited from ReferenceOptions.lazy

Set to omit the property from the select clause for lazy loading.

* **@see**

  <https://mikro-orm.io/docs/defining-entities#lazy-scalar-properties>

### [**](#length)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L133)optionalinheritedlength

**length?

<!-- -->

: number

Inherited from ReferenceOptions.length

Set length of database column, used for datetime/timestamp/varchar column types for Generator. (SQL only)

### [**](#mappedby)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L533)mappedBy

**mappedBy: (string & keyof

<!-- -->

Target) | (e) => any

Point to the owning side property name.

### [**](#name)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L87)optionalinheritedname

**name?

<!-- -->

: string

Inherited from ReferenceOptions.name

Alias for `fieldName`.

### [**](#nullable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L183)optionalinheritednullable

**nullable?

<!-- -->

: boolean

Inherited from ReferenceOptions.nullable

Set column as nullable for Generator.

### [**](#onCreate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L154)optionalinheritedonCreate

**onCreate?

<!-- -->

: (entity, em) => any

Inherited from ReferenceOptions.onCreate

Automatically set the property value when entity gets created, executed during flush operation.

***

#### Type declaration

* * **(entity, em): any

  * #### Parameters

    * ##### entity: Owner

    * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

    #### Returns any

### [**](#onUpdate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L159)optionalinheritedonUpdate

**onUpdate?

<!-- -->

: (entity, em) => any

Inherited from ReferenceOptions.onUpdate

Automatically update the property value every time entity gets updated, executed during flush operation.

***

#### Type declaration

* * **(entity, em): any

  * #### Parameters

    * ##### entity: Owner

    * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

    #### Returns any

### [**](#orderBy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L509)optionalorderBy

**orderBy?

<!-- -->

: [QueryOrderMap](https://mikro-orm.io/api/core.md#QueryOrderMap)\<Target> | [QueryOrderMap](https://mikro-orm.io/api/core.md#QueryOrderMap)\<Target>\[]

Set default ordering.

### [**](#orphanRemoval)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L506)optionalorphanRemoval

**orphanRemoval?

<!-- -->

: boolean

Remove the entity when it gets disconnected from the relationship (see [Cascading](https://mikro-orm.io/docs/cascading.md)).

### [**](#persist)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L191)optionalinheritedpersist

**persist?

<!-- -->

: boolean

Inherited from ReferenceOptions.persist

Set false to define Property.

### [**](#precision)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L137)optionalinheritedprecision

**precision?

<!-- -->

: number

Inherited from ReferenceOptions.precision

Set precision of database column to represent the number of significant digits. (SQL only)

### [**](#primary)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L238)optionalinheritedprimary

**primary?

<!-- -->

: boolean

Inherited from ReferenceOptions.primary

Set true to define entity's unique primary key identifier. Alias for `@PrimaryKey()` decorator

* **@see**

  <https://mikro-orm.io/docs/decorators#primarykey>

### [**](#ref)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L199)optionalinheritedref

**ref?

<!-- -->

: boolean

Inherited from ReferenceOptions.ref

Enable `ScalarReference` wrapper for lazy values. Use this in combination with `lazy: true` to have a type-safe accessor object in place of the value.

### [**](#referenceColumnName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L527)optionalreferenceColumnName

**referenceColumnName?

<!-- -->

: string

Override the default database column name on the target entity (see [Naming Strategy](https://mikro-orm.io/docs/naming-strategy.md)). This option is only for simple properties represented by a single column.

### [**](#referencedColumnNames)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L530)optionalreferencedColumnNames

**referencedColumnNames?

<!-- -->

: string\[]

Override the default database column name on the target entity (see [Naming Strategy](https://mikro-orm.io/docs/naming-strategy.md)). This option is suitable for composite keys, where one property is represented by multiple columns.

### [**](#returning)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L149)optionalinheritedreturning

**returning?

<!-- -->

: boolean

Inherited from ReferenceOptions.returning

Add the property to the `returning` statement.

### [**](#runtimeType)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L129)optionalinheritedruntimeType

**runtimeType?

<!-- -->

: string

Inherited from ReferenceOptions.runtimeType

Runtime type of the property. This is the JS type that your property is mapped to, e.g. `string` or `number`, and is normally inferred automatically via `reflect-metadata`. In some cases, the inference won't work, and you might need to specify the `runtimeType` explicitly - the most common one is when you use a union type with null like `foo: number | null`.

### [**](#scale)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L141)optionalinheritedscale

**scale?

<!-- -->

: number

Inherited from ReferenceOptions.scale

Set scale of database column to represents the number of digits after the decimal point. (SQL only)

### [**](#serializedName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L339)optionalinheritedserializedName

**serializedName?

<!-- -->

: string

Inherited from ReferenceOptions.serializedName

Specify name of key for the serialized value.

### [**](#serializedPrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L329)optionalinheritedserializedPrimaryKey

**serializedPrimaryKey?

<!-- -->

: boolean

Inherited from ReferenceOptions.serializedPrimaryKey

Set to define serialized primary key for MongoDB. (virtual) Alias for `@SerializedPrimaryKey()` decorator.

* **@see**

  <https://mikro-orm.io/docs/decorators#serializedprimarykey>

### [**](#serializer)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L335)optionalinheritedserializer

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

  * #### Parameters

    * ##### value: any

    * ##### optionaloptions: [SerializeOptions](https://mikro-orm.io/api/core/interface/SerializeOptions.md)\<any, never, never>

    #### Returns any

### [**](#setter)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L250)optionalinheritedsetter

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

### [**](#strategy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L374)optionalinheritedstrategy

**strategy?

<!-- -->

: [LoadStrategy](https://mikro-orm.io/api/core/enum/LoadStrategy.md) | select-in | joined | balanced

Inherited from ReferenceOptions.strategy

Override the default loading strategy for this property. This option has precedence over the global `loadStrategy`, but can be overridden by `FindOptions.strategy`.

### [**](#type)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L115)optionalinheritedtype

**type?

<!-- -->

: string | [AnyString](https://mikro-orm.io/api/core.md#AnyString) | Date | uint8array | array | enumArray | unknown | [Type](https://mikro-orm.io/api/core/class/Type.md)\<any, any> | ObjectId | [Constructor](https://mikro-orm.io/api/core.md#Constructor)\<Partial\<any>> | [Constructor](https://mikro-orm.io/api/core.md#Constructor)<[Type](https://mikro-orm.io/api/core/class/Type.md)\<any, any>> | () => unknown | ColumnType

Inherited from ReferenceOptions.type

Explicitly specify the runtime type.

* **@see**

  * <https://mikro-orm.io/docs/metadata-providers>
  * <https://mikro-orm.io/docs/custom-types>

### [**](#unique)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L219)optionalinheritedunique

**unique?

<!-- -->

: string | boolean

Inherited from ReferenceOptions.unique

Set column as unique for Generator. (SQL only)

### [**](#unsigned)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L187)optionalinheritedunsigned

**unsigned?

<!-- -->

: boolean

Inherited from ReferenceOptions.unsigned

Set column as unsigned for Generator. (SQL only)

### [**](#version)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L207)optionalinheritedversion

**version?

<!-- -->

: boolean

Inherited from ReferenceOptions.version

Set to true to enable Locking via version field. (SQL only)

### [**](#where)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L512)optionalwhere

**where?

<!-- -->

: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<Target>

Condition for [Declarative partial loading](https://mikro-orm.io/docs/collections.md#declarative-partial-loading).
