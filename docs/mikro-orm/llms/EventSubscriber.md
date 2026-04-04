# Source: https://mikro-orm.io/api/core/interface/EventSubscriber.md

# EventSubscriber<!-- --> \<T>

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
* [**getSubscribedEntities](#getSubscribedEntities)
* [**onFlush](#onFlush)
* [**onInit](#onInit)
* [**onLoad](#onLoad)

## Methods<!-- -->[**](#Methods)

### [**](#afterCreate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L27)optionalafterCreate

* ****afterCreate**(args): void | Promise\<void>

- #### Parameters

  * ##### args: [EventArgs](https://mikro-orm.io/api/core/interface/EventArgs.md)\<T>

  #### Returns void | Promise\<void>

### [**](#afterDelete)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L33)optionalafterDelete

* ****afterDelete**(args): void | Promise\<void>

- #### Parameters

  * ##### args: [EventArgs](https://mikro-orm.io/api/core/interface/EventArgs.md)\<T>

  #### Returns void | Promise\<void>

### [**](#afterFlush)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L36)optionalafterFlush

* ****afterFlush**(args): void | Promise\<void>

- #### Parameters

  * ##### args: [FlushEventArgs](https://mikro-orm.io/api/core/interface/FlushEventArgs.md)

  #### Returns void | Promise\<void>

### [**](#afterTransactionCommit)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L41)optionalafterTransactionCommit

* ****afterTransactionCommit**(args): void | Promise\<void>

- #### Parameters

  * ##### args: [TransactionEventArgs](https://mikro-orm.io/api/core/interface/TransactionEventArgs.md)

  #### Returns void | Promise\<void>

### [**](#afterTransactionRollback)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L43)optionalafterTransactionRollback

* ****afterTransactionRollback**(args): void | Promise\<void>

- #### Parameters

  * ##### args: [TransactionEventArgs](https://mikro-orm.io/api/core/interface/TransactionEventArgs.md)

  #### Returns void | Promise\<void>

### [**](#afterTransactionStart)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L39)optionalafterTransactionStart

* ****afterTransactionStart**(args): void | Promise\<void>

- #### Parameters

  * ##### args: [TransactionEventArgs](https://mikro-orm.io/api/core/interface/TransactionEventArgs.md)

  #### Returns void | Promise\<void>

### [**](#afterUpdate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L29)optionalafterUpdate

* ****afterUpdate**(args): void | Promise\<void>

- #### Parameters

  * ##### args: [EventArgs](https://mikro-orm.io/api/core/interface/EventArgs.md)\<T>

  #### Returns void | Promise\<void>

### [**](#afterUpsert)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L31)optionalafterUpsert

* ****afterUpsert**(args): void | Promise\<void>

- #### Parameters

  * ##### args: [EventArgs](https://mikro-orm.io/api/core/interface/EventArgs.md)\<T>

  #### Returns void | Promise\<void>

### [**](#beforeCreate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L26)optionalbeforeCreate

* ****beforeCreate**(args): void | Promise\<void>

- #### Parameters

  * ##### args: [EventArgs](https://mikro-orm.io/api/core/interface/EventArgs.md)\<T>

  #### Returns void | Promise\<void>

### [**](#beforeDelete)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L32)optionalbeforeDelete

* ****beforeDelete**(args): void | Promise\<void>

- #### Parameters

  * ##### args: [EventArgs](https://mikro-orm.io/api/core/interface/EventArgs.md)\<T>

  #### Returns void | Promise\<void>

### [**](#beforeFlush)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L34)optionalbeforeFlush

* ****beforeFlush**(args): void | Promise\<void>

- #### Parameters

  * ##### args: [FlushEventArgs](https://mikro-orm.io/api/core/interface/FlushEventArgs.md)

  #### Returns void | Promise\<void>

### [**](#beforeTransactionCommit)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L40)optionalbeforeTransactionCommit

* ****beforeTransactionCommit**(args): void | Promise\<void>

- #### Parameters

  * ##### args: [TransactionEventArgs](https://mikro-orm.io/api/core/interface/TransactionEventArgs.md)

  #### Returns void | Promise\<void>

### [**](#beforeTransactionRollback)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L42)optionalbeforeTransactionRollback

* ****beforeTransactionRollback**(args): void | Promise\<void>

- #### Parameters

  * ##### args: [TransactionEventArgs](https://mikro-orm.io/api/core/interface/TransactionEventArgs.md)

  #### Returns void | Promise\<void>

### [**](#beforeTransactionStart)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L38)optionalbeforeTransactionStart

* ****beforeTransactionStart**(args): void | Promise\<void>

- #### Parameters

  * ##### args: [TransactionEventArgs](https://mikro-orm.io/api/core/interface/TransactionEventArgs.md)

  #### Returns void | Promise\<void>

### [**](#beforeUpdate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L28)optionalbeforeUpdate

* ****beforeUpdate**(args): void | Promise\<void>

- #### Parameters

  * ##### args: [EventArgs](https://mikro-orm.io/api/core/interface/EventArgs.md)\<T>

  #### Returns void | Promise\<void>

### [**](#beforeUpsert)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L30)optionalbeforeUpsert

* ****beforeUpsert**(args): void | Promise\<void>

- #### Parameters

  * ##### args: [EventArgs](https://mikro-orm.io/api/core/interface/EventArgs.md)\<T>

  #### Returns void | Promise\<void>

### [**](#getSubscribedEntities)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L23)optionalgetSubscribedEntities

* ****getSubscribedEntities**(): [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>\[]

- #### Returns [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>\[]

### [**](#onFlush)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L35)optionalonFlush

* ****onFlush**(args): void | Promise\<void>

- #### Parameters

  * ##### args: [FlushEventArgs](https://mikro-orm.io/api/core/interface/FlushEventArgs.md)

  #### Returns void | Promise\<void>

### [**](#onInit)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L24)optionalonInit

* ****onInit**(args): void

- #### Parameters

  * ##### args: [EventArgs](https://mikro-orm.io/api/core/interface/EventArgs.md)\<T>

  #### Returns void

### [**](#onLoad)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L25)optionalonLoad

* ****onLoad**(args): void | Promise\<void>

- #### Parameters

  * ##### args: [EventArgs](https://mikro-orm.io/api/core/interface/EventArgs.md)\<T>

  #### Returns void | Promise\<void>
