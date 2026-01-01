# Source: https://mikro-orm.io/api/core/function/BeforeDelete.md

# BeforeDelete<!-- -->

### Callable

* ****BeforeDelete**(): (target, method) => void

***

* Called before deleting entity, but only when providing initialized entity to EM#remove()

  ***

  #### Returns (target, method) => void

  * * **(target, method): void

    - #### Parameters

      * ##### target: any
      * ##### method: string

      #### Returns void
