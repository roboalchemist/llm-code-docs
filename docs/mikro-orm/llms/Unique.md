# Source: https://mikro-orm.io/api/core/function/Unique.md

# Unique<!-- -->

### Callable

* ****Unique**\<T, H>(options): (target, propertyName) => any

***

* #### Parameters

  * ##### options: [UniqueOptions](https://mikro-orm.io/api/core/interface/UniqueOptions.md)\<T, H> = <!-- -->{}

  #### Returns (target, propertyName) => any

  * * **(target, propertyName): any

    - #### Parameters

      * ##### target: T
      * ##### optionalpropertyName: T extends [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<unknown> ? undefined : keyof<!-- --> T

      #### Returns any
