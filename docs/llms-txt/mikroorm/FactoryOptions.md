# Source: https://mikro-orm.io/api/core/interface/FactoryOptions.md

# FactoryOptions<!-- -->

## Index[**](#index)

### Properties

* [**convertCustomTypes](#convertCustomTypes)
* [**initialized](#initialized)
* [**key](#key)
* [**merge](#merge)
* [**newEntity](#newEntity)
* [**normalizeAccessors](#normalizeAccessors)
* [**parentSchema](#parentSchema)
* [**processOnCreateHooksEarly](#processOnCreateHooksEarly)
* [**recomputeSnapshot](#recomputeSnapshot)
* [**refresh](#refresh)
* [**schema](#schema)

## Properties<!-- -->[**](#properties)

### [**](#convertCustomTypes)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityFactory.ts#L39)optionalconvertCustomTypes

**convertCustomTypes?

<!-- -->

: boolean

### [**](#initialized)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityFactory.ts#L30)optionalinitialized

**initialized?

<!-- -->

: boolean

### [**](#key)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityFactory.ts#L48)optionalkey

**key?

<!-- -->

: string

Property name to use for identity map lookup instead of the primary key. This is useful for creating references by unique non-PK properties.

### [**](#merge)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityFactory.ts#L37)optionalmerge

**merge?

<!-- -->

: boolean

### [**](#newEntity)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityFactory.ts#L31)optionalnewEntity

**newEntity?

<!-- -->

: boolean

### [**](#normalizeAccessors)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityFactory.ts#L43)optionalnormalizeAccessors

**normalizeAccessors?

<!-- -->

: boolean

### [**](#parentSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityFactory.ts#L42)optionalparentSchema

**parentSchema?

<!-- -->

: string

### [**](#processOnCreateHooksEarly)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityFactory.ts#L36)optionalprocessOnCreateHooksEarly

**processOnCreateHooksEarly?

<!-- -->

: boolean

Property `onCreate` hooks are normally executed during `flush` operation. With this option, they will be processed early inside `em.create()` method.

### [**](#recomputeSnapshot)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityFactory.ts#L40)optionalrecomputeSnapshot

**recomputeSnapshot?

<!-- -->

: boolean

### [**](#refresh)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityFactory.ts#L38)optionalrefresh

**refresh?

<!-- -->

: boolean

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityFactory.ts#L41)optionalschema

**schema?

<!-- -->

: string
