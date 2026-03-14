# Source: https://mikro-orm.io/api/core/interface/SeederOptions.md

# SeederOptions<!-- -->

Configuration options for database seeders.

* **@see**

  <https://mikro-orm.io/docs/seeding>

## Index[**](#index)

### Properties

* [**defaultSeeder](#defaultSeeder)
* [**emit](#emit)
* [**fileName](#fileName)
* [**glob](#glob)
* [**path](#path)
* [**pathTs](#pathTs)
* [**seedersList](#seedersList)

## Properties<!-- -->[**](#properties)

### [**](#defaultSeeder)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L672)optionaldefaultSeeder

**defaultSeeder?

<!-- -->

: string = ‘DatabaseSeeder’

Name of the default seeder class to run.

### [**](#emit)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L677)optionalemit

**emit?

<!-- -->

: js | ts = js | ts

File extension for generated seeder files.

### [**](#fileName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L682)optionalfileName

**fileName?

<!-- -->

: (className) => string = (className) => string

Custom function to generate seeder file names.

***

#### Type declaration

* * **(className): string

  * #### Parameters

    * ##### className: string

    #### Returns string

### [**](#glob)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L667)optionalglob

**glob?

<!-- -->

: string = ’!(\*.d).{js,ts}’

Glob pattern to match seeder files.

### [**](#path)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L657)optionalpath

**path?

<!-- -->

: string = ’./seeders’

Path to the folder with seeder files (for compiled JavaScript files).

### [**](#pathTs)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L662)optionalpathTs

**pathTs?

<!-- -->

: string

Path to the folder with seeder files (for TypeScript source files). Used when running in TypeScript mode.

### [**](#seedersList)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L684)optionalseedersList

**seedersList?

<!-- -->

: ([Constructor](https://mikro-orm.io/api/core.md#Constructor)\<Seeder<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<any>>> | [SeederObject](https://mikro-orm.io/api/core/interface/SeederObject.md))\[]

List of seeder classes or objects to use instead of file-based discovery.
