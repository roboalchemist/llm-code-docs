# Source: https://mikro-orm.io/api/core/function/serialize.md

# serialize<!-- -->

Converts entity instance to POJO, converting the `Collection`s to arrays and unwrapping the `Reference` wrapper, while respecting the serialization options. This method accepts either a single entity or an array of entities, and returns the corresponding POJO or an array of POJO. To serialize a single entity, you can also use `wrap(entity).serialize()` which handles a single entity only.

```
const dtos = serialize([user1, user, ...], { exclude: ['id', 'email'], forceObject: true });
const [dto2, dto3] = serialize([user2, user3], { exclude: ['id', 'email'], forceObject: true });
const dto1 = serialize(user, { exclude: ['id', 'email'], forceObject: true });
const dto2 = wrap(user).serialize({ exclude: ['id', 'email'], forceObject: true });
```

### Callable

* ****serialize**\<Entity, Naked, Populate, Exclude, Config>(entity, options): Naked extends object\[] ? [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<ArrayElement\<Naked>, Populate>, CleanTypeConfig\<Config>>\[] : [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Naked, Populate>, CleanTypeConfig\<Config>>

***

* Converts entity instance to POJO, converting the `Collection`s to arrays and unwrapping the `Reference` wrapper, while respecting the serialization options. This method accepts either a single entity or an array of entities, and returns the corresponding POJO or an array of POJO. To serialize a single entity, you can also use `wrap(entity).serialize()` which handles a single entity only.

  ```
  const dtos = serialize([user1, user, ...], { exclude: ['id', 'email'], forceObject: true });
  const [dto2, dto3] = serialize([user2, user3], { exclude: ['id', 'email'], forceObject: true });
  const dto1 = serialize(user, { exclude: ['id', 'email'], forceObject: true });
  const dto2 = wrap(user).serialize({ exclude: ['id', 'email'], forceObject: true });
  ```

  ***

  #### Parameters

  * ##### entity: Entity
  * ##### optionaloptions: Config & [SerializeOptions](https://mikro-orm.io/api/core/interface/SerializeOptions.md)<[UnboxArray](https://mikro-orm.io/api/core.md#UnboxArray)\<Entity>, Populate, Exclude>

  #### Returns Naked extends object\[] ? [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<ArrayElement\<Naked>, Populate>, CleanTypeConfig\<Config>>\[] : [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Naked, Populate>, CleanTypeConfig\<Config>>
