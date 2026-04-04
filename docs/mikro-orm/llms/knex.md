# Source: https://mikro-orm.io/api/knex/interface/Knex.md

# Knex<!-- --> \<TRecord, TResult>

### Hierarchy

* QueryInterface\<TRecord, TResult>
* EventEmitter
  * *Knex*

### Callable

* ****Knex**\<TTable>(tableName, options): QueryBuilder\<TableType\<TTable>, DeferredKeySelection\<ResolveTableType\<TableType\<TTable>, base>, never, false, {}, false, {}, never>\[]>
* ****Knex**\<TRecord2, TResult2>(tableName, options): QueryBuilder\<TRecord2, TResult2>

***

* #### Parameters

  * ##### tableName: TTable
  * ##### optionaloptions: PgTableOptions

  #### Returns QueryBuilder\<TableType\<TTable>, DeferredKeySelection\<ResolveTableType\<TableType\<TTable>, base>, never, false, {}, false, {}, never>\[]>

## Index[**](#Index)

### Properties

* [**\_\_knex\_\_](#__knex__)
* [**andHaving](#andHaving)
* [**andHavingNotIn](#andHavingNotIn)
* [**andWhere](#andWhere)
* [**andWhereBetween](#andWhereBetween)
* [**andWhereILike](#andWhereILike)
* [**andWhereJsonNotSubsetOf](#andWhereJsonNotSubsetOf)
* [**andWhereJsonNotSupersetOf](#andWhereJsonNotSupersetOf)
* [**andWhereJsonObject](#andWhereJsonObject)
* [**andWhereJsonPath](#andWhereJsonPath)
* [**andWhereJsonSubsetOf](#andWhereJsonSubsetOf)
* [**andWhereJsonSupersetOf](#andWhereJsonSupersetOf)
* [**andWhereLike](#andWhereLike)
* [**andWhereNot](#andWhereNot)
* [**andWhereNotBetween](#andWhereNotBetween)
* [**andWhereNotJsonObject](#andWhereNotJsonObject)
* [**andWhereRaw](#andWhereRaw)
* [**as](#as)
* [**avg](#avg)
* [**avgDistinct](#avgDistinct)
* [**client](#client)
* [**column](#column)
* [**columns](#columns)
* [**comment](#comment)
* [**count](#count)
* [**countDistinct](#countDistinct)
* [**crossJoin](#crossJoin)
* [**denseRank](#denseRank)
* [**distinct](#distinct)
* [**distinctOn](#distinctOn)
* [**except](#except)
* [**first](#first)
* [**fn](#fn)
* [**from](#from)
* [**fromRaw](#fromRaw)
* [**fullOuterJoin](#fullOuterJoin)
* [**groupBy](#groupBy)
* [**groupByRaw](#groupByRaw)
* [**having](#having)
* [**havingBetween](#havingBetween)
* [**havingIn](#havingIn)
* [**havingNotBetween](#havingNotBetween)
* [**havingNotIn](#havingNotIn)
* [**havingNotNull](#havingNotNull)
* [**havingNull](#havingNull)
* [**havingRaw](#havingRaw)
* [**havingWrapped](#havingWrapped)
* [**hintComment](#hintComment)
* [**innerJoin](#innerJoin)
* [**intersect](#intersect)
* [**into](#into)
* [**isTransaction](#isTransaction)
* [**join](#join)
* [**joinRaw](#joinRaw)
* [**jsonExtract](#jsonExtract)
* [**jsonInsert](#jsonInsert)
* [**jsonRemove](#jsonRemove)
* [**jsonSet](#jsonSet)
* [**leftJoin](#leftJoin)
* [**leftOuterJoin](#leftOuterJoin)
* [**max](#max)
* [**migrate](#migrate)
* [**min](#min)
* [**orderBy](#orderBy)
* [**orderByRaw](#orderByRaw)
* [**orHaving](#orHaving)
* [**orHavingBetween](#orHavingBetween)
* [**orHavingNotBetween](#orHavingNotBetween)
* [**orHavingNotIn](#orHavingNotIn)
* [**orHavingNotNull](#orHavingNotNull)
* [**orHavingNull](#orHavingNull)
* [**orHavingRaw](#orHavingRaw)
* [**orWhere](#orWhere)
* [**orWhereBetween](#orWhereBetween)
* [**orWhereExists](#orWhereExists)
* [**orWhereILike](#orWhereILike)
* [**orWhereIn](#orWhereIn)
* [**orWhereJsonNotSubsetOf](#orWhereJsonNotSubsetOf)
* [**orWhereJsonNotSupersetOf](#orWhereJsonNotSupersetOf)
* [**orWhereJsonObject](#orWhereJsonObject)
* [**orWhereJsonPath](#orWhereJsonPath)
* [**orWhereJsonSubsetOf](#orWhereJsonSubsetOf)
* [**orWhereJsonSupersetOf](#orWhereJsonSupersetOf)
* [**orWhereLike](#orWhereLike)
* [**orWhereNot](#orWhereNot)
* [**orWhereNotBetween](#orWhereNotBetween)
* [**orWhereNotExists](#orWhereNotExists)
* [**orWhereNotIn](#orWhereNotIn)
* [**orWhereNotJsonObject](#orWhereNotJsonObject)
* [**orWhereNotNull](#orWhereNotNull)
* [**orWhereNull](#orWhereNull)
* [**orWhereRaw](#orWhereRaw)
* [**outerJoin](#outerJoin)
* [**partitionBy](#partitionBy)
* [**rank](#rank)
* [**raw](#raw)
* [**ref](#ref)
* [**rightJoin](#rightJoin)
* [**rightOuterJoin](#rightOuterJoin)
* [**rowNumber](#rowNumber)
* [**schema](#schema)
* [**seed](#seed)
* [**select](#select)
* [**sum](#sum)
* [**sumDistinct](#sumDistinct)
* [**table](#table)
* [**union](#union)
* [**unionAll](#unionAll)
* [**updateFrom](#updateFrom)
* [**userParams](#userParams)
* [**using](#using)
* [**VERSION](#VERSION)
* [**where](#where)
* [**whereBetween](#whereBetween)
* [**whereExists](#whereExists)
* [**whereILike](#whereILike)
* [**whereIn](#whereIn)
* [**whereJsonNotSubsetOf](#whereJsonNotSubsetOf)
* [**whereJsonNotSupersetOf](#whereJsonNotSupersetOf)
* [**whereJsonObject](#whereJsonObject)
* [**whereJsonPath](#whereJsonPath)
* [**whereJsonSubsetOf](#whereJsonSubsetOf)
* [**whereJsonSupersetOf](#whereJsonSupersetOf)
* [**whereLike](#whereLike)
* [**whereNot](#whereNot)
* [**whereNotBetween](#whereNotBetween)
* [**whereNotExists](#whereNotExists)
* [**whereNotIn](#whereNotIn)
* [**whereNotJsonObject](#whereNotJsonObject)
* [**whereNotNull](#whereNotNull)
* [**whereNull](#whereNull)
* [**whereRaw](#whereRaw)
* [**whereWrapped](#whereWrapped)
* [**with](#with)
* [**withMaterialized](#withMaterialized)
* [**withNotMaterialized](#withNotMaterialized)
* [**withRaw](#withRaw)
* [**withRecursive](#withRecursive)
* [**withSchema](#withSchema)
* [**withWrapped](#withWrapped)

### Methods

* [**\[captureRejectionSymbol\]](#\[captureRejectionSymbol])
* [**addListener](#addListener)
* [**batchInsert](#batchInsert)
* [**clear](#clear)
* [**clearCounters](#clearCounters)
* [**clearGroup](#clearGroup)
* [**clearHaving](#clearHaving)
* [**clearOrder](#clearOrder)
* [**clearSelect](#clearSelect)
* [**clearWhere](#clearWhere)
* [**decrement](#decrement)
* [**del](#del)
* [**delete](#delete)
* [**destroy](#destroy)
* [**emit](#emit)
* [**eventNames](#eventNames)
* [**getMaxListeners](#getMaxListeners)
* [**increment](#increment)
* [**initialize](#initialize)
* [**insert](#insert)
* [**limit](#limit)
* [**listenerCount](#listenerCount)
* [**listeners](#listeners)
* [**modify](#modify)
* [**off](#off)
* [**offset](#offset)
* [**on](#on)
* [**once](#once)
* [**onConflict](#onConflict)
* [**pluck](#pluck)
* [**prependListener](#prependListener)
* [**prependOnceListener](#prependOnceListener)
* [**queryBuilder](#queryBuilder)
* [**rawListeners](#rawListeners)
* [**removeAllListeners](#removeAllListeners)
* [**removeListener](#removeListener)
* [**returning](#returning)
* [**setMaxListeners](#setMaxListeners)
* [**transaction](#transaction)
* [**transactionProvider](#transactionProvider)
* [**truncate](#truncate)
* [**update](#update)
* [**upsert](#upsert)
* [**withUserParams](#withUserParams)

## Properties<!-- -->[**](#Properties)

### [**](#__knex__)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L395)\_\_knex\_\_

**\_\_knex\_\_: string

### [**](#andHaving)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L723)inheritedandHaving

**andHaving: Having\<TRecord, TResult>

Inherited from Knex.QueryInterface.andHaving

### [**](#andHavingNotIn)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L733)inheritedandHavingNotIn

**andHavingNotIn: HavingRange\<TRecord, TResult>

Inherited from Knex.QueryInterface.andHavingNotIn

### [**](#andWhere)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L644)inheritedandWhere

**andWhere: Where\<TRecord, TResult>

Inherited from Knex.QueryInterface.andWhere

### [**](#andWhereBetween)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L674)inheritedandWhereBetween

**andWhereBetween: WhereBetween\<TRecord, TResult>

Inherited from Knex.QueryInterface.andWhereBetween

### [**](#andWhereILike)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L666)inheritedandWhereILike

**andWhereILike: Where\<TRecord, TResult>

Inherited from Knex.QueryInterface.andWhereILike

### [**](#andWhereJsonNotSubsetOf)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L702)inheritedandWhereJsonNotSubsetOf

**andWhereJsonNotSubsetOf: WhereJsonObject\<TRecord, TResult>

Inherited from Knex.QueryInterface.andWhereJsonNotSubsetOf

### [**](#andWhereJsonNotSupersetOf)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L695)inheritedandWhereJsonNotSupersetOf

**andWhereJsonNotSupersetOf: WhereJsonObject\<TRecord, TResult>

Inherited from Knex.QueryInterface.andWhereJsonNotSupersetOf

### [**](#andWhereJsonObject)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L681)inheritedandWhereJsonObject

**andWhereJsonObject: WhereJsonObject\<TRecord, TResult>

Inherited from Knex.QueryInterface.andWhereJsonObject

### [**](#andWhereJsonPath)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L688)inheritedandWhereJsonPath

**andWhereJsonPath: WhereJsonPath\<TRecord, TResult>

Inherited from Knex.QueryInterface.andWhereJsonPath

### [**](#andWhereJsonSubsetOf)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L699)inheritedandWhereJsonSubsetOf

**andWhereJsonSubsetOf: WhereJsonObject\<TRecord, TResult>

Inherited from Knex.QueryInterface.andWhereJsonSubsetOf

### [**](#andWhereJsonSupersetOf)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L692)inheritedandWhereJsonSupersetOf

**andWhereJsonSupersetOf: WhereJsonObject\<TRecord, TResult>

Inherited from Knex.QueryInterface.andWhereJsonSupersetOf

### [**](#andWhereLike)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L663)inheritedandWhereLike

**andWhereLike: Where\<TRecord, TResult>

Inherited from Knex.QueryInterface.andWhereLike

### [**](#andWhereNot)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L647)inheritedandWhereNot

**andWhereNot: Where\<TRecord, TResult>

Inherited from Knex.QueryInterface.andWhereNot

### [**](#andWhereNotBetween)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L677)inheritedandWhereNotBetween

**andWhereNotBetween: WhereBetween\<TRecord, TResult>

Inherited from Knex.QueryInterface.andWhereNotBetween

### [**](#andWhereNotJsonObject)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L684)inheritedandWhereNotJsonObject

**andWhereNotJsonObject: WhereJsonObject\<TRecord, TResult>

Inherited from Knex.QueryInterface.andWhereNotJsonObject

### [**](#andWhereRaw)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L651)inheritedandWhereRaw

**andWhereRaw: WhereRaw\<TRecord, TResult>

Inherited from Knex.QueryInterface.andWhereRaw

### [**](#as)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L600)inheritedas

**as: As\<TRecord, TResult>

Inherited from Knex.QueryInterface.as

### [**](#avg)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L787)inheritedavg

**avg: TypePreservingAggregation\<TRecord, TResult, any>

Inherited from Knex.QueryInterface.avg

### [**](#avgDistinct)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L788)inheritedavgDistinct

**avgDistinct: TypePreservingAggregation\<TRecord, TResult, any>

Inherited from Knex.QueryInterface.avgDistinct

### [**](#client)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L429)client

**client: any

### [**](#column)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L602)inheritedcolumn

**column: Select\<TRecord, TResult>

Inherited from Knex.QueryInterface.column

### [**](#columns)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L601)inheritedcolumns

**columns: Select\<TRecord, TResult>

Inherited from Knex.QueryInterface.columns

### [**](#comment)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L603)inheritedcomment

**comment: Comment\<TRecord, TResult>

Inherited from Knex.QueryInterface.comment

### [**](#count)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L773)inheritedcount

**count: AsymmetricAggregation\<TRecord, TResult, string | number>

Inherited from Knex.QueryInterface.count

### [**](#countDistinct)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L778)inheritedcountDistinct

**countDistinct: AsymmetricAggregation\<TRecord, TResult, string | number>

Inherited from Knex.QueryInterface.countDistinct

### [**](#crossJoin)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L622)inheritedcrossJoin

**crossJoin: Join\<TRecord, TResult>

Inherited from Knex.QueryInterface.crossJoin

### [**](#denseRank)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L816)inheriteddenseRank

**denseRank: AnalyticFunction\<TRecord, TResult>

Inherited from Knex.QueryInterface.denseRank

### [**](#distinct)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L609)inheriteddistinct

**distinct: Distinct\<TRecord, TResult>

Inherited from Knex.QueryInterface.distinct

### [**](#distinctOn)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L610)inheriteddistinctOn

**distinctOn: DistinctOn\<TRecord, TResult>

Inherited from Knex.QueryInterface.distinctOn

### [**](#except)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L719)inheritedexcept

**except: Except\<TRecord, TResult>

Inherited from Knex.QueryInterface.except

### [**](#first)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L820)inheritedfirst

**first: Select\<TRecord, AddUnionMember\<UnwrapArrayMember\<TResult>, undefined>>

Inherited from Knex.QueryInterface.first

### [**](#fn)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L432)fn

**fn: FunctionHelper

### [**](#from)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L605)inheritedfrom

**from: Table\<TRecord, TResult>

Inherited from Knex.QueryInterface.from

### [**](#fromRaw)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L606)inheritedfromRaw

**fromRaw: Table\<TRecord, TResult>

Inherited from Knex.QueryInterface.fromRaw

### [**](#fullOuterJoin)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L621)inheritedfullOuterJoin

**fullOuterJoin: Join\<TRecord, TResult>

Inherited from Knex.QueryInterface.fullOuterJoin

### [**](#groupBy)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L705)inheritedgroupBy

**groupBy: GroupBy\<TRecord, TResult>

Inherited from Knex.QueryInterface.groupBy

### [**](#groupByRaw)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L706)inheritedgroupByRaw

**groupByRaw: RawQueryBuilder\<TRecord, TResult>

Inherited from Knex.QueryInterface.groupByRaw

### [**](#having)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L722)inheritedhaving

**having: Having\<TRecord, TResult>

Inherited from Knex.QueryInterface.having

### [**](#havingBetween)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L731)inheritedhavingBetween

**havingBetween: HavingRange\<TRecord, TResult>

Inherited from Knex.QueryInterface.havingBetween

### [**](#havingIn)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L727)inheritedhavingIn

**havingIn: HavingRange\<TRecord, TResult>

Inherited from Knex.QueryInterface.havingIn

### [**](#havingNotBetween)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L729)inheritedhavingNotBetween

**havingNotBetween: HavingRange\<TRecord, TResult>

Inherited from Knex.QueryInterface.havingNotBetween

### [**](#havingNotIn)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L732)inheritedhavingNotIn

**havingNotIn: HavingRange\<TRecord, TResult>

Inherited from Knex.QueryInterface.havingNotIn

### [**](#havingNotNull)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L736)inheritedhavingNotNull

**havingNotNull: HavingNull\<TRecord, TResult>

Inherited from Knex.QueryInterface.havingNotNull

### [**](#havingNull)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L735)inheritedhavingNull

**havingNull: HavingNull\<TRecord, TResult>

Inherited from Knex.QueryInterface.havingNull

### [**](#havingRaw)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L724)inheritedhavingRaw

**havingRaw: RawQueryBuilder\<TRecord, TResult>

Inherited from Knex.QueryInterface.havingRaw

### [**](#havingWrapped)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L653)inheritedhavingWrapped

**havingWrapped: WhereWrapped\<TRecord, TResult>

Inherited from Knex.QueryInterface.havingWrapped

### [**](#hintComment)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L604)inheritedhintComment

**hintComment: HintComment\<TRecord, TResult>

Inherited from Knex.QueryInterface.hintComment

### [**](#innerJoin)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L615)inheritedinnerJoin

**innerJoin: Join\<TRecord, TResult>

Inherited from Knex.QueryInterface.innerJoin

### [**](#intersect)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L718)inheritedintersect

**intersect: Intersect\<TRecord, TResult>

Inherited from Knex.QueryInterface.intersect

### [**](#into)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L607)inheritedinto

**into: Table\<TRecord, TResult>

Inherited from Knex.QueryInterface.into

### [**](#isTransaction)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L436)optionalisTransaction

**isTransaction?

<!-- -->

: boolean

### [**](#join)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L613)inheritedjoin

**join: Join\<TRecord, TResult>

Inherited from Knex.QueryInterface.join

### [**](#joinRaw)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L614)inheritedjoinRaw

**joinRaw: JoinRaw\<TRecord, TResult>

Inherited from Knex.QueryInterface.joinRaw

### [**](#jsonExtract)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L625)inheritedjsonExtract

**jsonExtract: JsonExtract\<TRecord, TResult>

Inherited from Knex.QueryInterface.jsonExtract

### [**](#jsonInsert)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L627)inheritedjsonInsert

**jsonInsert: JsonInsert\<TRecord, TResult>

Inherited from Knex.QueryInterface.jsonInsert

### [**](#jsonRemove)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L628)inheritedjsonRemove

**jsonRemove: JsonRemove\<TRecord, TResult>

Inherited from Knex.QueryInterface.jsonRemove

### [**](#jsonSet)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L626)inheritedjsonSet

**jsonSet: JsonSet\<TRecord, TResult>

Inherited from Knex.QueryInterface.jsonSet

### [**](#leftJoin)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L616)inheritedleftJoin

**leftJoin: Join\<TRecord, TResult>

Inherited from Knex.QueryInterface.leftJoin

### [**](#leftOuterJoin)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L617)inheritedleftOuterJoin

**leftOuterJoin: Join\<TRecord, TResult>

Inherited from Knex.QueryInterface.leftOuterJoin

### [**](#max)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L784)inheritedmax

**max: TypePreservingAggregation\<TRecord, TResult, any>

Inherited from Knex.QueryInterface.max

### [**](#migrate)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L430)migrate

**migrate: Migrator

### [**](#min)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L783)inheritedmin

**min: TypePreservingAggregation\<TRecord, TResult, any>

Inherited from Knex.QueryInterface.min

### [**](#orderBy)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L709)inheritedorderBy

**orderBy: OrderBy\<TRecord, TResult>

Inherited from Knex.QueryInterface.orderBy

### [**](#orderByRaw)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L710)inheritedorderByRaw

**orderByRaw: RawQueryBuilder\<TRecord, TResult>

Inherited from Knex.QueryInterface.orderByRaw

### [**](#orHaving)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L725)inheritedorHaving

**orHaving: Having\<TRecord, TResult>

Inherited from Knex.QueryInterface.orHaving

### [**](#orHavingBetween)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L730)inheritedorHavingBetween

**orHavingBetween: HavingRange\<TRecord, TResult>

Inherited from Knex.QueryInterface.orHavingBetween

### [**](#orHavingNotBetween)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L728)inheritedorHavingNotBetween

**orHavingNotBetween: HavingRange\<TRecord, TResult>

Inherited from Knex.QueryInterface.orHavingNotBetween

### [**](#orHavingNotIn)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L734)inheritedorHavingNotIn

**orHavingNotIn: HavingRange\<TRecord, TResult>

Inherited from Knex.QueryInterface.orHavingNotIn

### [**](#orHavingNotNull)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L738)inheritedorHavingNotNull

**orHavingNotNull: HavingNull\<TRecord, TResult>

Inherited from Knex.QueryInterface.orHavingNotNull

### [**](#orHavingNull)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L737)inheritedorHavingNull

**orHavingNull: HavingNull\<TRecord, TResult>

Inherited from Knex.QueryInterface.orHavingNull

### [**](#orHavingRaw)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L726)inheritedorHavingRaw

**orHavingRaw: RawQueryBuilder\<TRecord, TResult>

Inherited from Knex.QueryInterface.orHavingRaw

### [**](#orWhere)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L645)inheritedorWhere

**orWhere: Where\<TRecord, TResult>

Inherited from Knex.QueryInterface.orWhere

### [**](#orWhereBetween)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L673)inheritedorWhereBetween

**orWhereBetween: WhereBetween\<TRecord, TResult>

Inherited from Knex.QueryInterface.orWhereBetween

### [**](#orWhereExists)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L655)inheritedorWhereExists

**orWhereExists: WhereExists\<TRecord, TResult>

Inherited from Knex.QueryInterface.orWhereExists

### [**](#orWhereILike)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L667)inheritedorWhereILike

**orWhereILike: Where\<TRecord, TResult>

Inherited from Knex.QueryInterface.orWhereILike

### [**](#orWhereIn)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L659)inheritedorWhereIn

**orWhereIn: WhereIn\<TRecord, TResult>

Inherited from Knex.QueryInterface.orWhereIn

### [**](#orWhereJsonNotSubsetOf)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L701)inheritedorWhereJsonNotSubsetOf

**orWhereJsonNotSubsetOf: WhereJsonObject\<TRecord, TResult>

Inherited from Knex.QueryInterface.orWhereJsonNotSubsetOf

### [**](#orWhereJsonNotSupersetOf)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L694)inheritedorWhereJsonNotSupersetOf

**orWhereJsonNotSupersetOf: WhereJsonObject\<TRecord, TResult>

Inherited from Knex.QueryInterface.orWhereJsonNotSupersetOf

### [**](#orWhereJsonObject)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L680)inheritedorWhereJsonObject

**orWhereJsonObject: WhereJsonObject\<TRecord, TResult>

Inherited from Knex.QueryInterface.orWhereJsonObject

### [**](#orWhereJsonPath)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L687)inheritedorWhereJsonPath

**orWhereJsonPath: WhereJsonPath\<TRecord, TResult>

Inherited from Knex.QueryInterface.orWhereJsonPath

### [**](#orWhereJsonSubsetOf)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L698)inheritedorWhereJsonSubsetOf

**orWhereJsonSubsetOf: WhereJsonObject\<TRecord, TResult>

Inherited from Knex.QueryInterface.orWhereJsonSubsetOf

### [**](#orWhereJsonSupersetOf)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L691)inheritedorWhereJsonSupersetOf

**orWhereJsonSupersetOf: WhereJsonObject\<TRecord, TResult>

Inherited from Knex.QueryInterface.orWhereJsonSupersetOf

### [**](#orWhereLike)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L664)inheritedorWhereLike

**orWhereLike: Where\<TRecord, TResult>

Inherited from Knex.QueryInterface.orWhereLike

### [**](#orWhereNot)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L648)inheritedorWhereNot

**orWhereNot: Where\<TRecord, TResult>

Inherited from Knex.QueryInterface.orWhereNot

### [**](#orWhereNotBetween)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L676)inheritedorWhereNotBetween

**orWhereNotBetween: WhereBetween\<TRecord, TResult>

Inherited from Knex.QueryInterface.orWhereNotBetween

### [**](#orWhereNotExists)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L657)inheritedorWhereNotExists

**orWhereNotExists: WhereExists\<TRecord, TResult>

Inherited from Knex.QueryInterface.orWhereNotExists

### [**](#orWhereNotIn)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L661)inheritedorWhereNotIn

**orWhereNotIn: WhereIn\<TRecord, TResult>

Inherited from Knex.QueryInterface.orWhereNotIn

### [**](#orWhereNotJsonObject)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L683)inheritedorWhereNotJsonObject

**orWhereNotJsonObject: WhereJsonObject\<TRecord, TResult>

Inherited from Knex.QueryInterface.orWhereNotJsonObject

### [**](#orWhereNotNull)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L671)inheritedorWhereNotNull

**orWhereNotNull: WhereNull\<TRecord, TResult>

Inherited from Knex.QueryInterface.orWhereNotNull

### [**](#orWhereNull)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L669)inheritedorWhereNull

**orWhereNull: WhereNull\<TRecord, TResult>

Inherited from Knex.QueryInterface.orWhereNull

### [**](#orWhereRaw)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L650)inheritedorWhereRaw

**orWhereRaw: WhereRaw\<TRecord, TResult>

Inherited from Knex.QueryInterface.orWhereRaw

### [**](#outerJoin)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L620)inheritedouterJoin

**outerJoin: Join\<TRecord, TResult>

Inherited from Knex.QueryInterface.outerJoin

### [**](#partitionBy)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L713)inheritedpartitionBy

**partitionBy: PartitionBy\<TRecord, TResult>

Inherited from Knex.QueryInterface.partitionBy

### [**](#rank)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L815)inheritedrank

**rank: AnalyticFunction\<TRecord, TResult>

Inherited from Knex.QueryInterface.rank

### [**](#raw)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L397)raw

**raw: RawBuilder\<TRecord, any>

### [**](#ref)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L433)ref

**ref: RefBuilder

### [**](#rightJoin)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L618)inheritedrightJoin

**rightJoin: Join\<TRecord, TResult>

Inherited from Knex.QueryInterface.rightJoin

### [**](#rightOuterJoin)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L619)inheritedrightOuterJoin

**rightOuterJoin: Join\<TRecord, TResult>

Inherited from Knex.QueryInterface.rightOuterJoin

### [**](#rowNumber)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L817)inheritedrowNumber

**rowNumber: AnalyticFunction\<TRecord, TResult>

Inherited from Knex.QueryInterface.rowNumber

### [**](#schema)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L423)schema

**schema: SchemaBuilder

### [**](#seed)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L431)seed

**seed: Seeder

### [**](#select)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L599)inheritedselect

**select: Select\<TRecord, TResult>

Inherited from Knex.QueryInterface.select

### [**](#sum)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L785)inheritedsum

**sum: TypePreservingAggregation\<TRecord, TResult, any>

Inherited from Knex.QueryInterface.sum

### [**](#sumDistinct)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L786)inheritedsumDistinct

**sumDistinct: TypePreservingAggregation\<TRecord, TResult, any>

Inherited from Knex.QueryInterface.sumDistinct

### [**](#table)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L608)inheritedtable

**table: Table\<TRecord, TResult>

Inherited from Knex.QueryInterface.table

### [**](#union)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L716)inheritedunion

**union: Union\<TRecord, TResult>

Inherited from Knex.QueryInterface.union

### [**](#unionAll)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L717)inheritedunionAll

**unionAll: Union\<TRecord, TResult>

Inherited from Knex.QueryInterface.unionAll

### [**](#updateFrom)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1155)inheritedupdateFrom

**updateFrom: Table\<TRecord, TResult>

Inherited from Knex.QueryInterface.updateFrom

### [**](#userParams)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L434)userParams

**userParams: Record\<string, any>

### [**](#using)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L631)inheritedusing

**using: Using\<TRecord, TResult>

Inherited from Knex.QueryInterface.using

### [**](#VERSION)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L394)VERSION

**VERSION: string

### [**](#where)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L643)inheritedwhere

**where: Where\<TRecord, TResult>

Inherited from Knex.QueryInterface.where

### [**](#whereBetween)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L672)inheritedwhereBetween

**whereBetween: WhereBetween\<TRecord, TResult>

Inherited from Knex.QueryInterface.whereBetween

### [**](#whereExists)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L654)inheritedwhereExists

**whereExists: WhereExists\<TRecord, TResult>

Inherited from Knex.QueryInterface.whereExists

### [**](#whereILike)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L665)inheritedwhereILike

**whereILike: Where\<TRecord, TResult>

Inherited from Knex.QueryInterface.whereILike

### [**](#whereIn)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L658)inheritedwhereIn

**whereIn: WhereIn\<TRecord, TResult>

Inherited from Knex.QueryInterface.whereIn

### [**](#whereJsonNotSubsetOf)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L700)inheritedwhereJsonNotSubsetOf

**whereJsonNotSubsetOf: WhereJsonObject\<TRecord, TResult>

Inherited from Knex.QueryInterface.whereJsonNotSubsetOf

### [**](#whereJsonNotSupersetOf)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L693)inheritedwhereJsonNotSupersetOf

**whereJsonNotSupersetOf: WhereJsonObject\<TRecord, TResult>

Inherited from Knex.QueryInterface.whereJsonNotSupersetOf

### [**](#whereJsonObject)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L679)inheritedwhereJsonObject

**whereJsonObject: WhereJsonObject\<TRecord, TResult>

Inherited from Knex.QueryInterface.whereJsonObject

### [**](#whereJsonPath)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L686)inheritedwhereJsonPath

**whereJsonPath: WhereJsonPath\<TRecord, TResult>

Inherited from Knex.QueryInterface.whereJsonPath

### [**](#whereJsonSubsetOf)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L697)inheritedwhereJsonSubsetOf

**whereJsonSubsetOf: WhereJsonObject\<TRecord, TResult>

Inherited from Knex.QueryInterface.whereJsonSubsetOf

### [**](#whereJsonSupersetOf)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L690)inheritedwhereJsonSupersetOf

**whereJsonSupersetOf: WhereJsonObject\<TRecord, TResult>

Inherited from Knex.QueryInterface.whereJsonSupersetOf

### [**](#whereLike)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L662)inheritedwhereLike

**whereLike: Where\<TRecord, TResult>

Inherited from Knex.QueryInterface.whereLike

### [**](#whereNot)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L646)inheritedwhereNot

**whereNot: Where\<TRecord, TResult>

Inherited from Knex.QueryInterface.whereNot

### [**](#whereNotBetween)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L675)inheritedwhereNotBetween

**whereNotBetween: WhereBetween\<TRecord, TResult>

Inherited from Knex.QueryInterface.whereNotBetween

### [**](#whereNotExists)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L656)inheritedwhereNotExists

**whereNotExists: WhereExists\<TRecord, TResult>

Inherited from Knex.QueryInterface.whereNotExists

### [**](#whereNotIn)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L660)inheritedwhereNotIn

**whereNotIn: WhereIn\<TRecord, TResult>

Inherited from Knex.QueryInterface.whereNotIn

### [**](#whereNotJsonObject)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L682)inheritedwhereNotJsonObject

**whereNotJsonObject: WhereJsonObject\<TRecord, TResult>

Inherited from Knex.QueryInterface.whereNotJsonObject

### [**](#whereNotNull)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L670)inheritedwhereNotNull

**whereNotNull: WhereNull\<TRecord, TResult>

Inherited from Knex.QueryInterface.whereNotNull

### [**](#whereNull)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L668)inheritedwhereNull

**whereNull: WhereNull\<TRecord, TResult>

Inherited from Knex.QueryInterface.whereNull

### [**](#whereRaw)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L649)inheritedwhereRaw

**whereRaw: WhereRaw\<TRecord, TResult>

Inherited from Knex.QueryInterface.whereRaw

### [**](#whereWrapped)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L652)inheritedwhereWrapped

**whereWrapped: WhereWrapped\<TRecord, TResult>

Inherited from Knex.QueryInterface.whereWrapped

### [**](#with)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L634)inheritedwith

**with: With\<TRecord, TResult>

Inherited from Knex.QueryInterface.with

### [**](#withMaterialized)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L635)inheritedwithMaterialized

**withMaterialized: With\<TRecord, TResult>

Inherited from Knex.QueryInterface.withMaterialized

### [**](#withNotMaterialized)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L636)inheritedwithNotMaterialized

**withNotMaterialized: With\<TRecord, TResult>

Inherited from Knex.QueryInterface.withNotMaterialized

### [**](#withRaw)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L638)inheritedwithRaw

**withRaw: WithRaw\<TRecord, TResult>

Inherited from Knex.QueryInterface.withRaw

### [**](#withRecursive)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L637)inheritedwithRecursive

**withRecursive: With\<TRecord, TResult>

Inherited from Knex.QueryInterface.withRecursive

### [**](#withSchema)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L639)inheritedwithSchema

**withSchema: WithSchema\<TRecord, TResult>

Inherited from Knex.QueryInterface.withSchema

### [**](#withWrapped)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L640)inheritedwithWrapped

**withWrapped: WithWrapped\<TRecord, TResult>

Inherited from Knex.QueryInterface.withWrapped

## Methods<!-- -->[**](#Methods)

### [**](#\[captureRejectionSymbol])[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/@types/node/events.d.ts#L103)optionalinherited\[captureRejectionSymbol]

* ****\[captureRejectionSymbol]**\<K>(error, event, ...args): void

- Inherited from events.EventEmitter.\[captureRejectionSymbol]

  #### Parameters

  * ##### error: Error
  * ##### event: string | symbol
  * ##### rest...args: AnyRest

  #### Returns void

### [**](#addListener)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/@types/node/events.d.ts#L642)inheritedaddListener

* ****addListener**\<K>(eventName, listener): this

- Inherited from events.EventEmitter.addListener

  Alias for `emitter.on(eventName, listener)`.

  * **@since**

    v0.1.26

  ***

  #### Parameters

  * ##### eventName: string | symbol
  * ##### listener: (...args) => void


  #### Returns this

### [**](#batchInsert)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L415)batchInsert

* ****batchInsert**\<TRecord2, TResult2>(tableName, data, chunkSize): BatchInsertBuilder\<TRecord2, TResult2>

- #### Parameters

  * ##### tableName: TableDescriptor
  * ##### data: TRecord2 extends CompositeTableType\<unknown, unknown, Partial\<unknown>, Partial\<unknown>> ? readonly<!-- --> ResolveTableType\<TRecord2\<TRecord2>, insert>\[] : readonly<!-- --> DbRecordArr\<TRecord2>\[]
  * ##### optionalchunkSize: number

  #### Returns BatchInsertBuilder\<TRecord2, TResult2>

### [**](#clear)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L760)inheritedclear

* ****clear**(statement): QueryBuilder\<TRecord, TResult>

- Inherited from Knex.QueryInterface.clear

  #### Parameters

  * ##### statement: ClearStatements

  #### Returns QueryBuilder\<TRecord, TResult>

### [**](#clearCounters)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L759)inheritedclearCounters

* ****clearCounters**(): QueryBuilder\<TRecord, TResult>

- Inherited from Knex.QueryInterface.clearCounters

  #### Returns QueryBuilder\<TRecord, TResult>

### [**](#clearGroup)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L756)inheritedclearGroup

* ****clearGroup**(): QueryBuilder\<TRecord, TResult>

- Inherited from Knex.QueryInterface.clearGroup

  #### Returns QueryBuilder\<TRecord, TResult>

### [**](#clearHaving)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L758)inheritedclearHaving

* ****clearHaving**(): QueryBuilder\<TRecord, TResult>

- Inherited from Knex.QueryInterface.clearHaving

  #### Returns QueryBuilder\<TRecord, TResult>

### [**](#clearOrder)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L757)inheritedclearOrder

* ****clearOrder**(): QueryBuilder\<TRecord, TResult>

- Inherited from Knex.QueryInterface.clearOrder

  #### Returns QueryBuilder\<TRecord, TResult>

### [**](#clearSelect)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L741)inheritedclearSelect

* ****clearSelect**(): QueryBuilder\<TRecord, UnwrapArrayMember\<TResult> extends DeferredKeySelection\<TBase, TKeys, true, any, any, any, any> ? DeferredKeySelection\<TBase, never, false, {}, false, {}, never>\[] : TResult>

- Inherited from Knex.QueryInterface.clearSelect

  #### Returns QueryBuilder\<TRecord, UnwrapArrayMember\<TResult> extends DeferredKeySelection\<TBase, TKeys, true, any, any, any, any> ? DeferredKeySelection\<TBase, never, false, {}, false, {}, never>\[] : TResult>

### [**](#clearWhere)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L755)inheritedclearWhere

* ****clearWhere**(): QueryBuilder\<TRecord, TResult>

- Inherited from Knex.QueryInterface.clearWhere

  #### Returns QueryBuilder\<TRecord, TResult>

### [**](#decrement)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L802)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L806)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L810)inheriteddecrement

* ****decrement**(columnName, amount): QueryBuilder\<TRecord, number>
* ****decrement**(columnName, amount): QueryBuilder\<TRecord, number>
* ****decrement**(columns): QueryBuilder\<TRecord, number>

- Inherited from Knex.QueryInterface.decrement

  #### Parameters

  * ##### columnName: keyof<!-- --> TRecord
  * ##### optionalamount: number

  #### Returns QueryBuilder\<TRecord, number>

### [**](#del)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1157)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1161)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1172)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1183)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1187)inheriteddel

* ****del**(returning, options): QueryBuilder\<TRecord, DeferredKeySelection\<TRecord, never, false, {}, false, {}, never>\[]>
* ****del**\<TKey, TResult2>(returning, options): QueryBuilder\<TRecord, TResult2>
* ****del**\<TKey, TResult2>(returning, options): QueryBuilder\<TRecord, TResult2\[]>
* ****del**\<TResult2>(returning, options): QueryBuilder\<TRecord, TResult2>
* ****del**\<TResult2>(): QueryBuilder\<TRecord, TResult2>

- Inherited from Knex.QueryInterface.del

  #### Parameters

  * ##### returning: \*
  * ##### optionaloptions: DMLOptions

  #### Returns QueryBuilder\<TRecord, DeferredKeySelection\<TRecord, never, false, {}, false, {}, never>\[]>

### [**](#delete)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1189)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1193)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1204)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1215)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1219)inheriteddelete

* ****delete**(returning, options): QueryBuilder\<TRecord, DeferredKeySelection\<TRecord, never, false, {}, false, {}, never>\[]>
* ****delete**\<TKey, TResult2>(returning, options): QueryBuilder\<TRecord, TResult2>
* ****delete**\<TKey, TResult2>(returning, options): QueryBuilder\<TRecord, TResult2>
* ****delete**\<TResult2>(returning, options): QueryBuilder\<TRecord, TResult2>
* ****delete**\<TResult2>(): QueryBuilder\<TRecord, TResult2>

- Inherited from Knex.QueryInterface.delete

  #### Parameters

  * ##### returning: \*
  * ##### optionaloptions: DMLOptions

  #### Returns QueryBuilder\<TRecord, DeferredKeySelection\<TRecord, never, false, {}, false, {}, never>\[]>

### [**](#destroy)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L412)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L413)destroy

* ****destroy**(callback): void
* ****destroy**(): Promise\<void>

- #### Parameters

  * ##### callback: Function

  #### Returns void

### [**](#emit)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/@types/node/events.d.ts#L904)inheritedemit

* ****emit**\<K>(eventName, ...args): boolean

- Inherited from events.EventEmitter.emit

  Synchronously calls each of the listeners registered for the event named `eventName`, in the order they were registered, passing the supplied arguments to each.

  Returns `true` if the event had listeners, `false` otherwise.

  ```
  import { EventEmitter } from 'node:events';
  const myEmitter = new EventEmitter();

  // First listener
  myEmitter.on('event', function firstListener() {
    console.log('Helloooo! first listener');
  });
  // Second listener
  myEmitter.on('event', function secondListener(arg1, arg2) {
    console.log(`event with parameters ${arg1}, ${arg2} in second listener`);
  });
  // Third listener
  myEmitter.on('event', function thirdListener(...args) {
    const parameters = args.join(', ');
    console.log(`event with parameters ${parameters} in third listener`);
  });

  console.log(myEmitter.listeners('event'));

  myEmitter.emit('event', 1, 2, 3, 4, 5);

  // Prints:
  // [
  //   [Function: firstListener],
  //   [Function: secondListener],
  //   [Function: thirdListener]
  // ]
  // Helloooo! first listener
  // event with parameters 1, 2 in second listener
  // event with parameters 1, 2, 3, 4, 5 in third listener
  ```

  * **@since**

    v0.1.26

  ***

  #### Parameters

  * ##### eventName: string | symbol
  * ##### rest...args: AnyRest

  #### Returns boolean

### [**](#eventNames)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/@types/node/events.d.ts#L967)inheritedeventNames

* ****eventNames**(): (string | symbol)\[]

- Inherited from events.EventEmitter.eventNames

  Returns an array listing the events for which the emitter has registered listeners. The values in the array are strings or `Symbol`s.

  ```
  import { EventEmitter } from 'node:events';

  const myEE = new EventEmitter();
  myEE.on('foo', () => {});
  myEE.on('bar', () => {});

  const sym = Symbol('symbol');
  myEE.on(sym, () => {});

  console.log(myEE.eventNames());
  // Prints: [ 'foo', 'bar', Symbol(symbol) ]
  ```

  * **@since**

    v6.0.0

  ***

  #### Returns (string | symbol)\[]

### [**](#getMaxListeners)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/@types/node/events.d.ts#L819)inheritedgetMaxListeners

* ****getMaxListeners**(): number

- Inherited from events.EventEmitter.getMaxListeners

  Returns the current max listener value for the `EventEmitter` which is either set by `emitter.setMaxListeners(n)` or defaults to EventEmitter.defaultMaxListeners.

  * **@since**

    v1.0.0

  ***

  #### Returns number

### [**](#increment)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L790)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L794)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L798)inheritedincrement

* ****increment**(columnName, amount): QueryBuilder\<TRecord, number>
* ****increment**(columnName, amount): QueryBuilder\<TRecord, number>
* ****increment**(columns): QueryBuilder\<TRecord, number>

- Inherited from Knex.QueryInterface.increment

  #### Parameters

  * ##### columnName: keyof<!-- --> TRecord
  * ##### optionalamount: number

  #### Returns QueryBuilder\<TRecord, number>

### [**](#initialize)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L411)initialize

* ****initialize**(config): void

- #### Parameters

  * ##### optionalconfig: Config\<any>

  #### Returns void

### [**](#insert)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L830)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L839)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L855)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L871)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L887)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L903)inheritedinsert

* ****insert**(data, returning, options): QueryBuilder\<TRecord, DeferredKeySelection\<TRecord, never, false, {}, false, {}, never>\[]>
* ****insert**\<TKey, TResult2>(data, returning, options): QueryBuilder\<TRecord, TResult2>
* ****insert**\<TKey, TResult2>(data, returning, options): QueryBuilder\<TRecord, TResult2>
* ****insert**\<TKey, TResult2>(data, returning, options): QueryBuilder\<TRecord, TResult2>
* ****insert**\<TKey, TResult2>(data, returning, options): QueryBuilder\<TRecord, TResult2>
* ****insert**\<TResult2>(data): QueryBuilder\<TRecord, TResult2>

- Inherited from Knex.QueryInterface.insert

  #### Parameters

  * ##### data: TRecord extends CompositeTableType\<unknown, unknown, Partial\<unknown>, Partial\<unknown>> ? ResolveTableType\<TRecord\<TRecord>, insert> | readonly<!-- --> ResolveTableType\<TRecord\<TRecord>, insert>\[] : DbRecordArr\<TRecord> | readonly<!-- --> DbRecordArr\<TRecord>\[]
  * ##### returning: \*
  * ##### optionaloptions: DMLOptions

  #### Returns QueryBuilder\<TRecord, DeferredKeySelection\<TRecord, never, false, {}, false, {}, never>\[]>

### [**](#limit)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L767)inheritedlimit

* ****limit**(limit, options): QueryBuilder\<TRecord, TResult>

- Inherited from Knex.QueryInterface.limit

  #### Parameters

  * ##### limit: number
  * ##### optionaloptions: string | Readonly<{ skipBinding?<!-- -->: boolean }>

  #### Returns QueryBuilder\<TRecord, TResult>

### [**](#listenerCount)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/@types/node/events.d.ts#L913)inheritedlistenerCount

* ****listenerCount**\<K>(eventName, listener): number

- Inherited from events.EventEmitter.listenerCount

  Returns the number of listeners listening for the event named `eventName`. If `listener` is provided, it will return how many times the listener is found in the list of the listeners of the event.

  * **@since**

    v3.2.0

  ***

  #### Parameters

  * ##### eventName: string | symbol

    The name of the event being listened for

  * ##### optionallistener: Function

    The event handler function

  #### Returns number

### [**](#listeners)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/@types/node/events.d.ts#L832)inheritedlisteners

* ****listeners**\<K>(eventName): Function\[]

- Inherited from events.EventEmitter.listeners

  Returns a copy of the array of listeners for the event named `eventName`.

  ```
  server.on('connection', (stream) => {
    console.log('someone connected!');
  });
  console.log(util.inspect(server.listeners('connection')));
  // Prints: [ [Function] ]
  ```

  * **@since**

    v0.1.26

  ***

  #### Parameters

  * ##### eventName: string | symbol

  #### Returns Function\[]

### [**](#modify)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L992)inheritedmodify

* ****modify**\<TRecord2, TResult2>(callback, ...args): QueryBuilder\<TRecord2, TResult2>

- Inherited from Knex.QueryInterface.modify

  #### Parameters

  * ##### callback: QueryCallbackWithArgs\<TRecord, any>
  * ##### rest...args: any\[]

  #### Returns QueryBuilder\<TRecord2, TResult2>

### [**](#off)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/@types/node/events.d.ts#L792)inheritedoff

* ****off**\<K>(eventName, listener): this

- Inherited from events.EventEmitter.off

  Alias for `emitter.removeListener()`.

  * **@since**

    v10.0.0

  ***

  #### Parameters

  * ##### eventName: string | symbol
  * ##### listener: (...args) => void


  #### Returns this

### [**](#offset)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L763)inheritedoffset

* ****offset**(offset, options): QueryBuilder\<TRecord, TResult>

- Inherited from Knex.QueryInterface.offset

  #### Parameters

  * ##### offset: number
  * ##### optionaloptions: boolean | Readonly<{ skipBinding?<!-- -->: boolean }>

  #### Returns QueryBuilder\<TRecord, TResult>

### [**](#on)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/@types/node/events.d.ts#L674)inheritedon

* ****on**\<K>(eventName, listener): this

- Inherited from events.EventEmitter.on

  Adds the `listener` function to the end of the listeners array for the event named `eventName`. No checks are made to see if the `listener` has already been added. Multiple calls passing the same combination of `eventName` and `listener` will result in the `listener` being added, and called, multiple times.

  ```
  server.on('connection', (stream) => {
    console.log('someone connected!');
  });
  ```

  Returns a reference to the `EventEmitter`, so that calls can be chained.

  By default, event listeners are invoked in the order they are added. The `emitter.prependListener()` method can be used as an alternative to add the event listener to the beginning of the listeners array.

  ```
  import { EventEmitter } from 'node:events';
  const myEE = new EventEmitter();
  myEE.on('foo', () => console.log('a'));
  myEE.prependListener('foo', () => console.log('b'));
  myEE.emit('foo');
  // Prints:
  //   b
  //   a
  ```

  * **@since**

    v0.1.101

  ***

  #### Parameters

  * ##### eventName: string | symbol

    The name of the event.

  * ##### listener: (...args) => void

    The callback function



  #### Returns this

### [**](#once)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/@types/node/events.d.ts#L704)inheritedonce

* ****once**\<K>(eventName, listener): this

- Inherited from events.EventEmitter.once

  Adds a **one-time** `listener` function for the event named `eventName`. The next time `eventName` is triggered, this listener is removed and then invoked.

  ```
  server.once('connection', (stream) => {
    console.log('Ah, we have our first user!');
  });
  ```

  Returns a reference to the `EventEmitter`, so that calls can be chained.

  By default, event listeners are invoked in the order they are added. The `emitter.prependOnceListener()` method can be used as an alternative to add the event listener to the beginning of the listeners array.

  ```
  import { EventEmitter } from 'node:events';
  const myEE = new EventEmitter();
  myEE.once('foo', () => console.log('a'));
  myEE.prependOnceListener('foo', () => console.log('b'));
  myEE.emit('foo');
  // Prints:
  //   b
  //   a
  ```

  * **@since**

    v0.3.0

  ***

  #### Parameters

  * ##### eventName: string | symbol

    The name of the event.

  * ##### listener: (...args) => void

    The callback function



  #### Returns this

### [**](#onConflict)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1140)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1143)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1147)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1149)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1151)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1153)inheritedonConflict

* ****onConflict**\<TKey>(column): OnConflictQueryBuilder\<TRecord, TResult>
* ****onConflict**\<TKey>(columns): OnConflictQueryBuilder\<TRecord, TResult>
* ****onConflict**(columns): OnConflictQueryBuilder\<TRecord, TResult>
* ****onConflict**(columns): OnConflictQueryBuilder\<TRecord, TResult>
* ****onConflict**(raw): OnConflictQueryBuilder\<TRecord, TResult>
* ****onConflict**(): OnConflictQueryBuilder\<TRecord, TResult>

- Inherited from Knex.QueryInterface.onConflict

  #### Parameters

  * ##### column: TKey

  #### Returns OnConflictQueryBuilder\<TRecord, TResult>

### [**](#pluck)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L825)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L828)inheritedpluck

* ****pluck**\<K>(column): QueryBuilder\<TRecord, TRecord\[K]\[]>
* ****pluck**\<TResult2>(column): QueryBuilder\<TRecord, TResult2>

- Inherited from Knex.QueryInterface.pluck

  #### Parameters

  * ##### column: K

  #### Returns QueryBuilder\<TRecord, TRecord\[K]\[]>

### [**](#prependListener)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/@types/node/events.d.ts#L931)inheritedprependListener

* ****prependListener**\<K>(eventName, listener): this

- Inherited from events.EventEmitter.prependListener

  Adds the `listener` function to the *beginning* of the listeners array for the event named `eventName`. No checks are made to see if the `listener` has already been added. Multiple calls passing the same combination of `eventName` and `listener` will result in the `listener` being added, and called, multiple times.

  ```
  server.prependListener('connection', (stream) => {
    console.log('someone connected!');
  });
  ```

  Returns a reference to the `EventEmitter`, so that calls can be chained.

  * **@since**

    v6.0.0

  ***

  #### Parameters

  * ##### eventName: string | symbol

    The name of the event.

  * ##### listener: (...args) => void

    The callback function



  #### Returns this

### [**](#prependOnceListener)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/@types/node/events.d.ts#L947)inheritedprependOnceListener

* ****prependOnceListener**\<K>(eventName, listener): this

- Inherited from events.EventEmitter.prependOnceListener

  Adds a **one-time**`listener` function for the event named `eventName` to the *beginning* of the listeners array. The next time `eventName` is triggered, this listener is removed, and then invoked.

  ```
  server.prependOnceListener('connection', (stream) => {
    console.log('Ah, we have our first user!');
  });
  ```

  Returns a reference to the `EventEmitter`, so that calls can be chained.

  * **@since**

    v6.0.0

  ***

  #### Parameters

  * ##### eventName: string | symbol

    The name of the event.

  * ##### listener: (...args) => void

    The callback function



  #### Returns this

### [**](#queryBuilder)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L424)queryBuilder

* ****queryBuilder**\<TRecord2, TResult2>(): QueryBuilder\<TRecord2, TResult2>

- #### Returns QueryBuilder\<TRecord2, TResult2>

### [**](#rawListeners)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/@types/node/events.d.ts#L863)inheritedrawListeners

* ****rawListeners**\<K>(eventName): Function\[]

- Inherited from events.EventEmitter.rawListeners

  Returns a copy of the array of listeners for the event named `eventName`, including any wrappers (such as those created by `.once()`).

  ```
  import { EventEmitter } from 'node:events';
  const emitter = new EventEmitter();
  emitter.once('log', () => console.log('log once'));

  // Returns a new Array with a function `onceWrapper` which has a property
  // `listener` which contains the original listener bound above
  const listeners = emitter.rawListeners('log');
  const logFnWrapper = listeners[0];

  // Logs "log once" to the console and does not unbind the `once` event
  logFnWrapper.listener();

  // Logs "log once" to the console and removes the listener
  logFnWrapper();

  emitter.on('log', () => console.log('log persistently'));
  // Will return a new Array with a single function bound by `.on()` above
  const newListeners = emitter.rawListeners('log');

  // Logs "log persistently" twice
  newListeners[0]();
  emitter.emit('log');
  ```

  * **@since**

    v9.4.0

  ***

  #### Parameters

  * ##### eventName: string | symbol

  #### Returns Function\[]

### [**](#removeAllListeners)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/@types/node/events.d.ts#L803)inheritedremoveAllListeners

* ****removeAllListeners**(eventName): this

- Inherited from events.EventEmitter.removeAllListeners

  Removes all listeners, or those of the specified `eventName`.

  It is bad practice to remove listeners added elsewhere in the code, particularly when the `EventEmitter` instance was created by some other component or module (e.g. sockets or file streams).

  Returns a reference to the `EventEmitter`, so that calls can be chained.

  * **@since**

    v0.1.26

  ***

  #### Parameters

  * ##### optionaleventName: string | symbol

  #### Returns this

### [**](#removeListener)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/@types/node/events.d.ts#L787)inheritedremoveListener

* ****removeListener**\<K>(eventName, listener): this

- Inherited from events.EventEmitter.removeListener

  Removes the specified `listener` from the listener array for the event named `eventName`.

  ```
  const callback = (stream) => {
    console.log('someone connected!');
  };
  server.on('connection', callback);
  // ...
  server.removeListener('connection', callback);
  ```

  `removeListener()` will remove, at most, one instance of a listener from the listener array. If any single listener has been added multiple times to the listener array for the specified `eventName`, then `removeListener()` must be called multiple times to remove each instance.

  Once an event is emitted, all listeners attached to it at the time of emitting are called in order. This implies that any `removeListener()` or `removeAllListeners()` calls *after* emitting and *before* the last listener finishes execution will not remove them from`emit()` in progress. Subsequent events behave as expected.

  ```
  import { EventEmitter } from 'node:events';
  class MyEmitter extends EventEmitter {}
  const myEmitter = new MyEmitter();

  const callbackA = () => {
    console.log('A');
    myEmitter.removeListener('event', callbackB);
  };

  const callbackB = () => {
    console.log('B');
  };

  myEmitter.on('event', callbackA);

  myEmitter.on('event', callbackB);

  // callbackA removes listener callbackB but it will still be called.
  // Internal listener array at time of emit [callbackA, callbackB]
  myEmitter.emit('event');
  // Prints:
  //   A
  //   B

  // callbackB is now removed.
  // Internal listener array [callbackA]
  myEmitter.emit('event');
  // Prints:
  //   A
  ```

  Because listeners are managed using an internal array, calling this will change the position indices of any listener registered *after* the listener being removed. This will not impact the order in which listeners are called, but it means that any copies of the listener array as returned by the `emitter.listeners()` method will need to be recreated.

  When a single function has been added as a handler multiple times for a single event (as in the example below), `removeListener()` will remove the most recently added instance. In the example the `once('ping')` listener is removed:

  ```
  import { EventEmitter } from 'node:events';
  const ee = new EventEmitter();

  function pong() {
    console.log('pong');
  }

  ee.on('ping', pong);
  ee.once('ping', pong);
  ee.removeListener('ping', pong);

  ee.emit('ping');
  ee.emit('ping');
  ```

  Returns a reference to the `EventEmitter`, so that calls can be chained.

  * **@since**

    v0.1.26

  ***

  #### Parameters

  * ##### eventName: string | symbol
  * ##### listener: (...args) => void


  #### Returns this

### [**](#returning)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1106)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1110)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1121)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1135)inheritedreturning

* ****returning**(column, options): QueryBuilder\<TRecord, DeferredKeySelection\<TRecord, never, false, {}, false, {}, never>\[]>
* ****returning**\<TKey, TResult2>(column, options): QueryBuilder\<TRecord, TResult2>
* ****returning**\<TKey, TResult2>(columns, options): QueryBuilder\<TRecord, TResult2>
* ****returning**\<TResult2>(column, options): QueryBuilder\<TRecord, TResult2>

- Inherited from Knex.QueryInterface.returning

  #### Parameters

  * ##### column: \*
  * ##### optionaloptions: DMLOptions

  #### Returns QueryBuilder\<TRecord, DeferredKeySelection\<TRecord, never, false, {}, false, {}, never>\[]>

### [**](#setMaxListeners)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/@types/node/events.d.ts#L813)inheritedsetMaxListeners

* ****setMaxListeners**(n): this

- Inherited from events.EventEmitter.setMaxListeners

  By default `EventEmitter`s will print a warning if more than `10` listeners are added for a particular event. This is a useful default that helps finding memory leaks. The `emitter.setMaxListeners()` method allows the limit to be modified for this specific `EventEmitter` instance. The value can be set to `Infinity` (or `0`) to indicate an unlimited number of listeners.

  Returns a reference to the `EventEmitter`, so that calls can be chained.

  * **@since**

    v0.3.5

  ***

  #### Parameters

  * ##### n: number

  #### Returns this

### [**](#transaction)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L402)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L403)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L407)transaction

* ****transaction**(config): Promise\<Transaction\<any, any\[]>>
* ****transaction**(transactionScope, config): Promise\<Transaction\<any, any\[]>>
* ****transaction**\<T>(transactionScope, config): Promise\<T>

- #### Parameters

  * ##### optionalconfig: TransactionConfig

  #### Returns Promise\<Transaction\<any, any\[]>>

### [**](#transactionProvider)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L399)transactionProvider

* ****transactionProvider**(config): TransactionProvider

- #### Parameters

  * ##### optionalconfig: TransactionConfig

  #### Returns TransactionProvider

### [**](#truncate)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1221)inheritedtruncate

* ****truncate**(): QueryBuilder\<TRecord, void>

- Inherited from Knex.QueryInterface.truncate

  #### Returns QueryBuilder\<TRecord, void>

### [**](#update)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L996)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1010)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1024)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1028)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1034)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1039)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1053)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1067)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1081)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1095)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L1101)inheritedupdate

* ****update**\<K1, K2, TResult2>(columnName, value, returning, options): QueryBuilder\<TRecord, TResult2>
* ****update**\<K1, K2, TResult2>(columnName, value, returning, options): QueryBuilder\<TRecord, TResult2>
* ****update**\<K>(columnName, value): QueryBuilder\<TRecord, number>
* ****update**\<TResult2>(columnName, value, returning, options): QueryBuilder\<TRecord, TResult2>
* ****update**(data, returning, options): QueryBuilder\<TRecord, DeferredKeySelection\<TRecord, never, false, {}, false, {}, never>\[]>
* ****update**\<TKey, TResult2>(data, returning, options): QueryBuilder\<TRecord, TResult2>
* ****update**\<TKey, TResult2>(data, returning, options): QueryBuilder\<TRecord, TResult2>
* ****update**\<TKey, TResult2>(data, returning, options): QueryBuilder\<TRecord, TResult2>
* ****update**\<TKey, TResult2>(data, returning, options): QueryBuilder\<TRecord, TResult2>
* ****update**\<TResult2>(data): QueryBuilder\<TRecord, TResult2>
* ****update**\<TResult2>(columnName, value): QueryBuilder\<TRecord, TResult2>

- Inherited from Knex.QueryInterface.update

  #### Parameters

  * ##### columnName: K1
  * ##### value: DbColumn\<ResolveTableType\<TRecord, update>\[K1]>
  * ##### returning: K2
  * ##### optionaloptions: DMLOptions

  #### Returns QueryBuilder\<TRecord, TResult2>

### [**](#upsert)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L911)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L920)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L936)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L952)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L968)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L984)inheritedupsert

* ****upsert**(data, returning, options): QueryBuilder\<TRecord, DeferredKeySelection\<TRecord, never, false, {}, false, {}, never>\[]>
* ****upsert**\<TKey, TResult2>(data, returning, options): QueryBuilder\<TRecord, TResult2>
* ****upsert**\<TKey, TResult2>(data, returning, options): QueryBuilder\<TRecord, TResult2>
* ****upsert**\<TKey, TResult2>(data, returning, options): QueryBuilder\<TRecord, TResult2>
* ****upsert**\<TKey, TResult2>(data, returning, options): QueryBuilder\<TRecord, TResult2>
* ****upsert**\<TResult2>(data): QueryBuilder\<TRecord, TResult2>

- Inherited from Knex.QueryInterface.upsert

  #### Parameters

  * ##### data: TRecord extends CompositeTableType\<unknown, unknown, Partial\<unknown>, Partial\<unknown>> ? ResolveTableType\<TRecord\<TRecord>, upsert> | readonly<!-- --> ResolveTableType\<TRecord\<TRecord>, upsert>\[] : DbRecordArr\<TRecord> | readonly<!-- --> DbRecordArr\<TRecord>\[]
  * ##### returning: \*
  * ##### optionaloptions: DMLOptions

  #### Returns QueryBuilder\<TRecord, DeferredKeySelection\<TRecord, never, false, {}, false, {}, never>\[]>

### [**](#withUserParams)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L435)withUserParams

* ****withUserParams**(params): [Knex](https://mikro-orm.io/api/knex/interface/Knex.md)\<any, any\[]>

- #### Parameters

  * ##### params: Record\<string, any>

  #### Returns [Knex](https://mikro-orm.io/api/knex/interface/Knex.md)\<any, any\[]>
