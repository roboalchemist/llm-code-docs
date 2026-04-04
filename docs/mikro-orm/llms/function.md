# Source: https://mikro-orm.io/api/core/function.md

# Index<!-- -->

### Callable

* ****Index**\<T, H>(options): (target, propertyName) => any

***

* #### Parameters

  * ##### options: [IndexOptions](https://mikro-orm.io/api/core/interface/IndexOptions.md)\<T, H> = <!-- -->{}

  #### Returns (target, propertyName) => any

  * * **(target, propertyName): any

    - #### Parameters

      * ##### target: T
      * ##### optionalpropertyName: T extends [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<unknown> ? undefined : keyof<!-- --> T

      #### Returns any
