# Source: https://mikro-orm.io/api/core/interface/SerializeOptions.md

# SerializeOptions<!-- --> \<T, P, E>

## Index[**](#Index)

### Properties

* [**exclude](#exclude)
* [**forceObject](#forceObject)
* [**groups](#groups)
* [**ignoreSerializers](#ignoreSerializers)
* [**includeHidden](#includeHidden)
* [**populate](#populate)
* [**skipNull](#skipNull)

## Properties<!-- -->[**](#Properties)

### [**](#exclude)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/serialization/EntitySerializer.ts#L292)optionalexclude

**exclude?

<!-- -->

: readonly

<!-- -->

[AutoPath](https://mikro-orm.io/api/core.md#AutoPath)\<T, E, never, 9>\[]

Specify which properties should be omitted.

### [**](#forceObject)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/serialization/EntitySerializer.ts#L295)optionalforceObject

**forceObject?

<!-- -->

: boolean

Enforce unpopulated references to be returned as objects, e.g. `{ author: { id: 1 } }` instead of `{ author: 1 }`.

### [**](#groups)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/serialization/EntitySerializer.ts#L307)optionalgroups

**groups?

<!-- -->

: string\[]

Only include properties for a specific group. If a property does not specify any group, it will be included, otherwise only properties with a matching group are included.

### [**](#ignoreSerializers)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/serialization/EntitySerializer.ts#L298)optionalignoreSerializers

**ignoreSerializers?

<!-- -->

: boolean

Ignore custom property serializers.

### [**](#includeHidden)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/serialization/EntitySerializer.ts#L301)optionalincludeHidden

**includeHidden?

<!-- -->

: boolean

Include properties marked as `hidden`.

### [**](#populate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/serialization/EntitySerializer.ts#L289)optionalpopulate

**populate?

<!-- -->

: readonly

<!-- -->

[AutoPath](https://mikro-orm.io/api/core.md#AutoPath)\<T, P, \*, 9>\[]

Specify which relation should be serialized as populated and which as a FK.

### [**](#skipNull)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/serialization/EntitySerializer.ts#L304)optionalskipNull

**skipNull?

<!-- -->

: boolean

Skip properties with `null` value.
