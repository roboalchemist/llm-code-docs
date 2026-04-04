# Source: https://mikro-orm.io/api/core/interface/FactoryOptions.md

# FactoryOptions<!-- -->

## Index[**](#Index)

### Properties

* [**convertCustomTypes](#convertCustomTypes)
* [**initialized](#initialized)
* [**merge](#merge)
* [**newEntity](#newEntity)
* [**normalizeAccessors](#normalizeAccessors)
* [**parentSchema](#parentSchema)
* [**processOnCreateHooksEarly](#processOnCreateHooksEarly)
* [**recomputeSnapshot](#recomputeSnapshot)
* [**refresh](#refresh)
* [**schema](#schema)

## Properties<!-- -->[**](#Properties)

### [**](#convertCustomTypes)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityFactory.ts#L40)optionalconvertCustomTypes

**convertCustomTypes?

<!-- -->

: boolean

### [**](#initialized)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityFactory.ts#L31)optionalinitialized

**initialized?

<!-- -->

: boolean

### [**](#merge)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityFactory.ts#L38)optionalmerge

**merge?

<!-- -->

: boolean

### [**](#newEntity)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityFactory.ts#L32)optionalnewEntity

**newEntity?

<!-- -->

: boolean

### [**](#normalizeAccessors)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityFactory.ts#L44)optionalnormalizeAccessors

**normalizeAccessors?

<!-- -->

: boolean

### [**](#parentSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityFactory.ts#L43)optionalparentSchema

**parentSchema?

<!-- -->

: string

### [**](#processOnCreateHooksEarly)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityFactory.ts#L37)optionalprocessOnCreateHooksEarly

**processOnCreateHooksEarly?

<!-- -->

: boolean

Property `onCreate` hooks are normally executed during `flush` operation. With this option, they will be processed early inside `em.create()` method.

### [**](#recomputeSnapshot)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityFactory.ts#L41)optionalrecomputeSnapshot

**recomputeSnapshot?

<!-- -->

: boolean

### [**](#refresh)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityFactory.ts#L39)optionalrefresh

**refresh?

<!-- -->

: boolean

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityFactory.ts#L42)optionalschema

**schema?

<!-- -->

: string
