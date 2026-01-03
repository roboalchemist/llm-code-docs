# Source: https://mikro-orm.io/api/core/function/Embedded.md

# Embedded<!-- -->

### Callable

* ****Embedded**\<Owner, Target>(type, options): (target, propertyName) => any

***

* #### Parameters

  * ##### type: [EmbeddedOptions](https://mikro-orm.io/api/core/interface/EmbeddedOptions.md)\<Owner, Target> | () => [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<Target> | [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<Target>\[] = <!-- -->{}
  *
    ##### options: [EmbeddedOptions](https://mikro-orm.io/api/core/interface/EmbeddedOptions.md)\<Owner, Target> = <!-- -->{}

  #### Returns (target, propertyName) => any

  * * **(target, propertyName): any

    - #### Parameters

      * ##### target: Partial\<any>
      * ##### propertyName: string

      #### Returns any
