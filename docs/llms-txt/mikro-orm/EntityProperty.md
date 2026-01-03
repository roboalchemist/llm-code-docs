# Source: https://mikro-orm.io/api/core/interface/EntityProperty.md

# EntityProperty<!-- --> \<Owner, Target>

## Index[**](#Index)

### Properties

* [**accessor](#accessor)
* [**array](#array)
* [**autoincrement](#autoincrement)
* [**cascade](#cascade)
* [**columnTypes](#columnTypes)
* [**comment](#comment)
* [**concurrencyCheck](#concurrencyCheck)
* [**createForeignKeyConstraint](#createForeignKeyConstraint)
* [**customOrder](#customOrder)
* [**customType](#customType)
* [**customTypes](#customTypes)
* [**default](#default)
* [**defaultRaw](#defaultRaw)
* [**deferMode](#deferMode)
* [**deleteRule](#deleteRule)
* [**discriminatorColumn](#discriminatorColumn)
* [**eager](#eager)
* [**embeddable](#embeddable)
* [**embedded](#embedded)
* [**embeddedPath](#embeddedPath)
* [**embeddedProps](#embeddedProps)
* [**entity](#entity)
* [**enum](#enum)
* [**extra](#extra)
* [**fieldNameRaw](#fieldNameRaw)
* [**fieldNames](#fieldNames)
* [**filters](#filters)
* [**fixedOrder](#fixedOrder)
* [**fixedOrderColumn](#fixedOrderColumn)
* [**foreignKeyName](#foreignKeyName)
* [**formula](#formula)
* [**generated](#generated)
* [**getter](#getter)
* [**getterName](#getterName)
* [**groups](#groups)
* [**hasConvertToDatabaseValueSQL](#hasConvertToDatabaseValueSQL)
* [**hasConvertToJSValueSQL](#hasConvertToJSValueSQL)
* [**hidden](#hidden)
* [**hydrate](#hydrate)
* [**ignoreSchemaChanges](#ignoreSchemaChanges)
* [**index](#index)
* [**inherited](#inherited)
* [**inversedBy](#inversedBy)
* [**inverseJoinColumns](#inverseJoinColumns)
* [**items](#items)
* [**joinColumns](#joinColumns)
* [**kind](#kind)
* [**lazy](#lazy)
* [**length](#length)
* [**mappedBy](#mappedBy)
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
* [**ownColumns](#ownColumns)
* [**owner](#owner)
* [**persist](#persist)
* [**pivotEntity](#pivotEntity)
* [**pivotTable](#pivotTable)
* [**precision](#precision)
* [**prefix](#prefix)
* [**prefixMode](#prefixMode)
* [**primary](#primary)
* [**ref](#ref)
* [**referencedColumnNames](#referencedColumnNames)
* [**referencedPKs](#referencedPKs)
* [**referencedTableName](#referencedTableName)
* [**returning](#returning)
* [**runtimeType](#runtimeType)
* [**scale](#scale)
* [**serializedName](#serializedName)
* [**serializedPrimaryKey](#serializedPrimaryKey)
* [**serializer](#serializer)
* [**setter](#setter)
* [**strategy](#strategy)
* [**targetMeta](#targetMeta)
* [**trackChanges](#trackChanges)
* [**type](#type)
* [**unique](#unique)
* [**unsigned](#unsigned)
* [**updateRule](#updateRule)
* [**userDefined](#userDefined)
* [**version](#version)
* [**where](#where)

## Properties<!-- -->[**](#Properties)

### [**](#accessor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L549)optionalaccessor

**accessor?

<!-- -->

: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Owner, false>

### [**](#array)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L510)optionalarray

**array?

<!-- -->

: boolean

### [**](#autoincrement)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L504)optionalautoincrement

**autoincrement?

<!-- -->

: boolean

### [**](#cascade)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L550)cascade

**cascade: [Cascade](https://mikro-orm.io/api/core/enum/Cascade.md)\[]

### [**](#columnTypes)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L498)columnTypes

**columnTypes: string\[]

### [**](#comment)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L575)optionalcomment

**comment?

<!-- -->

: string

### [**](#concurrencyCheck)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L544)optionalconcurrencyCheck

**concurrencyCheck?

<!-- -->

: boolean

### [**](#createForeignKeyConstraint)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L582)createForeignKeyConstraint

**createForeignKeyConstraint: boolean

### [**](#customOrder)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L562)optionalcustomOrder

**customOrder?

<!-- -->

: string\[] | number\[] | boolean\[]

### [**](#customType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L500)optionalcustomType

**customType?

<!-- -->

: [Type](https://mikro-orm.io/api/core/class/Type.md)\<any, any>

### [**](#customTypes)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L501)customTypes

**customTypes: (undefined | [Type](https://mikro-orm.io/api/core/class/Type.md)\<any, any>)\[]

### [**](#default)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L518)optionaldefault

**default?

<!-- -->

: null | string | number | boolean

### [**](#defaultRaw)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L519)optionaldefaultRaw

**defaultRaw?

<!-- -->

: string

### [**](#deferMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L581)optionaldeferMode

**deferMode?

<!-- -->

: [DeferMode](https://mikro-orm.io/api/core/enum/DeferMode.md)

### [**](#deleteRule)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L554)optionaldeleteRule

**deleteRule?

<!-- -->

: [AnyString](https://mikro-orm.io/api/core.md#AnyString) | cascade | no action | set null | set default

### [**](#discriminatorColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L528)optionaldiscriminatorColumn

**discriminatorColumn?

<!-- -->

: string

### [**](#eager)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L545)optionaleager

**eager?

<!-- -->

: boolean

### [**](#embeddable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L526)embeddable

**embeddable: [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<Owner>

### [**](#embedded)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L524)optionalembedded

**embedded?

<!-- -->

: \[[EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Owner, false>, [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Owner, false>]

### [**](#embeddedPath)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L525)optionalembeddedPath

**embeddedPath?

<!-- -->

: string\[]

### [**](#embeddedProps)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L527)embeddedProps

**embeddedProps: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>>

### [**](#entity)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L494)entity

**entity: () => [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<Owner>

#### Type declaration

* * **(): [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<Owner>

  - #### Returns [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<Owner>

### [**](#enum)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L540)optionalenum

**enum?

<!-- -->

: boolean

### [**](#extra)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L577)optionalextra

**extra?

<!-- -->

: string

mysql only

### [**](#fieldNameRaw)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L517)optionalfieldNameRaw

**fieldNameRaw?

<!-- -->

: string

### [**](#fieldNames)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L516)fieldNames

**fieldNames: string\[]

### [**](#filters)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L521)optionalfilters

**filters?

<!-- -->

: [FilterOptions](https://mikro-orm.io/api/core.md#FilterOptions)

### [**](#fixedOrder)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L563)optionalfixedOrder

**fixedOrder?

<!-- -->

: boolean

### [**](#fixedOrderColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L564)optionalfixedOrderColumn

**fixedOrderColumn?

<!-- -->

: string

### [**](#foreignKeyName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L583)optionalforeignKeyName

**foreignKeyName?

<!-- -->

: string

### [**](#formula)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L520)optionalformula

**formula?

<!-- -->

: (alias) => string

#### Type declaration

* * **(alias): string

  - #### Parameters

    * ##### alias: string

    #### Returns string

### [**](#generated)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L499)optionalgenerated

**generated?

<!-- -->

: string | GeneratedColumnCallback\<Owner>

### [**](#getter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L547)optionalgetter

**getter?

<!-- -->

: boolean

### [**](#getterName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L548)optionalgetterName

**getterName?

<!-- -->

: keyof

<!-- -->

Owner

### [**](#groups)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L508)optionalgroups

**groups?

<!-- -->

: string\[]

### [**](#hasConvertToDatabaseValueSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L503)hasConvertToDatabaseValueSQL

**hasConvertToDatabaseValueSQL: boolean

### [**](#hasConvertToJSValueSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L502)hasConvertToJSValueSQL

**hasConvertToJSValueSQL: boolean

### [**](#hidden)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L539)optionalhidden

**hidden?

<!-- -->

: boolean

### [**](#hydrate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L537)optionalhydrate

**hydrate?

<!-- -->

: boolean

### [**](#ignoreSchemaChanges)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L580)optionalignoreSchemaChanges

**ignoreSchemaChanges?

<!-- -->

: (type | extra | default)\[]

### [**](#index)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L530)optionalindex

**index?

<!-- -->

: string | boolean

### [**](#inherited)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L533)optionalinherited

**inherited?

<!-- -->

: boolean

### [**](#inversedBy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L558)inversedBy

**inversedBy: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Target, false>

### [**](#inverseJoinColumns)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L569)inverseJoinColumns

**inverseJoinColumns: string\[]

### [**](#items)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L541)optionalitems

**items?

<!-- -->

: (string | number)\[]

### [**](#joinColumns)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L567)joinColumns

**joinColumns: string\[]

### [**](#kind)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L514)kind

**kind: [ReferenceKind](https://mikro-orm.io/api/core/enum/ReferenceKind.md)

### [**](#lazy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L509)optionallazy

**lazy?

<!-- -->

: boolean

### [**](#length)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L511)optionallength

**length?

<!-- -->

: number

### [**](#mappedBy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L559)mappedBy

**mappedBy: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Target, false>

### [**](#mapToPk)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L535)optionalmapToPk

**mapToPk?

<!-- -->

: boolean

### [**](#name)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L493)name

**name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Owner, false>

### [**](#nativeEnumName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L542)optionalnativeEnumName

**nativeEnumName?

<!-- -->

: string

### [**](#nullable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L532)optionalnullable

**nullable?

<!-- -->

: boolean

### [**](#object)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L529)optionalobject

**object?

<!-- -->

: boolean

### [**](#onCreate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L552)optionalonCreate

**onCreate?

<!-- -->

: (entity, em) => any

#### Type declaration

* * **(entity, em): any

  - #### Parameters

    * ##### entity: Owner
    * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

    #### Returns any

### [**](#onUpdate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L553)optionalonUpdate

**onUpdate?

<!-- -->

: (entity, em) => any

#### Type declaration

* * **(entity, em): any

  - #### Parameters

    * ##### entity: Owner
    * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

    #### Returns any

### [**](#optional)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L579)optionaloptional

**optional?

<!-- -->

: boolean

### [**](#orderBy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L561)optionalorderBy

**orderBy?

<!-- -->

: [QueryOrderMap](https://mikro-orm.io/api/core.md#QueryOrderMap)\<Owner> | [QueryOrderMap](https://mikro-orm.io/api/core.md#QueryOrderMap)\<Owner>\[]

### [**](#orphanRemoval)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L551)optionalorphanRemoval

**orphanRemoval?

<!-- -->

: boolean

### [**](#ownColumns)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L568)ownColumns

**ownColumns: string\[]

### [**](#owner)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L557)owner

**owner: boolean

### [**](#persist)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L536)optionalpersist

**persist?

<!-- -->

: boolean

### [**](#pivotEntity)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L566)pivotEntity

**pivotEntity: string

### [**](#pivotTable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L565)pivotTable

**pivotTable: string

### [**](#precision)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L512)optionalprecision

**precision?

<!-- -->

: number

### [**](#prefix)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L522)optionalprefix

**prefix?

<!-- -->

: string | boolean

### [**](#prefixMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L523)optionalprefixMode

**prefixMode?

<!-- -->

: [EmbeddedPrefixMode](https://mikro-orm.io/api/core.md#EmbeddedPrefixMode)

### [**](#primary)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L506)optionalprimary

**primary?

<!-- -->

: boolean

### [**](#ref)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L515)optionalref

**ref?

<!-- -->

: boolean

### [**](#referencedColumnNames)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L570)referencedColumnNames

**referencedColumnNames: string\[]

### [**](#referencedPKs)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L572)referencedPKs

**referencedPKs: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Owner, false>\[]

### [**](#referencedTableName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L571)referencedTableName

**referencedTableName: string

### [**](#returning)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L505)optionalreturning

**returning?

<!-- -->

: boolean

### [**](#runtimeType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L496)runtimeType

**runtimeType: string | number | bigint | boolean | object | [AnyString](https://mikro-orm.io/api/core.md#AnyString) | Buffer | Date | any

### [**](#scale)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L513)optionalscale

**scale?

<!-- -->

: number

### [**](#serializedName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L574)optionalserializedName

**serializedName?

<!-- -->

: string

### [**](#serializedPrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L507)serializedPrimaryKey

**serializedPrimaryKey: boolean

### [**](#serializer)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L573)optionalserializer

**serializer?

<!-- -->

: (value, options) => any

#### Type declaration

* * **(value, options): any

  - #### Parameters

    * ##### value: any
    * ##### optionaloptions: [SerializeOptions](https://mikro-orm.io/api/core/interface/SerializeOptions.md)\<any, never, never>

    #### Returns any

### [**](#setter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L546)optionalsetter

**setter?

<!-- -->

: boolean

### [**](#strategy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L556)optionalstrategy

**strategy?

<!-- -->

: [LoadStrategy](https://mikro-orm.io/api/core/enum/LoadStrategy.md)

### [**](#targetMeta)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L497)optionaltargetMeta

**targetMeta?

<!-- -->

: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<Target>

### [**](#trackChanges)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L538)optionaltrackChanges

**trackChanges?

<!-- -->

: boolean

### [**](#type)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L495)type

**type: string | bigint | boolean | uuid | date | time | datetime | blob | uint8array | array | enumArray | enum | json | integer | smallint | tinyint | mediumint | float | double | decimal | character | text | interval | unknown | [AnyString](https://mikro-orm.io/api/core.md#AnyString)

### [**](#unique)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L531)optionalunique

**unique?

<!-- -->

: string | boolean

### [**](#unsigned)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L534)optionalunsigned

**unsigned?

<!-- -->

: boolean

### [**](#updateRule)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L555)optionalupdateRule

**updateRule?

<!-- -->

: [AnyString](https://mikro-orm.io/api/core.md#AnyString) | cascade | no action | set null | set default

### [**](#userDefined)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L578)optionaluserDefined

**userDefined?

<!-- -->

: boolean

### [**](#version)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L543)optionalversion

**version?

<!-- -->

: boolean

### [**](#where)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L560)optionalwhere

**where?

<!-- -->

: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<Target>
