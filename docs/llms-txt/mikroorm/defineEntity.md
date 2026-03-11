# Source: https://mikro-orm.io/api/core/function/defineEntity.md

# defineEntity<!-- -->

### Callable

* ****defineEntity**\<TName, TTableName, TProperties, TPK, TBase, TRepository, TForceObject>(meta): [EntitySchemaWithMeta](https://mikro-orm.io/api/core/interface/EntitySchemaWithMeta.md)\<TName, TTableName, [InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, TRepository, TForceObject>, TBase, TProperties>
* ****defineEntity**\<TEntity, TProperties, TClassName, TTableName, TBase, TClass>(meta): [EntitySchemaWithMeta](https://mikro-orm.io/api/core/interface/EntitySchemaWithMeta.md)\<TClassName, TTableName, TEntity, TBase, TProperties, TClass>

***

* #### Parameters

  * ##### meta: [EntityMetadataWithProperties](https://mikro-orm.io/api/core/interface/EntityMetadataWithProperties.md)\<TName, TTableName, TProperties, TPK, TBase, TRepository, TForceObject>

  #### Returns [EntitySchemaWithMeta](https://mikro-orm.io/api/core/interface/EntitySchemaWithMeta.md)\<TName, TTableName, [InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, TRepository, TForceObject>, TBase, TProperties>

## Index[**](#index)

### Properties

* [**properties](#properties)

## Properties<!-- -->[**](#properties)

### [**](#properties)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1313)properties

**properties: [PropertyBuilders](https://mikro-orm.io/api/core.md#PropertyBuilders)
