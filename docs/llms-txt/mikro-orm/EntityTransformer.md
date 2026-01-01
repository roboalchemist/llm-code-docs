# Source: https://mikro-orm.io/api/core/class/EntityTransformer.md

# EntityTransformer<!-- -->

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**toObject](#toObject)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)constructor

* ****new EntityTransformer**(): [EntityTransformer](https://mikro-orm.io/api/core/class/EntityTransformer.md)

- #### Returns [EntityTransformer](https://mikro-orm.io/api/core/class/EntityTransformer.md)

## Methods<!-- -->[**](#Methods)

### [**](#toObject)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/serialization/EntityTransformer.ts#L29)statictoObject

* ****toObject**\<Entity, Ignored>(entity, ignoreFields, raw): Omit<[EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity>, Ignored>

- #### Parameters

  * ##### entity: Entity
  * ##### ignoreFields: Ignored\[] = <!-- -->\[]
  * ##### raw: boolean = <!-- -->false

  #### Returns Omit<[EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity>, Ignored>
