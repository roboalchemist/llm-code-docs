# Source: https://mikro-orm.io/api/core/interface/LoadHint.md

# LoadHint<!-- --> \<Entity, Hint, Fields, Excludes>

### Hierarchy

* *LoadHint*
  * [FindOptions](https://mikro-orm.io/api/core/interface/FindOptions.md)

## Index[**](#Index)

### Properties

* [**exclude](#exclude)
* [**fields](#fields)
* [**populate](#populate)

## Properties<!-- -->[**](#Properties)

### [**](#exclude)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L112)optionalexclude

**exclude?

<!-- -->

: readonly

<!-- -->

[AutoPath](https://mikro-orm.io/api/core.md#AutoPath)\<Entity, Excludes, never, 9>\[]

### [**](#fields)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L111)optionalfields

**fields?

<!-- -->

: readonly

<!-- -->

[AutoPath](https://mikro-orm.io/api/core.md#AutoPath)\<Entity, Fields, \*, 9>\[]

### [**](#populate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L110)optionalpopulate

**populate?

<!-- -->

: [Populate](https://mikro-orm.io/api/core.md#Populate)\<Entity, Hint>
