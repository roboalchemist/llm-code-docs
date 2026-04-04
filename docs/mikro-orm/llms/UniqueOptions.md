# Source: https://mikro-orm.io/api/core/interface/UniqueOptions.md

# UniqueOptions<!-- --> \<T, H>

### Hierarchy

* BaseOptions\<T, H>
  * *UniqueOptions*

## Index[**](#Index)

### Properties

* [**deferMode](#deferMode)
* [**expression](#expression)
* [**name](#name)
* [**options](#options)
* [**properties](#properties)

## Properties<!-- -->[**](#Properties)

### [**](#deferMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Indexed.ts#L39)optionaldeferMode

**deferMode?

<!-- -->

: [DeferMode](https://mikro-orm.io/api/core/enum/DeferMode.md) | immediate | deferred

### [**](#expression)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Indexed.ts#L35)optionalinheritedexpression

**expression?

<!-- -->

: string | (T extends [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<P> ? [IndexCallback](https://mikro-orm.io/api/core.md#IndexCallback)\<P> : [IndexCallback](https://mikro-orm.io/api/core.md#IndexCallback)\<T>)

Inherited from BaseOptions.expression

### [**](#name)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Indexed.ts#L32)optionalinheritedname

**name?

<!-- -->

: string

Inherited from BaseOptions.name

### [**](#options)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Indexed.ts#L34)optionalinheritedoptions

**options?

<!-- -->

: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

Inherited from BaseOptions.options

### [**](#properties)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Indexed.ts#L33)optionalinheritedproperties

**properties?

<!-- -->

: T extends [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<P> ? Properties\<P, H> : Properties\<T, H>

Inherited from BaseOptions.properties
