# Source: https://mikro-orm.io/api/core/function/ref.md

# ref<!-- -->

shortcut for `wrap(entity).toReference()`

### Callable

* ****ref**\<I, T>(entity): ([Ref](https://mikro-orm.io/api/core.md#Ref)\<T> & [LoadedReference](https://mikro-orm.io/api/core/interface/LoadedReference.md)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<T, AddEager\<T>>>) | AddOptional\<typeof entity>
* ****ref**\<I, T, PKV>(entityType, pk): [Ref](https://mikro-orm.io/api/core.md#Ref)\<T> | AddOptional\<typeof pk>

***

* shortcut for `wrap(entity).toReference()`

  ***

  #### Parameters

  * ##### entity: I

  #### Returns ([Ref](https://mikro-orm.io/api/core.md#Ref)\<T> & [LoadedReference](https://mikro-orm.io/api/core/interface/LoadedReference.md)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<T, AddEager\<T>>>) | AddOptional\<typeof entity>
