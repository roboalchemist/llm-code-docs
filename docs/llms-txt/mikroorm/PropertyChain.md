# Source: https://mikro-orm.io/api/core/interface/PropertyChain.md

# PropertyChain<!-- --> \<Value, Options>

Lightweight chain result type for property builders - reduces type instantiation cost by avoiding full class resolution.

## Index[**](#index)

### Properties

* [**\~options](#~options)
* [**\~type](#~type)

### Methods

* [**$type](#$type)
* [**accessor](#accessor)
* [**array](#array)
* [**autoincrement](#autoincrement)
* [**cascade](#cascade)
* [**columnType](#columntype)
* [**columnTypes](#columntypes)
* [**comment](#comment)
* [**concurrencyCheck](#concurrencycheck)
* [**createForeignKeyConstraint](#createforeignkeyconstraint)
* [**customOrder](#customorder)
* [**default](#default)
* [**defaultRaw](#defaultraw)
* [**deferMode](#defermode)
* [**deleteRule](#deleterule)
* [**discriminator](#discriminator)
* [**discriminatorMap](#discriminatormap)
* [**eager](#eager)
* [**extra](#extra)
* [**fieldName](#fieldname)
* [**fieldNames](#fieldnames)
* [**filters](#filters)
* [**fixedOrder](#fixedorder)
* [**fixedOrderColumn](#fixedordercolumn)
* [**foreignKeyName](#foreignkeyname)
* [**formula](#formula)
* [**generated](#generated)
* [**getter](#getter)
* [**getterName](#gettername)
* [**groups](#groups)
* [**hidden](#hidden)
* [**hydrate](#hydrate)
* [**check](#check)
* [**ignoreSchemaChanges](#ignoreschemachanges)
* [**index](#index)
* [**inversedBy](#inversedby)
* [**inverseJoinColumn](#inversejoincolumn)
* [**inverseJoinColumns](#inversejoincolumns)
* [**joinColumn](#joincolumn)
* [**joinColumns](#joincolumns)
* [**lazy](#lazy)
* [**length](#length)
* [**mappedBy](#mappedby)
* [**mapToPk](#maptopk)
* [**name](#name)
* [**nativeEnumName](#nativeenumname)
* [**nullable](#nullable)
* [**object](#object)
* [**onCreate](#oncreate)
* [**onUpdate](#onupdate)
* [**orderBy](#orderby)
* [**orphanRemoval](#orphanremoval)
* [**ownColumns](#owncolumns)
* [**owner](#owner)
* [**persist](#persist)
* [**pivotEntity](#pivotentity)
* [**pivotTable](#pivottable)
* [**precision](#precision)
* [**prefix](#prefix)
* [**prefixMode](#prefixmode)
* [**primary](#primary)
* [**ref](#ref)
* [**referenceColumnName](#referencecolumnname)
* [**referencedColumnNames](#referencedcolumnnames)
* [**returning](#returning)
* [**runtimeType](#runtimetype)
* [**scale](#scale)
* [**serializedName](#serializedname)
* [**serializedPrimaryKey](#serializedprimarykey)
* [**serializer](#serializer)
* [**setter](#setter)
* [**strategy](#strategy)
* [**targetKey](#targetkey)
* [**type](#type)
* [**unique](#unique)
* [**unsigned](#unsigned)
* [**updateRule](#updaterule)
* [**version](#version)
* [**where](#where)

## Properties<!-- -->[**](#properties)

### [**](#~options)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L92)\~options

**\~options: Options

### [**](#~type)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L91)optional\~type

**\~type?

<!-- -->

: { value: Value }

#### Type declaration

* ##### value: Value

## Methods<!-- -->[**](#methods)

### [**](#$type)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L95)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L96)$type

* ****$type**\<T>(): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<T, Options>
* ****$type**\<Runtime, Raw, Serialized>(): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)<[IType](https://mikro-orm.io/api/core.md#IType)\<Runtime, Raw, Serialized>, Options>

* #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<T, Options>

### [**](#accessor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L147)accessor

* ****accessor**(accessor): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

* #### Parameters

  * ##### optionalaccessor: string | boolean

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

### [**](#array)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L198)array

* ****array**(): HasKind\<Options, enum | embedded> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Omit\<Options, array> & { array: true }> : never

* #### Returns HasKind\<Options, enum | embedded> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Omit\<Options, array> & { array: true }> : never

### [**](#autoincrement)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L103)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L104)autoincrement

* ****autoincrement**(): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Omit\<Options, autoincrement> & { autoincrement: true }>
* ****autoincrement**(autoincrement): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Omit\<Options, autoincrement> & { autoincrement: false }>

* #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Omit\<Options, autoincrement> & { autoincrement: true }>

### [**](#cascade)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L156)cascade

* ****cascade**(...cascade): HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### rest...cascade: [Cascade](https://mikro-orm.io/api/core/enum/Cascade.md)\[]

  #### Returns HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

### [**](#columntype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L123)columnType

* ****columnType**(columnType): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

* #### Parameters

  * ##### columnType: [AnyString](https://mikro-orm.io/api/core.md#AnyString) | ColumnType

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

### [**](#columntypes)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L124)columnTypes

* ****columnTypes**(...columnTypes): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

* #### Parameters

  * ##### rest...columnTypes: ([AnyString](https://mikro-orm.io/api/core.md#AnyString) | ColumnType)\[]

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

### [**](#comment)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L146)comment

* ****comment**(comment): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

* #### Parameters

  * ##### comment: string

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

### [**](#concurrencycheck)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L131)concurrencyCheck

* ****concurrencyCheck**(concurrencyCheck): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

* #### Parameters

  * ##### optionalconcurrencyCheck: boolean

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

### [**](#createforeignkeyconstraint)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L250)createForeignKeyConstraint

* ****createForeignKeyConstraint**(createForeignKeyConstraint): HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### optionalcreateForeignKeyConstraint: boolean

  #### Returns HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

### [**](#customorder)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L141)customOrder

* ****customOrder**(...customOrder): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

* #### Parameters

  * ##### rest...customOrder: string\[] | number\[] | boolean\[]

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

### [**](#default)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L114)default

* ****default**(defaultValue): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Omit\<Options, default> & { default: any }>

* #### Parameters

  * ##### defaultValue: null | string | number | boolean | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | Date | string\[] | number\[]

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Omit\<Options, default> & { default: any }>

### [**](#defaultraw)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L117)defaultRaw

* ****defaultRaw**(defaultRaw): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options & { defaultRaw: string }>

* #### Parameters

  * ##### defaultRaw: string

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options & { defaultRaw: string }>

### [**](#defermode)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L247)deferMode

* ****deferMode**(deferMode): HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### deferMode: [DeferMode](https://mikro-orm.io/api/core/enum/DeferMode.md) | immediate | deferred

  #### Returns HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

### [**](#deleterule)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L241)deleteRule

* ****deleteRule**(deleteRule): HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### deleteRule: [AnyString](https://mikro-orm.io/api/core.md#AnyString) | cascade | no action | set null | set default

  #### Returns HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

### [**](#discriminator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L180)discriminator

* ****discriminator**(discriminator): HasKind\<Options, m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### discriminator: string

  #### Returns HasKind\<Options, m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

### [**](#discriminatormap)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L183)discriminatorMap

* ****discriminatorMap**(discriminatorMap): HasKind\<Options, m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### discriminatorMap: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<string>

  #### Returns HasKind\<Options, m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

### [**](#eager)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L153)eager

* ****eager**(eager): HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### optionaleager: boolean

  #### Returns HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

### [**](#extra)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L142)extra

* ****extra**(extra): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

* #### Parameters

  * ##### extra: string

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

### [**](#fieldname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L110)fieldName

* ****fieldName**\<T>(fieldName): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Omit\<Options, fieldName> & { fieldName: T }>

* #### Parameters

  * ##### fieldName: T

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Omit\<Options, fieldName> & { fieldName: T }>

### [**](#fieldnames)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L120)fieldNames

* ****fieldNames**(...fieldNames): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

* #### Parameters

  * ##### rest...fieldNames: string\[]

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

### [**](#filters)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L162)filters

* ****filters**(filters): HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### filters: [FilterOptions](https://mikro-orm.io/api/core.md#FilterOptions)

  #### Returns HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

### [**](#fixedorder)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L192)fixedOrder

* ****fixedOrder**(fixedOrder): HasKind\<Options, m:n> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### optionalfixedOrder: boolean

  #### Returns HasKind\<Options, m:n> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

### [**](#fixedordercolumn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L193)fixedOrderColumn

* ****fixedOrderColumn**(fixedOrderColumn): HasKind\<Options, m:n> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### fixedOrderColumn: string

  #### Returns HasKind\<Options, m:n> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

### [**](#foreignkeyname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L253)foreignKeyName

* ****foreignKeyName**(foreignKeyName): HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### foreignKeyName: string

  #### Returns HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

### [**](#formula)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L118)formula

* ****formula**(formula): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Omit\<Options, formula> & { formula: any }>

* #### Parameters

  * ##### formula: string | [FormulaCallback](https://mikro-orm.io/api/core.md#FormulaCallback)\<any>

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Omit\<Options, formula> & { formula: any }>

### [**](#generated)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L132)generated

* ****generated**(generated): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

* #### Parameters

  * ##### generated: string | [GeneratedColumnCallback](https://mikro-orm.io/api/core.md#GeneratedColumnCallback)\<any>

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

### [**](#getter)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L135)getter

* ****getter**(getter): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

* #### Parameters

  * ##### optionalgetter: boolean

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

### [**](#gettername)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L136)getterName

* ****getterName**(getterName): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

* #### Parameters

  * ##### getterName: string

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

### [**](#groups)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L140)groups

* ****groups**(...groups): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

* #### Parameters

  * ##### rest...groups: string\[]

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

### [**](#hidden)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L102)hidden

* ****hidden**(): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Omit\<Options, hidden> & { hidden: true }>

* #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Omit\<Options, hidden> & { hidden: true }>

### [**](#hydrate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L130)hydrate

* ****hydrate**(hydrate): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

* #### Parameters

  * ##### optionalhydrate: boolean

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

### [**](#check)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L133)check

* ****check**(check): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

* #### Parameters

  * ##### check: string | [CheckCallback](https://mikro-orm.io/api/core.md#CheckCallback)\<any>

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

### [**](#ignoreschemachanges)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L143)ignoreSchemaChanges

* ****ignoreSchemaChanges**(...ignoreSchemaChanges): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

* #### Parameters

  * ##### rest...ignoreSchemaChanges: (type | extra | default)\[]

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

### [**](#index)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L144)index

* ****index**(index): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

* #### Parameters

  * ##### optionalindex: string | boolean

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

### [**](#inversedby)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L168)inversedBy

* ****inversedBy**(inversedBy): HasKind\<Options, m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### inversedBy: (keyof<!-- --> Value & string) | (e) => any

  #### Returns HasKind\<Options, m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

### [**](#inversejoincolumn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L223)inverseJoinColumn

* ****inverseJoinColumn**(inverseJoinColumn): HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### inverseJoinColumn: string

  #### Returns HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

### [**](#inversejoincolumns)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L226)inverseJoinColumns

* ****inverseJoinColumns**(...inverseJoinColumns): HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### rest...inverseJoinColumns: string\[]

  #### Returns HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

### [**](#joincolumn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L217)joinColumn

* ****joinColumn**(joinColumn): HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### joinColumn: string

  #### Returns HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

### [**](#joincolumns)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L220)joinColumns

* ****joinColumns**(...joinColumns): HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### rest...joinColumns: string\[]

  #### Returns HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

### [**](#lazy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L108)lazy

* ****lazy**(): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

* #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

### [**](#length)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L125)length

* ****length**(length): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

* #### Parameters

  * ##### length: number

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

### [**](#mappedby)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L165)mappedBy

* ****mappedBy**(mappedBy): HasKind\<Options, 1:m | m:n | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### mappedBy: (keyof<!-- --> Value & string) | (e) => any

  #### Returns HasKind\<Options, 1:m | m:n | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

### [**](#maptopk)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L174)mapToPk

* ****mapToPk**(): HasKind\<Options, m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Omit\<Options, mapToPk> & { mapToPk: true }> : never

* #### Returns HasKind\<Options, m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Omit\<Options, mapToPk> & { mapToPk: true }> : never

### [**](#name)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L109)name

* ****name**\<T>(name): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Omit\<Options, fieldName> & { fieldName: T }>

* #### Parameters

  * ##### name: T

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Omit\<Options, fieldName> & { fieldName: T }>

### [**](#nativeenumname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L208)nativeEnumName

* ****nativeEnumName**(nativeEnumName): HasKind\<Options, enum> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### nativeEnumName: string

  #### Returns HasKind\<Options, enum> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

### [**](#nullable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L99)nullable

* ****nullable**(): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Omit\<Options, nullable> & { nullable: true }>

* #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Omit\<Options, nullable> & { nullable: true }>

### [**](#object)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L205)object

* ****object**(object): HasKind\<Options, embedded> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### optionalobject: boolean

  #### Returns HasKind\<Options, embedded> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

### [**](#oncreate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L111)onCreate

* ****onCreate**(onCreate): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options & { onCreate: (...args) => any }>

* #### Parameters

  * ##### onCreate: (entity, em) => Value

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options & { onCreate: (...args) => any }>

### [**](#onupdate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L119)onUpdate

* ****onUpdate**(onUpdate): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

* #### Parameters

  * ##### onUpdate: (entity, em) => Value

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

### [**](#orderby)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L211)orderBy

* ****orderBy**(...orderBy): HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### rest...orderBy: [QueryOrderMap](https://mikro-orm.io/api/core.md#QueryOrderMap)\<object>\[]

  #### Returns HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

### [**](#orphanremoval)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L177)orphanRemoval

* ****orphanRemoval**(orphanRemoval): HasKind\<Options, 1:m | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### optionalorphanRemoval: boolean

  #### Returns HasKind\<Options, 1:m | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

### [**](#owncolumns)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L235)ownColumns

* ****ownColumns**(...ownColumns): HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### rest...ownColumns: string\[]

  #### Returns HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

### [**](#owner)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L171)owner

* ****owner**(): HasKind\<Options, m:n | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Omit\<Options, owner> & { owner: true }> : never

* #### Returns HasKind\<Options, m:n | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Omit\<Options, owner> & { owner: true }> : never

### [**](#persist)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L105)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L106)persist

* ****persist**(): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Omit\<Options, persist> & { persist: true }>
* ****persist**(persist): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Omit\<Options, persist> & { persist: false }>

* #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Omit\<Options, persist> & { persist: true }>

### [**](#pivotentity)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L189)pivotEntity

* ****pivotEntity**(pivotEntity): HasKind\<Options, m:n> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### pivotEntity: () => [EntityName](https://mikro-orm.io/api/core.md#EntityName)

  #### Returns HasKind\<Options, m:n> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

### [**](#pivottable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L188)pivotTable

* ****pivotTable**(pivotTable): HasKind\<Options, m:n> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### pivotTable: string

  #### Returns HasKind\<Options, m:n> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

### [**](#precision)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L126)precision

* ****precision**(precision): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

* #### Parameters

  * ##### precision: number

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

### [**](#prefix)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L201)prefix

* ****prefix**(prefix): HasKind\<Options, embedded> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### prefix: string | boolean

  #### Returns HasKind\<Options, embedded> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

### [**](#prefixmode)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L202)prefixMode

* ****prefixMode**(prefixMode): HasKind\<Options, embedded> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### prefixMode: [EmbeddedPrefixMode](https://mikro-orm.io/api/core.md#EmbeddedPrefixMode)

  #### Returns HasKind\<Options, embedded> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

### [**](#primary)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L101)primary

* ****primary**(): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Omit\<Options, primary> & { primary: true }>

* #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Omit\<Options, primary> & { primary: true }>

### [**](#ref)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L100)ref

* ****ref**(): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Omit\<Options, ref> & { ref: true }>

* #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Omit\<Options, ref> & { ref: true }>

### [**](#referencecolumnname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L229)referenceColumnName

* ****referenceColumnName**(referenceColumnName): HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### referenceColumnName: string

  #### Returns HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

### [**](#referencedcolumnnames)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L232)referencedColumnNames

* ****referencedColumnNames**(...referencedColumnNames): HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### rest...referencedColumnNames: string\[]

  #### Returns HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

### [**](#returning)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L128)returning

* ****returning**(returning): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

* #### Parameters

  * ##### optionalreturning: boolean

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

### [**](#runtimetype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L122)runtimeType

* ****runtimeType**(runtimeType): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

* #### Parameters

  * ##### runtimeType: string

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

### [**](#scale)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L127)scale

* ****scale**(scale): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

* #### Parameters

  * ##### scale: number

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

### [**](#serializedname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L139)serializedName

* ****serializedName**(serializedName): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

* #### Parameters

  * ##### serializedName: string

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

### [**](#serializedprimarykey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L137)serializedPrimaryKey

* ****serializedPrimaryKey**(serializedPrimaryKey): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

* #### Parameters

  * ##### optionalserializedPrimaryKey: boolean

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

### [**](#serializer)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L138)serializer

* ****serializer**(serializer): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

* #### Parameters

  * ##### serializer: (value, options) => any

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

### [**](#setter)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L134)setter

* ****setter**(setter): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

* #### Parameters

  * ##### optionalsetter: boolean

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

### [**](#strategy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L159)strategy

* ****strategy**(strategy): HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### strategy: [LoadStrategy](https://mikro-orm.io/api/core/enum/LoadStrategy.md) | select-in | joined | balanced

  #### Returns HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

### [**](#targetkey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L238)targetKey

* ****targetKey**(targetKey): HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### targetKey: keyof<!-- --> Value & string

  #### Returns HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

### [**](#type)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L121)type

* ****type**(type): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

* #### Parameters

  * ##### type: undefined | string | [AnyString](https://mikro-orm.io/api/core.md#AnyString) | Date | uint8array | array | enumArray | unknown | [Type](https://mikro-orm.io/api/core/class/Type.md)\<any, any> | ObjectId | [Constructor](https://mikro-orm.io/api/core.md#Constructor)\<Partial\<any>> | [Constructor](https://mikro-orm.io/api/core.md#Constructor)<[Type](https://mikro-orm.io/api/core/class/Type.md)\<any, any>> | () => unknown | ColumnType

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

### [**](#unique)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L145)unique

* ****unique**(unique): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

* #### Parameters

  * ##### optionalunique: string | boolean

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

### [**](#unsigned)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L129)unsigned

* ****unsigned**(unsigned): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

* #### Parameters

  * ##### optionalunsigned: boolean

  #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options>

### [**](#updaterule)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L244)updateRule

* ****updateRule**(updateRule): HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### updateRule: [AnyString](https://mikro-orm.io/api/core.md#AnyString) | cascade | no action | set null | set default

  #### Returns HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

### [**](#version)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L107)version

* ****version**(): [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Omit\<Options, version> & { version: true }>

* #### Returns [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Omit\<Options, version> & { version: true }>

### [**](#where)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L214)where

* ****where**(...where): HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never

* #### Parameters

  * ##### rest...where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<object>\[]

  #### Returns HasKind\<Options, 1:m | m:n | m:1 | 1:1> extends true ? [PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)\<Value, Options> : never
