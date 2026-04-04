# Source: https://mikro-orm.io/api/core/function/OneToMany.md

# OneToMany<!-- -->

### Callable

* ****OneToMany**\<Target, Owner>(entity, mappedBy, options): (target, propertyName) => void
* ****OneToMany**\<Target, Owner>(options): (target, propertyName) => void

***

* #### Parameters

  * ##### entity: string | (e) => [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<Target>
  *
    ##### mappedBy: (string & keyof<!-- --> Target) | (e) => any
  *
    ##### optionaloptions: Partial<[OneToManyOptions](https://mikro-orm.io/api/core/interface/OneToManyOptions.md)\<Owner, Target>>

  #### Returns (target, propertyName) => void

  * * **(target, propertyName): void

    - #### Parameters

      * ##### target: [AnyEntity](https://mikro-orm.io/api/core.md#AnyEntity)
      * ##### propertyName: string

      #### Returns void
