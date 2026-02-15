# Source: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkstore/index.md

---

title: RTKStore · Cloudflare Realtime docs
lastUpdated: 2026-02-10T18:29:47.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkstore/
  md: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkstore/index.md
---

[]()

This module represents a single global store. The store can be accessed from the `meeting.stores` module.

**Returns**: An instance of RTKStore.\
**Example**

```js
const handRaiseRTKStore = meeting.stores.stores.get('handRaise');
```

* [RTKStore](#module_RTKStore) ⇒

  * [module.exports](#exp_module_RTKStore--module.exports) ⏏

    * [new module.exports(args)](#new_module_RTKStore--module.exports_new)
    * [.set(key, value, \[sync\], \[emit\])](#module_RTKStore--module.exports+set) ⇒ `Promise.<void>`
    * [.bulkSet(data)](#module_RTKStore--module.exports+bulkSet) ⇒ `Promise.<void>`
    * [.update(key, value, \[sync\])](#module_RTKStore--module.exports+update) ⇒ `Promise.<void>`
    * [.delete(key, \[sync\], \[emit\])](#module_RTKStore--module.exports+delete) ⇒ `Promise.<void>`
    * [.bulkDelete(data)](#module_RTKStore--module.exports+bulkDelete) ⇒ `Promise.<void>`
    * [.get(key)](#module_RTKStore--module.exports+get) ⇒ `any`
    * [.getAll()](#module_RTKStore--module.exports+getAll) ⇒ `RTKStoreData`
    * [.updateRateLimits(num, period)](#module_RTKStore--module.exports+updateRateLimits)
    * [.updateBulkRateLimits(num, period)](#module_RTKStore--module.exports+updateBulkRateLimits)
    * [.subscribe(key, cb)](#module_RTKStore--module.exports+subscribe) ⇒ `void`
    * [.unsubscribe(key, \[cb\])](#module_RTKStore--module.exports+unsubscribe) ⇒ `void`
    * [.populate(data)](#module_RTKStore--module.exports+populate)

[]()

### module.exports ⏏

**Kind**: Exported class\
[]()

#### new module.exports(args)

| Param | Type |
| - | - |
| args | `Object` |
| args.name | `string` |
| args.socketHandler | `PluginSocketHandler` |
| args.meetingId | `string` |

[]()

#### module.exports.set(key, value, \[sync], \[emit]) ⇒ `Promise.<void>`

Sets a value in the store.

**Kind**: instance method of [`module.exports`](#exp_module_RTKStore--module.exports)\
**Returns**: `Promise.<void>` - A promise.

| Param | Type | Default | Description |
| - | - | - | - |
| key | `string` | | Unique identifier used to store value. |
| value | `any` | | Data to be set. |
| \[sync] | `boolean` | `true` | Whether to sync change to remote store. |
| \[emit] | `boolean` | `false` | Whether to emit to local subscribers. |

[]()

#### module.exports.bulkSet(data) ⇒ `Promise.<void>`

Sets multiple values in the store.

**Kind**: instance method of [`module.exports`](#exp_module_RTKStore--module.exports)\
**Returns**: `Promise.<void>` - A promise.

| Param | Type |
| - | - |
| data | `Array.<{key: string, payload: any}>` |

[]()

#### module.exports.update(key, value, \[sync]) ⇒ `Promise.<void>`

Updates an already existing value in the store. If the value stored is `['a', 'b']`, the operation `store.update(key, ['c'])` will modify the value to `['a','b','c']`.

**Kind**: instance method of [`module.exports`](#exp_module_RTKStore--module.exports)\
**Returns**: `Promise.<void>` - A promise.

| Param | Type | Default | Description |
| - | - | - | - |
| key | `string` | | Unique identifier used to store value. |
| value | `any` | | Data to be updated. |
| \[sync] | `boolean` | `true` | Whether to sync change to remote store. |

[]()

#### module.exports.delete(key, \[sync], \[emit]) ⇒ `Promise.<void>`

Deletes a key value pair form the store.

**Kind**: instance method of [`module.exports`](#exp_module_RTKStore--module.exports)\
**Returns**: `Promise.<void>` - A promise.

| Param | Type | Default | Description |
| - | - | - | - |
| key | `string` | | Unique identifier used to store value. |
| \[sync] | `boolean` | `true` | Whether to sync change to remote store. |
| \[emit] | `boolean` | `false` | Whether to emit to local subscribers. |

[]()

#### module.exports.bulkDelete(data) ⇒ `Promise.<void>`

Deletes multiple values from the store.

**Kind**: instance method of [`module.exports`](#exp_module_RTKStore--module.exports)\
**Returns**: `Promise.<void>` - A promise.

| Param | Type |
| - | - |
| data | `Array.<{key: string}>` |

[]()

#### module.exports.get(key) ⇒ `any`

Returns value for the given key.

**Kind**: instance method of [`module.exports`](#exp_module_RTKStore--module.exports)\
**Returns**: `any` - Value for the given key.

| Param | Type | Description |
| - | - | - |
| key | `string` | Unique identifier used to store value. |

[]()

#### module.exports.getAll() ⇒ `RTKStoreData`

Returns the entire store.

**Kind**: instance method of [`module.exports`](#exp_module_RTKStore--module.exports)\
**Returns**: `RTKStoreData` - An instance of RTKStoreData.\
[]()

#### module.exports.updateRateLimits(num, period)

**Kind**: instance method of [`module.exports`](#exp_module_RTKStore--module.exports)

| Param | Type |
| - | - |
| num | `number` |
| period | `number` |

[]()

#### module.exports.updateBulkRateLimits(num, period)

**Kind**: instance method of [`module.exports`](#exp_module_RTKStore--module.exports)

| Param | Type |
| - | - |
| num | `number` |
| period | `number` |

[]()

#### module.exports.subscribe(key, cb) ⇒ `void`

Listens for data change on a store key.

**Kind**: instance method of [`module.exports`](#exp_module_RTKStore--module.exports)\
**Returns**: `void` - void

| Param | Type | Description |
| - | - | - |
| key | `string` | Unique identifier used to store value. |
| cb | `function` | The callback function that gets executed when data is modified. |

[]()

#### module.exports.unsubscribe(key, \[cb]) ⇒ `void`

Removes all listeners for a key on the store.

**Kind**: instance method of [`module.exports`](#exp_module_RTKStore--module.exports)\
**Returns**: `void` - void

| Param | Type | Description |
| - | - | - |
| key | `string` | Unique identifier used to store value. |
| \[cb] | `function` | Callback to be removed. |

[]()

#### module.exports.populate(data)

**Kind**: instance method of [`module.exports`](#exp_module_RTKStore--module.exports)

| Param | Type |
| - | - |
| data | `RTKStoreData` |
