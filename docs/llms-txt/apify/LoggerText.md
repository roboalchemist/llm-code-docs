# Source: https://docs.apify.com/sdk/js/reference/class/LoggerText.md

# externalLoggerText<!-- -->

This is an abstract class that should be extended by custom logger classes.

this.\_log() method must be implemented by them.

### Hierarchy

* [Logger](https://docs.apify.com/sdk/js/sdk/js/reference/class/Logger.md)
  * *LoggerText*

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**captureRejections](#captureRejections)
* [**captureRejectionSymbol](#captureRejectionSymbol)
* [**defaultMaxListeners](#defaultMaxListeners)
* [**errorMonitor](#errorMonitor)

### Methods

* [**\_log](#_log)
* [**\_outputWithConsole](#_outputWithConsole)
* [**\[captureRejectionSymbol\]](#\[captureRejectionSymbol])
* [**addListener](#addListener)
* [**emit](#emit)
* [**eventNames](#eventNames)
* [**getMaxListeners](#getMaxListeners)
* [**getOptions](#getOptions)
* [**listenerCount](#listenerCount)
* [**listeners](#listeners)
* [**log](#log)
* [**off](#off)
* [**on](#on)
* [**once](#once)
* [**prependListener](#prependListener)
* [**prependOnceListener](#prependOnceListener)
* [**rawListeners](#rawListeners)
* [**removeAllListeners](#removeAllListeners)
* [**removeListener](#removeListener)
* [**setMaxListeners](#setMaxListeners)
* [**setOptions](#setOptions)
* [**addAbortListener](#addAbortListener)
* [**getEventListeners](#getEventListeners)
* [**getMaxListeners](#getMaxListeners)
* [**listenerCount](#listenerCount)
* [**on](#on)
* [**once](#once)
* [**setMaxListeners](#setMaxListeners)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@apify/log/src/index.d.ts#L246)externalconstructor

* ****new LoggerText**(options): [LoggerText](https://docs.apify.com/sdk/js/sdk/js/reference/class/LoggerText.md)

- Overrides Logger.constructor

  #### Parameters

  * ##### externaloptionaloptions: <!-- -->{}


  #### Returns [LoggerText](https://docs.apify.com/sdk/js/sdk/js/reference/class/LoggerText.md)

## Properties<!-- -->[**](#Properties)

### [**](#captureRejections)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@types/node/events.d.ts#L459)staticexternalinheritedcaptureRejections

**captureRejections: boolean

Inherited from Logger.captureRejections

Value: [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type)

Change the default `captureRejections` option on all new `EventEmitter` objects.

* **@since**

  v13.4.0, v12.16.0

### [**](#captureRejectionSymbol)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@types/node/events.d.ts#L452)staticexternalreadonlyinheritedcaptureRejectionSymbol

**captureRejectionSymbol: typeof captureRejectionSymbol

Inherited from Logger.captureRejectionSymbol

Value: `Symbol.for('nodejs.rejection')`

See how to write a custom `rejection handler`.

* **@since**

  v13.4.0, v12.16.0

### [**](#defaultMaxListeners)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@types/node/events.d.ts#L498)staticexternalinheriteddefaultMaxListeners

**defaultMaxListeners: number

Inherited from Logger.defaultMaxListeners

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

### [**](#errorMonitor)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@types/node/events.d.ts#L445)staticexternalreadonlyinheritederrorMonitor

**errorMonitor: typeof errorMonitor

Inherited from Logger.errorMonitor

This symbol shall be used to install a listener for only monitoring `'error'` events. Listeners installed using this symbol are called before the regular `'error'` listeners are called.

Installing a listener using this symbol does not change the behavior once an `'error'` event is emitted. Therefore, the process will still crash if no regular `'error'` listener is installed.

* **@since**

  v13.6.0, v12.17.0

## Methods<!-- -->[**](#Methods)

### [**](#_log)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@apify/log/src/index.d.ts#L247)external\_log

* ****\_log**(level, message, data, exception, opts): string

- Overrides Logger.\_log

  #### Parameters

  * ##### externallevel: [LogLevel](https://docs.apify.com/sdk/js/sdk/js/reference/enum/LogLevel.md)
  * ##### externalmessage: string
  * ##### externaloptionaldata: any
  * ##### externaloptionalexception: unknown
  * ##### externaloptionalopts: Record\<string, any>

  #### Returns string

### [**](#_outputWithConsole)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@apify/log/src/index.d.ts#L36)externalinherited\_outputWithConsole

* ****\_outputWithConsole**(level, line): void

- Inherited from Logger.\_outputWithConsole

  #### Parameters

  * ##### externallevel: [LogLevel](https://docs.apify.com/sdk/js/sdk/js/reference/enum/LogLevel.md)
  * ##### externalline: string

  #### Returns void

### [**](#\[captureRejectionSymbol])[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@types/node/events.d.ts#L136)externaloptionalinherited\[captureRejectionSymbol]

* ****\[captureRejectionSymbol]**\<K>(error, event, ...args): void

- Inherited from Logger.\[captureRejectionSymbol]

  #### Parameters

  * ##### externalerror: Error
  * ##### externalevent: string | symbol
  * ##### externalrest...args: AnyRest

  #### Returns void

### [**](#addListener)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@types/node/events.d.ts#L597)externalinheritedaddListener

* ****addListener**\<K>(eventName, listener): this

- Inherited from Logger.addListener

  Alias for `emitter.on(eventName, listener)`.

  * **@since**

    v0.1.26

  ***

  #### Parameters

  * ##### externaleventName: string | symbol
  * ##### externallistener: (...args) => void


  #### Returns this

### [**](#emit)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@types/node/events.d.ts#L859)externalinheritedemit

* ****emit**\<K>(eventName, ...args): boolean

- Inherited from Logger.emit

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

### [**](#eventNames)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@types/node/events.d.ts#L922)externalinheritedeventNames

* ****eventNames**(): (string | symbol)\[]

- Inherited from Logger.eventNames

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

### [**](#getMaxListeners)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@types/node/events.d.ts#L774)externalinheritedgetMaxListeners

* ****getMaxListeners**(): number

- Inherited from Logger.getMaxListeners

  Returns the current max listener value for the `EventEmitter` which is either set by `emitter.setMaxListeners(n)` or defaults to defaultMaxListeners.

  * **@since**

    v1.0.0

  ***

  #### Returns number

### [**](#getOptions)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@apify/log/src/index.d.ts#L35)externalinheritedgetOptions

* ****getOptions**(): Record\<string, any>

- Inherited from Logger.getOptions

  #### Returns Record\<string, any>

### [**](#listenerCount)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@types/node/events.d.ts#L868)externalinheritedlistenerCount

* ****listenerCount**\<K>(eventName, listener): number

- Inherited from Logger.listenerCount

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

### [**](#listeners)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@types/node/events.d.ts#L787)externalinheritedlisteners

* ****listeners**\<K>(eventName): Function\[]

- Inherited from Logger.listeners

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

### [**](#log)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@apify/log/src/index.d.ts#L38)externalinheritedlog

* ****log**(level, message, ...args): void

- Inherited from Logger.log

  #### Parameters

  * ##### externallevel: [LogLevel](https://docs.apify.com/sdk/js/sdk/js/reference/enum/LogLevel.md)
  * ##### externalmessage: string
  * ##### externalrest...args: any\[]

  #### Returns void

### [**](#off)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@types/node/events.d.ts#L747)externalinheritedoff

* ****off**\<K>(eventName, listener): this

- Inherited from Logger.off

  Alias for `emitter.removeListener()`.

  * **@since**

    v10.0.0

  ***

  #### Parameters

  * ##### externaleventName: string | symbol
  * ##### externallistener: (...args) => void


  #### Returns this

### [**](#on)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@types/node/events.d.ts#L629)externalinheritedon

* ****on**\<K>(eventName, listener): this

- Inherited from Logger.on

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

### [**](#once)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@types/node/events.d.ts#L659)externalinheritedonce

* ****once**\<K>(eventName, listener): this

- Inherited from Logger.once

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

### [**](#prependListener)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@types/node/events.d.ts#L886)externalinheritedprependListener

* ****prependListener**\<K>(eventName, listener): this

- Inherited from Logger.prependListener

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

### [**](#prependOnceListener)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@types/node/events.d.ts#L902)externalinheritedprependOnceListener

* ****prependOnceListener**\<K>(eventName, listener): this

- Inherited from Logger.prependOnceListener

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

### [**](#rawListeners)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@types/node/events.d.ts#L818)externalinheritedrawListeners

* ****rawListeners**\<K>(eventName): Function\[]

- Inherited from Logger.rawListeners

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

### [**](#removeAllListeners)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@types/node/events.d.ts#L758)externalinheritedremoveAllListeners

* ****removeAllListeners**(eventName): this

- Inherited from Logger.removeAllListeners

  Removes all listeners, or those of the specified `eventName`.

  It is bad practice to remove listeners added elsewhere in the code, particularly when the `EventEmitter` instance was created by some other component or module (e.g. sockets or file streams).

  Returns a reference to the `EventEmitter`, so that calls can be chained.

  * **@since**

    v0.1.26

  ***

  #### Parameters

  * ##### externaloptionaleventName: string | symbol

  #### Returns this

### [**](#removeListener)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@types/node/events.d.ts#L742)externalinheritedremoveListener

* ****removeListener**\<K>(eventName, listener): this

- Inherited from Logger.removeListener

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

### [**](#setMaxListeners)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@types/node/events.d.ts#L768)externalinheritedsetMaxListeners

* ****setMaxListeners**(n): this

- Inherited from Logger.setMaxListeners

  By default `EventEmitter`s will print a warning if more than `10` listeners are added for a particular event. This is a useful default that helps finding memory leaks. The `emitter.setMaxListeners()` method allows the limit to be modified for this specific `EventEmitter` instance. The value can be set to `Infinity` (or `0`) to indicate an unlimited number of listeners.

  Returns a reference to the `EventEmitter`, so that calls can be chained.

  * **@since**

    v0.3.5

  ***

  #### Parameters

  * ##### externaln: number

  #### Returns this

### [**](#setOptions)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@apify/log/src/index.d.ts#L34)externalinheritedsetOptions

* ****setOptions**(options): void

- Inherited from Logger.setOptions

  #### Parameters

  * ##### externaloptions: Record\<string, any>

  #### Returns void

### [**](#addAbortListener)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@types/node/events.d.ts#L437)staticexternalinheritedaddAbortListener

* ****addAbortListener**(signal, resource): Disposable

- Inherited from Logger.addAbortListener

  experimental

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

### [**](#getEventListeners)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@types/node/events.d.ts#L358)staticexternalinheritedgetEventListeners

* ****getEventListeners**(emitter, name): Function\[]

- Inherited from Logger.getEventListeners

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

### [**](#getMaxListeners)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@types/node/events.d.ts#L387)staticexternalinheritedgetMaxListeners

* ****getMaxListeners**(emitter): number

- Inherited from Logger.getMaxListeners

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

### [**](#listenerCount)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@types/node/events.d.ts#L330)staticexternalinheritedlistenerCount

* ****listenerCount**(emitter, eventName): number

- Inherited from Logger.listenerCount

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

### [**](#on)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@types/node/events.d.ts#L303)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@types/node/events.d.ts#L308)staticexternalinheritedon

* ****on**(emitter, eventName, options): AsyncIterator\<any\[], any, any>
* ****on**(emitter, eventName, options): AsyncIterator\<any\[], any, any>

- Inherited from Logger.on

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

  #### Returns AsyncIterator\<any\[], any, any>

  An `AsyncIterator` that iterates `eventName` events emitted by the `emitter`

### [**](#once)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@types/node/events.d.ts#L217)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@types/node/events.d.ts#L222)staticexternalinheritedonce

* ****once**(emitter, eventName, options): Promise\<any\[]>
* ****once**(emitter, eventName, options): Promise\<any\[]>

- Inherited from Logger.once

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

### [**](#setMaxListeners)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@types/node/events.d.ts#L402)staticexternalinheritedsetMaxListeners

* ****setMaxListeners**(n, ...eventTargets): void

- Inherited from Logger.setMaxListeners

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
