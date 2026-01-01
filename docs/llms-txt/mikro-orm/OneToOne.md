# Source: https://mikro-orm.io/api/core/function/OneToOne.md

# OneToOne<!-- -->

### Callable

* ****OneToOne**\<Target, Owner>(entity, mappedByOrOptions, options): (target, propertyName) => any

***

* #### Parameters

  * ##### optionalentity: string | [OneToOneOptions](https://mikro-orm.io/api/core/interface/OneToOneOptions.md)\<Owner, Target> | (e) => [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<Target>
  *
    ##### optionalmappedByOrOptions: (string & keyof<!-- --> Target) | (e) => any | Partial<[OneToOneOptions](https://mikro-orm.io/api/core/interface/OneToOneOptions.md)\<Owner, Target>>
  *
    ##### options: Partial<[OneToOneOptions](https://mikro-orm.io/api/core/interface/OneToOneOptions.md)\<Owner, Target>> = <!-- -->{}

  #### Returns (target, propertyName) => any

  * * **(target, propertyName): any

    - #### Parameters

      * ##### target: Partial\<any>
      * ##### propertyName: string

      #### Returns any
