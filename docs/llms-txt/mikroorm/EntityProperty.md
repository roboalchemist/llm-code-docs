# Source: https://mikro-orm.io/api/core/interface/EntityProperty.md

# EntityProperty<!-- --> \<Owner, Target>

## Index[**](#index)

### Properties

* [**accessor](#accessor)
* [**array](#array)
* [**autoincrement](#autoincrement)
* [**cascade](#cascade)
* [**columnTypes](#columntypes)
* [**comment](#comment)
* [**concurrencyCheck](#concurrencyCheck)
* [**createForeignKeyConstraint](#createforeignkeyconstraint)
* [**customOrder](#customOrder)
* [**customType](#customType)
* [**customTypes](#customtypes)
* [**default](#default)
* [**defaultRaw](#defaultRaw)
* [**deferMode](#deferMode)
* [**deleteRule](#deleteRule)
* [**discriminator](#discriminator)
* [**discriminatorColumn](#discriminatorColumn)
* [**discriminatorMap](#discriminatorMap)
* [**discriminatorValue](#discriminatorValue)
* [**eager](#eager)
* [**embeddable](#embeddable)
* [**embedded](#embedded)
* [**embeddedPath](#embeddedPath)
* [**embeddedProps](#embeddedprops)
* [**entity](#entity)
* [**enum](#enum)
* [**extra](#extra)
* [**fieldNameRaw](#fieldNameRaw)
* [**fieldNames](#fieldnames)
* [**filters](#filters)
* [**fixedOrder](#fixedOrder)
* [**fixedOrderColumn](#fixedOrderColumn)
* [**foreignKeyName](#foreignKeyName)
* [**formula](#formula)
* [**generated](#generated)
* [**getter](#getter)
* [**getterName](#getterName)
* [**groups](#groups)
* [**hasConvertToDatabaseValueSQL](#hasconverttodatabasevaluesql)
* [**hasConvertToJSValueSQL](#hasconverttojsvaluesql)
* [**hidden](#hidden)
* [**hydrate](#hydrate)
* [**ignoreSchemaChanges](#ignoreSchemaChanges)
* [**index](#index)
* [**inherited](#inherited)
* [**inversedBy](#inversedby)
* [**inverseJoinColumns](#inversejoincolumns)
* [**items](#items)
* [**joinColumns](#joincolumns)
* [**kind](#kind)
* [**lazy](#lazy)
* [**length](#length)
* [**mappedBy](#mappedby)
* [**mapToPk](#mapToPk)
* [**name](#name)
* [**nativeEnumName](#nativeEnumName)
* [**nullable](#nullable)
* [**object](#object)
* [**onCreate](#onCreate)
* [**onUpdate](#onUpdate)
* [**optional](#optional)
* [**orderBy](#orderBy)
* [**orphanRemoval](#orphanRemoval)
* [**ownColumns](#owncolumns)
* [**owner](#owner)
* [**persist](#persist)
* [**pivotEntity](#pivotentity)
* [**pivotTable](#pivottable)
* [**polymorphic](#polymorphic)
* [**polymorphTargets](#polymorphTargets)
* [**precision](#precision)
* [**prefix](#prefix)
* [**prefixMode](#prefixMode)
* [**primary](#primary)
* [**ref](#ref)
* [**referencedColumnNames](#referencedcolumnnames)
* [**referencedPKs](#referencedpks)
* [**referencedTableName](#referencedtablename)
* [**renamedFrom](#renamedFrom)
* [**returning](#returning)
* [**runtimeType](#runtimetype)
* [**scale](#scale)
* [**serializedName](#serializedName)
* [**serializedPrimaryKey](#serializedprimarykey)
* [**serializer](#serializer)
* [**setter](#setter)
* [**stiFieldNameMap](#stiFieldNameMap)
* [**stiFieldNames](#stiFieldNames)
* [**stiMerged](#stiMerged)
* [**strategy](#strategy)
* [**target](#target)
* [**targetKey](#targetKey)
* [**targetMeta](#targetMeta)
* [**type](#type)
* [**unique](#unique)
* [**unsigned](#unsigned)
* [**updateRule](#updateRule)
* [**userDefined](#userDefined)
* [**version](#version)
* [**where](#where)

## Properties<!-- -->[**](#properties)

### [**](#accessor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L846)optionalaccessor

**accessor?

<!-- -->

: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Owner, false>

### [**](#array)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L799)optionalarray

**array?

<!-- -->

: boolean

### [**](#autoincrement)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L793)optionalautoincrement

**autoincrement?

<!-- -->

: boolean

### [**](#cascade)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L847)cascade

**cascade: [Cascade](https://mikro-orm.io/api/core/enum/Cascade.md)\[]

### [**](#columntypes)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L787)columnTypes

**columnTypes: string\[]

### [**](#comment)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L873)optionalcomment

**comment?

<!-- -->

: string

### [**](#concurrencyCheck)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L841)optionalconcurrencyCheck

**concurrencyCheck?

<!-- -->

: boolean

### [**](#createforeignkeyconstraint)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L880)createForeignKeyConstraint

**createForeignKeyConstraint: boolean

### [**](#customOrder)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L859)optionalcustomOrder

**customOrder?

<!-- -->

: string\[] | number\[] | boolean\[]

### [**](#customType)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L789)optionalcustomType

**customType?

<!-- -->

: [Type](https://mikro-orm.io/api/core/class/Type.md)\<any, any>

### [**](#customtypes)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L790)customTypes

**customTypes: (undefined | [Type](https://mikro-orm.io/api/core/class/Type.md)\<any, any>)\[]

### [**](#default)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L807)optionaldefault

**default?

<!-- -->

: null | string | number | boolean

### [**](#defaultRaw)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L808)optionaldefaultRaw

**defaultRaw?

<!-- -->

: string

### [**](#deferMode)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L879)optionaldeferMode

**deferMode?

<!-- -->

: [DeferMode](https://mikro-orm.io/api/core/enum/DeferMode.md)

### [**](#deleteRule)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L851)optionaldeleteRule

**deleteRule?

<!-- -->

: [AnyString](https://mikro-orm.io/api/core.md#AnyString) | cascade | no action | set null | set default

### [**](#discriminator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L818)optionaldiscriminator

**discriminator?

<!-- -->

: string

### [**](#discriminatorColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L817)optionaldiscriminatorColumn

**discriminatorColumn?

<!-- -->

: string

### [**](#discriminatorMap)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L821)optionaldiscriminatorMap

**discriminatorMap?

<!-- -->

: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<Target>>

### [**](#discriminatorValue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L822)optionaldiscriminatorValue

**discriminatorValue?

<!-- -->

: string

### [**](#eager)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L842)optionaleager

**eager?

<!-- -->

: boolean

### [**](#embeddable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L815)embeddable

**embeddable: [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<Owner>

### [**](#embedded)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L813)optionalembedded

**embedded?

<!-- -->

: \[[EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Owner, false>, [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Owner, false>]

### [**](#embeddedPath)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L814)optionalembeddedPath

**embeddedPath?

<!-- -->

: string\[]

### [**](#embeddedprops)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L816)embeddedProps

**embeddedProps: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>>

### [**](#entity)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L782)entity

**entity: () => [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<Owner>

#### Type declaration

* * **(): [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<Owner>

  * #### Returns [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<Owner>

### [**](#enum)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L837)optionalenum

**enum?

<!-- -->

: boolean

### [**](#extra)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L875)optionalextra

**extra?

<!-- -->

: string

mysql only

### [**](#fieldNameRaw)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L806)optionalfieldNameRaw

**fieldNameRaw?

<!-- -->

: string

### [**](#fieldnames)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L805)fieldNames

**fieldNames: string\[]

### [**](#filters)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L810)optionalfilters

**filters?

<!-- -->

: [FilterOptions](https://mikro-orm.io/api/core.md#FilterOptions)

### [**](#fixedOrder)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L860)optionalfixedOrder

**fixedOrder?

<!-- -->

: boolean

### [**](#fixedOrderColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L861)optionalfixedOrderColumn

**fixedOrderColumn?

<!-- -->

: string

### [**](#foreignKeyName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L881)optionalforeignKeyName

**foreignKeyName?

<!-- -->

: string

### [**](#formula)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L809)optionalformula

**formula?

<!-- -->

: [FormulaCallback](https://mikro-orm.io/api/core.md#FormulaCallback)\<Owner>

### [**](#generated)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L788)optionalgenerated

**generated?

<!-- -->

: string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | [GeneratedColumnCallback](https://mikro-orm.io/api/core.md#GeneratedColumnCallback)\<Owner>

### [**](#getter)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L844)optionalgetter

**getter?

<!-- -->

: boolean

### [**](#getterName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L845)optionalgetterName

**getterName?

<!-- -->

: keyof

<!-- -->

Owner

### [**](#groups)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L797)optionalgroups

**groups?

<!-- -->

: string\[]

### [**](#hasconverttodatabasevaluesql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L792)hasConvertToDatabaseValueSQL

**hasConvertToDatabaseValueSQL: boolean

### [**](#hasconverttojsvaluesql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L791)hasConvertToJSValueSQL

**hasConvertToJSValueSQL: boolean

### [**](#hidden)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L836)optionalhidden

**hidden?

<!-- -->

: boolean

### [**](#hydrate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L835)optionalhydrate

**hydrate?

<!-- -->

: boolean

### [**](#ignoreSchemaChanges)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L878)optionalignoreSchemaChanges

**ignoreSchemaChanges?

<!-- -->

: (type | extra | default)\[]

### [**](#index)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L824)optionalindex

**index?

<!-- -->

: string | boolean

### [**](#inherited)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L827)optionalinherited

**inherited?

<!-- -->

: boolean

### [**](#inversedby)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L855)inversedBy

**inversedBy: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Target, false>

### [**](#inversejoincolumns)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L866)inverseJoinColumns

**inverseJoinColumns: string\[]

### [**](#items)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L838)optionalitems

**items?

<!-- -->

: (string | number)\[]

### [**](#joincolumns)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L864)joinColumns

**joinColumns: string\[]

### [**](#kind)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L803)kind

**kind: [ReferenceKind](https://mikro-orm.io/api/core/enum/ReferenceKind.md)

### [**](#lazy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L798)optionallazy

**lazy?

<!-- -->

: boolean

### [**](#length)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L800)optionallength

**length?

<!-- -->

: number

### [**](#mappedby)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L856)mappedBy

**mappedBy: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Target, false>

### [**](#mapToPk)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L833)optionalmapToPk

**mapToPk?

<!-- -->

: boolean

### [**](#name)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L781)name

**name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Owner, false>

### [**](#nativeEnumName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L839)optionalnativeEnumName

**nativeEnumName?

<!-- -->

: string

### [**](#nullable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L826)optionalnullable

**nullable?

<!-- -->

: boolean

### [**](#object)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L823)optionalobject

**object?

<!-- -->

: boolean

### [**](#onCreate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L849)optionalonCreate

**onCreate?

<!-- -->

: (entity, em) => any

#### Type declaration

* * **(entity, em): any

  * #### Parameters

    * ##### entity: Owner

    * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

    #### Returns any

### [**](#onUpdate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L850)optionalonUpdate

**onUpdate?

<!-- -->

: (entity, em) => any

#### Type declaration

* * **(entity, em): any

  * #### Parameters

    * ##### entity: Owner

    * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

    #### Returns any

### [**](#optional)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L877)optionaloptional

**optional?

<!-- -->

: boolean

### [**](#orderBy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L858)optionalorderBy

**orderBy?

<!-- -->

: [QueryOrderMap](https://mikro-orm.io/api/core.md#QueryOrderMap)\<Owner> | [QueryOrderMap](https://mikro-orm.io/api/core.md#QueryOrderMap)\<Owner>\[]

### [**](#orphanRemoval)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L848)optionalorphanRemoval

**orphanRemoval?

<!-- -->

: boolean

### [**](#owncolumns)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L865)ownColumns

**ownColumns: string\[]

### [**](#owner)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L854)owner

**owner: boolean

### [**](#persist)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L834)optionalpersist

**persist?

<!-- -->

: boolean

### [**](#pivotentity)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L863)pivotEntity

**pivotEntity: [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<Target>

### [**](#pivottable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L862)pivotTable

**pivotTable: string

### [**](#polymorphic)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L819)optionalpolymorphic

**polymorphic?

<!-- -->

: boolean

### [**](#polymorphTargets)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L820)optionalpolymorphTargets

**polymorphTargets?

<!-- -->

: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>\[]

### [**](#precision)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L801)optionalprecision

**precision?

<!-- -->

: number

### [**](#prefix)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L811)optionalprefix

**prefix?

<!-- -->

: string | boolean

### [**](#prefixMode)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L812)optionalprefixMode

**prefixMode?

<!-- -->

: [EmbeddedPrefixMode](https://mikro-orm.io/api/core.md#EmbeddedPrefixMode)

### [**](#primary)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L795)optionalprimary

**primary?

<!-- -->

: boolean

### [**](#ref)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L804)optionalref

**ref?

<!-- -->

: boolean

### [**](#referencedcolumnnames)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L867)referencedColumnNames

**referencedColumnNames: string\[]

### [**](#referencedpks)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L869)referencedPKs

**referencedPKs: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Owner, false>\[]

### [**](#referencedtablename)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L868)referencedTableName

**referencedTableName: string

### [**](#renamedFrom)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L828)optionalrenamedFrom

**renamedFrom?

<!-- -->

: string

### [**](#returning)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L794)optionalreturning

**returning?

<!-- -->

: boolean

### [**](#runtimetype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L785)runtimeType

**runtimeType: string | number | bigint | boolean | object | [AnyString](https://mikro-orm.io/api/core.md#AnyString) | Buffer | Date | any

### [**](#scale)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L802)optionalscale

**scale?

<!-- -->

: number

### [**](#serializedName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L872)optionalserializedName

**serializedName?

<!-- -->

: string

### [**](#serializedprimarykey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L796)serializedPrimaryKey

**serializedPrimaryKey: boolean

### [**](#serializer)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L871)optionalserializer

**serializer?

<!-- -->

: (value, options) => any

#### Type declaration

* * **(value, options): any

  * #### Parameters

    * ##### value: any

    * ##### optionaloptions: [SerializeOptions](https://mikro-orm.io/api/core/interface/SerializeOptions.md)\<any, never, never>

    #### Returns any

### [**](#setter)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L843)optionalsetter

**setter?

<!-- -->

: boolean

### [**](#stiFieldNameMap)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L831)optionalstiFieldNameMap

**stiFieldNameMap?

<!-- -->

: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<string>

### [**](#stiFieldNames)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L830)optionalstiFieldNames

**stiFieldNames?

<!-- -->

: string\[]

### [**](#stiMerged)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L829)optionalstiMerged

**stiMerged?

<!-- -->

: boolean

### [**](#strategy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L853)optionalstrategy

**strategy?

<!-- -->

: [LoadStrategy](https://mikro-orm.io/api/core/enum/LoadStrategy.md)

### [**](#target)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L783)target

**target: [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<Target>

### [**](#targetKey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L870)optionaltargetKey

**targetKey?

<!-- -->

: string

### [**](#targetMeta)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L786)optionaltargetMeta

**targetMeta?

<!-- -->

: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<Target, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<Target>>

### [**](#type)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L784)type

**type: string | bigint | boolean | [AnyString](https://mikro-orm.io/api/core.md#AnyString) | uuid | date | time | datetime | blob | uint8array | array | enumArray | enum | json | integer | smallint | tinyint | mediumint | float | double | decimal | character | text | interval | unknown

### [**](#unique)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L825)optionalunique

**unique?

<!-- -->

: string | boolean

### [**](#unsigned)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L832)optionalunsigned

**unsigned?

<!-- -->

: boolean

### [**](#updateRule)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L852)optionalupdateRule

**updateRule?

<!-- -->

: [AnyString](https://mikro-orm.io/api/core.md#AnyString) | cascade | no action | set null | set default

### [**](#userDefined)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L876)optionaluserDefined

**userDefined?

<!-- -->

: boolean

### [**](#version)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L840)optionalversion

**version?

<!-- -->

: boolean

### [**](#where)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L857)optionalwhere

**where?

<!-- -->

: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<Target>
