# Source: https://mikro-orm.io/api/core/interface/AssignOptions.md

# AssignOptions<!-- --> \<Convert>

## Index[**](#Index)

### Properties

* [**convertCustomTypes](#convertCustomTypes)
* [**em](#em)
* [**ignoreUndefined](#ignoreUndefined)
* [**merge](#merge)
* [**mergeEmbeddedProperties](#mergeEmbeddedProperties)
* [**mergeObjectProperties](#mergeObjectProperties)
* [**onlyOwnProperties](#onlyOwnProperties)
* [**onlyProperties](#onlyProperties)
* [**schema](#schema)
* [**updateByPrimaryKey](#updateByPrimaryKey)
* [**updateNestedEntities](#updateNestedEntities)

## Properties<!-- -->[**](#Properties)

### [**](#convertCustomTypes)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityAssigner.ts#L350)optionalconvertCustomTypes

**convertCustomTypes?

<!-- -->

: Convert

`assign` excepts runtime values for properties using custom types. To be able to assign raw database values, you can enable the `convertCustomTypes` option. Defaults to `false`.

### [**](#em)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityAssigner.ts#L386)optionalem

**em?

<!-- -->

: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

When using the static `assign()` helper, you can pass the EntityManager instance explicitly via the `em` option. This is only needed when you try to assign a relation property. The value is automatically inferred from the target entity when it is managed, or when you use `em.assign()` instead.

### [**](#ignoreUndefined)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityAssigner.ts#L344)optionalignoreUndefined

**ignoreUndefined?

<!-- -->

: boolean

With `ignoreUndefined` enabled, `undefined` properties passed in the payload are skipped. Defaults to `false`.

### [**](#merge)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityAssigner.ts#L371)optionalmerge

**merge?

<!-- -->

: boolean

When assigning to a relation property, if the value is a POJO and `updateByPrimaryKey` is enabled, we check if the target exists in the identity map based on its primary key and call `assign` on it recursively. If there is no primary key provided, or the entity is not present in the context, such an entity is considered as new (resulting in `INSERT` query), created via `em.create()`. You can use `merge: true` to use `em.merge()` instead, which means there won't be any query used for persisting the relation. Defaults to `false`.

### [**](#mergeEmbeddedProperties)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityAssigner.ts#L362)optionalmergeEmbeddedProperties

**mergeEmbeddedProperties?

<!-- -->

: boolean

When assigning to an embedded property, the values are deeply merged with the existing data. Use `mergeEmbeddedProperties: false` to replace them instead. Defaults to `true`.

### [**](#mergeObjectProperties)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityAssigner.ts#L356)optionalmergeObjectProperties

**mergeObjectProperties?

<!-- -->

: boolean

When assigning to a JSON property, the value is replaced. Use `mergeObjectProperties: true` to enable deep merging of the payload with the existing value. Defaults to `false`.

### [**](#onlyOwnProperties)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityAssigner.ts#L339)optionalonlyOwnProperties

**onlyOwnProperties?

<!-- -->

: boolean

With `onlyOwnProperties` enabled, inverse sides of to-many relations are skipped, and payloads of other relations are converted to foreign keys. Defaults to `false`.

### [**](#onlyProperties)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityAssigner.ts#L333)optionalonlyProperties

**onlyProperties?

<!-- -->

: boolean

When you have some properties in the payload that are not represented by an entity property mapping, you can skip such unknown properties via `onlyProperties: true`. Defaults to `false`.

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityAssigner.ts#L379)optionalschema

**schema?

<!-- -->

: string

When assigning to a to-many relation properties (`Collection`) with `updateNestedEntities` and `updateByPrimaryKey` enabled (default), you can use this option to override the relation schema. This is used only when trying to find the entity reference in the current context. If it is not found, we create the relation entity using the target entity schema. The value is automatically inferred from the target entity.

### [**](#updateByPrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityAssigner.ts#L327)optionalupdateByPrimaryKey

**updateByPrimaryKey?

<!-- -->

: boolean

When assigning to a relation property with object payload and `updateNestedEntities` enabled (default), you can control how a payload without a primary key is handled. By default, it is considered as a new object, resulting in an `INSERT` query. Use `updateByPrimaryKey: false` to allow assigning the data on an existing relation instead. Defaults to `true`.

### [**](#updateNestedEntities)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityAssigner.ts#L319)optionalupdateNestedEntities

**updateNestedEntities?

<!-- -->

: boolean

Allows disabling processing of nested relations. When disabled, an object payload in place of a relation always results in an `INSERT` query. To assign a value of the relation, use the foreign key instead of an object. Defaults to `true`.
