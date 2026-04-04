# Source: https://mikro-orm.io/api/core/interface/ISeedManager.md

# ISeedManager<!-- -->

### Implemented by

* [SeedManager](https://mikro-orm.io/api/seeder/class/SeedManager.md)

## Index[**](#Index)

### Methods

* [**createSeeder](#createSeeder)
* [**seed](#seed)

## Methods<!-- -->[**](#Methods)

### [**](#createSeeder)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L1330)createSeeder

* ****createSeeder**(className): Promise\<string>

- #### Parameters

  * ##### className: string

  #### Returns Promise\<string>

### [**](#seed)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L1327)seed

* ****seed**(...classNames): Promise\<void>

- #### Parameters

  * ##### rest...classNames: [Constructor](https://mikro-orm.io/api/core.md#Constructor)\<Seeder<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<any>>>\[]

  #### Returns Promise\<void>
