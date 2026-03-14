# Source: https://mikro-orm.io/api/core/interface/SerializeOptions.md

# SerializeOptions<!-- --> \<T, P, E>

## Index[**](#index)

### Properties

* [**convertCustomTypes](#convertCustomTypes)
* [**exclude](#exclude)
* [**forceObject](#forceObject)
* [**groups](#groups)
* [**ignoreSerializers](#ignoreSerializers)
* [**includeHidden](#includeHidden)
* [**populate](#populate)
* [**skipNull](#skipNull)

## Properties<!-- -->[**](#properties)

### [**](#convertCustomTypes)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/serialization/EntitySerializer.ts#L374)optionalconvertCustomTypes

**convertCustomTypes?

<!-- -->

: boolean

Convert custom types to their database representation. By default, the `Type.toJSON` method is invoked instead.

### [**](#exclude)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/serialization/EntitySerializer.ts#L356)optionalexclude

**exclude?

<!-- -->

: readonly

<!-- -->

[AutoPath](https://mikro-orm.io/api/core.md#AutoPath)\<T, E, never, 9>\[]

Specify which properties should be omitted.

### [**](#forceObject)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/serialization/EntitySerializer.ts#L359)optionalforceObject

**forceObject?

<!-- -->

: boolean

Enforce unpopulated references to be returned as objects, e.g. `{ author: { id: 1 } }` instead of `{ author: 1 }`.

### [**](#groups)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/serialization/EntitySerializer.ts#L371)optionalgroups

**groups?

<!-- -->

: string\[]

Only include properties for a specific group. If a property does not specify any group, it will be included, otherwise only properties with a matching group are included.

### [**](#ignoreSerializers)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/serialization/EntitySerializer.ts#L362)optionalignoreSerializers

**ignoreSerializers?

<!-- -->

: boolean

Ignore custom property serializers.

### [**](#includeHidden)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/serialization/EntitySerializer.ts#L365)optionalincludeHidden

**includeHidden?

<!-- -->

: boolean

Include properties marked as `hidden`.

### [**](#populate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/serialization/EntitySerializer.ts#L353)optionalpopulate

**populate?

<!-- -->

: readonly

<!-- -->

[AutoPath](https://mikro-orm.io/api/core.md#AutoPath)\<T, P, \*, 9>\[]

Specify which relation should be serialized as populated and which as a FK.

### [**](#skipNull)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/serialization/EntitySerializer.ts#L368)optionalskipNull

**skipNull?

<!-- -->

: boolean

Skip properties with `null` value.
