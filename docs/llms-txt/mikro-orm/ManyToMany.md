# Source: https://mikro-orm.io/api/core/function/ManyToMany.md

# ManyToMany<!-- -->

### Callable

* ****ManyToMany**\<T, O>(entity, mappedBy, options): (target, propertyName) => any

***

* #### Parameters

  * ##### optionalentity: string | [ManyToManyOptions](https://mikro-orm.io/api/core/interface/ManyToManyOptions.md)\<T, O> | () => [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>
  *
    ##### optionalmappedBy: (string & keyof<!-- --> T) | (e) => any
  *
    ##### options: Partial<[ManyToManyOptions](https://mikro-orm.io/api/core/interface/ManyToManyOptions.md)\<T, O>> = <!-- -->{}

  #### Returns (target, propertyName) => any

  * * **(target, propertyName): any

    - #### Parameters

      * ##### target: Partial\<any>
      * ##### propertyName: string

      #### Returns any
