# Source: https://mikro-orm.io/api/core/interface/ISeedManager.md

# ISeedManager<!-- -->

### Implemented by

* [SeedManager](https://mikro-orm.io/api/seeder/class/SeedManager.md)

## Index[**](#index)

### Methods

* [**create](#create)
* [**seed](#seed)

## Methods<!-- -->[**](#methods)

### [**](#create)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1862)create

* ****create**(className): Promise\<string>

* #### Parameters

  * ##### className: string

  #### Returns Promise\<string>

### [**](#seed)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1859)seed

* ****seed**(...classNames): Promise\<void>

* #### Parameters

  * ##### rest...classNames: [Constructor](https://mikro-orm.io/api/core.md#Constructor)\<Seeder<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<any>>>\[]

  #### Returns Promise\<void>
