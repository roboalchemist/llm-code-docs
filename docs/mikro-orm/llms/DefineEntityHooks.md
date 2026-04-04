# Source: https://mikro-orm.io/api/core/interface/DefineEntityHooks.md

# DefineEntityHooks<!-- --> \<T>

### Hierarchy

* Partial\<MapToArray\<Pick<[EventSubscriber](https://mikro-orm.io/api/core/interface/EventSubscriber.md)\<T>, keyof
  <!-- -->
  typeof [EventType](https://mikro-orm.io/api/core/enum/EventType.md)>>>
  * *DefineEntityHooks*

## Index[**](#Index)

### Methods

* [**afterCreate](#afterCreate)
* [**afterDelete](#afterDelete)
* [**afterFlush](#afterFlush)
* [**afterTransactionCommit](#afterTransactionCommit)
* [**afterTransactionRollback](#afterTransactionRollback)
* [**afterTransactionStart](#afterTransactionStart)
* [**afterUpdate](#afterUpdate)
* [**afterUpsert](#afterUpsert)
* [**beforeCreate](#beforeCreate)
* [**beforeDelete](#beforeDelete)
* [**beforeFlush](#beforeFlush)
* [**beforeTransactionCommit](#beforeTransactionCommit)
* [**beforeTransactionRollback](#beforeTransactionRollback)
* [**beforeTransactionStart](#beforeTransactionStart)
* [**beforeUpdate](#beforeUpdate)
* [**beforeUpsert](#beforeUpsert)
* [**onFlush](#onFlush)
* [**onInit](#onInit)
* [**onLoad](#onLoad)

## Methods<!-- -->[**](#Methods)

### [**](#afterCreate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L27)optionalinheritedafterCreate

**afterCreate?

<!-- -->

:

Inherited from Partial.afterCreate

### [**](#afterDelete)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L33)optionalinheritedafterDelete

**afterDelete?

<!-- -->

:

Inherited from Partial.afterDelete

### [**](#afterFlush)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L36)optionalinheritedafterFlush

**afterFlush?

<!-- -->

:

Inherited from Partial.afterFlush

### [**](#afterTransactionCommit)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L41)optionalinheritedafterTransactionCommit

**afterTransactionCommit?

<!-- -->

:

Inherited from Partial.afterTransactionCommit

### [**](#afterTransactionRollback)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L43)optionalinheritedafterTransactionRollback

**afterTransactionRollback?

<!-- -->

:

Inherited from Partial.afterTransactionRollback

### [**](#afterTransactionStart)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L39)optionalinheritedafterTransactionStart

**afterTransactionStart?

<!-- -->

:

Inherited from Partial.afterTransactionStart

### [**](#afterUpdate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L29)optionalinheritedafterUpdate

**afterUpdate?

<!-- -->

:

Inherited from Partial.afterUpdate

### [**](#afterUpsert)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L31)optionalinheritedafterUpsert

**afterUpsert?

<!-- -->

:

Inherited from Partial.afterUpsert

### [**](#beforeCreate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L26)optionalinheritedbeforeCreate

**beforeCreate?

<!-- -->

:

Inherited from Partial.beforeCreate

### [**](#beforeDelete)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L32)optionalinheritedbeforeDelete

**beforeDelete?

<!-- -->

:

Inherited from Partial.beforeDelete

### [**](#beforeFlush)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L34)optionalinheritedbeforeFlush

**beforeFlush?

<!-- -->

:

Inherited from Partial.beforeFlush

### [**](#beforeTransactionCommit)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L40)optionalinheritedbeforeTransactionCommit

**beforeTransactionCommit?

<!-- -->

:

Inherited from Partial.beforeTransactionCommit

### [**](#beforeTransactionRollback)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L42)optionalinheritedbeforeTransactionRollback

**beforeTransactionRollback?

<!-- -->

:

Inherited from Partial.beforeTransactionRollback

### [**](#beforeTransactionStart)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L38)optionalinheritedbeforeTransactionStart

**beforeTransactionStart?

<!-- -->

:

Inherited from Partial.beforeTransactionStart

### [**](#beforeUpdate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L28)optionalinheritedbeforeUpdate

**beforeUpdate?

<!-- -->

:

Inherited from Partial.beforeUpdate

### [**](#beforeUpsert)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L30)optionalinheritedbeforeUpsert

**beforeUpsert?

<!-- -->

:

Inherited from Partial.beforeUpsert

### [**](#onFlush)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L35)optionalinheritedonFlush

**onFlush?

<!-- -->

:

Inherited from Partial.onFlush

### [**](#onInit)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L24)optionalinheritedonInit

**onInit?

<!-- -->

:

Inherited from Partial.onInit

### [**](#onLoad)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L25)optionalinheritedonLoad

**onLoad?

<!-- -->

:

Inherited from Partial.onLoad
