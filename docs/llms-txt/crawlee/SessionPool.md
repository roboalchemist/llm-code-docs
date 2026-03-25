# Source: https://crawlee.dev/js/api/core/class/SessionPool.md

# SessionPool<!-- -->

Handles the rotation, creation and persistence of user-like sessions. Creates a pool of [Session](https://crawlee.dev/js/api/core/class/Session.md) instances, that are randomly rotated. When some session is marked as blocked, it is removed and new one is created instead (the pool never returns an unusable session). Learn more in the [Session management guide](https://crawlee.dev/js/docs/guides/session-management.md).

You can create one by calling the [SessionPool.open](https://crawlee.dev/js/api/core/class/SessionPool.md#open) function.

Session pool is already integrated into crawlers, and it can significantly improve your scraper performance with just 2 lines of code.

**Example usage:**

```
const crawler = new CheerioCrawler({
    useSessionPool: true,
    persistCookiesPerSession: true,
    // ...
})
```

You can configure the pool with many options. See the [SessionPoolOptions](https://crawlee.dev/js/api/core/interface/SessionPoolOptions.md). Session pool is by default persisted in default [KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md). If you want to have one pool for all runs you have to specify [SessionPoolOptions.persistStateKeyValueStoreId](https://crawlee.dev/js/api/core/interface/SessionPoolOptions.md#persistStateKeyValueStoreId).

**Advanced usage:**

```
const sessionPool = await SessionPool.open({
    maxPoolSize: 25,
    sessionOptions:{
         maxAgeSecs: 10,
         maxUsageCount: 150, // for example when you know that the site blocks after 150 requests.
    },
    persistStateKeyValueStoreId: 'my-key-value-store-for-sessions',
    persistStateKey: 'my-session-pool',
});

// Get random session from the pool
const session1 = await sessionPool.getSession();
const session2 = await sessionPool.getSession();
const session3 = await sessionPool.getSession();

// Now you can mark the session either failed or successful

// Marks session as bad after unsuccessful usage -> it increases error count (soft retire)
session1.markBad()

// Marks as successful.
session2.markGood()

// Retires session -> session is removed from the pool
session3.retire()
```

\**Default session allocation flow:*

1. Until the `SessionPool` reaches `maxPoolSize`, new sessions are created, provided to the user and added to the pool
2. Blocked/retired sessions stay in the pool but are never provided to the user
3. Once the pool is full (live plus blocked session count reaches `maxPoolSize`), a random session from the pool is provided.
4. If a blocked session would be picked, instead all blocked sessions are evicted from the pool and a new session is created and provided

### Hierarchy

* EventEmitter
  * *SessionPool*

## Index[**](#Index)

### Properties

* [**config](#config)
* [**captureRejections](#captureRejections)
* [**captureRejectionSymbol](#captureRejectionSymbol)
* [**defaultMaxListeners](#defaultMaxListeners)
* [**errorMonitor](#errorMonitor)

### Accessors

* [**retiredSessionsCount](#retiredSessionsCount)
* [**usableSessionsCount](#usableSessionsCount)

### Methods

* [**\[captureRejectionSymbol\]](#\[captureRejectionSymbol])
* [**addListener](#addListener)
* [**addSession](#addSession)
* [**emit](#emit)
* [**eventNames](#eventNames)
* [**getMaxListeners](#getMaxListeners)
* [**getSession](#getSession)
* [**getState](#getState)
* [**initialize](#initialize)
* [**listenerCount](#listenerCount)
* [**listeners](#listeners)
* [**off](#off)
* [**on](#on)
* [**once](#once)
* [**persistState](#persistState)
* [**prependListener](#prependListener)
* [**prependOnceListener](#prependOnceListener)
* [**rawListeners](#rawListeners)
* [**removeAllListeners](#removeAllListeners)
* [**removeListener](#removeListener)
* [**resetStore](#resetStore)
* [**setMaxListeners](#setMaxListeners)
* [**teardown](#teardown)
* [**addAbortListener](#addAbortListener)
* [**getEventListeners](#getEventListeners)
* [**getMaxListeners](#getMaxListeners)
* [**listenerCount](#listenerCount)
* [**on](#on)
* [**once](#once)
* [**open](#open)
* [**setMaxListeners](#setMaxListeners)

## Properties<!-- -->[**](#Properties)

### [**](#config)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session_pool.ts#L160)readonlyconfig

**config: [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md) =

<!-- -->

...

### [**](#captureRejections)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@types/node/events.d.ts#L425)staticexternalinheritedcaptureRejections

**captureRejections: boolean

Inherited from EventEmitter.captureRejections

Value: [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type)

Change the default `captureRejections` option on all new `EventEmitter` objects.

* **@since**

  v13.4.0, v12.16.0

### [**](#captureRejectionSymbol)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@types/node/events.d.ts#L418)staticexternalreadonlyinheritedcaptureRejectionSymbol

**captureRejectionSymbol: typeof captureRejectionSymbol

Inherited from EventEmitter.captureRejectionSymbol

Value: `Symbol.for('nodejs.rejection')`

See how to write a custom `rejection handler`.

* **@since**

  v13.4.0, v12.16.0

### [**](#defaultMaxListeners)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@types/node/events.d.ts#L464)staticexternalinheriteddefaultMaxListeners

**defaultMaxListeners: number

Inherited from EventEmitter.defaultMaxListeners

By default, a maximum of `10` listeners can be registered for any single event. This limit can be changed for individual `EventEmitter` instances using the `emitter.setMaxListeners(n)` method. To change the default for *all*`EventEmitter` instances, the `events.defaultMaxListeners` property can be used. If this value is not a positive number, a `RangeError` is thrown.

Take caution when setting the `events.defaultMaxListeners` because the change affects *all* `EventEmitter` instances, including those created before the change is made. However, calling `emitter.setMaxListeners(n)` still has precedence over `events.defaultMaxListeners`.

This is not a hard limit. The `EventEmitter` instance will allow more listeners to be added but will output a trace warning to stderr indicating that a "possible EventEmitter memory leak" has been detected. For any single `EventEmitter`, the `emitter.getMaxListeners()` and `emitter.setMaxListeners()` methods can be used to temporarily avoid this warning:

```
import { EventEmitter } from 'node:events';
const emitter = new EventEmitter();
emitter.setMaxListeners(emitter.getMaxListeners() + 1);
emitter.once('event', () => {
  // do stuff
  emitter.setMaxListeners(Math.max(emitter.getMaxListeners() - 1, 0));
});
```

The `--trace-warnings` command-line flag can be used to display the stack trace for such warnings.

The emitted warning can be inspected with `process.on('warning')` and will have the additional `emitter`, `type`, and `count` properties, referring to the event emitter instance, the event's name and the number of attached listeners, respectively. Its `name` property is set to `'MaxListenersExceededWarning'`.

* **@since**

  v0.11.2

### [**](#errorMonitor)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@types/node/events.d.ts#L411)staticexternalreadonlyinheritederrorMonitor

**errorMonitor: typeof errorMonitor

Inherited from EventEmitter.errorMonitor

This symbol shall be used to install a listener for only monitoring `'error'` events. Listeners installed using this symbol are called before the regular `'error'` listeners are called.

Installing a listener using this symbol does not change the behavior once an `'error'` event is emitted. Therefore, the process will still crash if no regular `'error'` listener is installed.

* **@since**

  v13.6.0, v12.17.0

## Accessors<!-- -->[**](#Accessors)

### [**](#retiredSessionsCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session_pool.ts#L224)retiredSessionsCount

* **get retiredSessionsCount(): number

- Gets count of retired sessions in the pool.

  ***

  #### Returns number

### [**](#usableSessionsCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session_pool.ts#L217)usableSessionsCount

* **get usableSessionsCount(): number

- Gets count of usable sessions in the pool.

  ***

  #### Returns number

## Methods<!-- -->[**](#Methods)

### [**](#\[captureRejectionSymbol])[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@types/node/events.d.ts#L103)externaloptionalinherited\[captureRejectionSymbol]

* ****\[captureRejectionSymbol]**\<K>(error, event, ...args): void

- Inherited from EventEmitter.\[captureRejectionSymbol]

  #### Parameters

  * ##### externalerror: Error
  * ##### externalevent: string | symbol
  * ##### externalrest...args: AnyRest

  #### Returns void

### [**](#addListener)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@types/node/events.d.ts#L642)externalinheritedaddListener

* ****addListener**\<K>(eventName, listener): this

- Inherited from EventEmitter.addListener

  Alias for `emitter.on(eventName, listener)`.

  * **@since**

    v0.1.26

  ***

  #### Parameters

  * ##### externaleventName: string | symbol
  * ##### externallistener: (...args) => void


  #### Returns this

### [**](#addSession)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session_pool.ts#L264)addSession

* ****addSession**(options): Promise\<void>

- Adds a new session to the session pool. The pool automatically creates sessions up to the maximum size of the pool, but this allows you to add more sessions once the max pool size is reached. This also allows you to add session with overridden session options (e.g. with specific session id).

  ***

  #### Parameters

  * ##### optionaloptions: [Session](https://crawlee.dev/js/api/core/class/Session.md) | [SessionOptions](https://crawlee.dev/js/api/core/interface/SessionOptions.md) = <!-- -->{}

    The configuration options for the session being added to the session pool.

  #### Returns Promise\<void>

### [**](#emit)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@types/node/events.d.ts#L904)externalinheritedemit

* ****emit**\<K>(eventName, ...args): boolean

- Inherited from EventEmitter.emit

  Synchronously calls each of the listeners registered for the event named `eventName`, in the order they were registered, passing the supplied arguments to each.

  Returns `true` if the event had listeners, `false` otherwise.

  ```
  import { EventEmitter } from 'node:events';
  const myEmitter = new EventEmitter();

  // First listener
  myEmitter.on('event', function firstListener() {
    console.log('Helloooo! first listener');
  });
  // Second listener
  myEmitter.on('event', function secondListener(arg1, arg2) {
    console.log(`event with parameters ${arg1}, ${arg2} in second listener`);
  });
  // Third listener
  myEmitter.on('event', function thirdListener(...args) {
    const parameters = args.join(', ');
    console.log(`event with parameters ${parameters} in third listener`);
  });

  console.log(myEmitter.listeners('event'));

  myEmitter.emit('event', 1, 2, 3, 4, 5);

  // Prints:
  // [
  //   [Function: firstListener],
  //   [Function: secondListener],
  //   [Function: thirdListener]
  // ]
  // Helloooo! first listener
  // event with parameters 1, 2 in second listener
  // event with parameters 1, 2, 3, 4, 5 in third listener
  ```

  * **@since**

    v0.1.26

  ***

  #### Parameters

  * ##### externaleventName: string | symbol
  * ##### externalrest...args: AnyRest

  #### Returns boolean

### [**](#eventNames)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@types/node/events.d.ts#L967)externalinheritedeventNames

* ****eventNames**(): (string | symbol)\[]

- Inherited from EventEmitter.eventNames

  Returns an array listing the events for which the emitter has registered listeners. The values in the array are strings or `Symbol`s.

  ```
  import { EventEmitter } from 'node:events';

  const myEE = new EventEmitter();
  myEE.on('foo', () => {});
  myEE.on('bar', () => {});

  const sym = Symbol('symbol');
  myEE.on(sym, () => {});

  console.log(myEE.eventNames());
  // Prints: [ 'foo', 'bar', Symbol(symbol) ]
  ```

  * **@since**

    v6.0.0

  ***

  #### Returns (string | symbol)\[]

### [**](#getMaxListeners)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@types/node/events.d.ts#L819)externalinheritedgetMaxListeners

* ****getMaxListeners**(): number

- Inherited from EventEmitter.getMaxListeners

  Returns the current max listener value for the `EventEmitter` which is either set by `emitter.setMaxListeners(n)` or defaults to EventEmitter.defaultMaxListeners.

  * **@since**

    v1.0.0

  ***

  #### Returns number

### [**](#getSession)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session_pool.ts#L291)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session_pool.ts#L296)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session_pool.ts#L305)getSession

* ****getSession**(): Promise<[Session](https://crawlee.dev/js/api/core/class/Session.md)>
* ****getSession**(sessionId): Promise<[Session](https://crawlee.dev/js/api/core/class/Session.md)>

- Gets session. If there is space for new session, it creates and returns new session. If the session pool is full, it picks a session from the pool, If the picked session is usable it is returned, otherwise it creates and returns a new one.

  ***

  #### Returns Promise<[Session](https://crawlee.dev/js/api/core/class/Session.md)>

### [**](#getState)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session_pool.ts#L348)getState

* ****getState**(): { retiredSessionsCount: number; sessions: [SessionState](https://crawlee.dev/js/api/core/interface/SessionState.md)\[]; usableSessionsCount: number }

- Returns an object representing the internal state of the `SessionPool` instance. Note that the object's fields can change in future releases.

  ***

  #### Returns { retiredSessionsCount: number; sessions: [SessionState](https://crawlee.dev/js/api/core/interface/SessionState.md)\[]; usableSessionsCount: number }

  * ##### retiredSessionsCount: number
  * ##### sessions: [SessionState](https://crawlee.dev/js/api/core/interface/SessionState.md)\[]
  * ##### usableSessionsCount: number

### [**](#initialize)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session_pool.ts#L232)initialize

* ****initialize**(): Promise\<void>

- Starts periodic state persistence and potentially loads SessionPool state from [KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md). It is called automatically by the [SessionPool.open](https://crawlee.dev/js/api/core/class/SessionPool.md#open) function.

  ***

  #### Returns Promise\<void>

### [**](#listenerCount)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@types/node/events.d.ts#L913)externalinheritedlistenerCount

* ****listenerCount**\<K>(eventName, listener): number

- Inherited from EventEmitter.listenerCount

  Returns the number of listeners listening for the event named `eventName`. If `listener` is provided, it will return how many times the listener is found in the list of the listeners of the event.

  * **@since**

    v3.2.0

  ***

  #### Parameters

  * ##### externaleventName: string | symbol

    The name of the event being listened for

  * ##### externaloptionallistener: Function

    The event handler function

  #### Returns number

### [**](#listeners)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@types/node/events.d.ts#L832)externalinheritedlisteners

* ****listeners**\<K>(eventName): Function\[]

- Inherited from EventEmitter.listeners

  Returns a copy of the array of listeners for the event named `eventName`.

  ```
  server.on('connection', (stream) => {
    console.log('someone connected!');
  });
  console.log(util.inspect(server.listeners('connection')));
  // Prints: [ [Function] ]
  ```

  * **@since**

    v0.1.26

  ***

  #### Parameters

  * ##### externaleventName: string | symbol

  #### Returns Function\[]

### [**](#off)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@types/node/events.d.ts#L792)externalinheritedoff

* ****off**\<K>(eventName, listener): this

- Inherited from EventEmitter.off

  Alias for `emitter.removeListener()`.

  * **@since**

    v10.0.0

  ***

  #### Parameters

  * ##### externaleventName: string | symbol
  * ##### externallistener: (...args) => void


  #### Returns this

### [**](#on)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@types/node/events.d.ts#L674)externalinheritedon

* ****on**\<K>(eventName, listener): this

- Inherited from EventEmitter.on

  Adds the `listener` function to the end of the listeners array for the event named `eventName`. No checks are made to see if the `listener` has already been added. Multiple calls passing the same combination of `eventName` and `listener` will result in the `listener` being added, and called, multiple times.

  ```
  server.on('connection', (stream) => {
    console.log('someone connected!');
  });
  ```

  Returns a reference to the `EventEmitter`, so that calls can be chained.

  By default, event listeners are invoked in the order they are added. The `emitter.prependListener()` method can be used as an alternative to add the event listener to the beginning of the listeners array.

  ```
  import { EventEmitter } from 'node:events';
  const myEE = new EventEmitter();
  myEE.on('foo', () => console.log('a'));
  myEE.prependListener('foo', () => console.log('b'));
  myEE.emit('foo');
  // Prints:
  //   b
  //   a
  ```

  * **@since**

    v0.1.101

  ***

  #### Parameters

  * ##### externaleventName: string | symbol

    The name of the event.

  * ##### externallistener: (...args) => void

    The callback function



  #### Returns this

### [**](#once)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@types/node/events.d.ts#L704)externalinheritedonce

* ****once**\<K>(eventName, listener): this

- Inherited from EventEmitter.once

  Adds a **one-time** `listener` function for the event named `eventName`. The next time `eventName` is triggered, this listener is removed and then invoked.

  ```
  server.once('connection', (stream) => {
    console.log('Ah, we have our first user!');
  });
  ```

  Returns a reference to the `EventEmitter`, so that calls can be chained.

  By default, event listeners are invoked in the order they are added. The `emitter.prependOnceListener()` method can be used as an alternative to add the event listener to the beginning of the listeners array.

  ```
  import { EventEmitter } from 'node:events';
  const myEE = new EventEmitter();
  myEE.once('foo', () => console.log('a'));
  myEE.prependOnceListener('foo', () => console.log('b'));
  myEE.emit('foo');
  // Prints:
  //   b
  //   a
  ```

  * **@since**

    v0.3.0

  ***

  #### Parameters

  * ##### externaleventName: string | symbol

    The name of the event.

  * ##### externallistener: (...args) => void

    The callback function



  #### Returns this

### [**](#persistState)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session_pool.ts#L361)persistState

* ****persistState**(options): Promise\<void>

- Persists the current state of the `SessionPool` into the default [KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md). The state is persisted automatically in regular intervals.

  ***

  #### Parameters

  * ##### optionaloptions: [PersistenceOptions](https://crawlee.dev/js/api/core/interface/PersistenceOptions.md)

    Override the persistence options provided in the constructor

  #### Returns Promise\<void>

### [**](#prependListener)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@types/node/events.d.ts#L931)externalinheritedprependListener

* ****prependListener**\<K>(eventName, listener): this

- Inherited from EventEmitter.prependListener

  Adds the `listener` function to the *beginning* of the listeners array for the event named `eventName`. No checks are made to see if the `listener` has already been added. Multiple calls passing the same combination of `eventName` and `listener` will result in the `listener` being added, and called, multiple times.

  ```
  server.prependListener('connection', (stream) => {
    console.log('someone connected!');
  });
  ```

  Returns a reference to the `EventEmitter`, so that calls can be chained.

  * **@since**

    v6.0.0

  ***

  #### Parameters

  * ##### externaleventName: string | symbol

    The name of the event.

  * ##### externallistener: (...args) => void

    The callback function



  #### Returns this

### [**](#prependOnceListener)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@types/node/events.d.ts#L947)externalinheritedprependOnceListener

* ****prependOnceListener**\<K>(eventName, listener): this

- Inherited from EventEmitter.prependOnceListener

  Adds a **one-time**`listener` function for the event named `eventName` to the *beginning* of the listeners array. The next time `eventName` is triggered, this listener is removed, and then invoked.

  ```
  server.prependOnceListener('connection', (stream) => {
    console.log('Ah, we have our first user!');
  });
  ```

  Returns a reference to the `EventEmitter`, so that calls can be chained.

  * **@since**

    v6.0.0

  ***

  #### Parameters

  * ##### externaleventName: string | symbol

    The name of the event.

  * ##### externallistener: (...args) => void

    The callback function



  #### Returns this

### [**](#rawListeners)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@types/node/events.d.ts#L863)externalinheritedrawListeners

* ****rawListeners**\<K>(eventName): Function\[]

- Inherited from EventEmitter.rawListeners

  Returns a copy of the array of listeners for the event named `eventName`, including any wrappers (such as those created by `.once()`).

  ```
  import { EventEmitter } from 'node:events';
  const emitter = new EventEmitter();
  emitter.once('log', () => console.log('log once'));

  // Returns a new Array with a function `onceWrapper` which has a property
  // `listener` which contains the original listener bound above
  const listeners = emitter.rawListeners('log');
  const logFnWrapper = listeners[0];

  // Logs "log once" to the console and does not unbind the `once` event
  logFnWrapper.listener();

  // Logs "log once" to the console and removes the listener
  logFnWrapper();

  emitter.on('log', () => console.log('log persistently'));
  // Will return a new Array with a single function bound by `.on()` above
  const newListeners = emitter.rawListeners('log');

  // Logs "log persistently" twice
  newListeners[0]();
  emitter.emit('log');
  ```

  * **@since**

    v9.4.0

  ***

  #### Parameters

  * ##### externaleventName: string | symbol

  #### Returns Function\[]

### [**](#removeAllListeners)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@types/node/events.d.ts#L803)externalinheritedremoveAllListeners

* ****removeAllListeners**(eventName): this

- Inherited from EventEmitter.removeAllListeners

  Removes all listeners, or those of the specified `eventName`.

  It is bad practice to remove listeners added elsewhere in the code, particularly when the `EventEmitter` instance was created by some other component or module (e.g. sockets or file streams).

  Returns a reference to the `EventEmitter`, so that calls can be chained.

  * **@since**

    v0.1.26

  ***

  #### Parameters

  * ##### externaloptionaleventName: string | symbol

  #### Returns this

### [**](#removeListener)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@types/node/events.d.ts#L787)externalinheritedremoveListener

* ****removeListener**\<K>(eventName, listener): this

- Inherited from EventEmitter.removeListener

  Removes the specified `listener` from the listener array for the event named `eventName`.

  ```
  const callback = (stream) => {
    console.log('someone connected!');
  };
  server.on('connection', callback);
  // ...
  server.removeListener('connection', callback);
  ```

  `removeListener()` will remove, at most, one instance of a listener from the listener array. If any single listener has been added multiple times to the listener array for the specified `eventName`, then `removeListener()` must be called multiple times to remove each instance.

  Once an event is emitted, all listeners attached to it at the time of emitting are called in order. This implies that any `removeListener()` or `removeAllListeners()` calls *after* emitting and *before* the last listener finishes execution will not remove them from`emit()` in progress. Subsequent events behave as expected.

  ```
  import { EventEmitter } from 'node:events';
  class MyEmitter extends EventEmitter {}
  const myEmitter = new MyEmitter();

  const callbackA = () => {
    console.log('A');
    myEmitter.removeListener('event', callbackB);
  };

  const callbackB = () => {
    console.log('B');
  };

  myEmitter.on('event', callbackA);

  myEmitter.on('event', callbackB);

  // callbackA removes listener callbackB but it will still be called.
  // Internal listener array at time of emit [callbackA, callbackB]
  myEmitter.emit('event');
  // Prints:
  //   A
  //   B

  // callbackB is now removed.
  // Internal listener array [callbackA]
  myEmitter.emit('event');
  // Prints:
  //   A
  ```

  Because listeners are managed using an internal array, calling this will change the position indices of any listener registered *after* the listener being removed. This will not impact the order in which listeners are called, but it means that any copies of the listener array as returned by the `emitter.listeners()` method will need to be recreated.

  When a single function has been added as a handler multiple times for a single event (as in the example below), `removeListener()` will remove the most recently added instance. In the example the `once('ping')` listener is removed:

  ```
  import { EventEmitter } from 'node:events';
  const ee = new EventEmitter();

  function pong() {
    console.log('pong');
  }

  ee.on('ping', pong);
  ee.once('ping', pong);
  ee.removeListener('ping', pong);

  ee.emit('ping');
  ee.emit('ping');
  ```

  Returns a reference to the `EventEmitter`, so that calls can be chained.

  * **@since**

    v0.1.26

  ***

  #### Parameters

  * ##### externaleventName: string | symbol
  * ##### externallistener: (...args) => void


  #### Returns this

### [**](#resetStore)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session_pool.ts#L336)resetStore

* ****resetStore**(options): Promise\<void>

- #### Parameters

  * ##### optionaloptions: [PersistenceOptions](https://crawlee.dev/js/api/core/interface/PersistenceOptions.md)

    Override the persistence options provided in the constructor

  #### Returns Promise\<void>

### [**](#setMaxListeners)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@types/node/events.d.ts#L813)externalinheritedsetMaxListeners

* ****setMaxListeners**(n): this

- Inherited from EventEmitter.setMaxListeners

  By default `EventEmitter`s will print a warning if more than `10` listeners are added for a particular event. This is a useful default that helps finding memory leaks. The `emitter.setMaxListeners()` method allows the limit to be modified for this specific `EventEmitter` instance. The value can be set to `Infinity` (or `0`) to indicate an unlimited number of listeners.

  Returns a reference to the `EventEmitter`, so that calls can be chained.

  * **@since**

    v0.3.5

  ***

  #### Parameters

  * ##### externaln: number

  #### Returns this

### [**](#teardown)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session_pool.ts#L388)teardown

* ****teardown**(): Promise\<void>

- Removes listener from `persistState` event. This function should be called after you are done with using the `SessionPool` instance.

  ***

  #### Returns Promise\<void>

### [**](#addAbortListener)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@types/node/events.d.ts#L403)staticexternalinheritedaddAbortListener

* ****addAbortListener**(signal, resource): Disposable

- Inherited from EventEmitter.addAbortListener

  Listens once to the `abort` event on the provided `signal`.

  Listening to the `abort` event on abort signals is unsafe and may lead to resource leaks since another third party with the signal can call `e.stopImmediatePropagation()`. Unfortunately Node.js cannot change this since it would violate the web standard. Additionally, the original API makes it easy to forget to remove listeners.

  This API allows safely using `AbortSignal`s in Node.js APIs by solving these two issues by listening to the event such that `stopImmediatePropagation` does not prevent the listener from running.

  Returns a disposable so that it may be unsubscribed from more easily.

  ```
  import { addAbortListener } from 'node:events';

  function example(signal) {
    let disposable;
    try {
      signal.addEventListener('abort', (e) => e.stopImmediatePropagation());
      disposable = addAbortListener(signal, (e) => {
        // Do something when signal is aborted.
      });
    } finally {
      disposable?.[Symbol.dispose]();
    }
  }
  ```

  * **@since**

    v20.5.0

  ***

  #### Parameters

  * ##### externalsignal: AbortSignal
  * ##### externalresource: (event) => void


  #### Returns Disposable

  Disposable that removes the `abort` listener.

### [**](#getEventListeners)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@types/node/events.d.ts#L325)staticexternalinheritedgetEventListeners

* ****getEventListeners**(emitter, name): Function\[]

- Inherited from EventEmitter.getEventListeners

  Returns a copy of the array of listeners for the event named `eventName`.

  For `EventEmitter`s this behaves exactly the same as calling `.listeners` on the emitter.

  For `EventTarget`s this is the only way to get the event listeners for the event target. This is useful for debugging and diagnostic purposes.

  ```
  import { getEventListeners, EventEmitter } from 'node:events';

  {
    const ee = new EventEmitter();
    const listener = () => console.log('Events are fun');
    ee.on('foo', listener);
    console.log(getEventListeners(ee, 'foo')); // [ [Function: listener] ]
  }
  {
    const et = new EventTarget();
    const listener = () => console.log('Events are fun');
    et.addEventListener('foo', listener);
    console.log(getEventListeners(et, 'foo')); // [ [Function: listener] ]
  }
  ```

  * **@since**

    v15.2.0, v14.17.0

  ***

  #### Parameters

  * ##### externalemitter: EventEmitter\<DefaultEventMap> | EventTarget
  * ##### externalname: string | symbol

  #### Returns Function\[]

### [**](#getMaxListeners)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@types/node/events.d.ts#L354)staticexternalinheritedgetMaxListeners

* ****getMaxListeners**(emitter): number

- Inherited from EventEmitter.getMaxListeners

  Returns the currently set max amount of listeners.

  For `EventEmitter`s this behaves exactly the same as calling `.getMaxListeners` on the emitter.

  For `EventTarget`s this is the only way to get the max event listeners for the event target. If the number of event handlers on a single EventTarget exceeds the max set, the EventTarget will print a warning.

  ```
  import { getMaxListeners, setMaxListeners, EventEmitter } from 'node:events';

  {
    const ee = new EventEmitter();
    console.log(getMaxListeners(ee)); // 10
    setMaxListeners(11, ee);
    console.log(getMaxListeners(ee)); // 11
  }
  {
    const et = new EventTarget();
    console.log(getMaxListeners(et)); // 10
    setMaxListeners(11, et);
    console.log(getMaxListeners(et)); // 11
  }
  ```

  * **@since**

    v19.9.0

  ***

  #### Parameters

  * ##### externalemitter: EventEmitter\<DefaultEventMap> | EventTarget

  #### Returns number

### [**](#listenerCount)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@types/node/events.d.ts#L297)staticexternalinheritedlistenerCount

* ****listenerCount**(emitter, eventName): number

- Inherited from EventEmitter.listenerCount

  A class method that returns the number of listeners for the given `eventName` registered on the given `emitter`.

  ```
  import { EventEmitter, listenerCount } from 'node:events';

  const myEmitter = new EventEmitter();
  myEmitter.on('event', () => {});
  myEmitter.on('event', () => {});
  console.log(listenerCount(myEmitter, 'event'));
  // Prints: 2
  ```

  * **@since**

    v0.9.12

  * **@deprecated**

    Since v3.2.0 - Use `listenerCount` instead.

  ***

  #### Parameters

  * ##### externalemitter: EventEmitter\<DefaultEventMap>

    The emitter to query

  * ##### externaleventName: string | symbol

    The event name

  #### Returns number

### [**](#on)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@types/node/events.d.ts#L270)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@types/node/events.d.ts#L275)staticexternalinheritedon

* ****on**(emitter, eventName, options): AsyncIterator\<any\[], undefined, any>
* ****on**(emitter, eventName, options): AsyncIterator\<any\[], undefined, any>

- Inherited from EventEmitter.on

  ```
  import { on, EventEmitter } from 'node:events';
  import process from 'node:process';

  const ee = new EventEmitter();

  // Emit later on
  process.nextTick(() => {
    ee.emit('foo', 'bar');
    ee.emit('foo', 42);
  });

  for await (const event of on(ee, 'foo')) {
    // The execution of this inner block is synchronous and it
    // processes one event at a time (even with await). Do not use
    // if concurrent execution is required.
    console.log(event); // prints ['bar'] [42]
  }
  // Unreachable here
  ```

  Returns an `AsyncIterator` that iterates `eventName` events. It will throw if the `EventEmitter` emits `'error'`. It removes all listeners when exiting the loop. The `value` returned by each iteration is an array composed of the emitted event arguments.

  An `AbortSignal` can be used to cancel waiting on events:

  ```
  import { on, EventEmitter } from 'node:events';
  import process from 'node:process';

  const ac = new AbortController();

  (async () => {
    const ee = new EventEmitter();

    // Emit later on
    process.nextTick(() => {
      ee.emit('foo', 'bar');
      ee.emit('foo', 42);
    });

    for await (const event of on(ee, 'foo', { signal: ac.signal })) {
      // The execution of this inner block is synchronous and it
      // processes one event at a time (even with await). Do not use
      // if concurrent execution is required.
      console.log(event); // prints ['bar'] [42]
    }
    // Unreachable here
  })();

  process.nextTick(() => ac.abort());
  ```

  Use the `close` option to specify an array of event names that will end the iteration:

  ```
  import { on, EventEmitter } from 'node:events';
  import process from 'node:process';

  const ee = new EventEmitter();

  // Emit later on
  process.nextTick(() => {
    ee.emit('foo', 'bar');
    ee.emit('foo', 42);
    ee.emit('close');
  });

  for await (const event of on(ee, 'foo', { close: ['close'] })) {
    console.log(event); // prints ['bar'] [42]
  }
  // the loop will exit after 'close' is emitted
  console.log('done'); // prints 'done'
  ```

  * **@since**

    v13.6.0, v12.16.0

  ***

  #### Parameters

  * ##### externalemitter: EventEmitter\<DefaultEventMap>
  * ##### externaleventName: string | symbol
  * ##### externaloptionaloptions: StaticEventEmitterIteratorOptions

  #### Returns AsyncIterator\<any\[], undefined, any>

  An `AsyncIterator` that iterates `eventName` events emitted by the `emitter`

### [**](#once)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@types/node/events.d.ts#L184)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@types/node/events.d.ts#L189)staticexternalinheritedonce

* ****once**(emitter, eventName, options): Promise\<any\[]>
* ****once**(emitter, eventName, options): Promise\<any\[]>

- Inherited from EventEmitter.once

  Creates a `Promise` that is fulfilled when the `EventEmitter` emits the given event or that is rejected if the `EventEmitter` emits `'error'` while waiting. The `Promise` will resolve with an array of all the arguments emitted to the given event.

  This method is intentionally generic and works with the web platform [EventTarget](https://dom.spec.whatwg.org/#interface-eventtarget) interface, which has no special`'error'` event semantics and does not listen to the `'error'` event.

  ```
  import { once, EventEmitter } from 'node:events';
  import process from 'node:process';

  const ee = new EventEmitter();

  process.nextTick(() => {
    ee.emit('myevent', 42);
  });

  const [value] = await once(ee, 'myevent');
  console.log(value);

  const err = new Error('kaboom');
  process.nextTick(() => {
    ee.emit('error', err);
  });

  try {
    await once(ee, 'myevent');
  } catch (err) {
    console.error('error happened', err);
  }
  ```

  The special handling of the `'error'` event is only used when `events.once()` is used to wait for another event. If `events.once()` is used to wait for the '`error'` event itself, then it is treated as any other kind of event without special handling:

  ```
  import { EventEmitter, once } from 'node:events';

  const ee = new EventEmitter();

  once(ee, 'error')
    .then(([err]) => console.log('ok', err.message))
    .catch((err) => console.error('error', err.message));

  ee.emit('error', new Error('boom'));

  // Prints: ok boom
  ```

  An `AbortSignal` can be used to cancel waiting for the event:

  ```
  import { EventEmitter, once } from 'node:events';

  const ee = new EventEmitter();
  const ac = new AbortController();

  async function foo(emitter, event, signal) {
    try {
      await once(emitter, event, { signal });
      console.log('event emitted!');
    } catch (error) {
      if (error.name === 'AbortError') {
        console.error('Waiting for the event was canceled!');
      } else {
        console.error('There was an error', error.message);
      }
    }
  }

  foo(ee, 'foo', ac.signal);
  ac.abort(); // Abort waiting for the event
  ee.emit('foo'); // Prints: Waiting for the event was canceled!
  ```

  * **@since**

    v11.13.0, v10.16.0

  ***

  #### Parameters

  * ##### externalemitter: EventEmitter\<DefaultEventMap>
  * ##### externaleventName: string | symbol
  * ##### externaloptionaloptions: StaticEventEmitterOptions

  #### Returns Promise\<any\[]>

### [**](#open)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session_pool.ts#L512)staticopen

* ****open**(options, config): Promise<[SessionPool](https://crawlee.dev/js/api/core/class/SessionPool.md)>

- Opens a SessionPool and returns a promise resolving to an instance of the [SessionPool](https://crawlee.dev/js/api/core/class/SessionPool.md) class that is already initialized.

  For more details and code examples, see the [SessionPool](https://crawlee.dev/js/api/core/class/SessionPool.md) class.

  ***

  #### Parameters

  * ##### optionaloptions: [SessionPoolOptions](https://crawlee.dev/js/api/core/interface/SessionPoolOptions.md)
  * ##### optionalconfig: [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md)

  #### Returns Promise<[SessionPool](https://crawlee.dev/js/api/core/class/SessionPool.md)>

### [**](#setMaxListeners)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@types/node/events.d.ts#L369)staticexternalinheritedsetMaxListeners

* ****setMaxListeners**(n, ...eventTargets): void

- Inherited from EventEmitter.setMaxListeners

  ```
  import { setMaxListeners, EventEmitter } from 'node:events';

  const target = new EventTarget();
  const emitter = new EventEmitter();

  setMaxListeners(5, target, emitter);
  ```

  * **@since**

    v15.4.0

  ***

  #### Parameters

  * ##### externaloptionaln: number

    A non-negative number. The maximum number of listeners per `EventTarget` event.

  * ##### externalrest...eventTargets: (EventEmitter\<DefaultEventMap> | EventTarget)\[]

    Zero or more {EventTarget} or {EventEmitter} instances. If none are specified, `n` is set as the default max for all newly created {EventTarget} and {EventEmitter} objects.

  #### Returns void
