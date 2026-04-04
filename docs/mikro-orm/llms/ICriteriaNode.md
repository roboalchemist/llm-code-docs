# Source: https://mikro-orm.io/api/knex/interface/ICriteriaNode.md

# ICriteriaNode<!-- --> \<T>

## Index[**](#Index)

### Properties

* [**entityName](#entityName)
* [**index](#index)
* [**key](#key)
* [**parent](#parent)
* [**payload](#payload)
* [**prop](#prop)
* [**strict](#strict)

### Methods

* [**getPath](#getPath)
* [**getPivotPath](#getPivotPath)
* [**process](#process)
* [**renameFieldToPK](#renameFieldToPK)
* [**shouldInline](#shouldInline)
* [**shouldRename](#shouldRename)
* [**willAutoJoin](#willAutoJoin)

## Properties<!-- -->[**](#Properties)

### [**](#entityName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L197)readonlyentityName

**entityName: string

### [**](#index)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L203)optionalindex

**index?

<!-- -->

: number

### [**](#key)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L199)optionalreadonlykey

**key?

<!-- -->

: string

### [**](#parent)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L198)optionalreadonlyparent

**parent?

<!-- -->

: [ICriteriaNode](https://mikro-orm.io/api/knex/interface/ICriteriaNode.md)\<T>

### [**](#payload)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L201)payload

**payload: any

### [**](#prop)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L202)optionalprop

**prop?

<!-- -->

: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

### [**](#strict)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L200)optionalreadonlystrict

**strict?

<!-- -->

: boolean

## Methods<!-- -->[**](#Methods)

### [**](#getPath)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L209)getPath

* ****getPath**(addIndex): string

- #### Parameters

  * ##### optionaladdIndex: boolean

  #### Returns string

### [**](#getPivotPath)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L210)getPivotPath

* ****getPivotPath**(path): string

- #### Parameters

  * ##### path: string

  #### Returns string

### [**](#process)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L204)process

* ****process**(qb, options): any

- #### Parameters

  * ##### qb: [IQueryBuilder](https://mikro-orm.io/api/knex/interface/IQueryBuilder.md)\<T>
  * ##### optionaloptions: [ICriteriaNodeProcessOptions](https://mikro-orm.io/api/knex/interface/ICriteriaNodeProcessOptions.md)

  #### Returns any

### [**](#renameFieldToPK)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L208)renameFieldToPK

* ****renameFieldToPK**\<T>(qb, ownerAlias): string

- #### Parameters

  * ##### qb: [IQueryBuilder](https://mikro-orm.io/api/knex/interface/IQueryBuilder.md)\<T>
  * ##### optionalownerAlias: string

  #### Returns string

### [**](#shouldInline)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L205)shouldInline

* ****shouldInline**(payload): boolean

- #### Parameters

  * ##### payload: any

  #### Returns boolean

### [**](#shouldRename)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L207)shouldRename

* ****shouldRename**(payload): boolean

- #### Parameters

  * ##### payload: any

  #### Returns boolean

### [**](#willAutoJoin)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L206)willAutoJoin

* ****willAutoJoin**(qb, alias, options): boolean

- #### Parameters

  * ##### qb: [IQueryBuilder](https://mikro-orm.io/api/knex/interface/IQueryBuilder.md)\<T>
  * ##### optionalalias: string
  * ##### optionaloptions: [ICriteriaNodeProcessOptions](https://mikro-orm.io/api/knex/interface/ICriteriaNodeProcessOptions.md)

  #### Returns boolean
