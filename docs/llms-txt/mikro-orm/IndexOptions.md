# Source: https://mikro-orm.io/api/core/interface/IndexOptions.md

# IndexOptions<!-- --> \<T, H>

### Hierarchy

* BaseOptions\<T, H>
  * *IndexOptions*

## Index[**](#Index)

### Properties

* [**expression](#expression)
* [**name](#name)
* [**options](#options)
* [**properties](#properties)
* [**type](#type)

## Properties<!-- -->[**](#Properties)

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

### [**](#type)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Indexed.ts#L43)optionaltype

**type?

<!-- -->

: string
