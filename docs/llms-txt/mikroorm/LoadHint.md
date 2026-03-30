# Source: https://mikro-orm.io/api/core/interface/LoadHint.md

# LoadHint<!-- --> \<Entity, Hint, Fields, Excludes>

### Hierarchy

* *LoadHint*
  * [FindOptions](https://mikro-orm.io/api/core/interface/FindOptions.md)

## Index[**](#index)

### Properties

* [**exclude](#exclude)
* [**fields](#fields)
* [**populate](#populate)

## Properties<!-- -->[**](#properties)

### [**](#exclude)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L229)optionalexclude

**exclude?

<!-- -->

: readonly

<!-- -->

[AutoPath](https://mikro-orm.io/api/core.md#AutoPath)\<Entity, Excludes, never, 9>\[]

### [**](#fields)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L228)optionalfields

**fields?

<!-- -->

: readonly

<!-- -->

[AutoPath](https://mikro-orm.io/api/core.md#AutoPath)\<Entity, Fields, \*, 9>\[]

### [**](#populate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L227)optionalpopulate

**populate?

<!-- -->

: [Populate](https://mikro-orm.io/api/core.md#Populate)\<Entity, Hint>
