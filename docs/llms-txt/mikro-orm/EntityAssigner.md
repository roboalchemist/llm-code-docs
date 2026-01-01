# Source: https://mikro-orm.io/api/core/class/EntityAssigner.md

# EntityAssigner<!-- -->

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**assign](#assign)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)constructor

* ****new EntityAssigner**(): [EntityAssigner](https://mikro-orm.io/api/core/class/EntityAssigner.md)

- #### Returns [EntityAssigner](https://mikro-orm.io/api/core/class/EntityAssigner.md)

## Methods<!-- -->[**](#Methods)

### [**](#assign)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityAssigner.ts#L30)staticassign

* ****assign**\<Entity, Naked, Convert, Data>(entity, data, options): [MergeSelected](https://mikro-orm.io/api/core.md#MergeSelected)\<Entity, Naked, keyof
  <!-- -->
  Data & string>

- #### Parameters

  * ##### entity: Entity
  * ##### data: Data & [IsSubset](https://mikro-orm.io/api/core.md#IsSubset)<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<Naked, Convert>, Data>
  * ##### options: [AssignOptions](https://mikro-orm.io/api/core/interface/AssignOptions.md)\<Convert> = <!-- -->{}

  #### Returns [MergeSelected](https://mikro-orm.io/api/core.md#MergeSelected)\<Entity, Naked, keyof<!-- --> Data & string>
