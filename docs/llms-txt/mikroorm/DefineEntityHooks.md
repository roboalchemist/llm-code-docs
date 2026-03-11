# Source: https://mikro-orm.io/api/core/interface/DefineEntityHooks.md

# DefineEntityHooks<!-- --> \<T>

## Index[**](#index)

### Properties

* [**afterCreate](#afterCreate)
* [**afterDelete](#afterDelete)
* [**afterUpdate](#afterUpdate)
* [**afterUpsert](#afterUpsert)
* [**beforeCreate](#beforeCreate)
* [**beforeDelete](#beforeDelete)
* [**beforeUpdate](#beforeUpdate)
* [**beforeUpsert](#beforeUpsert)
* [**onInit](#onInit)
* [**onLoad](#onLoad)

## Properties<!-- -->[**](#properties)

### [**](#afterCreate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1322)optionalafterCreate

**afterCreate?

<!-- -->

: EntityHookValue\<T, afterCreate>

### [**](#afterDelete)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1328)optionalafterDelete

**afterDelete?

<!-- -->

: EntityHookValue\<T, afterDelete>

### [**](#afterUpdate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1324)optionalafterUpdate

**afterUpdate?

<!-- -->

: EntityHookValue\<T, afterUpdate>

### [**](#afterUpsert)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1326)optionalafterUpsert

**afterUpsert?

<!-- -->

: EntityHookValue\<T, afterUpsert>

### [**](#beforeCreate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1321)optionalbeforeCreate

**beforeCreate?

<!-- -->

: EntityHookValue\<T, beforeCreate>

### [**](#beforeDelete)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1327)optionalbeforeDelete

**beforeDelete?

<!-- -->

: EntityHookValue\<T, beforeDelete>

### [**](#beforeUpdate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1323)optionalbeforeUpdate

**beforeUpdate?

<!-- -->

: EntityHookValue\<T, beforeUpdate>

### [**](#beforeUpsert)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1325)optionalbeforeUpsert

**beforeUpsert?

<!-- -->

: EntityHookValue\<T, beforeUpsert>

### [**](#onInit)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1319)optionalonInit

**onInit?

<!-- -->

: EntityHookValue\<T, onInit>

### [**](#onLoad)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1320)optionalonLoad

**onLoad?

<!-- -->

: EntityHookValue\<T, onLoad>
