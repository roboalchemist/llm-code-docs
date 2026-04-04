# Source: https://mikro-orm.io/api/core/class/EntitySerializer.md

# EntitySerializer<!-- -->

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**serialize](#serialize)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)constructor

* ****new EntitySerializer**(): [EntitySerializer](https://mikro-orm.io/api/core/class/EntitySerializer.md)

- #### Returns [EntitySerializer](https://mikro-orm.io/api/core/class/EntitySerializer.md)

## Methods<!-- -->[**](#Methods)

### [**](#serialize)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/serialization/EntitySerializer.ts#L61)staticserialize

* ****serialize**\<T, P, E>(entity, options): [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<T, P>>

- #### Parameters

  * ##### entity: T
  * ##### options: [SerializeOptions](https://mikro-orm.io/api/core/interface/SerializeOptions.md)\<T, P, E> = <!-- -->{}

  #### Returns [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<T, P>>
