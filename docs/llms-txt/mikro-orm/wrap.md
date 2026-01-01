# Source: https://mikro-orm.io/api/core/function/wrap.md

# wrap<!-- -->

wraps entity type with WrappedEntity internal properties and helpers like init/isInitialized/populated/toJSON use `preferHelper = true` to have access to the internal `__` properties like `__meta` or `__em`

### Callable

* ****wrap**\<T>(entity, preferHelper): IWrappedEntityInternal\<T>
* ****wrap**\<T>(entity, preferHelper): [IWrappedEntity](https://mikro-orm.io/api/core/interface/IWrappedEntity.md)\<T>

***

* returns WrappedEntity instance associated with this entity. This includes all the internal properties like `__meta` or `__em`.

  ***

  #### Parameters

  * ##### entity: T
  * ##### preferHelper: true

  #### Returns IWrappedEntityInternal\<T>
