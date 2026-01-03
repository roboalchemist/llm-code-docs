# Source: https://mikro-orm.io/api/knex/interface/IndexDef.md

# IndexDef<!-- -->

## Index[**](#Index)

### Properties

* [**columnNames](#columnNames)
* [**composite](#composite)
* [**constraint](#constraint)
* [**deferMode](#deferMode)
* [**expression](#expression)
* [**keyName](#keyName)
* [**options](#options)
* [**primary](#primary)
* [**type](#type)
* [**unique](#unique)

## Properties<!-- -->[**](#Properties)

### [**](#columnNames)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L88)columnNames

**columnNames: string\[]

### [**](#composite)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L93)optionalcomposite

**composite?

<!-- -->

: boolean

### [**](#constraint)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L91)constraint

**constraint: boolean

### [**](#deferMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L97)optionaldeferMode

**deferMode?

<!-- -->

: [DeferMode](https://mikro-orm.io/api/core/enum/DeferMode.md) | immediate | deferred

### [**](#expression)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L94)optionalexpression

**expression?

<!-- -->

: string

### [**](#keyName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L89)keyName

**keyName: string

### [**](#options)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L95)optionaloptions

**options?

<!-- -->

: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

### [**](#primary)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L92)primary

**primary: boolean

### [**](#type)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L96)optionaltype

**type?

<!-- -->

: string | Readonly<{ indexType?

<!-- -->

: string; predicate?

<!-- -->

: QueryBuilder\<any, any>; storageEngineIndexType?

<!-- -->

: hash | btree }>

### [**](#unique)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L90)unique

**unique: boolean
